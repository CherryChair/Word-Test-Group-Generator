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
        # self.groupsTable = QScrollArea(self.centralwidget)
        # self.groupsTable.setObjectName(u"groupsTable")
        # self.groupsTable.setGeometry(QRect(30, 270, 711, 281))
        # self.groupsTable.setWidgetResizable(True)
        # self.scrollAreaWidgetContents = QWidget()
        # self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        # self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 709, 279))
        # self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        # self.verticalLayout.setObjectName(u"verticalLayout")
        # self.tasksDivisionLayout_1 = QHBoxLayout()
        # self.tasksDivisionLayout_1.setObjectName(u"tasksDivisionLayout_1")
        # self.tasksDivisionLabel_1 = QLabel(self.scrollAreaWidgetContents)
        # self.tasksDivisionLabel_1.setObjectName(u"tasksDivisionLabel_1")

        # self.tasksDivisionLayout_1.addWidget(self.tasksDivisionLabel_1)

        # self.tasksDivisionBox_1 = QSpinBox(self.scrollAreaWidgetContents)
        # self.tasksDivisionBox_1.setObjectName(u"tasksDivisionBox_1")

        # self.tasksDivisionLayout_1.addWidget(self.tasksDivisionBox_1)


        # self.verticalLayout.addLayout(self.tasksDivisionLayout_1)

        # self.groupsTable.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 130, 221, 92))
        self.initialDataLayout = QFormLayout(self.layoutWidget)
        self.initialDataLayout.setObjectName(u"initialDataLayout")
        self.initialDataLayout.setContentsMargins(0, 0, 0, 0)
        self.classPeopleLabel = QLabel(self.layoutWidget)
        self.classPeopleLabel.setObjectName(u"classPeopleLabel")

        self.initialDataLayout.setWidget(0, QFormLayout.LabelRole, self.classPeopleLabel)

        self.classSizeBox = QSpinBox(self.layoutWidget)
        self.classSizeBox.setObjectName(u"classSizeBox")
        self.classSizeBox.setMinimum(1)
        self.classSizeBox.setMaximum(200)

        self.initialDataLayout.setWidget(0, QFormLayout.FieldRole, self.classSizeBox)

        self.groupsNumberLabel = QLabel(self.layoutWidget)
        self.groupsNumberLabel.setObjectName(u"groupsNumberLabel")

        self.initialDataLayout.setWidget(1, QFormLayout.LabelRole, self.groupsNumberLabel)

        self.groupsNumberBox = QSpinBox(self.layoutWidget)
        self.groupsNumberBox.setObjectName(u"groupsNumberBox")
        self.groupsNumberBox.setMinimum(1)

        self.initialDataLayout.setWidget(1, QFormLayout.FieldRole, self.groupsNumberBox)

        self.tasksNumberLabel = QLabel(self.layoutWidget)
        self.tasksNumberLabel.setObjectName(u"tasksNumberLabel")

        self.initialDataLayout.setWidget(2, QFormLayout.LabelRole, self.tasksNumberLabel)

        self.tasksNumberBox = QSpinBox(self.layoutWidget)
        self.tasksNumberBox.setObjectName(u"tasksNumberBox")
        self.tasksNumberBox.setMinimum(1)

        self.initialDataLayout.setWidget(2, QFormLayout.FieldRole, self.tasksNumberBox)

        self.examGenerationButton = QPushButton(self.centralwidget)
        self.examGenerationButton.setObjectName(u"examGenerationButton")
        self.examGenerationButton.setGeometry(QRect(590, 560, 151, 25))
        self.groupsTableLabel = QLabel(self.centralwidget)
        self.groupsTableLabel.setObjectName(u"groupsTableLabel")
        self.groupsTableLabel.setGeometry(QRect(200, 240, 351, 20))
        self.examNameLabel = QLabel(self.centralwidget)
        self.examNameLabel.setObjectName(u"examNameLabel")
        self.examNameLabel.setGeometry(QRect(30, 80, 135, 17))
        self.examNameBox = QPlainTextEdit(self.centralwidget)
        self.examNameBox.setObjectName(u"examNameBox")
        self.examNameBox.setGeometry(QRect(170, 70, 568, 29))
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
        # self.tasksDivisionLabel_1.setText(QCoreApplication.translate("MainWindow", u"Grupa nr 1", None))
        self.classPeopleLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba os\u00f3b w klasie", None))
        self.groupsNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba u\u0142o\u017conych grup", None))
        self.tasksNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba u\u0142o\u017conych zada\u0144", None))
        self.examGenerationButton.setText(QCoreApplication.translate("MainWindow", u"Generuj sprawdzian", None))
        self.groupsTableLabel.setText(QCoreApplication.translate("MainWindow", u"Liczba dodatkowych os\u00f3b z zadaniami z danej grupy", None))
        self.examNameLabel.setText(QCoreApplication.translate("MainWindow", u"Nazwa sprawdzianu", None))
        self.examNameBox.setPlainText(QCoreApplication.translate("MainWindow", u"sprawdzian", None))
    # retranslateUi

