import sys
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QVBoxLayout, QPushButton, QWidget, QStatusBar, QLabel
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtCore import Qt

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Text Editor')
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.text_edit.textChanged.connect(self.update_word_count)
        self.setCentralWidget(self.text_edit)

        self.create_actions()
        self.create_menus()
        self.create_toolbar()
        self.create_status_bar()

    def create_actions(self):
        self.open_action = QAction('Open', self)
        self.open_action.triggered.connect(self.open_file)
        self.open_action.setShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_0))

        self.save_action = QAction('Save', self)
        self.save_action.triggered.connect(self.save_file)
        self.save_action.setShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_S))

        self.copy_action = QAction('Copy', self)
        self.copy_action.triggered.connect(self.text_edit.copy)
        self.copy_action.setShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_C))

        self.cut_action = QAction('Cut', self)
        self.cut_action.triggered.connect(self.text_edit.cut)
        self.cut_action.setShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_X))

        self.paste_action = QAction('Paste', self)
        self.paste_action.triggered.connect(self.text_edit.paste)
        self.paste_action.setShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_V))

        self.undo_action = QAction('Undo', self)
        self.undo_action.triggered.connect(self.text_edit.undo)
        self.undo_action.setShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_Z))

        self.redo_action = QAction('Redo', self)
        self.redo_action.triggered.connect(self.text_edit.redo)
        self.redo_action.setShortcut(QKeySequence(Qt.KeyboardModifier.ControlModifier | Qt.Key.Key_Y))

    def create_menus(self):
        self.menu_bar = self.menuBar()

        file_menu = self.menu_bar.addMenu('File')
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)

        edit_menu = self.menu_bar.addMenu('Edit')
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.paste_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.undo_action)
        edit_menu.addAction(self.redo_action)

    def create_toolbar(self):
        self.tool_bar = self.addToolBar('Toolbar')
        self.tool_bar.addAction(self.open_action)
        self.tool_bar.addAction(self.save_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.copy_action)
        self.tool_bar.addAction(self.cut_action)
        self.tool_bar.addAction(self.paste_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.undo_action)
        self.tool_bar.addAction(self.redo_action)

    def create_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        # word count and character count
        self.word_count_label = QLabel("Word Count: 0")
        self.character_count_label = QLabel("Character Count: 0")
        self.status_bar.addWidget(self.word_count_label)
        self.status_bar.addWidget(self.character_count_label)

    def update_word_count(self):
        text = self.text_edit.toPlainText()
        words = text.split()
        characters = len(text)
        word_count = len(words)

        self.word_count_label.setText(f"Word Count: {word_count}")
        self.character_count_label.setText(f"Character Count: {characters}")

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName()
        if file_path:
            with open(file_path, 'r') as file:
                self.text_edit.setPlainText(file.read())

    def save_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getSaveFileName()
        if file_path:
            if not file_path.endswith('.txt'):
                file_path += '.txt'
            with open(file_path, 'w') as file:
                file.write(self.text_edit.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec())

