# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmDataEditorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmDataEditor(object):
    def setupUi(self, frmDataEditor):
        frmDataEditor.setObjectName("frmDataEditor")
        frmDataEditor.resize(1016, 751)
        self.centralwidget = QtWidgets.QWidget(frmDataEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget2.setObjectName("tabWidget2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnInFile = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInFile.sizePolicy().hasHeightForWidth())
        self.btnInFile.setSizePolicy(sizePolicy)
        self.btnInFile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-opened-folder-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInFile.setIcon(icon)
        self.btnInFile.setIconSize(QtCore.QSize(48, 48))
        self.btnInFile.setObjectName("btnInFile")
        self.horizontalLayout.addWidget(self.btnInFile)
        self.btnMerge = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMerge.sizePolicy().hasHeightForWidth())
        self.btnMerge.setSizePolicy(sizePolicy)
        self.btnMerge.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-add-folder-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMerge.setIcon(icon1)
        self.btnMerge.setIconSize(QtCore.QSize(48, 48))
        self.btnMerge.setObjectName("btnMerge")
        self.horizontalLayout.addWidget(self.btnMerge)
        self.btnSave = QtWidgets.QPushButton(self.tab)
        self.btnSave.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-save-close-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon2)
        self.btnSave.setIconSize(QtCore.QSize(48, 48))
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnSaveAs = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveAs.sizePolicy().hasHeightForWidth())
        self.btnSaveAs.setSizePolicy(sizePolicy)
        self.btnSaveAs.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-save-all-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveAs.setIcon(icon3)
        self.btnSaveAs.setIconSize(QtCore.QSize(48, 48))
        self.btnSaveAs.setObjectName("btnSaveAs")
        self.horizontalLayout.addWidget(self.btnSaveAs)
        self.btnRefresh = QtWidgets.QPushButton(self.tab)
        self.btnRefresh.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon4)
        self.btnRefresh.setIconSize(QtCore.QSize(48, 48))
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout.addWidget(self.btnRefresh)
        self.btnValue = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnValue.sizePolicy().hasHeightForWidth())
        self.btnValue.setSizePolicy(sizePolicy)
        self.btnValue.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-eye-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnValue.setIcon(icon5)
        self.btnValue.setIconSize(QtCore.QSize(48, 48))
        self.btnValue.setObjectName("btnValue")
        self.horizontalLayout.addWidget(self.btnValue)
        self.btnIn = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnIn.sizePolicy().hasHeightForWidth())
        self.btnIn.setSizePolicy(sizePolicy)
        self.btnIn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-forward-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIn.setIcon(icon6)
        self.btnIn.setIconSize(QtCore.QSize(48, 48))
        self.btnIn.setObjectName("btnIn")
        self.horizontalLayout.addWidget(self.btnIn)
        self.txtInside = QtWidgets.QSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtInside.sizePolicy().hasHeightForWidth())
        self.txtInside.setSizePolicy(sizePolicy)
        self.txtInside.setMinimumSize(QtCore.QSize(60, 54))
        self.txtInside.setMaximumSize(QtCore.QSize(6, 54))
        self.txtInside.setMaximum(999999999)
        self.txtInside.setObjectName("txtInside")
        self.horizontalLayout.addWidget(self.txtInside)
        self.btnBack = QtWidgets.QPushButton(self.tab)
        self.btnBack.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy)
        self.btnBack.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-back-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon7)
        self.btnBack.setIconSize(QtCore.QSize(48, 48))
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnRename = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRename.sizePolicy().hasHeightForWidth())
        self.btnRename.setSizePolicy(sizePolicy)
        self.btnRename.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-rename-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRename.setIcon(icon8)
        self.btnRename.setIconSize(QtCore.QSize(48, 48))
        self.btnRename.setObjectName("btnRename")
        self.horizontalLayout_4.addWidget(self.btnRename)
        self.btnRemove = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemove.sizePolicy().hasHeightForWidth())
        self.btnRemove.setSizePolicy(sizePolicy)
        self.btnRemove.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemove.setIcon(icon9)
        self.btnRemove.setIconSize(QtCore.QSize(48, 48))
        self.btnRemove.setObjectName("btnRemove")
        self.horizontalLayout_4.addWidget(self.btnRemove)
        self.btnTranspose = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTranspose.sizePolicy().hasHeightForWidth())
        self.btnTranspose.setSizePolicy(sizePolicy)
        self.btnTranspose.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-rotate-left-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTranspose.setIcon(icon10)
        self.btnTranspose.setIconSize(QtCore.QSize(48, 48))
        self.btnTranspose.setObjectName("btnTranspose")
        self.horizontalLayout_4.addWidget(self.btnTranspose)
        self.btnScale = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnScale.sizePolicy().hasHeightForWidth())
        self.btnScale.setSizePolicy(sizePolicy)
        self.btnScale.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-normal-distribution-histogram-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnScale.setIcon(icon11)
        self.btnScale.setIconSize(QtCore.QSize(48, 48))
        self.btnScale.setObjectName("btnScale")
        self.horizontalLayout_4.addWidget(self.btnScale)
        self.btnClone = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClone.sizePolicy().hasHeightForWidth())
        self.btnClone.setSizePolicy(sizePolicy)
        self.btnClone.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-clone-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClone.setIcon(icon12)
        self.btnClone.setIconSize(QtCore.QSize(48, 48))
        self.btnClone.setObjectName("btnClone")
        self.horizontalLayout_4.addWidget(self.btnClone)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btnReshape = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReshape.sizePolicy().hasHeightForWidth())
        self.btnReshape.setSizePolicy(sizePolicy)
        self.btnReshape.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-3d-object-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReshape.setIcon(icon13)
        self.btnReshape.setIconSize(QtCore.QSize(48, 48))
        self.btnReshape.setObjectName("btnReshape")
        self.horizontalLayout_4.addWidget(self.btnReshape)
        self.btnSelectPart = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSelectPart.sizePolicy().hasHeightForWidth())
        self.btnSelectPart.setSizePolicy(sizePolicy)
        self.btnSelectPart.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-3d-model-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelectPart.setIcon(icon14)
        self.btnSelectPart.setIconSize(QtCore.QSize(48, 48))
        self.btnSelectPart.setObjectName("btnSelectPart")
        self.horizontalLayout_4.addWidget(self.btnSelectPart)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btnHConcat = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHConcat.sizePolicy().hasHeightForWidth())
        self.btnHConcat.setSizePolicy(sizePolicy)
        self.btnHConcat.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-select-row-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHConcat.setIcon(icon15)
        self.btnHConcat.setIconSize(QtCore.QSize(48, 48))
        self.btnHConcat.setObjectName("btnHConcat")
        self.horizontalLayout_4.addWidget(self.btnHConcat)
        self.btnVConcat = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVConcat.sizePolicy().hasHeightForWidth())
        self.btnVConcat.setSizePolicy(sizePolicy)
        self.btnVConcat.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-select-column-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVConcat.setIcon(icon16)
        self.btnVConcat.setIconSize(QtCore.QSize(48, 48))
        self.btnVConcat.setObjectName("btnVConcat")
        self.horizontalLayout_4.addWidget(self.btnVConcat)
        self.btnCConcat = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCConcat.sizePolicy().hasHeightForWidth())
        self.btnCConcat.setSizePolicy(sizePolicy)
        self.btnCConcat.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-select-cell-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCConcat.setIcon(icon17)
        self.btnCConcat.setIconSize(QtCore.QSize(48, 48))
        self.btnCConcat.setObjectName("btnCConcat")
        self.horizontalLayout_4.addWidget(self.btnCConcat)
        self.btnConcat = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConcat.sizePolicy().hasHeightForWidth())
        self.btnConcat.setSizePolicy(sizePolicy)
        self.btnConcat.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-table-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConcat.setIcon(icon18)
        self.btnConcat.setIconSize(QtCore.QSize(48, 48))
        self.btnConcat.setObjectName("btnConcat")
        self.horizontalLayout_4.addWidget(self.btnConcat)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.lwData = QtWidgets.QTreeWidget(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lwData.setFont(font)
        self.lwData.setObjectName("lwData")
        self.lwData.headerItem().setText(0, "1")
        self.verticalLayout_2.addWidget(self.lwData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_33 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_2.addWidget(self.label_33)
        self.txtInFile = QtWidgets.QLineEdit(self.tab_3)
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.horizontalLayout_2.addWidget(self.txtInFile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnRun = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRun.sizePolicy().hasHeightForWidth())
        self.btnRun.setSizePolicy(sizePolicy)
        self.btnRun.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-play-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRun.setIcon(icon19)
        self.btnRun.setIconSize(QtCore.QSize(48, 48))
        self.btnRun.setObjectName("btnRun")
        self.horizontalLayout_3.addWidget(self.btnRun)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btnOpenCode = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenCode.sizePolicy().hasHeightForWidth())
        self.btnOpenCode.setSizePolicy(sizePolicy)
        self.btnOpenCode.setText("")
        self.btnOpenCode.setIcon(icon)
        self.btnOpenCode.setIconSize(QtCore.QSize(48, 48))
        self.btnOpenCode.setObjectName("btnOpenCode")
        self.horizontalLayout_3.addWidget(self.btnOpenCode)
        self.btnSaveCode = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveCode.sizePolicy().hasHeightForWidth())
        self.btnSaveCode.setSizePolicy(sizePolicy)
        self.btnSaveCode.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/Icons/icons8-save-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveCode.setIcon(icon20)
        self.btnSaveCode.setIconSize(QtCore.QSize(48, 48))
        self.btnSaveCode.setObjectName("btnSaveCode")
        self.horizontalLayout_3.addWidget(self.btnSaveCode)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.Code = QtWidgets.QWidget(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Code.sizePolicy().hasHeightForWidth())
        self.Code.setSizePolicy(sizePolicy)
        self.Code.setObjectName("Code")
        self.verticalLayout_4.addWidget(self.Code)
        self.lblCodeFile = QtWidgets.QLabel(self.tab_4)
        self.lblCodeFile.setObjectName("lblCodeFile")
        self.verticalLayout_4.addWidget(self.lblCodeFile)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.tabWidget2.addTab(self.tab_4, "")
        self.horizontalLayout_6.addWidget(self.tabWidget2)
        frmDataEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmDataEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setGeometry(QtCore.QRect(309, 169, 184, 69))
        self.menuFile.setTitle("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("../Icons/icons8-menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuFile.setIcon(icon21)
        self.menuFile.setObjectName("menuFile")
        frmDataEditor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmDataEditor)
        self.statusbar.setObjectName("statusbar")
        frmDataEditor.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(frmDataEditor)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("../Icons/icons8-shutdown-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon22)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(frmDataEditor)
        self.tabWidget2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(frmDataEditor)

    def retranslateUi(self, frmDataEditor):
        _translate = QtCore.QCoreApplication.translate
        frmDataEditor.setWindowTitle(_translate("frmDataEditor", "MainWindow"))
        self.btnInFile.setToolTip(_translate("frmDataEditor", "Open File"))
        self.btnMerge.setToolTip(_translate("frmDataEditor", "Merge to current data"))
        self.btnSave.setToolTip(_translate("frmDataEditor", "Save"))
        self.btnSaveAs.setToolTip(_translate("frmDataEditor", "Save as ..."))
        self.btnRefresh.setToolTip(_translate("frmDataEditor", "Reload File"))
        self.btnValue.setToolTip(_translate("frmDataEditor", "View Data"))
        self.btnIn.setToolTip(_translate("frmDataEditor", "Go to Index"))
        self.btnBack.setToolTip(_translate("frmDataEditor", "Back"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmDataEditor", "General"))
        self.btnRename.setToolTip(_translate("frmDataEditor", "Rename"))
        self.btnRemove.setToolTip(_translate("frmDataEditor", "Remove"))
        self.btnTranspose.setToolTip(_translate("frmDataEditor", "Transpose"))
        self.btnScale.setToolTip(_translate("frmDataEditor", "Zero Score"))
        self.btnClone.setToolTip(_translate("frmDataEditor", "Clone"))
        self.btnReshape.setToolTip(_translate("frmDataEditor", "Reshape"))
        self.btnSelectPart.setToolTip(_translate("frmDataEditor", "Select Part of Data"))
        self.btnHConcat.setToolTip(_translate("frmDataEditor", "Vertically concatenate"))
        self.btnVConcat.setToolTip(_translate("frmDataEditor", "Horizontally concatenate"))
        self.btnCConcat.setToolTip(_translate("frmDataEditor", "Cross concatenate"))
        self.btnConcat.setToolTip(_translate("frmDataEditor", "Axis n concatenate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmDataEditor", "Feature"))
        self.lwData.setSortingEnabled(True)
        self.label_33.setText(_translate("frmDataEditor", "Address"))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_3), _translate("frmDataEditor", "Data"))
        self.btnRun.setToolTip(_translate("frmDataEditor", "Run Code"))
        self.btnOpenCode.setToolTip(_translate("frmDataEditor", "Open Code File"))
        self.btnSaveCode.setToolTip(_translate("frmDataEditor", "Save Code File"))
        self.lblCodeFile.setText(_translate("frmDataEditor", "TextLabel"))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_4), _translate("frmDataEditor", "Edit"))
        self.actionExit.setText(_translate("frmDataEditor", "Exit"))

import icon_rc
