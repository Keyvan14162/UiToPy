import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

import untitled

app = QApplication(sys.argv)

form = QtWidgets.QWidget()
ui = untitled.Ui_Form()
ui.setupUi(form)

strFileName = ""


class main():

    def file_open(self):
        global strFileName  # convert fonksiyonunda da lazım

        # .ui dosyasını seciyo
        self.file_name = QFileDialog.getOpenFileName(form, "Choose an .ui file", os.getenv("HOME"), filter="*.ui")
        strFileName = str(self.file_name[0])
        print(strFileName.replace("/", "\\"))  # Niyeyse \ yerine / koyuyo dosya yolunda
        # burda onları degistiriyo

        # Labellara bilgi metni yazdırıyo
        ui.label_choosen_file.setText("Path: " + str(self.file_name[0]))
        ui.label_2.setText("File Choosed")

    def convert(self):
        global strFileName

        # .ui dosyası secilmediyse
        if ui.label_choosen_file.text() == "<html><head/><body><p>no file selected</p></body></html>":
            ui.label_2.setText("Choose the File First")

        else:

            # işlemi komut satırında çalıştırdığı bir komutla yapıyo, PyQt5 yüklü olmalı
            # zaten bu uygulamayı kullancaksa birisi illa yüklüdür
            self.dosya_ismi = QFileDialog.getSaveFileName(form, "Save File", os.getenv("HOME"), filter="*.py")
            commandd = ("python -m PyQt5.uic.pyuic " + strFileName + " -o " + str(self.dosya_ismi[0]).replace("/", "\\")
                        + " -x")
            # print(commandd)
            os.system(commandd)
            ui.label_converted_file.setText("Path: " + str(self.dosya_ismi[0]))
            ui.label_2.setText("File Converted")


main = main()

ui.pushButton_choose.clicked.connect(main.file_open)
ui.pushButton_convert.clicked.connect(main.convert)

form.setWindowIcon(QIcon("python.png"))

form.setWindowTitle("UiToPy")
form.show()
sys.exit(app.exec_())
