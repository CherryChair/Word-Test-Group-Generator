from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QSpinBox, QLabel, QHBoxLayout, QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea
from PySide2.QtCore import QRect
from PySide2.QtCore import QCoreApplication
from exam_generation import get_task_division, create_word_doc, get_list_of_occurances
import sys


class ExamGeneratorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupScrollArea()
        self.fillScrollArea()
        self.ui.groupsNumberBox.valueChanged.connect(self.changeScrollArea)
        self.ui.examGenerationButton.clicked.connect(self.create_doc)

    def changeScrollArea(self):
        for item in self.task_layouts + self.task_boxes + self.task_labels:
            item.deleteLater()
        self.fillScrollArea()

    def setupScrollArea(self):
        self.ui.groupsTable = QScrollArea(self.ui.centralwidget)
        self.ui.groupsTable.setObjectName(u"groupsTable")
        self.ui.groupsTable.setGeometry(QRect(30, 270, 711, 281))
        self.ui.groupsTable.setWidgetResizable(True)
        self.ui.scrollAreaWidgetContents = QWidget()
        self.ui.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.ui.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 709, 279))
        self.ui.verticalLayout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.ui.verticalLayout.setObjectName(u"verticalLayout")
        self.ui.groupsTable.setWidget(self.ui.scrollAreaWidgetContents)

    def fillScrollArea(self):
        self.task_layouts = []
        self.task_boxes = []
        self.task_labels = []
        for i in range(0, self.ui.groupsNumberBox.value()):
            self.task_layouts.append(QHBoxLayout())
            self.task_layouts[i].setObjectName(f"tasksDivisionLayout_{i+1}")
            self.task_labels.append(QLabel(self.ui.scrollAreaWidgetContents))
            self.task_labels[i].setObjectName(f"tasksDivisionLabel_{i+1}")

            self.task_layouts[i].addWidget(self.task_labels[i])

            self.task_boxes.append(QSpinBox(self.ui.scrollAreaWidgetContents))
            self.task_boxes[i].setObjectName(f"tasksDivisionBox_{i+1}")

            self.task_layouts[i].addWidget(self.task_boxes[i])

            self.ui.verticalLayout.addLayout(self.task_layouts[i])
            self.task_labels[i].setText(QCoreApplication.translate("MainWindow", f"Grupa nr {i+1}", None))

    def create_doc(self):
        people_number = self.ui.classSizeBox.value()
        groups_number = self.ui.groupsNumberBox.value()
        tasks_number = self.ui.tasksNumberBox.value()
        group_task_divison = []
        filename = self.ui.examNameBox.toPlainText()
        for group in range(0, groups_number):
            group_task_divison.append(self.task_boxes[group].value())
        info_table = []
        info_table.append(people_number)
        info_table.append(groups_number)
        info_table.append(tasks_number)
        info_table.append(group_task_divison)
        task_division = get_task_division(info_table)
        create_word_doc(task_division, filename)
        list_of_occurances = get_list_of_occurances(task_division)


def guiMain(args):
    app = QApplication(args)
    window = ExamGeneratorWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)


# if __name__ == "__main__":
#     main_window = Ui_MainWindow()
#     init_task_division_layout = main_window.ui.tasksDivisionLayout_1
#     init_task_division_box = main_window.ui.tasksDivisionBox_1
#     init_task_division_label = main_window.ui.tasksDivisionLabel_1
#     main_window.ui.task_layouts = [init_task_division_label]
#     main_window.ui.task_boxes = [init_task_division_box]
#     main_window.ui.task_labels = [init_task_division_label]
#     for i in range(1, 10):
#         main_window.ui.task_layouts.append(QHBoxLayout())
#         main_window.ui.task_layouts[i].setObjectName(u"tasksDivisionLayout_1")
#         main_window.ui.task_labels.append(QLabel(main_window.ui.scrollAreaWidgetContents))
#         main_window.ui.task_labels[i].setObjectName(u"tasksDivisionLabel_1")

#         main_window.ui.task_layouts[i].addWidget(main_window.ui.task_labels[i])

#         main_window.ui.task_boxes.append(QSpinBox(main_window.ui.scrollAreaWidgetContents))
#         main_window.ui.task_boxes[i].setObjectName(u"tasksDivisionBox_1")

#         main_window.ui.task_layouts[i].addWidget(main_window.ui.task_boxes[i])
#         main_window.ui.task_labels.setText(QCoreApplication.translate("MainWindow", f"Grupa nr {i}", None))
#     main_window.show()
#     sys.exit(app.exec_())
