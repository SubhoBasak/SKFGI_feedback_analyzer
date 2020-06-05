import sys
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtGui import QIcon
from main_window import Ui_MainWindow

import pandas as pd

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Setup():
    def __init__(self):
        self.data = None

        self.root = QMainWindow()
        self.window = Ui_MainWindow()
        self.window.setupUi(self.root)
        self.window.retranslateUi(self.root)

        self.window.menuFile.addAction(QIcon('icons/open.ico'), 'Open', self.open_func, 'Ctrl+O')
        self.window.menuFile.addSeparator()
        self.window.menuFile.addAction(QIcon('icons/save.ico'), 'Save', self.open_func, 'Ctrl+S')
        self.window.menuFile.addAction(QIcon('icons/save_as.ico'), 'Save As', self.open_func, 'Ctrl+Shift+S')
        self.window.menuFile.addSeparator()
        self.window.menuFile.addAction(QIcon('icons/exit.ico'), 'Quit', lambda : 0, 'Alt+F4') # todo, make this ready for deploy

        self.window.menuView.addAction(QIcon('icons/preview.ico'), 'Preview', self.open_func, 'Ctrl+P')

        self.window.menuHelp.addAction(QIcon('icons/about.ico'), 'Help', self.open_func, 'Ctrl+H')
        self.window.menuHelp.addAction(QIcon('icons/update.ico'), 'Check for update', self.open_func, 'Ctrl+U')

        self.window.open_button.clicked.connect(self.open_func)
        self.window.drop_button.clicked.connect(self.drop_func)
        self.window.select_button.clicked.connect(self.select_func)
        self.window.copy_csv_button.clicked.connect(self.copy_func)

        self.root.show()

    def open_func(self):
        self.file_dialog = QFileDialog()
        file_path, _ = self.file_dialog.getOpenFileName()
        if file_path != '':
            self.data = pd.read_csv(file_path)
            self.update_table()

    def update_table(self):
        if self.data.__class__.__name__  == 'DataFrame':
            self.df_model = PandasModel(self.data)
            self.window.data_table.setModel(self.df_model)
            self.window.column_list.clear()
            self.window.column_list.addItems(list(self.data))

    def drop_func(self):
        if self.data.__class__.__name__  == 'DataFrame':
            col = [tmp.text() for tmp in self.window.column_list.selectedItems()]
            self.data.drop(col, axis = 1, inplace= True)
            self.update_table()

    def select_func(self):
        if self.data.__class__.__name__ == 'DataFrame':
            col = [tmp.text() for tmp in self.window.column_list.selectedItems()]
            self.data = self.data[col].copy()
            self.update_table()

    def copy_func(self):
        if self.data.__class__.__name__ == 'DataFrame':
            tmp = 'skfgi_feed_back_copy_'+str(datetime.isoformat(datetime.now()))+'.csv'
            tmp = tmp.replace(':', '-')
            self.data.to_csv(tmp, index = False)
            self.msg_box = QMessageBox()
            self.msg_box.setWindowIcon(QIcon('icons/logo.png'))
            self.msg_box.setWindowTitle('Data Saved')
            self.msg_box.setInformativeText('New csv file is saved as '+tmp)
            self.msg_box.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup = Setup()
    sys.exit(app.exec_())