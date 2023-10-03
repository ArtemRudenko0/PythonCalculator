################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/calculate_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"color: white;\n"
"background-color: #121212;\n"
"font-family: Rubik;\n"
"font-size: 16px;\n"
"font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_temp = QLabel(self.centralwidget)
        self.label_temp.setObjectName(u"label_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_temp.sizePolicy().hasHeightForWidth())
        self.label_temp.setSizePolicy(sizePolicy)
        self.label_temp.setStyleSheet(u"color: #888")
        self.label_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_temp)

        self.Edit_entry = QLineEdit(self.centralwidget)
        self.Edit_entry.setObjectName(u"Edit_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Edit_entry.sizePolicy().hasHeightForWidth())
        self.Edit_entry.setSizePolicy(sizePolicy1)
        self.Edit_entry.setLayoutDirection(Qt.LeftToRight)
        self.Edit_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.Edit_entry.setMaxLength(10)
        self.Edit_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Edit_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.Edit_entry)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_2, 4, 1, 1, 1)

        self.button_clear = QPushButton(self.centralwidget)
        self.button_clear.setObjectName(u"button_clear")
        sizePolicy2.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_clear, 1, 0, 1, 1)

        self.button_9 = QPushButton(self.centralwidget)
        self.button_9.setObjectName(u"button_9")
        sizePolicy2.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_9, 2, 2, 1, 1)

        self.button_7 = QPushButton(self.centralwidget)
        self.button_7.setObjectName(u"button_7")
        sizePolicy2.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_7, 2, 0, 1, 1)

        self.button_erase = QPushButton(self.centralwidget)
        self.button_erase.setObjectName(u"button_erase")
        sizePolicy2.setHeightForWidth(self.button_erase.sizePolicy().hasHeightForWidth())
        self.button_erase.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_erase, 1, 2, 1, 1)

        self.button_5 = QPushButton(self.centralwidget)
        self.button_5.setObjectName(u"button_5")
        sizePolicy2.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_5, 3, 1, 1, 1)

        self.button_0 = QPushButton(self.centralwidget)
        self.button_0.setObjectName(u"button_0")
        sizePolicy2.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_0, 5, 1, 1, 1)

        self.button_neg = QPushButton(self.centralwidget)
        self.button_neg.setObjectName(u"button_neg")
        sizePolicy2.setHeightForWidth(self.button_neg.sizePolicy().hasHeightForWidth())
        self.button_neg.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_neg, 5, 0, 1, 1)

        self.button_point = QPushButton(self.centralwidget)
        self.button_point.setObjectName(u"button_point")
        sizePolicy2.setHeightForWidth(self.button_point.sizePolicy().hasHeightForWidth())
        self.button_point.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_point, 5, 2, 1, 1)

        self.button_6 = QPushButton(self.centralwidget)
        self.button_6.setObjectName(u"button_6")
        sizePolicy2.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_6, 3, 2, 1, 1)

        self.button_4 = QPushButton(self.centralwidget)
        self.button_4.setObjectName(u"button_4")
        sizePolicy2.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_4, 3, 0, 1, 1)

        self.button_8 = QPushButton(self.centralwidget)
        self.button_8.setObjectName(u"button_8")
        sizePolicy2.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_8, 2, 1, 1, 1)

        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        sizePolicy2.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_1, 4, 0, 1, 1)

        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        sizePolicy2.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_3, 4, 2, 1, 1)

        self.button_div = QPushButton(self.centralwidget)
        self.button_div.setObjectName(u"button_div")
        sizePolicy2.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_div, 1, 3, 1, 1)

        self.button_mul = QPushButton(self.centralwidget)
        self.button_mul.setObjectName(u"button_mul")
        sizePolicy2.setHeightForWidth(self.button_mul.sizePolicy().hasHeightForWidth())
        self.button_mul.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_mul, 2, 3, 1, 1)

        self.button_sub = QPushButton(self.centralwidget)
        self.button_sub.setObjectName(u"button_sub")
        sizePolicy2.setHeightForWidth(self.button_sub.sizePolicy().hasHeightForWidth())
        self.button_sub.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_sub, 3, 3, 1, 1)

        self.button_add = QPushButton(self.centralwidget)
        self.button_add.setObjectName(u"button_add")
        sizePolicy2.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_add, 4, 3, 1, 1)

        self.button_calc = QPushButton(self.centralwidget)
        self.button_calc.setObjectName(u"button_calc")
        sizePolicy2.setHeightForWidth(self.button_calc.sizePolicy().hasHeightForWidth())
        self.button_calc.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_calc, 5, 3, 1, 1)

        self.button_CE = QPushButton(self.centralwidget)
        self.button_CE.setObjectName(u"button_CE")
        sizePolicy2.setHeightForWidth(self.button_CE.sizePolicy().hasHeightForWidth())
        self.button_CE.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_CE, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.label_temp.setText("")
        self.Edit_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.button_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.button_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.button_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.button_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.button_erase.setText(QCoreApplication.translate("MainWindow", u"<-", None))
#if QT_CONFIG(shortcut)
        self.button_erase.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.button_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.button_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.button_neg.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.button_point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.button_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.button_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.button_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.button_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.button_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.button_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.button_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.button_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.button_mul.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(shortcut)
        self.button_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.button_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.button_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.button_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.button_calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.button_calc.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.button_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.button_CE.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

