import sys
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QAction

def open_file():
    file_dialog = QFileDialog(main_window)
    file_path, _ = file_dialog.getOpenFileName()
    if file_path:
        with open(file_path, 'r') as file:
            text_edit.setPlainText(file.read())

def save_file():
    file_dialog = QFileDialog(main_window)
    file_path, _ = file_dialog.getSaveFileName()
    if file_path:
        if not file_path.endswith('.txt'):
            file_path += '.txt'
        with open(file_path, 'w') as file:
            file.write(text_edit.toPlainText())

app = QApplication(sys.argv)
main_window = QMainWindow()

main_window.setWindowTitle('Text Editor')
main_window.setGeometry(100, 100, 800, 600)

text_edit = QTextEdit(main_window)
main_window.setCentralWidget(text_edit)

open_action = QAction('Open', main_window)
save_action = QAction('Save', main_window)

open_action.triggered.connect(open_file)
save_action.triggered.connect(save_file)

toolbar = main_window.addToolBar('Toolbar')
toolbar.addAction(open_action)
toolbar.addAction(save_action)

main_window.show()
sys.exit(app.exec())

