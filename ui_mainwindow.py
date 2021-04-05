# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 826)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(245, 20, 551, 45))
        font = QFont()
        font.setFamily(u"System-ui")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setFrameShadow(QFrame.Plain)
        self.titleLabel.setTextFormat(Qt.AutoText)
        self.titleLabel.setScaledContents(False)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(25, 160, 234, 92))
        self.initialDataLayout = QFormLayout(self.layoutWidget)
        self.initialDataLayout.setObjectName(u"initialDataLayout")
        self.initialDataLayout.setContentsMargins(0, 0, 0, 0)
        self.classPeopleLabel = QLabel(self.layoutWidget)
        self.classPeopleLabel.setObjectName(u"classPeopleLabel")

        self.initialDataLayout.setWidget(0, QFormLayout.LabelRole, self.classPeopleLabel)

        self.classSizeBox = QSpinBox(self.layoutWidget)
        self.classSizeBox.setObjectName(u"classSizeBox")
        self.classSizeBox.setMinimum(1)
        self.classSizeBox.setMaximum(10000)

        self.initialDataLayout.setWidget(0, QFormLayout.FieldRole, self.classSizeBox)

        self.groupsNumberLabel = QLabel(self.layoutWidget)
        self.groupsNumberLabel.setObjectName(u"groupsNumberLabel")

        self.initialDataLayout.setWidget(1, QFormLayout.LabelRole, self.groupsNumberLabel)

        self.groupsNumberBox = QSpinBox(self.layoutWidget)
        self.groupsNumberBox.setObjectName(u"groupsNumberBox")
        self.groupsNumberBox.setMinimum(1)
        self.groupsNumberBox.setMaximum(1)

        self.initialDataLayout.setWidget(1, QFormLayout.FieldRole, self.groupsNumberBox)

        self.tasksNumberLabel = QLabel(self.layoutWidget)
        self.tasksNumberLabel.setObjectName(u"tasksNumberLabel")

        self.initialDataLayout.setWidget(2, QFormLayout.LabelRole, self.tasksNumberLabel)

        self.tasksNumberBox = QSpinBox(self.layoutWidget)
        self.tasksNumberBox.setObjectName(u"tasksNumberBox")
        self.tasksNumberBox.setMinimum(1)
        self.tasksNumberBox.setMaximum(500)

        self.initialDataLayout.setWidget(2, QFormLayout.FieldRole, self.tasksNumberBox)

        self.examGenerationButton = QPushButton(self.centralwidget)
        self.examGenerationButton.setObjectName(u"examGenerationButton")
        self.examGenerationButton.setGeometry(QRect(880, 747, 151, 25))
        self.groupsTableLabel = QLabel(self.centralwidget)
        self.groupsTableLabel.setObjectName(u"groupsTableLabel")
        self.groupsTableLabel.setGeometry(QRect(345, 270, 351, 20))
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 750, 331, 19))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.assignedLabel = QLabel(self.layoutWidget2)
        self.assignedLabel.setObjectName(u"assignedLabel")

        self.horizontalLayout.addWidget(self.assignedLabel)

        self.assignedNumberLabel = QLabel(self.layoutWidget2)
        self.assignedNumberLabel.setObjectName(u"assignedNumberLabel")

        self.horizontalLayout.addWidget(self.assignedNumberLabel)

        self.examNameLabel = QLabel(self.centralwidget)
        self.examNameLabel.setObjectName(u"examNameLabel")
        self.examNameLabel.setGeometry(QRect(26, 117, 135, 17))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.examNameLabel.sizePolicy().hasHeightForWidth())
        self.examNameLabel.setSizePolicy(sizePolicy)
        self.examNameBox = QPlainTextEdit(self.centralwidget)
        self.examNameBox.setObjectName(u"examNameBox")
        self.examNameBox.setGeometry(QRect(190, 110, 521, 31))
        sizePolicy.setHeightForWidth(self.examNameBox.sizePolicy().hasHeightForWidth())
        self.examNameBox.setSizePolicy(sizePolicy)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 70, 1121, 16))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(32, 74, 135, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(48, 111, 203, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(40, 92, 169, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(16, 37, 67, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(21, 49, 90, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(143, 164, 195, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.line.setPalette(palette)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1046, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Generator sprawdzian\u00f3w", None))
        self.classPeopleLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba os\u00f3b w klasie", None))
        self.groupsNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba u\u0142o\u017conych grup", None))
        self.tasksNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba u\u0142o\u017conych zada\u0144", None))
        self.examGenerationButton.setText(QCoreApplication.translate("MainWindow", u"Generuj sprawdzian", None))
        self.groupsTableLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba dodatkowych os\u00f3b z zadaniami z danej grupy", None))
        self.assignedLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba os\u00f3b z przydzielonym zadaniem:", None))
        self.assignedNumberLabel.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.examNameLabel.setText(QCoreApplication.translate("MainWindow", u"Nazwa sprawdzianu", None))
        self.examNameBox.setPlainText(QCoreApplication.translate("MainWindow", u"sprawdzian", None))
    # retranslateUi

