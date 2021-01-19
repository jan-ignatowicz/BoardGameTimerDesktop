# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/resources/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(841, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_2.addWidget(self.exitButton, 0, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 7, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 8, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 6, 7, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 1, 7, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 8, 8, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 0, 2, 8, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 1, 5, 1, 1)
        self.playerNameLabel = QtWidgets.QLabel(Form)
        self.playerNameLabel.setObjectName("playerNameLabel")
        self.gridLayout_2.addWidget(self.playerNameLabel, 0, 5, 1, 1)
        self.addGameButton = QtWidgets.QPushButton(Form)
        self.addGameButton.setObjectName("addGameButton")
        self.gridLayout_2.addWidget(self.addGameButton, 7, 1, 1, 1)
        self.myGamesLabel = QtWidgets.QLabel(Form)
        self.myGamesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.myGamesLabel.setObjectName("myGamesLabel")
        self.gridLayout_2.addWidget(self.myGamesLabel, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 3, 7, 1, 1)
        self.myGamesListWidget = QtWidgets.QListWidget(Form)
        self.myGamesListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.myGamesListWidget.setObjectName("myGamesListWidget")
        item = QtWidgets.QListWidgetItem()
        self.myGamesListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.myGamesListWidget.addItem(item)
        self.gridLayout_2.addWidget(self.myGamesListWidget, 1, 1, 6, 1)
        self.gameQuickViewFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gameQuickViewFrame.sizePolicy().hasHeightForWidth())
        self.gameQuickViewFrame.setSizePolicy(sizePolicy)
        self.gameQuickViewFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameQuickViewFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gameQuickViewFrame.setObjectName("gameQuickViewFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gameQuickViewFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gameNameLabel = QtWidgets.QLabel(self.gameQuickViewFrame)
        self.gameNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gameNameLabel.setObjectName("gameNameLabel")
        self.gridLayout_4.addWidget(self.gameNameLabel, 0, 3, 1, 2)
        self.playersNumberSpinBox = QtWidgets.QSpinBox(self.gameQuickViewFrame)
        self.playersNumberSpinBox.setMinimum(1)
        self.playersNumberSpinBox.setMaximum(100)
        self.playersNumberSpinBox.setObjectName("playersNumberSpinBox")
        self.gridLayout_4.addWidget(self.playersNumberSpinBox, 2, 4, 1, 2)
        self.playersNumberLabel = QtWidgets.QLabel(self.gameQuickViewFrame)
        self.playersNumberLabel.setObjectName("playersNumberLabel")
        self.gridLayout_4.addWidget(self.playersNumberLabel, 2, 3, 1, 1)
        self.roundTimeInfoLabel = QtWidgets.QLabel(self.gameQuickViewFrame)
        self.roundTimeInfoLabel.setObjectName("roundTimeInfoLabel")
        self.gridLayout_4.addWidget(self.roundTimeInfoLabel, 3, 4, 1, 2)
        self.gameTimeLabel = QtWidgets.QLabel(self.gameQuickViewFrame)
        self.gameTimeLabel.setObjectName("gameTimeLabel")
        self.gridLayout_4.addWidget(self.gameTimeLabel, 4, 3, 1, 1)
        self.gameTimeInfoLabel = QtWidgets.QLabel(self.gameQuickViewFrame)
        self.gameTimeInfoLabel.setObjectName("gameTimeInfoLabel")
        self.gridLayout_4.addWidget(self.gameTimeInfoLabel, 4, 4, 1, 2)
        self.editGameButton = QtWidgets.QPushButton(self.gameQuickViewFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editGameButton.sizePolicy().hasHeightForWidth())
        self.editGameButton.setSizePolicy(sizePolicy)
        self.editGameButton.setObjectName("editGameButton")
        self.gridLayout_4.addWidget(self.editGameButton, 8, 6, 1, 1)
        self.deleteGameButton = QtWidgets.QPushButton(self.gameQuickViewFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteGameButton.sizePolicy().hasHeightForWidth())
        self.deleteGameButton.setSizePolicy(sizePolicy)
        self.deleteGameButton.setObjectName("deleteGameButton")
        self.gridLayout_4.addWidget(self.deleteGameButton, 8, 0, 1, 1)
        self.roundTimeLabel = QtWidgets.QLabel(self.gameQuickViewFrame)
        self.roundTimeLabel.setObjectName("roundTimeLabel")
        self.gridLayout_4.addWidget(self.roundTimeLabel, 3, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 8, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem11, 1, 3, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 8, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem13, 5, 3, 1, 2)
        self.gridLayout_2.addWidget(self.gameQuickViewFrame, 2, 4, 3, 2)
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setObjectName("playButton")
        self.gridLayout_2.addWidget(self.playButton, 6, 4, 1, 2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem14, 5, 4, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exitButton.setText(_translate("Form", "EXIT"))
        self.playerNameLabel.setText(_translate("Form", "PLAYER NAME"))
        self.addGameButton.setText(_translate("Form", "ADD GAME"))
        self.myGamesLabel.setText(_translate("Form", "My games"))
        __sortingEnabled = self.myGamesListWidget.isSortingEnabled()
        self.myGamesListWidget.setSortingEnabled(False)
        item = self.myGamesListWidget.item(0)
        item.setText(_translate("Form", "Game 1"))
        item = self.myGamesListWidget.item(1)
        item.setText(_translate("Form", "Game 2"))
        self.myGamesListWidget.setSortingEnabled(__sortingEnabled)
        self.gameNameLabel.setText(_translate("Form", "GAME NAME"))
        self.playersNumberLabel.setText(_translate("Form", "players"))
        self.roundTimeInfoLabel.setText(_translate("Form", "00:00"))
        self.gameTimeLabel.setText(_translate("Form", "game time"))
        self.gameTimeInfoLabel.setText(_translate("Form", "00:00"))
        self.editGameButton.setText(_translate("Form", "EDIT"))
        self.deleteGameButton.setText(_translate("Form", "DELETE"))
        self.roundTimeLabel.setText(_translate("Form", "round time"))
        self.playButton.setText(_translate("Form", "PLAY"))
