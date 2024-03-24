# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(763, 343)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LoadMP3 = QPushButton(self.centralwidget)
        self.LoadMP3.setObjectName(u"LoadMP3")
        self.LoadMP3.setGeometry(QRect(11, 20, 181, 61))
        font = QFont()
        font.setFamilies([u"Microsoft Yahei UI Light"])
        font.setPointSize(18)
        font.setBold(True)
        self.LoadMP3.setFont(font)
        self.SongName = QPlainTextEdit(self.centralwidget)
        self.SongName.setObjectName(u"SongName")
        self.SongName.setGeometry(QRect(121, 90, 301, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 90, 141, 31))
        self.label.setFont(font)
        self.SingerName = QPlainTextEdit(self.centralwidget)
        self.SingerName.setObjectName(u"SingerName")
        self.SingerName.setGeometry(QRect(121, 130, 301, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 130, 141, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 170, 141, 31))
        self.label_3.setFont(font)
        self.AlbumName = QPlainTextEdit(self.centralwidget)
        self.AlbumName.setObjectName(u"AlbumName")
        self.AlbumName.setGeometry(QRect(121, 170, 301, 31))
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(11, 220, 411, 71))
        self.Start.setFont(font)
        self.LoadJPG = QPushButton(self.centralwidget)
        self.LoadJPG.setObjectName(u"LoadJPG")
        self.LoadJPG.setGeometry(QRect(201, 20, 221, 61))
        self.LoadJPG.setFont(font)
        self.image = QLabel(self.centralwidget)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(440, 20, 300, 300))
        self.image.setPixmap(QPixmap(u"./Yulan.jpg"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music Information Modifier", None))
        self.LoadMP3.setText(QCoreApplication.translate("MainWindow", u"Load MP3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Artist: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Album: ", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"Start Convertion", None))
        self.LoadJPG.setText(QCoreApplication.translate("MainWindow", u"Load JPEG", None))
        self.image.setText("")
    # retranslateUi

