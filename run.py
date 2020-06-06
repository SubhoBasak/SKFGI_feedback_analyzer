import os
import sys
import requests
import threading
import webbrowser
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QWidget, QSplashScreen
from PyQt5.QtCore import QAbstractTableModel, Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from main_window import Ui_MainWindow
from about_window import Ui_About

import pandas as pd
import matplotlib.pyplot as plt

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
        self.loading_screen()
        self.data = None
        self.file = None
        self.version = '1.0.0'

        self.root = QMainWindow()
        self.window = Ui_MainWindow()
        self.window.setupUi(self.root)
        self.window.retranslateUi(self.root)

        self.window.menuFile.addAction(QIcon('icons/open.ico'), 'Open', self.open_func, 'Ctrl+O')
        self.window.menuFile.addSeparator()
        self.window.menuFile.addAction(QIcon('icons/save.ico'), 'Save', self.save_func, 'Ctrl+S')
        self.window.menuFile.addAction(QIcon('icons/save_as.ico'), 'Save As', self.save_as_func, 'Ctrl+Shift+S')
        self.window.menuFile.addSeparator()
        self.window.menuFile.addAction(QIcon('icons/exit.ico'), 'Quit', lambda: 0,
                                       'Alt+F4')  # todo, make this ready for deploy

        self.window.menuView.addAction(QIcon('icons/preview.ico'), 'Preview', self.create_hist, 'Ctrl+P')

        self.window.menuHelp.addAction(QIcon('icons/about.ico'), 'About', self.about_func, 'Ctrl+H')
        self.window.menuHelp.addAction(QIcon('icons/update.ico'), 'Check for update', self.open_func, 'Ctrl+U')

        self.window.open_button.clicked.connect(self.open_func)
        self.window.drop_button.clicked.connect(self.drop_func)
        self.window.select_button.clicked.connect(self.select_func)
        self.window.copy_csv_button.clicked.connect(self.copy_func)
        self.window.save_button.clicked.connect(self.save_func)
        self.window.preview_button.clicked.connect(self.create_hist)

        self.root.show()

    def loading_screen(self):
        self.splash_screen = QSplashScreen(QPixmap('icons/logo.png'))
        self.splash_screen.show()
        QTimer.singleShot(1000, self.splash_screen.close)

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

    def save_func(self): # todo, compelete this function
        if self.file:
            print(self.file)
        else:
            self.save_as_func(title = 'Save')

    def save_as_func(self, title = 'Save As'): # todo, complete this function
        self.file, _ = QFileDialog.getSaveFileName(caption=title)

    def about_func(self):
        self.about = Ui_About()
        self.about_widget = QWidget()
        self.about.setupUi(self.about_widget)
        self.about.retranslateUi(self.about_widget)

        tmp = os.path.join(os.path.dirname(__file__), 'Documentation/index.html')
        self.about.doc_button.clicked.connect(lambda : webbrowser.open(tmp))

        self.about_widget.show()

    def check_update(self): # todo, complete the function
        resp = requests.get(url = 'https://www.google.com') # todo, change to the correct url
        if resp.json().get('version') != self.version:
            pass

    def create_hist(self):
        self.thread = threading.Thread(target = self.__create_hist)
        self.thread.start()

    def __create_hist(self):
        if self.data.__class__.__name__ == 'DataFrame':
            for file in os.listdir('Tmp'):
                os.remove('Tmp/'+file)
            fig = plt.figure(figsize=(12, 7))
            for i, col in enumerate(self.data):
                hist_data = self.data[col].value_counts().to_dict()
                fig.clf()
                plt.bar(hist_data.keys(), hist_data.values())
                fig.savefig('Tmp/{}.png'.format(i))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup = Setup()
    sys.exit(app.exec_())