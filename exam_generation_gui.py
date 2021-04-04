from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QSpinBox, QLabel, QHBoxLayout, QApplication, QTableWidgetItem
from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QScrollArea, QMessageBox, QTableWidget
from PySide2.QtCore import QCoreApplication, QRect
from exam_generation import get_task_division, create_word_doc, get_list_of_occurances
import sys


class ExamGeneratorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.filling = []
        self.ui.setupUi(self)
        self.setupScrollArea()
        self.fillScrollArea()
        self.task_boxes[0].valueChanged.connect(self.updateAssignment)
        self.initial_filling()
        self.ui.groupsNumberBox.valueChanged.connect(self.changeScrollArea)
        self.ui.classSizeBox.valueChanged.connect(self.peopleValueChange)
        self.ui.examGenerationButton.clicked.connect(self.create_doc)

    def updateAssignment(self):
        task_box_sum = 0
        for box in self.task_boxes:
            task_box_sum += box.value()
        self.ui.assignedNumberLabel.setText(f"{task_box_sum + self.ui.groupsNumberBox.value()}/{self.ui.classSizeBox.value()}")

    def changeScrollArea(self):
        for item in self.task_layouts + self.task_boxes + self.task_labels:
            item.deleteLater()
        self.fillScrollArea()
        self.initial_filling()
        for box in self.task_boxes:
            box.valueChanged.connect(self.updateAssignment)
        self.ui.assignedNumberLabel.setText(f"{sum(self.filling) + self.ui.groupsNumberBox.value()}/{self.ui.classSizeBox.value()}")

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

    def peopleValueChange(self):
        self.ui.groupsNumberBox.setMaximum(self.ui.classSizeBox.value())
        self.initial_filling()
        self.ui.assignedNumberLabel.setText(f"{sum(self.filling) + self.ui.groupsNumberBox.value()}/{self.ui.classSizeBox.value()}")

    def create_doc(self):
        people_number = self.ui.classSizeBox.value()
        groups_number = self.ui.groupsNumberBox.value()
        tasks_number = self.ui.tasksNumberBox.value()
        group_task_divison = []
        for box in self.task_boxes:
            group_task_divison.append(box.value())
        if sum(group_task_divison) + groups_number > people_number:
            msg = QMessageBox(QMessageBox.Information, "Błąd!", "Przydzielono zadanie zbyt wielu osobom.")
            msg.show()
            msg.exec_()
            return
        if sum(group_task_divison) + groups_number < people_number:
            msg = QMessageBox(QMessageBox.Information, "Błąd!", "Przydzielono zadanie za małej ilości osób.")
            msg.show()
            msg.exec_()
            return
        filename = self.ui.examNameBox.toPlainText()
        info_table = []
        info_table.append(people_number)
        info_table.append(groups_number)
        info_table.append(tasks_number)
        info_table.append(group_task_divison)
        task_division = get_task_division(info_table)
        try:
            create_word_doc(task_division, filename)
        except Exception as e:
            msg = QMessageBox(QMessageBox.Information, "Błąd!", f"Niepoprawnie ustawiony folder z zadaniami.")
            msg.show()
            msg.exec_()
            return
        list_of_occurances = get_list_of_occurances(task_division)
        data = []
        for item, i in zip(list_of_occurances, range(0, len(list_of_occurances))):
            data.append([])
            for key in item:
                data[i].append(item[key])
        msg = QWidget()
        msg.setWindowTitle("Tabela powtórzeń")
        msg.table = QTableWidget(people_number, tasks_number + 1)
        msg.table.setObjectName('tableWidget')
        horizontal_headers = ["0 powtórzeń", "1 powtórzenie", "2 powtórzenia", "3 powtórzenia", "4 powtórzenia"]
        if tasks_number <= 4:
            msg.table.setHorizontalHeaderLabels(horizontal_headers[:tasks_number + 1])
        else:
            for task_number in range(5, tasks_number + 1):
                horizontal_headers += [f"{task_number} powtórzeń"]
            msg.table.setHorizontalHeaderLabels(horizontal_headers)
        for person_number in range(0, people_number):
            for reapeted_tasks in range(0, tasks_number + 1):
                item = QTableWidgetItem(str(list_of_occurances[person_number][reapeted_tasks]))
                msg.table.setItem(person_number, reapeted_tasks, item)
        msg.layout = QVBoxLayout()
        msg.layout.addWidget(msg.table)
        msg.setLayout(msg.layout)
        msg.showMaximized()
        msg.exec_()


    def initial_filling(self):
        people_number = self.ui.classSizeBox.value()
        groups_number = self.ui.groupsNumberBox.value()
        self.filling = [0]*(groups_number)
        i = 0
        while sum(self.filling) != people_number - groups_number:
            self.filling[i] += 1
            i += 1
            i = i % groups_number
        if not self.filling[-1]:
            self.filling[-1] = people_number // groups_number - 1
        for box, number in zip(self.task_boxes, self.filling):
            box.setValue(number)


def guiMain(args):
    app = QApplication(args)
    window = ExamGeneratorWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
