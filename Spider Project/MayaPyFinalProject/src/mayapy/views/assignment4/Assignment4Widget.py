# Assignment4Widget.py
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
class Assignment4Widget(PyGlassWidget, QDialog):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment4Widget, self).__init__(parent, **kwargs)
        self.minInput = QLineEdit("-1")
        self.maxInput = QLineEdit("1")
        self.exampleBtn.clicked.connect(self._handleExampleButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.perturbBtn.clicked.connect(self._handlePerturb)

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

#___________________________________________________________________________________________________ _handlePerturb
    def _handlePerturb(self):
        """
        This perturbs the selected object.

        """

        selectedObjects = cmds.ls(selection=True, long=True)

        vertsList = []
        for object in selectedObjects:
            totalVerts = cmds.polyEvaluate(object, vertex=True)

            for number in range(totalVerts):
                vertsList.append(object+'.vtx[{number}]'.format(number=number))

        for vert in vertsList:
            min = float(self.minInput.displayText())
            max = float(self.maxInput.displayText())
            randNumX = random.uniform(min, max)
            randNumY = random.uniform(min, max)
            randNumZ = random.uniform(min, max)
            cmds.select(vert, replace=True)
            cmds.move(randNumX, randNumY, randNumZ, relative=True)
            cmds.select(selectedObjects, replace=True)