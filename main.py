from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 379)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Menu = QtWidgets.QFrame(Form)
        self.Menu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu.setObjectName("Menu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Menu)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.Menu)
        self.slide_menu.setMinimumSize(QtCore.QSize(198, 0))
        self.slide_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.slide_menu)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/home.svg"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.verticalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.frame_6 = QtWidgets.QFrame(self.slide_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toolBox = QtWidgets.QToolBox(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 176, 208))
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_11 = QtWidgets.QFrame(self.page)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_11)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_7.addWidget(self.pushButton_13)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/monitor.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_10.setAutoRepeat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_7.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_11)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/shield.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_11.setAutoRepeat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_7.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_11)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/battery.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_12.setAutoRepeat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_7.addWidget(self.pushButton_12)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_11)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon4)
        self.pushButton_14.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_7.addWidget(self.pushButton_14)
        self.verticalLayout_6.addWidget(self.frame_11, 0, QtCore.Qt.AlignTop)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon5, "")
        self.DASHBOARD = QtWidgets.QWidget()
        self.DASHBOARD.setGeometry(QtCore.QRect(0, 0, 176, 208))
        self.DASHBOARD.setObjectName("DASHBOARD")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.DASHBOARD)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_12 = QtWidgets.QFrame(self.DASHBOARD)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_12)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/mic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon6)
        self.pushButton_15.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_9.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_12)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/message-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon7)
        self.pushButton_16.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_9.addWidget(self.pushButton_16)
        self.verticalLayout_8.addWidget(self.frame_12)
        self.label_4 = QtWidgets.QLabel(self.DASHBOARD)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4, 0, QtCore.Qt.AlignTop)
        self.toolBox.addItem(self.DASHBOARD, icon5, "")
        self.verticalLayout_5.addWidget(self.toolBox)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_10 = QtWidgets.QFrame(self.slide_menu)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/external-link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_11.addWidget(self.pushButton_9, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.verticalLayout_4.addWidget(self.frame_10, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.slide_menu)
        self.horizontalLayout.addWidget(self.Menu)
        self.Body = QtWidgets.QFrame(Form)
        self.Body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Body.setObjectName("Body")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Body)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QFrame(self.Body)
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.Header)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/list.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon9)
        self.pushButton_8.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_9.addWidget(self.pushButton_8)
        self.horizontalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_9 = QtWidgets.QFrame(self.Header)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit.setMinimumSize(QtCore.QSize(133, 0))
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit, 0, QtCore.Qt.AlignLeft)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_6.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon10)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_3.addWidget(self.frame_9, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_8 = QtWidgets.QFrame(self.Header)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_4.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/bell.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon12)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.horizontalLayout_3.addWidget(self.frame_8, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(self.Header)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_2.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon13)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_7)
        self.pushButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.horizontalLayout_3.addWidget(self.frame_7, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.Header, 0, QtCore.Qt.AlignTop)
        self.main_body = QtWidgets.QFrame(self.Body)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.main_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout.addWidget(self.main_body)
        self.footer = QtWidgets.QFrame(self.Body)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_4 = QtWidgets.QFrame(self.footer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_8.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.footer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/icons/camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon15)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_8.addWidget(self.frame_3, 0, QtCore.Qt.AlignBottom)
        self.resize = QtWidgets.QFrame(self.footer)
        self.resize.setMinimumSize(QtCore.QSize(10, 10))
        self.resize.setMaximumSize(QtCore.QSize(10, 10))
        self.resize.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resize.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resize.setObjectName("resize")
        self.horizontalLayout_8.addWidget(self.resize, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.Body)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "HOME ASSISTANT"))
        self.pushButton_13.setText(_translate("Form", "MEMBER"))
        self.pushButton_10.setText(_translate("Form", "DEVICES"))
        self.pushButton_11.setText(_translate("Form", "SECURITY"))
        self.pushButton_12.setText(_translate("Form", "POWER"))
        self.pushButton_14.setText(_translate("Form", "SETTINGS"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "HOME"))
        self.pushButton_15.setText(_translate("Form", "VOICE"))
        self.pushButton_16.setText(_translate("Form", "CHATBOT"))
        self.label_4.setText(_translate("Form", "─É├óy l├á hß╗ç thß╗æng quß║ún l├╜ nh├á th├┤ng minh"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.DASHBOARD), _translate("Form", "ASSISTANT"))
        self.pushButton_9.setText(_translate("Form", "Exit"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Search to text"))
        self.label.setText(_translate("Form", "Phan ─Éß╗⌐c C╞░╞íng"))
import icons_rc
