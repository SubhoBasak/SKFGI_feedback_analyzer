import os
import sys
import requests
import threading
import webbrowser
from datetime import datetime
from fpdf import FPDF

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QWidget, QSplashScreen, QColorDialog
from PyQt5.QtCore import QAbstractTableModel, Qt, QTimer, QSize
from PyQt5.QtGui import QIcon, QPixmap, QColor
from main_window import Ui_MainWindow
from about_window import Ui_About
from error_window import Ui_Error
from setting_window import Ui_Setting
from color_window import Ui_ColorPicker

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')

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
        self.output_data = None
        self.colors = ['#f0e443', '#f77e45', '#f74940', '#4bfa91', '#69d1d1', '#4a61f7']
        self.version = '1.0.0'
        self.map = [
            {'Excellent': 5,
             'Very Good': 4,
             'Good': 3,
             'Poor': 2,
             'Very Poor': 1},

            {'Yes': 3,
             'Partially Completed': 2,
             'No': 1}
        ]

        self.root = QMainWindow()
        self.window = Ui_MainWindow()
        self.window.setupUi(self.root)
        self.window.retranslateUi(self.root)

        self.window.menuFile.addAction(QIcon('icons/open.ico'), 'Open', self.open_func, 'Ctrl+O')
        self.window.menuFile.addSeparator()
        self.window.menuFile.addAction(QIcon('icons/save.ico'), 'Save', self.create_output, 'Ctrl+S')
        self.window.menuFile.addSeparator()
        self.window.menuFile.addAction(QIcon('icons/exit.ico'), 'Quit', lambda : exit(), 'Ctrl+Q')

        self.window.menuOptions.addAction(QIcon('icons/setting.ico'), 'Setting', self.open_setting, 'Ctrl+X')
        self.window.menuOptions.addAction(QIcon('icons/color'), 'Colors', self.change_graph_color, 'Ctrl+J')

        self.window.menuHelp.addAction(QIcon('icons/about.ico'), 'About', self.about_func, 'Ctrl+H')
        self.window.menuHelp.addAction(QIcon('icons/update.ico'), 'Check for update', self.check_update, 'Ctrl+U')

        self.window.open_button.clicked.connect(self.open_func)
        self.window.drop_button.clicked.connect(self.drop_func)
        self.window.select_button.clicked.connect(self.select_func)
        self.window.copy_csv_button.clicked.connect(self.copy_func)
        self.window.save_button.clicked.connect(self.create_output)

        self.window.column_list.setStyleSheet('color: blue;')

        self.root.show()

    def loading_screen(self):
        self.top = QSplashScreen(QPixmap('icons/logo.png'))
        self.top.show()
        QTimer.singleShot(1000, self.top.close)

    def open_func(self):
        self.file_dialog = QFileDialog()
        file_path, _ = self.file_dialog.getOpenFileName()
        if file_path != '':
            try:
                self.data = pd.read_csv(file_path)
                self.update_table()
            except Exception as e:
                self.top = Ui_Error()
                self.top_widget = QWidget()
                self.top.setupUi(self.top_widget)
                self.top.retranslateUi(self.top_widget)
                self.top.textBrowser.setTextColor(QColor(255, 0, 0))
                self.top.textBrowser.setText(repr(e))
                self.top_widget.show()

    def update_table(self):
        if self.data.__class__.__name__  == 'DataFrame':
            self.df_model = PandasModel(self.data)
            self.window.data_table.setModel(self.df_model)
            self.window.data_table.setStyleSheet(
                '''QHeaderView::section{
                        background-color: '#dcf7f7';
                        color: blue;
                        border: 0;}''')
            self.window.column_list.clear()
            self.window.column_list.addItems(list(self.data))

            c = 0
            for i in range(self.window.column_list.count()):
                self.window.column_list.item(i).setSizeHint(QSize(100, 35))
                if c:
                    self.window.column_list.item(i).setBackground(QColor('#dcf7f7'))
                    c = 0
                else:
                    self.window.column_list.item(i).setBackground(QColor('#ffffff'))
                    c = 1

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
            tmp = '\\skfgi_feed_back_copy_'+str(datetime.isoformat(datetime.now()))+'.csv'
            tmp = tmp.replace(':', '-')
            tmp = os.path.expanduser('~')+tmp
            self.data.to_csv(tmp, index = False)
            self.msg_box = QMessageBox()
            self.msg_box.setWindowIcon(QIcon('icons/logo.png'))
            self.msg_box.setWindowTitle('Data Saved')
            self.msg_box.setInformativeText('New csv file is saved as :\n'+tmp)
            self.msg_box.show()

    def about_func(self):
        self.top = Ui_About()
        self.top_widget = QWidget()
        self.top.setupUi(self.top_widget)
        self.top.retranslateUi(self.top_widget)

        tmp = os.path.join(os.path.dirname(__file__), 'Documentation/index.html').replace('/', '\\')
        self.top.doc_button.clicked.connect(lambda : webbrowser.open(tmp))

        self.top_widget.show()

    def check_update(self):
        try:
            self.top = QSplashScreen(QPixmap('icons/wait.png'))
            self.top.show()
            QTimer.singleShot(3000, self.top.close)

            resp = requests.get(url = 'https://raw.githubusercontent.com/SubhoBasak/SKFGI_feedback_analyzer/master/Output/version.txt')
            resp = resp.text.strip('\n').strip()
            self.tmp = QMessageBox()
            self.tmp.setWindowTitle('Update')
            self.tmp.setWindowIcon(QIcon('icons/logo.png'))
            if resp != self.version:
                self.tmp.setInformativeText('New update available!\nDownlaod from : https://raw.githubusercontent.com/SubhoBasak/SKFGI_feedback_analyzer/master/Output/mysetup.exe')
            else:
                self.tmp.setInformativeText('Already up-to-date')
            self.tmp.show()
        except Exception as e:
            self.top = Ui_Error()
            self.top_widget = QWidget()
            self.top.setupUi(self.top_widget)
            self.top.retranslateUi(self.top_widget)
            self.top.textBrowser.setTextColor(QColor(255, 0, 0))
            self.top.textBrowser.setText(repr(e))
            self.top_widget.show()

    def open_setting(self):
        self.top = Ui_Setting()
        self.top_widget = QWidget()
        self.top.setupUi(self.top_widget)
        self.top.retranslateUi(self.top_widget)

        tmp = [(self.top.map_in_1, self.top.map_out_1),
               (self.top.map_in_2, self.top.map_out_2),
               (self.top.map_in_3, self.top.map_out_3),
               (self.top.map_in_4, self.top.map_out_4),
               (self.top.map_in_5, self.top.map_out_5)]

        for x, y in zip(tmp, self.map[0].items()):
            x1, x2 = x
            y1, y2 = y
            x1.setText(y1), x2.setText(str(y2))

        tmp = [(self.top.map_in_11, self.top.map_out_11),
               (self.top.map_in_12, self.top.map_out_12),
               (self.top.map_in_13, self.top.map_out_13)]

        for x, y in zip(tmp, self.map[1].items()):
            x1, x2 = x
            y1, y2 = y
            x1.setText(y1), x2.setText(str(y2))

        self.top.map_ok_button.clicked.connect(self.change_map)
        self.top_widget.show()

    def change_map(self):
        tmp = [(self.top.map_in_1, self.top.map_out_1),
               (self.top.map_in_2, self.top.map_out_2),
               (self.top.map_in_3, self.top.map_out_3),
               (self.top.map_in_4, self.top.map_out_4),
               (self.top.map_in_5, self.top.map_out_5)]

        self.map = [{}, {}]
        for x, y in tmp:
            self.map[0][x.text()] = y.text()

        tmp = [(self.top.map_in_11, self.top.map_out_11),
               (self.top.map_in_12, self.top.map_out_12),
               (self.top.map_in_13, self.top.map_out_13)]

        for x, y in tmp:
            self.map[1][x.text()] = y.text()
        self.top_widget.close()

    def change_graph_color(self):
        self.top = Ui_ColorPicker()
        self.top_widget = QWidget()
        self.top.setupUi(self.top_widget)
        self.top.retranslateUi(self.top_widget)

        buttons = [self.top.color1_button, self.top.color2_button, self.top.color3_button,
                   self.top.color4_button, self.top.color5_button, self.top.color6_button]

        funcs = [self.get_color1, self.get_color2, self.get_color3,
                 self.get_color4, self.get_color5, self.get_color6]

        for i, b in enumerate(buttons):
            b.setStyleSheet('background : '+self.colors[i]+';')
            b.clicked.connect(funcs[i])

        self.top.close_color_picker.clicked.connect(self.top_widget.close)
        self.top_widget.show()

    def get_color1(self):
        win = QColorDialog()
        win.setWindowIcon(QIcon('icons/logo.png'))
        self.colors[0] = win.getColor().name()
        self.top.color1_button.setStyleSheet('background : '+self.colors[0])

    def get_color2(self):
        win = QColorDialog()
        win.setWindowIcon(QIcon('icons/logo.png'))
        self.colors[1] = win.getColor().name()
        self.top.color2_button.setStyleSheet('background : '+self.colors[1])

    def get_color3(self):
        win = QColorDialog()
        win.setWindowIcon(QIcon('icons/logo.png'))
        self.colors[2] = win.getColor().name()
        self.top.color3_button.setStyleSheet('background : '+self.colors[2])

    def get_color4(self):
        win = QColorDialog()
        win.setWindowIcon(QIcon('icons/logo.png'))
        self.colors[3] = win.getColor().name()
        self.top.color4_button.setStyleSheet('background : '+self.colors[3])

    def get_color5(self):
        win = QColorDialog()
        win.setWindowIcon(QIcon('icons/logo.png'))
        self.colors[4] = win.getColor().name()
        self.top.color5_button.setStyleSheet('background : '+self.colors[4])

    def get_color6(self):
        win = QColorDialog()
        win.setWindowIcon(QIcon('icons/logo.png'))
        self.colors[5] = win.getColor().name()
        self.top.color6_button.setStyleSheet('background : '+self.colors[5])

    def create_output(self):
        self.top = QSplashScreen(QPixmap('icons/wait.png'))
        self.top.show()

        self.thread = threading.Thread(target = self.thread_func)
        self.thread.start()

        QTimer.singleShot(10000, self.top.close)

    def thread_func(self):
        self.prepare_output_data()
        self.calculate_percentage_and_plot()
        tmp_path = self.create_pdf()
        webbrowser.open(tmp_path)

    def create_pdf(self):
        pdf_file = FPDF()
        pdf_file.add_page()
        for i in os.listdir('Tmp'):
            i = 'Tmp/'+i
            pdf_file.image(os.path.join(os.path.dirname(__file__), i), w = 196, h = 116)
            pdf_file.ln()
        tmp_path = os.path.join(os.path.expanduser('~'), 'feed_back'+datetime.now().isoformat().replace(':', '-')+'.pdf')
        pdf_file.output(tmp_path, 'F')
        return tmp_path

    def calculate_percentage_and_plot(self):
        if self.output_data.__class__.__name__ == 'DataFrame':
            for file in os.listdir('Tmp'):
                os.remove('Tmp/'+file)
            fig = plt.figure(figsize=(12, 7))
            main_group = self.output_data.groupby('subject')

            for name, grp in main_group:
                teachers_name = grp['teacher'].unique()
                q = []
                p = []
                count = 1
                for qus_, qus_grp in grp.groupby('question'):
                    p.append(round(qus_grp.mean()['feedback'], 1))
                    q.append('Q'+str(count))
                    count += 1

                fig.clf()
                axs1 = fig.add_axes([0.07, 0.1, 0.7, 0.8])
                fig.suptitle(name+'-'+'-'.join(teachers_name), fontsize = 25, color = 'orange')
                axs1.bar(q, p, color = self.colors)
                axs1.set_xticklabels(q, fontsize = 22)
                axs1.set_yticklabels([20, 40, 60, 80, 100], fontsize = 22)
                for xx, yy in enumerate(p):
                    axs1.text(xx-0.4, yy, yy, fontsize = 13)

                axs2 = fig.add_axes([0.8, 0.1, 0.1, 0.8])
                table_data = np.c_[q, p]
                length = len(table_data)
                cell_colors = [('#ffffff', '#ffffff'), ('#e6f0f0', '#e6f0f0')]*(length//2)
                if length%2 != 0:
                    cell_colors += [('#ffffff', '#ffffff')]
                tab = axs2.table(table_data, loc = 'upper center', cellColours=cell_colors, cellLoc = 'center')
                tab.set_fontsize(25)
                tab.scale(1, 2)
                axs2.axis(False)
                fig.savefig('Tmp/'+name+'-'+'-'.join(teachers_name)+'.png')

    def prepare_output_data(self):
        if self.data.__class__.__name__ == 'DataFrame':
            try:
                self.output_data = {'question': [], 'subject': [], 'teacher': [], 'feedback': []}
                ln = len(self.data)
                for col in self.data:
                    qus, sub, tec = col.split('[')
                    self.output_data['question'].append(qus.strip().strip(']'))
                    self.output_data['subject'].append(sub.strip().strip(']'))
                    self.output_data['teacher'].append(tec.strip().strip(']'))

                    sup_flag = 0
                    for m in self.map:
                        flag = 1
                        tmp_unique = m.keys()
                        for k in self.data[col].unique():
                            if k not in tmp_unique:
                                flag = 0
                                break
                        if flag:
                            tmp_col = self.data[col].map(m).astype('int32')
                            tmp_max = max(m.values())
                            sup_flag = 1
                            break
                    if not sup_flag:
                        self.top = Ui_Error()
                        self.top_widget = QWidget()
                        self.top.setupUi(self.top_widget)
                        self.top.retranslateUi(self.top_widget)

                        self.top.textBrowser.setText('Mapping error! Please set the map values proerly.\nOptions >> Settings')
                        self.top.textBrowser.setTextColor(QColor(255, 0, 0))

                        self.top_widget.show()
                    else:
                        self.output_data['feedback'].append(round(100*tmp_col.values.sum()/(tmp_max*len(tmp_col)), 2))
                self.output_data = pd.DataFrame(self.output_data)
            except Exception as e:
                self.top = Ui_Error()
                self.top_widget = QWidget()
                self.top.setupUi(self.top_widget)
                self.top.retranslateUi(self.top_widget)
                self.top.textBrowser.setTextColor(QColor(255, 0, 0))
                self.top.textBrowser.setText(repr(e))
                self.top_widget.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup = Setup()
    sys.exit(app.exec_())