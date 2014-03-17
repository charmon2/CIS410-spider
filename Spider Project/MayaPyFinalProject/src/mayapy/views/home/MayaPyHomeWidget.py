# MayaPyHomeWidget.py
# (C)2013
# Scott Ernst

import random as random
import sys
from PySide import QtGui
from nimble import cmds
from PySide.QtCore import*
from PySide.QtGui import*
from pyglass.widgets.PyGlassWidget import PyGlassWidget
from mayapy.enum.UserConfigEnum import UserConfigEnum
from mayapy.views.home.NimbleStatusElement import NimbleStatusElement

#___________________________________________________________________________________________________ MayaPyHomeWidget
class MayaPyHomeWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of MayaPyHomeWidget."""
        super(MayaPyHomeWidget, self).__init__(parent, **kwargs)
        self._firstView = True

        self.moveBtn.clicked.connect(self._handleMove)
        self.jumpBtn.clicked.connect(self._handleJump)
        self.attackBtn.clicked.connect(self._handleAttack)
        self.resetBtn.clicked.connect(self._handleReset)

        self._statusBox, statusLayout = self._createElementWidget(self, QtGui.QVBoxLayout, True)
        statusLayout.addStretch()

        self._nimbleStatus = NimbleStatusElement(
            self._statusBox,
            disabled=self.mainWindow.appConfig.get(UserConfigEnum.NIMBLE_TEST_STATUS, True) )
        statusLayout.addWidget(self._nimbleStatus)
#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _activateWidgetDisplayImpl
    def _activateWidgetDisplayImpl(self, **kwargs):
        if self._firstView:
            self._nimbleStatus.refresh()
            self._firstView = False

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleMove
    def _handleMove(self):
        cmds.playbackOptions(max=24, aet=24)
        cmds.setKeyframe("CTRL_L_legA", at="translateZ", v=float(cmds.getAttr('CTRL_L_legA.translateZ')), t=1)
        cmds.setKeyframe("CTRL_L_legA", at="translateZ", v=float(cmds.getAttr('CTRL_L_legA.translateZ')+2), t=6)
        cmds.setKeyframe("CTRL_L_legA", at="translateZ", v=float(cmds.getAttr('CTRL_L_legA.translateZ')), t=12)
        cmds.setKeyframe("CTRL_L_legA", at="translateZ", v=float(cmds.getAttr('CTRL_L_legA.translateZ')-2), t=18)
        cmds.setKeyframe("CTRL_L_legA", at="translateZ", v=float(cmds.getAttr('CTRL_L_legA.translateZ')), t=24)

        cmds.setKeyframe("CTRL_L_legB", at="translateZ", v=float(cmds.getAttr('CTRL_L_legB.translateZ')), t=1)
        cmds.setKeyframe("CTRL_L_legB", at="translateZ", v=float(cmds.getAttr('CTRL_L_legB.translateZ')-2), t=6)
        cmds.setKeyframe("CTRL_L_legB", at="translateZ", v=float(cmds.getAttr('CTRL_L_legB.translateZ')), t=12)
        cmds.setKeyframe("CTRL_L_legB", at="translateZ", v=float(cmds.getAttr('CTRL_L_legB.translateZ')+2), t=18)
        cmds.setKeyframe("CTRL_L_legB", at="translateZ", v=float(cmds.getAttr('CTRL_L_legB.translateZ')), t=24)

        cmds.setKeyframe("CTRL_L_legC", at="translateZ", v=float(cmds.getAttr('CTRL_L_legC.translateZ')), t=1)
        cmds.setKeyframe("CTRL_L_legC", at="translateZ", v=float(cmds.getAttr('CTRL_L_legC.translateZ')+2), t=6)
        cmds.setKeyframe("CTRL_L_legC", at="translateZ", v=float(cmds.getAttr('CTRL_L_legC.translateZ')), t=12)
        cmds.setKeyframe("CTRL_L_legC", at="translateZ", v=float(cmds.getAttr('CTRL_L_legC.translateZ')-2), t=18)
        cmds.setKeyframe("CTRL_L_legC", at="translateZ", v=float(cmds.getAttr('CTRL_L_legC.translateZ')), t=24)

        cmds.setKeyframe("CTRL_L_legD", at="translateZ", v=float(cmds.getAttr('CTRL_L_legD.translateZ')), t=1)
        cmds.setKeyframe("CTRL_L_legD", at="translateZ", v=float(cmds.getAttr('CTRL_L_legD.translateZ')-2), t=6)
        cmds.setKeyframe("CTRL_L_legD", at="translateZ", v=float(cmds.getAttr('CTRL_L_legD.translateZ')), t=12)
        cmds.setKeyframe("CTRL_L_legD", at="translateZ", v=float(cmds.getAttr('CTRL_L_legD.translateZ')+2), t=18)
        cmds.setKeyframe("CTRL_L_legD", at="translateZ", v=float(cmds.getAttr('CTRL_L_legD.translateZ')), t=24)

        cmds.setKeyframe("CTRL_R_legA", at="translateZ", v=float(cmds.getAttr('CTRL_R_legA.translateZ')), t=1)
        cmds.setKeyframe("CTRL_R_legA", at="translateZ", v=float(cmds.getAttr('CTRL_R_legA.translateZ')-2), t=6)
        cmds.setKeyframe("CTRL_R_legA", at="translateZ", v=float(cmds.getAttr('CTRL_R_legA.translateZ')), t=12)
        cmds.setKeyframe("CTRL_R_legA", at="translateZ", v=float(cmds.getAttr('CTRL_R_legA.translateZ')+2), t=18)
        cmds.setKeyframe("CTRL_R_legA", at="translateZ", v=float(cmds.getAttr('CTRL_R_legA.translateZ')), t=24)

        cmds.setKeyframe("CTRL_R_legB", at="translateZ", v=float(cmds.getAttr('CTRL_R_legB.translateZ')), t=1)
        cmds.setKeyframe("CTRL_R_legB", at="translateZ", v=float(cmds.getAttr('CTRL_R_legB.translateZ')+2), t=6)
        cmds.setKeyframe("CTRL_R_legB", at="translateZ", v=float(cmds.getAttr('CTRL_R_legB.translateZ')), t=12)
        cmds.setKeyframe("CTRL_R_legB", at="translateZ", v=float(cmds.getAttr('CTRL_R_legB.translateZ')-2), t=18)
        cmds.setKeyframe("CTRL_R_legB", at="translateZ", v=float(cmds.getAttr('CTRL_R_legB.translateZ')), t=24)

        cmds.setKeyframe("CTRL_R_legC", at="translateZ", v=float(cmds.getAttr('CTRL_R_legC.translateZ')), t=1)
        cmds.setKeyframe("CTRL_R_legC", at="translateZ", v=float(cmds.getAttr('CTRL_R_legC.translateZ')-2), t=6)
        cmds.setKeyframe("CTRL_R_legC", at="translateZ", v=float(cmds.getAttr('CTRL_R_legC.translateZ')), t=12)
        cmds.setKeyframe("CTRL_R_legC", at="translateZ", v=float(cmds.getAttr('CTRL_R_legC.translateZ')+2), t=18)
        cmds.setKeyframe("CTRL_R_legC", at="translateZ", v=float(cmds.getAttr('CTRL_R_legC.translateZ')), t=24)

        cmds.setKeyframe("CTRL_R_legD", at="translateZ", v=float(cmds.getAttr('CTRL_R_legD.translateZ')), t=1)
        cmds.setKeyframe("CTRL_R_legD", at="translateZ", v=float(cmds.getAttr('CTRL_R_legD.translateZ')+2), t=6)
        cmds.setKeyframe("CTRL_R_legD", at="translateZ", v=float(cmds.getAttr('CTRL_R_legD.translateZ')), t=12)
        cmds.setKeyframe("CTRL_R_legD", at="translateZ", v=float(cmds.getAttr('CTRL_R_legD.translateZ')-2), t=18)
        cmds.setKeyframe("CTRL_R_legD", at="translateZ", v=float(cmds.getAttr('CTRL_R_legD.translateZ')), t=24)


#___________________________________________________________________________________________________ _handleJump
    def _handleJump(self):
        cmds.playbackOptions(max=30, aet=30)
        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')), t=1)
        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')-4), t=12)
        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')-4), t=12)
        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')+18), t=18)
        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')-4), t=24)
        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')), t=30)


#___________________________________________________________________________________________________ _handleAttack
    def _handleAttack(self):
        cmds.playbackOptions(max=54, aet=54)
        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')), t=1)
        cmds.setKeyframe("MoveAll", at="translateZ", v=float(cmds.getAttr('MoveAll.translateZ')), t=1)
        cmds.setKeyframe("CTRL_innerFangL", at="translateY", v=float(cmds.getAttr('CTRL_innerFangL.translateY')), t=1)
        cmds.setKeyframe("CTRL_innerFangR", at="translateY", v=float(cmds.getAttr('CTRL_innerFangR.translateY')), t=1)
        cmds.setKeyframe("L_outerFang_JA", at="rotateZ", v=float(cmds.getAttr('L_outerFang_JA.rotateZ')), t=1)
        cmds.setKeyframe("R_outerFang_JA", at="rotateZ", v=float(cmds.getAttr('R_outerFang_JA.rotateZ')), t=1)

        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')), t=36)
        cmds.setKeyframe("MoveAll", at="translateZ", v=float(cmds.getAttr('MoveAll.translateZ')-3.5), t=36)
        cmds.setKeyframe("CTRL_innerFangL", at="translateY", v=float(cmds.getAttr('CTRL_innerFangL.translateY')+1.5), t=36)
        cmds.setKeyframe("CTRL_innerFangR", at="translateY", v=float(cmds.getAttr('CTRL_innerFangR.translateY')+1.5), t=36)
        cmds.setKeyframe("L_outerFang_JA", at="rotateZ", v=float(cmds.getAttr('L_outerFang_JA.rotateZ')+45), t=36)
        cmds.setKeyframe("R_outerFang_JA", at="rotateZ", v=float(cmds.getAttr('R_outerFang_JA.rotateZ')+45), t=36)

        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')), t=48)
        cmds.setKeyframe("MoveAll", at="translateZ", v=float(cmds.getAttr('MoveAll.translateZ')-3.5), t=48)
        cmds.setKeyframe("CTRL_innerFangL", at="translateY", v=float(cmds.getAttr('CTRL_innerFangL.translateY')+1.5), t=48)
        cmds.setKeyframe("CTRL_innerFangR", at="translateY", v=float(cmds.getAttr('CTRL_innerFangR.translateY')+1.5), t=48)
        cmds.setKeyframe("L_outerFang_JA", at="rotateZ", v=float(cmds.getAttr('L_outerFang_JA.rotateZ')+45), t=48)
        cmds.setKeyframe("R_outerFang_JA", at="rotateZ", v=float(cmds.getAttr('R_outerFang_JA.rotateZ')+45), t=48)

        cmds.setKeyframe("MoveAll", at="translateY", v=float(cmds.getAttr('MoveAll.translateY')-7), t=54)
        cmds.setKeyframe("MoveAll", at="translateZ", v=float(cmds.getAttr('MoveAll.translateZ')+5.5), t=54)
        cmds.setKeyframe("CTRL_innerFangL", at="translateY", v=float(cmds.getAttr('CTRL_innerFangL.translateY')), t=54)
        cmds.setKeyframe("CTRL_innerFangR", at="translateY", v=float(cmds.getAttr('CTRL_innerFangR.translateY')), t=54)
        cmds.setKeyframe("L_outerFang_JA", at="rotateZ", v=float(cmds.getAttr('L_outerFang_JA.rotateZ')), t=54)
        cmds.setKeyframe("R_outerFang_JA", at="rotateZ", v=float(cmds.getAttr('R_outerFang_JA.rotateZ')), t=54)


#___________________________________________________________________________________________________ _handleReset
    def _handleReset(self):
        cmds.currentTime(1)
        cmds.cutKey('MoveAll', 'CTRL_R_legD', 'CTRL_R_legC', 'CTRL_R_legB', 'CTRL_R_legA', 'CTRL_L_legD', 'CTRL_L_legC',
                    'CTRL_L_legB', 'CTRL_L_legA', 'CTRL_innerFangL', 'CTRL_innerFangR', 'R_outerFang_JA', 'L_outerFang_JA')



