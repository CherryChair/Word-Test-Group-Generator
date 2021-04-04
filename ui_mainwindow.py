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
        MainWindow.resize(774, 667)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(200, 10, 354, 45))
        font = QFont()
        font.setFamily(u"Ubuntu Condensed")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setFrameShadow(QFrame.Plain)
        self.titleLabel.setScaledContents(False)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 130, 234, 92))
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
        self.examGenerationButton.setGeometry(QRect(590, 570, 151, 25))
        self.groupsTableLabel = QLabel(self.centralwidget)
        self.groupsTableLabel.setObjectName(u"groupsTableLabel")
        self.groupsTableLabel.setGeometry(QRect(200, 240, 351, 20))
        self.examNameLabel = QLabel(self.centralwidget)
        self.examNameLabel.setObjectName(u"examNameLabel")
        self.examNameLabel.setGeometry(QRect(30, 80, 135, 17))
        self.examNameBox = QPlainTextEdit(self.centralwidget)
        self.examNameBox.setObjectName(u"examNameBox")
        self.examNameBox.setGeometry(QRect(170, 70, 568, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 570, 331, 19))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.assignedLabel = QLabel(self.widget)
        self.assignedLabel.setObjectName(u"assignedLabel")

        self.horizontalLayout.addWidget(self.assignedLabel)

        self.assignedNumberLabel = QLabel(self.widget)
        self.assignedNumberLabel.setObjectName(u"assignedNumberLabel")

        self.horizontalLayout.addWidget(self.assignedNumberLabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 774, 22))
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
        self.examNameLabel.setText(QCoreApplication.translate("MainWindow", u"Nazwa sprawdzianu", None))
        self.examNameBox.setPlainText(QCoreApplication.translate("MainWindow", u"sprawdzian", None))
        self.assignedLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba os\u00f3b z przydzielonym zadaniem:", None))
        self.assignedNumberLabel.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
    # retranslateUi

