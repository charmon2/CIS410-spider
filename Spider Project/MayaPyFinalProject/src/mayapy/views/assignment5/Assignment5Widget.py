# Assignment5Widget.py
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
class Assignment5Widget(PyGlassWidget, QDialog):
    """A class for Assignment 5"""


#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment5Widget, self).__init__(parent, **kwargs)

        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.createBallBtn.clicked.connect(self._handleCreateBall)
        self.deformBtn.clicked.connect(self._handleDeform)
        self.deformerSlider.valueChanged.connect(self._setValue)
        #QObject.connect(self.deformerSlider, SIGNAL('valueChanged()'), self._setValue)



#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

#___________________________________________________________________________________________________ _handleCreateBall
    def _handleCreateBall(self):
        cmds.polySphere(name='ball', r=2, sx=20, sy=20, ax=[0, 1, 0])
        cmds.polyColorPerVertex(rgb=(1, 1, 1), cdo=True)
        cmds.select('ball.f[380:399]', 'ball.f[320:339]', 'ball.f[280:299]', 'ball.f[240:259]', 'ball.f[200:219]', 'ball.f[160:179]', 'ball.f[120:139]', 'ball.f[80:99]', 'ball.f[40:59]', 'ball.f[0:19]')
        cmds.polyColorPerVertex(rgb=(1, 0, 0), cdo=True)
        cmds.select('ball')
        cmds.nonLinear( type='squash')

#___________________________________________________________________________________________________ _handleDeform
    def _handleDeform(self):

        val = self.deformerSlider.value()
        cmds.setAttr('squash1.factor', val)

#___________________________________________________________________________________________________ _setValue
    def _setValue(self):
        val = self.deformerSlider.value()

