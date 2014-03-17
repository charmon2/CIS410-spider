# Assignment3Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
# import maya.cmds as cmds
# import maya.mel as mel
import random as random
import sys
from PySide.QtCore import*
from PySide.QtGui import*



#___________________________________________________________________________________________________ Assignment1Widget
class Assignment3Widget(PyGlassWidget, QDialog):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment3Widget, self).__init__(parent, **kwargs)
        self.minInput = QLineEdit("-1")
        self.maxInput = QLineEdit("1")
        self.exampleBtn.clicked.connect(self._handleExampleButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.createH2oBtn.clicked.connect(self._handleCreateH2o)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleExampleButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)
#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

#___________________________________________________________________________________________________ _handleCreateH2o
    def _handleCreateH2o(self):
        """

        """
        #Sets the animation end time
        cmds.playbackOptions(max=240, aet=240)

        #this number sets the number of molecules to create
        molecules = 10

        #Creates each atom in the h2o molecule, aligns them properly, then groups them together .
        cmds.polySphere(name="oxygen", r=1.2)
        cmds.polySphere(name="hydrogenA", r=1.06)
        cmds.select("hydrogenA")
        cmds.move(0, -1.3, 0)
        cmds.group('oxygen', 'hydrogenA', n='oxygenHydrogenA')

        cmds.select('hydrogenA')
        cmds.rotate(0, 0, '-52.5', p=(0, 0, 0))

        cmds.polySphere(name="hydrogenB", r=1.06)
        cmds.select("hydrogenB")
        cmds.move(0, -1.3, 0)
        cmds.group('oxygen', 'hydrogenB', n='oxygenHydrogenB')

        cmds.select('hydrogenB')
        cmds.rotate(0, 0, '52.5', p=(0, 0, 0))

        cmds.select('hydrogenA', 'hydrogenB')
        cmds.polyColorPerVertex(rgb=(1, 1, 1), cdo=True)

        cmds.select('oxygen')
        cmds.polyColorPerVertex(rgb=(1, 0, 0), cdo=True)

        cmds.group('oxygenHydrogenB', 'oxygenHydrogenA', n='h2o')

        #duplicates the original molecule
        for i in range(1, molecules):
            cmds.duplicate('h2o')

        #list of planes for movement
        xyz = ['X', 'Y']

        #Sets movement for the original h2o molecule
        cmds.select("h2o")
        plane = random.choice(xyz)
        cmds.setKeyframe('h2o', at='translate'+plane, v=float(cmds.getAttr('h2o.translate'+plane)), t=1)
        cmds.setKeyframe('h2o', at='translate'+plane, v=5, t=240)

        #Iterates through each h2o group and assigns a random position and orientation for each molecule.
        #It also randomly choose a direction for the molecule to move in.
        for i in range(1, molecules):
            #random plane
            plane = random.choice(xyz)
            cmds.select("h2o"+str(i))
            #random position
            cmds.move(random.randrange(-9, 9), random.randrange(-9, 9), random.randrange(-9, 9))
            #random orientation
            cmds.rotate(random.randrange(0, 350), random.randrange(0, 350), random.randrange(0, 350))
            #sets the start and end position for movement
            cmds.setKeyframe('h2o'+str(i), at='translate'+plane, v=float(cmds.getAttr('h2o'+str(i)+'.translate'+plane)), t=1)
            cmds.setKeyframe('h2o'+str(i), at='translate'+plane, v=5, t=240)
            plane = random.choice(xyz)

        #Selects all the h2o molecules
        cmds.select("h2o", add=True)
        for i in range(1, molecules):
            cmds.select("h2o"+str(i))

        #Creates a new animation layer called vibrate and adds all the h2o molecules to it.
        cmds.animLayer('vibrate', aso=True)

        #Sets oscillation for original molecule
        cmds.setKeyframe('h2o', at='translateZ', v=float(cmds.getAttr('h2o.translateZ')), t=1)
        cmds.setKeyframe('h2o', at='translateZ', v=float(cmds.getAttr('h2o.translateZ'))+.2, t=2)
        #cmds.selectKey('h2o', t=(1,2), at="translateZ")
        cmds.selectKey('h2o', at='translateZ')
        cmds.setInfinity(pri='oscillate', poi='oscillate')

        #Sets oscillation for all other molecules
        for i in range(1, molecules):
            cmds.setKeyframe('h2o'+str(i), at='translateZ', v=float(cmds.getAttr('h2o'+str(i)+'.translateZ')), t=1)
            cmds.setKeyframe('h2o'+str(i), at='translateZ', v=float(cmds.getAttr('h2o'+str(i)+'.translateZ'))+.2, t=2)
            #cmds.selectKey('h2o'+str(i), t=(1,2), at="translateZ")
            cmds.selectKey('h2o'+str(i), at="translateZ")
            cmds.setInfinity(pri='oscillate', poi='oscillate')
