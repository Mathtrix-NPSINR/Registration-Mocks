# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowdVgAtK.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(628, 209)
        font = QFont()
        font.setFamilies([u"JetBrainsMono Nerd Font"])
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.welcome_label = QLabel(self.centralwidget)
        self.welcome_label.setObjectName(u"welcome_label")
        font1 = QFont()
        font1.setFamilies([u"JetBrainsMono Nerd Font"])
        font1.setPointSize(36)
        self.welcome_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.welcome_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.qr_code_registration_button = QPushButton(self.centralwidget)
        self.qr_code_registration_button.setObjectName(u"qr_code_registration_button")
        self.qr_code_registration_button.setEnabled(False)

        self.verticalLayout_2.addWidget(self.qr_code_registration_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.api_key_label = QLabel(self.centralwidget)
        self.api_key_label.setObjectName(u"api_key_label")
        self.api_key_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.api_key_label)

        self.api_key_field = QLineEdit(self.centralwidget)
        self.api_key_field.setObjectName(u"api_key_field")
        self.api_key_field.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.api_key_field)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.api_key_login_button = QPushButton(self.centralwidget)
        self.api_key_login_button.setObjectName(u"api_key_login_button")

        self.verticalLayout.addWidget(self.api_key_login_button)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mathtrix Registration Mocks", None))
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"Mathtrix Registration Mocks", None))
        self.qr_code_registration_button.setText(QCoreApplication.translate("MainWindow", u"QR Code Registration", None))
        self.api_key_label.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.api_key_login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

