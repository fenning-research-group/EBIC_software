# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName(_fromUtf8("MplMainWindow"))
        MplMainWindow.resize(1640, 1041)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MplMainWindow.sizePolicy().hasHeightForWidth())
        MplMainWindow.setSizePolicy(sizePolicy)
        MplMainWindow.setStyleSheet(_fromUtf8("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image: url(:/images/checkbox.png);\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"AbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
""))
        MplMainWindow.setDocumentMode(False)
        MplMainWindow.setDockNestingEnabled(True)
        MplMainWindow.setDockOptions(QtGui.QMainWindow.AllowNestedDocks|QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MplMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_6)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 746, 53))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_10.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_10.setSpacing(25)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.singleView = QtGui.QToolButton(self.layoutWidget)
        self.singleView.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Single.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/SingleOR.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.singleView.setIcon(icon)
        self.singleView.setIconSize(QtCore.QSize(30, 30))
        self.singleView.setCheckable(True)
        self.singleView.setChecked(True)
        self.singleView.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.singleView.setAutoRaise(True)
        self.singleView.setObjectName(_fromUtf8("singleView"))
        self.horizontalLayout_9.addWidget(self.singleView)
        self.quadView = QtGui.QToolButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Quad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/QuadOR.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.quadView.setIcon(icon1)
        self.quadView.setIconSize(QtCore.QSize(30, 30))
        self.quadView.setCheckable(True)
        self.quadView.setAutoExclusive(False)
        self.quadView.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.quadView.setAutoRaise(True)
        self.quadView.setObjectName(_fromUtf8("quadView"))
        self.horizontalLayout_9.addWidget(self.quadView)
        self.toolButton_9 = QtGui.QToolButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/HIST.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/HIST_OR.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_9.setIcon(icon2)
        self.toolButton_9.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_9.setCheckable(True)
        self.toolButton_9.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.toolButton_9.setAutoRaise(True)
        self.toolButton_9.setObjectName(_fromUtf8("toolButton_9"))
        self.horizontalLayout_9.addWidget(self.toolButton_9)
        self.toolButton_10 = QtGui.QToolButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Mline.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/MlineOR.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_10.setIcon(icon3)
        self.toolButton_10.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_10.setCheckable(True)
        self.toolButton_10.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.toolButton_10.setAutoRaise(True)
        self.toolButton_10.setObjectName(_fromUtf8("toolButton_10"))
        self.horizontalLayout_9.addWidget(self.toolButton_10)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_16.setSpacing(1)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.CrossHair = QtGui.QToolButton(self.layoutWidget)
        self.CrossHair.setWhatsThis(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Cross.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/CrossOR.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.CrossHair.setIcon(icon4)
        self.CrossHair.setIconSize(QtCore.QSize(30, 30))
        self.CrossHair.setCheckable(True)
        self.CrossHair.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.CrossHair.setAutoRaise(True)
        self.CrossHair.setObjectName(_fromUtf8("CrossHair"))
        self.horizontalLayout_16.addWidget(self.CrossHair)
        self.toolButton_4 = QtGui.QToolButton(self.layoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Measure.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon5)
        self.toolButton_4.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_4.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout_16.addWidget(self.toolButton_4)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.Sel = QtGui.QToolButton(self.layoutWidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Arrow_OR.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Sel.setIcon(icon6)
        self.Sel.setIconSize(QtCore.QSize(30, 30))
        self.Sel.setCheckable(True)
        self.Sel.setChecked(True)
        self.Sel.setAutoExclusive(False)
        self.Sel.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.Sel.setAutoRaise(True)
        self.Sel.setObjectName(_fromUtf8("Sel"))
        self.horizontalLayout_8.addWidget(self.Sel)
        self.Vis = QtGui.QToolButton(self.layoutWidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Eye.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Eye_OR.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Vis.setIcon(icon7)
        self.Vis.setIconSize(QtCore.QSize(30, 30))
        self.Vis.setCheckable(True)
        self.Vis.setChecked(True)
        self.Vis.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.Vis.setAutoRaise(True)
        self.Vis.setObjectName(_fromUtf8("Vis"))
        self.horizontalLayout_8.addWidget(self.Vis)
        self.ROI = QtGui.QToolButton(self.layoutWidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ROI.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/ROI_OR.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.ROI.setIcon(icon8)
        self.ROI.setIconSize(QtCore.QSize(40, 30))
        self.ROI.setCheckable(True)
        self.ROI.setAutoExclusive(False)
        self.ROI.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.ROI.setAutoRaise(True)
        self.ROI.setObjectName(_fromUtf8("ROI"))
        self.horizontalLayout_8.addWidget(self.ROI)
        self.ROICross = QtGui.QToolButton(self.layoutWidget)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Mark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/MarkOR.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ROICross.setIcon(icon9)
        self.ROICross.setIconSize(QtCore.QSize(30, 30))
        self.ROICross.setCheckable(True)
        self.ROICross.setAutoExclusive(False)
        self.ROICross.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.ROICross.setAutoRaise(True)
        self.ROICross.setObjectName(_fromUtf8("ROICross"))
        self.horizontalLayout_8.addWidget(self.ROICross)
        self.Line = QtGui.QToolButton(self.layoutWidget)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/LineP.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/LineP_OR.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.Line.setIcon(icon10)
        self.Line.setIconSize(QtCore.QSize(30, 30))
        self.Line.setCheckable(True)
        self.Line.setAutoExclusive(False)
        self.Line.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.Line.setAutoRaise(True)
        self.Line.setArrowType(QtCore.Qt.NoArrow)
        self.Line.setObjectName(_fromUtf8("Line"))
        self.horizontalLayout_8.addWidget(self.Line)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.toolButton = QtGui.QToolButton(self.layoutWidget)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/FLR.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon11)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(self.layoutWidget)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/FUD.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon12)
        self.toolButton_2.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.toolButton_8 = QtGui.QToolButton(self.layoutWidget)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Tran.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon13)
        self.toolButton_8.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_8.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.toolButton_8.setAutoRaise(True)
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.horizontalLayout_2.addWidget(self.toolButton_8)
        self.toolButton_3 = QtGui.QToolButton(self.layoutWidget)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/FFTicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon14)
        self.toolButton_3.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.tabImageAnalysis = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabImageAnalysis.sizePolicy().hasHeightForWidth())
        self.tabImageAnalysis.setSizePolicy(sizePolicy)
        self.tabImageAnalysis.setMinimumSize(QtCore.QSize(0, 950))
        font = QtGui.QFont()
        font.setKerning(False)
        self.tabImageAnalysis.setFont(font)
        self.tabImageAnalysis.setAcceptDrops(True)
        self.tabImageAnalysis.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabImageAnalysis.setIconSize(QtCore.QSize(30, 30))
        self.tabImageAnalysis.setUsesScrollButtons(True)
        self.tabImageAnalysis.setDocumentMode(True)
        self.tabImageAnalysis.setTabsClosable(False)
        self.tabImageAnalysis.setMovable(True)
        self.tabImageAnalysis.setObjectName(_fromUtf8("tabImageAnalysis"))
        self.tabImage = QtGui.QWidget()
        self.tabImage.setObjectName(_fromUtf8("tabImage"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabImage)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tabWidget_5 = QtGui.QTabWidget(self.tabImage)
        self.tabWidget_5.setObjectName(_fromUtf8("tabWidget_5"))
        self.tab_17 = QtGui.QWidget()
        self.tab_17.setObjectName(_fromUtf8("tab_17"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.tab_17)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.mpl = MplWidget(self.tab_17)
        self.mpl.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setMinimumSize(QtCore.QSize(0, 0))
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.verticalLayout_13.addWidget(self.mpl)
        self.tabWidget_5.addTab(self.tab_17, _fromUtf8(""))
        self.tab_18 = QtGui.QWidget()
        self.tab_18.setObjectName(_fromUtf8("tab_18"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tab_18)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.DockMain = DockArea(self.tab_18)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DockMain.sizePolicy().hasHeightForWidth())
        self.DockMain.setSizePolicy(sizePolicy)
        self.DockMain.setObjectName(_fromUtf8("DockMain"))
        self.verticalLayout_14.addWidget(self.DockMain)
        self.tabWidget_5.addTab(self.tab_18, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget_5)
        self.tabImageAnalysis.addTab(self.tabImage, _fromUtf8(""))
        self.tabAnalysis = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabAnalysis.sizePolicy().hasHeightForWidth())
        self.tabAnalysis.setSizePolicy(sizePolicy)
        self.tabAnalysis.setObjectName(_fromUtf8("tabAnalysis"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabAnalysis)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.analysisCh = QtGui.QTabWidget(self.tabAnalysis)
        self.analysisCh.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysisCh.sizePolicy().hasHeightForWidth())
        self.analysisCh.setSizePolicy(sizePolicy)
        self.analysisCh.setDocumentMode(True)
        self.analysisCh.setObjectName(_fromUtf8("analysisCh"))
        self.Ch1tab = QtGui.QWidget()
        self.Ch1tab.setObjectName(_fromUtf8("Ch1tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Ch1tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.mplCh1 = MplWidget(self.Ch1tab)
        self.mplCh1.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCh1.sizePolicy().hasHeightForWidth())
        self.mplCh1.setSizePolicy(sizePolicy)
        self.mplCh1.setMinimumSize(QtCore.QSize(0, 0))
        self.mplCh1.setObjectName(_fromUtf8("mplCh1"))
        self.verticalLayout_5.addWidget(self.mplCh1)
        self.analysisCh.addTab(self.Ch1tab, _fromUtf8(""))
        self.Ch2tap = QtGui.QWidget()
        self.Ch2tap.setObjectName(_fromUtf8("Ch2tap"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.Ch2tap)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.mplCh2 = MplWidget(self.Ch2tap)
        self.mplCh2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCh2.sizePolicy().hasHeightForWidth())
        self.mplCh2.setSizePolicy(sizePolicy)
        self.mplCh2.setMinimumSize(QtCore.QSize(0, 0))
        self.mplCh2.setObjectName(_fromUtf8("mplCh2"))
        self.verticalLayout_6.addWidget(self.mplCh2)
        self.analysisCh.addTab(self.Ch2tap, _fromUtf8(""))
        self.Ch3tab = QtGui.QWidget()
        self.Ch3tab.setObjectName(_fromUtf8("Ch3tab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.Ch3tab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.mplCh3 = MplWidget(self.Ch3tab)
        self.mplCh3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCh3.sizePolicy().hasHeightForWidth())
        self.mplCh3.setSizePolicy(sizePolicy)
        self.mplCh3.setMinimumSize(QtCore.QSize(0, 0))
        self.mplCh3.setObjectName(_fromUtf8("mplCh3"))
        self.verticalLayout_7.addWidget(self.mplCh3)
        self.analysisCh.addTab(self.Ch3tab, _fromUtf8(""))
        self.Ch4tab = QtGui.QWidget()
        self.Ch4tab.setObjectName(_fromUtf8("Ch4tab"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.Ch4tab)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.mplCh4 = MplWidget(self.Ch4tab)
        self.mplCh4.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCh4.sizePolicy().hasHeightForWidth())
        self.mplCh4.setSizePolicy(sizePolicy)
        self.mplCh4.setMinimumSize(QtCore.QSize(0, 0))
        self.mplCh4.setObjectName(_fromUtf8("mplCh4"))
        self.verticalLayout_8.addWidget(self.mplCh4)
        self.analysisCh.addTab(self.Ch4tab, _fromUtf8(""))
        self.Ch5tab = QtGui.QWidget()
        self.Ch5tab.setObjectName(_fromUtf8("Ch5tab"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.Ch5tab)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.mplCh5 = MplWidget(self.Ch5tab)
        self.mplCh5.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCh5.sizePolicy().hasHeightForWidth())
        self.mplCh5.setSizePolicy(sizePolicy)
        self.mplCh5.setMinimumSize(QtCore.QSize(0, 0))
        self.mplCh5.setObjectName(_fromUtf8("mplCh5"))
        self.verticalLayout_9.addWidget(self.mplCh5)
        self.analysisCh.addTab(self.Ch5tab, _fromUtf8(""))
        self.Ch6tab = QtGui.QWidget()
        self.Ch6tab.setObjectName(_fromUtf8("Ch6tab"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.Ch6tab)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.mplCh6 = MplWidget(self.Ch6tab)
        self.mplCh6.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCh6.sizePolicy().hasHeightForWidth())
        self.mplCh6.setSizePolicy(sizePolicy)
        self.mplCh6.setMinimumSize(QtCore.QSize(0, 0))
        self.mplCh6.setObjectName(_fromUtf8("mplCh6"))
        self.verticalLayout_10.addWidget(self.mplCh6)
        self.analysisCh.addTab(self.Ch6tab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.analysisCh)
        self.tabImageAnalysis.addTab(self.tabAnalysis, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.mpl_2 = MplWidget(self.tab_4)
        self.mpl_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl_2.sizePolicy().hasHeightForWidth())
        self.mpl_2.setSizePolicy(sizePolicy)
        self.mpl_2.setMinimumSize(QtCore.QSize(0, 0))
        self.mpl_2.setObjectName(_fromUtf8("mpl_2"))
        self.verticalLayout_11.addWidget(self.mpl_2)
        self.tabImageAnalysis.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.DockTest = DockArea(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DockTest.sizePolicy().hasHeightForWidth())
        self.DockTest.setSizePolicy(sizePolicy)
        self.DockTest.setObjectName(_fromUtf8("DockTest"))
        self.verticalLayout_22.addWidget(self.DockTest)
        self.tabImageAnalysis.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabImageAnalysis)
        MplMainWindow.setCentralWidget(self.centralwidget)
        self.mplmenubar = QtGui.QMenuBar(MplMainWindow)
        self.mplmenubar.setGeometry(QtCore.QRect(0, 0, 1640, 27))
        self.mplmenubar.setProperty("File", _fromUtf8(""))
        self.mplmenubar.setObjectName(_fromUtf8("mplmenubar"))
        self.mplmenuFile = QtGui.QMenu(self.mplmenubar)
        self.mplmenuFile.setObjectName(_fromUtf8("mplmenuFile"))
        self.menuEdit = QtGui.QMenu(self.mplmenubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MplMainWindow.setMenuBar(self.mplmenubar)
        self.control = QtGui.QDockWidget(MplMainWindow)
        self.control.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control.sizePolicy().hasHeightForWidth())
        self.control.setSizePolicy(sizePolicy)
        self.control.setMinimumSize(QtCore.QSize(416, 750))
        self.control.setAutoFillBackground(False)
        self.control.setFloating(False)
        self.control.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.control.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.control.setWindowTitle(_fromUtf8(""))
        self.control.setObjectName(_fromUtf8("control"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setEnabled(True)
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents_5)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 911))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget_4 = QtGui.QTabWidget(self.tab)
        self.tabWidget_4.setEnabled(True)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 374, 791))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy)
        self.tabWidget_4.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_4.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget_4.setDocumentMode(True)
        self.tabWidget_4.setObjectName(_fromUtf8("tabWidget_4"))
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName(_fromUtf8("tab_11"))
        self.tabWidget_6 = QtGui.QTabWidget(self.tab_11)
        self.tabWidget_6.setGeometry(QtCore.QRect(30, 200, 311, 341))
        self.tabWidget_6.setDocumentMode(True)
        self.tabWidget_6.setObjectName(_fromUtf8("tabWidget_6"))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setEnabled(True)
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.label_35 = QtGui.QLabel(self.tab_8)
        self.label_35.setGeometry(QtCore.QRect(90, 30, 32, 16))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_9 = QtGui.QLabel(self.tab_8)
        self.label_9.setGeometry(QtCore.QRect(240, 30, 34, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_36 = QtGui.QLabel(self.tab_8)
        self.label_36.setGeometry(QtCore.QRect(170, 30, 28, 16))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_8)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 50, 281, 228))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelCh4 = QtGui.QLineEdit(self.layoutWidget1)
        self.labelCh4.setObjectName(_fromUtf8("labelCh4"))
        self.gridLayout.addWidget(self.labelCh4, 3, 3, 1, 1)
        self.unitsCh1 = QtGui.QLineEdit(self.layoutWidget1)
        self.unitsCh1.setObjectName(_fromUtf8("unitsCh1"))
        self.gridLayout.addWidget(self.unitsCh1, 0, 1, 1, 1)
        self.labelCh3 = QtGui.QLineEdit(self.layoutWidget1)
        self.labelCh3.setObjectName(_fromUtf8("labelCh3"))
        self.gridLayout.addWidget(self.labelCh3, 2, 3, 1, 1)
        self.enCh6_2 = QtGui.QCheckBox(self.layoutWidget1)
        self.enCh6_2.setChecked(False)
        self.enCh6_2.setObjectName(_fromUtf8("enCh6_2"))
        self.gridLayout.addWidget(self.enCh6_2, 6, 0, 1, 1)
        self.labelCh2 = QtGui.QLineEdit(self.layoutWidget1)
        self.labelCh2.setObjectName(_fromUtf8("labelCh2"))
        self.gridLayout.addWidget(self.labelCh2, 1, 3, 1, 1)
        self.gainCh2 = QtGui.QLineEdit(self.layoutWidget1)
        self.gainCh2.setObjectName(_fromUtf8("gainCh2"))
        self.gridLayout.addWidget(self.gainCh2, 1, 2, 1, 1)
        self.unitsCh6_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.unitsCh6_2.setObjectName(_fromUtf8("unitsCh6_2"))
        self.gridLayout.addWidget(self.unitsCh6_2, 6, 1, 1, 1)
        self.unitsCh6_3 = QtGui.QLineEdit(self.layoutWidget1)
        self.unitsCh6_3.setObjectName(_fromUtf8("unitsCh6_3"))
        self.gridLayout.addWidget(self.unitsCh6_3, 7, 1, 1, 1)
        self.gainCh6 = QtGui.QLineEdit(self.layoutWidget1)
        self.gainCh6.setObjectName(_fromUtf8("gainCh6"))
        self.gridLayout.addWidget(self.gainCh6, 5, 2, 1, 1)
        self.enCh4 = QtGui.QCheckBox(self.layoutWidget1)
        self.enCh4.setObjectName(_fromUtf8("enCh4"))
        self.gridLayout.addWidget(self.enCh4, 3, 0, 1, 1)
        self.labelCh6_3 = QtGui.QLineEdit(self.layoutWidget1)
        self.labelCh6_3.setObjectName(_fromUtf8("labelCh6_3"))
        self.gridLayout.addWidget(self.labelCh6_3, 7, 3, 1, 1)
        self.unitsCh5 = QtGui.QLineEdit(self.layoutWidget1)
        self.unitsCh5.setObjectName(_fromUtf8("unitsCh5"))
        self.gridLayout.addWidget(self.unitsCh5, 4, 1, 1, 1)
        self.unitsCh4 = QtGui.QLineEdit(self.layoutWidget1)
        self.unitsCh4.setObjectName(_fromUtf8("unitsCh4"))
        self.gridLayout.addWidget(self.unitsCh4, 3, 1, 1, 1)
        self.labelCh5 = QtGui.QLineEdit(self.layoutWidget1)
        self.labelCh5.setObjectName(_fromUtf8("labelCh5"))
        self.gridLayout.addWidget(self.labelCh5, 4, 3, 1, 1)
        self.enCh3 = QtGui.QCheckBox(self.layoutWidget1)
        self.enCh3.setObjectName(_fromUtf8("enCh3"))
        self.gridLayout.addWidget(self.enCh3, 2, 0, 1, 1)
        self.gainCh6_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.gainCh6_2.setObjectName(_fromUtf8("gainCh6_2"))
        self.gridLayout.addWidget(self.gainCh6_2, 6, 2, 1, 1)
        self.enCh6_3 = QtGui.QCheckBox(self.layoutWidget1)
        self.enCh6_3.setChecked(False)
        self.enCh6_3.setObjectName(_fromUtf8("enCh6_3"))
        self.gridLayout.addWidget(self.enCh6_3, 7, 0, 1, 1)
        self.gainCh6_3 = QtGui.QLineEdit(self.layoutWidget1)
        self.gainCh6_3.setObjectName(_fromUtf8("gainCh6_3"))
        self.gridLayout.addWidget(self.gainCh6_3, 7, 2, 1, 1)
        self.gainCh3 = QtGui.QLineEdit(self.layoutWidget1)
        self.gainCh3.setObjectName(_fromUtf8("gainCh3"))
        self.gridLayout.addWidget(self.gainCh3, 2, 2, 1, 1)
        self.gainCh1 = QtGui.QLineEdit(self.layoutWidget1)
        self.gainCh1.setObjectName(_fromUtf8("gainCh1"))
        self.gridLayout.addWidget(self.gainCh1, 0, 2, 1, 1)
        self.enCh2 = QtGui.QCheckBox(self.layoutWidget1)
        self.enCh2.setObjectName(_fromUtf8("enCh2"))
        self.gridLayout.addWidget(self.enCh2, 1, 0, 1, 1)
        self.unitsCh6 = QtGui.QLineEdit(self.layoutWidget1)
        self.unitsCh6.setObjectName(_fromUtf8("unitsCh6"))
        self.gridLayout.addWidget(self.unitsCh6, 5, 1, 1, 1)
        self.unitsCh2 = QtGui.QLineEdit(self.layoutWidget1)
        self.unitsCh2.setObjectName(_fromUtf8("unitsCh2"))
        self.gridLayout.addWidget(self.unitsCh2, 1, 1, 1, 1)
        self.gainCh5 = QtGui.QLineEdit(self.layoutWidget1)
        self.gainCh5.setObjectName(_fromUtf8("gainCh5"))
        self.gridLayout.addWidget(self.gainCh5, 4, 2, 1, 1)
        self.gainCh4 = QtGui.QLineEdit(self.layoutWidget1)
        self.gainCh4.setObjectName(_fromUtf8("gainCh4"))
        self.gridLayout.addWidget(self.gainCh4, 3, 2, 1, 1)
        self.unitsCh3 = QtGui.QLineEdit(self.layoutWidget1)
        self.unitsCh3.setObjectName(_fromUtf8("unitsCh3"))
        self.gridLayout.addWidget(self.unitsCh3, 2, 1, 1, 1)
        self.labelCh6 = QtGui.QLineEdit(self.layoutWidget1)
        self.labelCh6.setObjectName(_fromUtf8("labelCh6"))
        self.gridLayout.addWidget(self.labelCh6, 5, 3, 1, 1)
        self.labelCh1 = QtGui.QLineEdit(self.layoutWidget1)
        self.labelCh1.setObjectName(_fromUtf8("labelCh1"))
        self.gridLayout.addWidget(self.labelCh1, 0, 3, 1, 1)
        self.labelCh6_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.labelCh6_2.setObjectName(_fromUtf8("labelCh6_2"))
        self.gridLayout.addWidget(self.labelCh6_2, 6, 3, 1, 1)
        self.enCh1 = QtGui.QCheckBox(self.layoutWidget1)
        self.enCh1.setObjectName(_fromUtf8("enCh1"))
        self.gridLayout.addWidget(self.enCh1, 0, 0, 1, 1)
        self.enCh5 = QtGui.QCheckBox(self.layoutWidget1)
        self.enCh5.setObjectName(_fromUtf8("enCh5"))
        self.gridLayout.addWidget(self.enCh5, 4, 0, 1, 1)
        self.enCh6 = QtGui.QCheckBox(self.layoutWidget1)
        self.enCh6.setChecked(False)
        self.enCh6.setObjectName(_fromUtf8("enCh6"))
        self.gridLayout.addWidget(self.enCh6, 5, 0, 1, 1)
        self.tabWidget_6.addTab(self.tab_8, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.Notes = QtGui.QTextEdit(self.tab_7)
        self.Notes.setGeometry(QtCore.QRect(6, 11, 275, 249))
        self.Notes.setObjectName(_fromUtf8("Notes"))
        self.tabWidget_6.addTab(self.tab_7, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.hDistance = QtGui.QLineEdit(self.tab_6)
        self.hDistance.setGeometry(QtCore.QRect(1, 77, 109, 27))
        self.hDistance.setObjectName(_fromUtf8("hDistance"))
        self.vDistance = QtGui.QLineEdit(self.tab_6)
        self.vDistance.setGeometry(QtCore.QRect(1, 110, 109, 27))
        self.vDistance.setObjectName(_fromUtf8("vDistance"))
        self.calBounds = QtGui.QPushButton(self.tab_6)
        self.calBounds.setGeometry(QtCore.QRect(1, 44, 92, 27))
        self.calBounds.setObjectName(_fromUtf8("calBounds"))
        self.writeCalibration = QtGui.QPushButton(self.tab_6)
        self.writeCalibration.setGeometry(QtCore.QRect(140, 180, 93, 27))
        self.writeCalibration.setObjectName(_fromUtf8("writeCalibration"))
        self.label_13 = QtGui.QLabel(self.tab_6)
        self.label_13.setGeometry(QtCore.QRect(117, 82, 132, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.tab_6)
        self.label_14.setGeometry(QtCore.QRect(117, 111, 132, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.calBoundsDislpay = QtGui.QLabel(self.tab_6)
        self.calBoundsDislpay.setGeometry(QtCore.QRect(115, 51, 181, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calBoundsDislpay.sizePolicy().hasHeightForWidth())
        self.calBoundsDislpay.setSizePolicy(sizePolicy)
        self.calBoundsDislpay.setObjectName(_fromUtf8("calBoundsDislpay"))
        self.imageBounds = QtGui.QPushButton(self.tab_6)
        self.imageBounds.setGeometry(QtCore.QRect(1, 143, 109, 27))
        self.imageBounds.setObjectName(_fromUtf8("imageBounds"))
        self.imageBoundDisplay = QtGui.QLabel(self.tab_6)
        self.imageBoundDisplay.setGeometry(QtCore.QRect(116, 149, 191, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageBoundDisplay.sizePolicy().hasHeightForWidth())
        self.imageBoundDisplay.setSizePolicy(sizePolicy)
        self.imageBoundDisplay.setObjectName(_fromUtf8("imageBoundDisplay"))
        self.CalScan = QtGui.QPushButton(self.tab_6)
        self.CalScan.setGeometry(QtCore.QRect(1, 11, 85, 27))
        self.CalScan.setObjectName(_fromUtf8("CalScan"))
        self.ScanSize = QtGui.QComboBox(self.tab_6)
        self.ScanSize.setGeometry(QtCore.QRect(107, 12, 108, 23))
        self.ScanSize.setObjectName(_fromUtf8("ScanSize"))
        self.ScanSize.addItem(_fromUtf8(""))
        self.ScanSize.addItem(_fromUtf8(""))
        self.ScanSize.addItem(_fromUtf8(""))
        self.ScanSize.addItem(_fromUtf8(""))
        self.tabWidget_6.addTab(self.tab_6, _fromUtf8(""))
        self.frame_4 = QtGui.QFrame(self.tab_11)
        self.frame_4.setGeometry(QtCore.QRect(4, 6, 373, 191))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.updateROI = QtGui.QPushButton(self.frame_4)
        self.updateROI.setGeometry(QtCore.QRect(8, 74, 91, 27))
        self.updateROI.setObjectName(_fromUtf8("updateROI"))
        self.layoutWidget2 = QtGui.QWidget(self.frame_4)
        self.layoutWidget2.setGeometry(QtCore.QRect(180, 0, 181, 111))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_20.setSpacing(2)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.SamplesPerPoint = QtGui.QSpinBox(self.layoutWidget2)
        self.SamplesPerPoint.setMinimumSize(QtCore.QSize(80, 30))
        self.SamplesPerPoint.setMaximumSize(QtCore.QSize(80, 30))
        self.SamplesPerPoint.setAlignment(QtCore.Qt.AlignCenter)
        self.SamplesPerPoint.setMinimum(1)
        self.SamplesPerPoint.setMaximum(50)
        self.SamplesPerPoint.setSingleStep(1)
        self.SamplesPerPoint.setObjectName(_fromUtf8("SamplesPerPoint"))
        self.horizontalLayout_12.addWidget(self.SamplesPerPoint)
        self.label_45 = QtGui.QLabel(self.layoutWidget2)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.horizontalLayout_12.addWidget(self.label_45)
        self.verticalLayout_20.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.OScomboBox = QtGui.QComboBox(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OScomboBox.sizePolicy().hasHeightForWidth())
        self.OScomboBox.setSizePolicy(sizePolicy)
        self.OScomboBox.setMinimumSize(QtCore.QSize(60, 30))
        self.OScomboBox.setMaxCount(10)
        self.OScomboBox.setFrame(False)
        self.OScomboBox.setModelColumn(0)
        self.OScomboBox.setObjectName(_fromUtf8("OScomboBox"))
        self.OScomboBox.addItem(_fromUtf8(""))
        self.OScomboBox.addItem(_fromUtf8(""))
        self.OScomboBox.addItem(_fromUtf8(""))
        self.OScomboBox.addItem(_fromUtf8(""))
        self.OScomboBox.addItem(_fromUtf8(""))
        self.OScomboBox.addItem(_fromUtf8(""))
        self.OScomboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_11.addWidget(self.OScomboBox)
        self.label_41 = QtGui.QLabel(self.layoutWidget2)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.horizontalLayout_11.addWidget(self.label_41)
        self.verticalLayout_20.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.dxMicrons = QtGui.QLineEdit(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dxMicrons.sizePolicy().hasHeightForWidth())
        self.dxMicrons.setSizePolicy(sizePolicy)
        self.dxMicrons.setMinimumSize(QtCore.QSize(50, 30))
        self.dxMicrons.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dxMicrons.setText(_fromUtf8(""))
        self.dxMicrons.setObjectName(_fromUtf8("dxMicrons"))
        self.horizontalLayout_13.addWidget(self.dxMicrons)
        self.label_15 = QtGui.QLabel(self.layoutWidget2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_13.addWidget(self.label_15)
        self.verticalLayout_20.addLayout(self.horizontalLayout_13)
        self.layoutWidget3 = QtGui.QWidget(self.frame_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 0, 151, 72))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_21.setSpacing(2)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.Delay = QtGui.QLineEdit(self.layoutWidget3)
        self.Delay.setMinimumSize(QtCore.QSize(40, 30))
        self.Delay.setObjectName(_fromUtf8("Delay"))
        self.horizontalLayout_15.addWidget(self.Delay)
        self.label_46 = QtGui.QLabel(self.layoutWidget3)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.horizontalLayout_15.addWidget(self.label_46)
        self.verticalLayout_21.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.Mag = QtGui.QLineEdit(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mag.sizePolicy().hasHeightForWidth())
        self.Mag.setSizePolicy(sizePolicy)
        self.Mag.setMinimumSize(QtCore.QSize(80, 30))
        self.Mag.setMaximumSize(QtCore.QSize(80, 30))
        self.Mag.setText(_fromUtf8(""))
        self.Mag.setObjectName(_fromUtf8("Mag"))
        self.horizontalLayout_14.addWidget(self.Mag)
        self.label_61 = QtGui.QLabel(self.layoutWidget3)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.horizontalLayout_14.addWidget(self.label_61)
        self.verticalLayout_21.addLayout(self.horizontalLayout_14)
        self.widget = QtGui.QWidget(self.frame_4)
        self.widget.setGeometry(QtCore.QRect(10, 110, 181, 67))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_17.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.verticalLayout_23 = QtGui.QVBoxLayout()
        self.verticalLayout_23.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.label_24 = QtGui.QLabel(self.widget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.verticalLayout_23.addWidget(self.label_24)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_23.addWidget(self.label)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_23.addWidget(self.label_6)
        self.horizontalLayout_17.addLayout(self.verticalLayout_23)
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.ROIdim = QtGui.QLabel(self.widget)
        self.ROIdim.setObjectName(_fromUtf8("ROIdim"))
        self.verticalLayout_19.addWidget(self.ROIdim)
        self.dwellT = QtGui.QLabel(self.widget)
        self.dwellT.setText(_fromUtf8(""))
        self.dwellT.setObjectName(_fromUtf8("dwellT"))
        self.verticalLayout_19.addWidget(self.dwellT)
        self.scanT = QtGui.QLabel(self.widget)
        self.scanT.setText(_fromUtf8(""))
        self.scanT.setObjectName(_fromUtf8("scanT"))
        self.verticalLayout_19.addWidget(self.scanT)
        self.horizontalLayout_17.addLayout(self.verticalLayout_19)
        self.progressBar_3 = QtGui.QProgressBar(self.tab_11)
        self.progressBar_3.setGeometry(QtCore.QRect(90, 550, 211, 16))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.saveName = QtGui.QLineEdit(self.tab_11)
        self.saveName.setGeometry(QtCore.QRect(60, 640, 144, 27))
        self.saveName.setObjectName(_fromUtf8("saveName"))
        self.Channel = QtGui.QSpinBox(self.tab_11)
        self.Channel.setGeometry(QtCore.QRect(60, 610, 55, 27))
        self.Channel.setAutoFillBackground(False)
        self.Channel.setAlignment(QtCore.Qt.AlignCenter)
        self.Channel.setMaximum(1)
        self.Channel.setObjectName(_fromUtf8("Channel"))
        self.layoutWidget4 = QtGui.QWidget(self.tab_11)
        self.layoutWidget4.setGeometry(QtCore.QRect(230, 580, 101, 91))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget4)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Scan = QtGui.QPushButton(self.layoutWidget4)
        self.Scan.setObjectName(_fromUtf8("Scan"))
        self.gridLayout_2.addWidget(self.Scan, 0, 0, 1, 1)
        self.SaveScan = QtGui.QPushButton(self.layoutWidget4)
        self.SaveScan.setObjectName(_fromUtf8("SaveScan"))
        self.gridLayout_2.addWidget(self.SaveScan, 2, 0, 1, 1)
        self.StopScan = QtGui.QPushButton(self.layoutWidget4)
        self.StopScan.setObjectName(_fromUtf8("StopScan"))
        self.gridLayout_2.addWidget(self.StopScan, 1, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_11, _fromUtf8(""))
        self.tab_14 = QtGui.QWidget()
        self.tab_14.setObjectName(_fromUtf8("tab_14"))
        self.tabWidget_7 = QtGui.QTabWidget(self.tab_14)
        self.tabWidget_7.setGeometry(QtCore.QRect(0, 7, 428, 491))
        self.tabWidget_7.setDocumentMode(True)
        self.tabWidget_7.setObjectName(_fromUtf8("tabWidget_7"))
        self.tab_20 = QtGui.QWidget()
        self.tab_20.setObjectName(_fromUtf8("tab_20"))
        self.BeamCurrent = QtGui.QLineEdit(self.tab_20)
        self.BeamCurrent.setGeometry(QtCore.QRect(10, 30, 146, 27))
        self.BeamCurrent.setObjectName(_fromUtf8("BeamCurrent"))
        self.label_62 = QtGui.QLabel(self.tab_20)
        self.label_62.setGeometry(QtCore.QRect(160, 30, 91, 17))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.label_10 = QtGui.QLabel(self.tab_20)
        self.label_10.setGeometry(QtCore.QRect(160, 60, 131, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.KV = QtGui.QLineEdit(self.tab_20)
        self.KV.setGeometry(QtCore.QRect(10, 60, 146, 27))
        self.KV.setObjectName(_fromUtf8("KV"))
        self.tabWidget_7.addTab(self.tab_20, _fromUtf8(""))
        self.tab_15 = QtGui.QWidget()
        self.tab_15.setObjectName(_fromUtf8("tab_15"))
        self.Aux1Spin = QtGui.QDoubleSpinBox(self.tab_15)
        self.Aux1Spin.setGeometry(QtCore.QRect(10, 40, 91, 25))
        self.Aux1Spin.setDecimals(3)
        self.Aux1Spin.setMinimum(-10.0)
        self.Aux1Spin.setMaximum(10.0)
        self.Aux1Spin.setSingleStep(0.001)
        self.Aux1Spin.setObjectName(_fromUtf8("Aux1Spin"))
        self.Aux2Spin = QtGui.QDoubleSpinBox(self.tab_15)
        self.Aux2Spin.setGeometry(QtCore.QRect(10, 80, 91, 25))
        self.Aux2Spin.setDecimals(3)
        self.Aux2Spin.setMinimum(-10.0)
        self.Aux2Spin.setMaximum(10.0)
        self.Aux2Spin.setSingleStep(0.001)
        self.Aux2Spin.setObjectName(_fromUtf8("Aux2Spin"))
        self.label_47 = QtGui.QLabel(self.tab_15)
        self.label_47.setGeometry(QtCore.QRect(104, 44, 62, 16))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.label_48 = QtGui.QLabel(self.tab_15)
        self.label_48.setGeometry(QtCore.QRect(104, 83, 62, 16))
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.SetAux1 = QtGui.QPushButton(self.tab_15)
        self.SetAux1.setGeometry(QtCore.QRect(160, 38, 71, 24))
        self.SetAux1.setObjectName(_fromUtf8("SetAux1"))
        self.SetAux2 = QtGui.QPushButton(self.tab_15)
        self.SetAux2.setGeometry(QtCore.QRect(160, 76, 71, 26))
        self.SetAux2.setObjectName(_fromUtf8("SetAux2"))
        self.label_49 = QtGui.QLabel(self.tab_15)
        self.label_49.setGeometry(QtCore.QRect(90, 130, 81, 21))
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_50 = QtGui.QLabel(self.tab_15)
        self.label_50.setGeometry(QtCore.QRect(90, 170, 81, 21))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.Aux1Value = QtGui.QLabel(self.tab_15)
        self.Aux1Value.setGeometry(QtCore.QRect(20, 130, 62, 17))
        self.Aux1Value.setObjectName(_fromUtf8("Aux1Value"))
        self.Aux2Value = QtGui.QLabel(self.tab_15)
        self.Aux2Value.setGeometry(QtCore.QRect(20, 170, 62, 17))
        self.Aux2Value.setObjectName(_fromUtf8("Aux2Value"))
        self.tabWidget_7.addTab(self.tab_15, _fromUtf8(""))
        self.Sweep_2 = QtGui.QWidget()
        self.Sweep_2.setObjectName(_fromUtf8("Sweep_2"))
        self.frame_5 = QtGui.QFrame(self.Sweep_2)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 311, 421))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.label_51 = QtGui.QLabel(self.frame_5)
        self.label_51.setGeometry(QtCore.QRect(10, 0, 51, 21))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.Aux1En = QtGui.QCheckBox(self.frame_5)
        self.Aux1En.setGeometry(QtCore.QRect(70, 0, 61, 20))
        self.Aux1En.setObjectName(_fromUtf8("Aux1En"))
        self.delayAux1 = QtGui.QLineEdit(self.frame_5)
        self.delayAux1.setGeometry(QtCore.QRect(0, 100, 41, 27))
        self.delayAux1.setObjectName(_fromUtf8("delayAux1"))
        self.label_11 = QtGui.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(50, 100, 51, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.SweepDir = QtGui.QComboBox(self.frame_5)
        self.SweepDir.setGeometry(QtCore.QRect(0, 160, 51, 29))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SweepDir.sizePolicy().hasHeightForWidth())
        self.SweepDir.setSizePolicy(sizePolicy)
        self.SweepDir.setObjectName(_fromUtf8("SweepDir"))
        self.SweepDir.addItem(_fromUtf8(""))
        self.SweepDir.addItem(_fromUtf8(""))
        self.label_42 = QtGui.QLabel(self.frame_5)
        self.label_42.setGeometry(QtCore.QRect(0, 140, 101, 20))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.TransChannel = QtGui.QSpinBox(self.frame_5)
        self.TransChannel.setGeometry(QtCore.QRect(0, 210, 55, 27))
        self.TransChannel.setMaximum(5)
        self.TransChannel.setObjectName(_fromUtf8("TransChannel"))
        self.label_8 = QtGui.QLabel(self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(60, 210, 25, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.SweepName = QtGui.QLineEdit(self.frame_5)
        self.SweepName.setGeometry(QtCore.QRect(130, 310, 113, 27))
        self.SweepName.setObjectName(_fromUtf8("SweepName"))
        self.layoutWidget5 = QtGui.QWidget(self.frame_5)
        self.layoutWidget5.setGeometry(QtCore.QRect(130, 30, 148, 97))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Aux1Start = QtGui.QDoubleSpinBox(self.layoutWidget5)
        self.Aux1Start.setDecimals(3)
        self.Aux1Start.setMinimum(0.0)
        self.Aux1Start.setMaximum(10.0)
        self.Aux1Start.setSingleStep(0.25)
        self.Aux1Start.setObjectName(_fromUtf8("Aux1Start"))
        self.verticalLayout_2.addWidget(self.Aux1Start)
        self.Aux1End = QtGui.QDoubleSpinBox(self.layoutWidget5)
        self.Aux1End.setDecimals(3)
        self.Aux1End.setMinimum(-10.0)
        self.Aux1End.setMaximum(10.0)
        self.Aux1End.setSingleStep(0.25)
        self.Aux1End.setObjectName(_fromUtf8("Aux1End"))
        self.verticalLayout_2.addWidget(self.Aux1End)
        self.Aux1VStep = QtGui.QDoubleSpinBox(self.layoutWidget5)
        self.Aux1VStep.setPrefix(_fromUtf8(""))
        self.Aux1VStep.setDecimals(3)
        self.Aux1VStep.setMinimum(-1.0)
        self.Aux1VStep.setMaximum(1.0)
        self.Aux1VStep.setSingleStep(0.001)
        self.Aux1VStep.setProperty("value", 0.01)
        self.Aux1VStep.setObjectName(_fromUtf8("Aux1VStep"))
        self.verticalLayout_2.addWidget(self.Aux1VStep)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.label_52 = QtGui.QLabel(self.layoutWidget5)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.verticalLayout_15.addWidget(self.label_52)
        self.label_53 = QtGui.QLabel(self.layoutWidget5)
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.verticalLayout_15.addWidget(self.label_53)
        self.label_54 = QtGui.QLabel(self.layoutWidget5)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.verticalLayout_15.addWidget(self.label_54)
        self.horizontalLayout_3.addLayout(self.verticalLayout_15)
        self.layoutWidget6 = QtGui.QWidget(self.frame_5)
        self.layoutWidget6.setGeometry(QtCore.QRect(0, 30, 124, 64))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.Aux1Min = QtGui.QDoubleSpinBox(self.layoutWidget6)
        self.Aux1Min.setDecimals(3)
        self.Aux1Min.setMinimum(0.0)
        self.Aux1Min.setMaximum(10.0)
        self.Aux1Min.setSingleStep(0.01)
        self.Aux1Min.setObjectName(_fromUtf8("Aux1Min"))
        self.verticalLayout_17.addWidget(self.Aux1Min)
        self.Aux1SpinMin_3 = QtGui.QDoubleSpinBox(self.layoutWidget6)
        self.Aux1SpinMin_3.setDecimals(3)
        self.Aux1SpinMin_3.setMinimum(0.0)
        self.Aux1SpinMin_3.setMaximum(10.0)
        self.Aux1SpinMin_3.setSingleStep(0.25)
        self.Aux1SpinMin_3.setObjectName(_fromUtf8("Aux1SpinMin_3"))
        self.verticalLayout_17.addWidget(self.Aux1SpinMin_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_17)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.label_55 = QtGui.QLabel(self.layoutWidget6)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.verticalLayout_16.addWidget(self.label_55)
        self.label_56 = QtGui.QLabel(self.layoutWidget6)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.verticalLayout_16.addWidget(self.label_56)
        self.horizontalLayout_4.addLayout(self.verticalLayout_16)
        self.layoutWidget7 = QtGui.QWidget(self.frame_5)
        self.layoutWidget7.setGeometry(QtCore.QRect(130, 160, 151, 31))
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.OScomboBox_2 = QtGui.QComboBox(self.layoutWidget7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OScomboBox_2.sizePolicy().hasHeightForWidth())
        self.OScomboBox_2.setSizePolicy(sizePolicy)
        self.OScomboBox_2.setObjectName(_fromUtf8("OScomboBox_2"))
        self.OScomboBox_2.addItem(_fromUtf8(""))
        self.OScomboBox_2.addItem(_fromUtf8(""))
        self.OScomboBox_2.addItem(_fromUtf8(""))
        self.OScomboBox_2.addItem(_fromUtf8(""))
        self.OScomboBox_2.addItem(_fromUtf8(""))
        self.OScomboBox_2.addItem(_fromUtf8(""))
        self.OScomboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.OScomboBox_2)
        self.label_16 = QtGui.QLabel(self.layoutWidget7)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_5.addWidget(self.label_16)
        self.layoutWidget8 = QtGui.QWidget(self.frame_5)
        self.layoutWidget8.setGeometry(QtCore.QRect(130, 130, 151, 29))
        self.layoutWidget8.setObjectName(_fromUtf8("layoutWidget8"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.SamplesPerPoint_2 = QtGui.QSpinBox(self.layoutWidget8)
        self.SamplesPerPoint_2.setMinimum(1)
        self.SamplesPerPoint_2.setMaximum(100)
        self.SamplesPerPoint_2.setSingleStep(1)
        self.SamplesPerPoint_2.setObjectName(_fromUtf8("SamplesPerPoint_2"))
        self.horizontalLayout_6.addWidget(self.SamplesPerPoint_2)
        self.label_12 = QtGui.QLabel(self.layoutWidget8)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_6.addWidget(self.label_12)
        self.layoutWidget9 = QtGui.QWidget(self.frame_5)
        self.layoutWidget9.setGeometry(QtCore.QRect(0, 240, 121, 101))
        self.layoutWidget9.setObjectName(_fromUtf8("layoutWidget9"))
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.TransGain = QtGui.QLineEdit(self.layoutWidget9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TransGain.sizePolicy().hasHeightForWidth())
        self.TransGain.setSizePolicy(sizePolicy)
        self.TransGain.setObjectName(_fromUtf8("TransGain"))
        self.horizontalLayout_7.addWidget(self.TransGain)
        self.label_17 = QtGui.QLabel(self.layoutWidget9)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_7.addWidget(self.label_17)
        self.verticalLayout_18.addLayout(self.horizontalLayout_7)
        self.Sweep = QtGui.QPushButton(self.layoutWidget9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sweep.sizePolicy().hasHeightForWidth())
        self.Sweep.setSizePolicy(sizePolicy)
        self.Sweep.setObjectName(_fromUtf8("Sweep"))
        self.verticalLayout_18.addWidget(self.Sweep)
        self.SaveSweep = QtGui.QPushButton(self.layoutWidget9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveSweep.sizePolicy().hasHeightForWidth())
        self.SaveSweep.setSizePolicy(sizePolicy)
        self.SaveSweep.setObjectName(_fromUtf8("SaveSweep"))
        self.verticalLayout_18.addWidget(self.SaveSweep)
        self.tabWidget_7.addTab(self.Sweep_2, _fromUtf8(""))
        self.tabWidget_4.addTab(self.tab_14, _fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 370, 371, 491))
        self.tabWidget_2.setToolTip(_fromUtf8(""))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.ScanCombo = QtGui.QComboBox(self.tab_10)
        self.ScanCombo.setGeometry(QtCore.QRect(3, 15, 177, 31))
        self.ScanCombo.setObjectName(_fromUtf8("ScanCombo"))
        self.unloadScan = QtGui.QToolButton(self.tab_10)
        self.unloadScan.setEnabled(False)
        self.unloadScan.setGeometry(QtCore.QRect(185, 17, 21, 27))
        self.unloadScan.setToolTip(_fromUtf8(""))
        self.unloadScan.setCheckable(True)
        self.unloadScan.setAutoRaise(False)
        self.unloadScan.setObjectName(_fromUtf8("unloadScan"))
        self.label_18 = QtGui.QLabel(self.tab_10)
        self.label_18.setGeometry(QtCore.QRect(46, 50, 62, 17))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.profilelist = QtGui.QComboBox(self.tab_10)
        self.profilelist.setEnabled(False)
        self.profilelist.setGeometry(QtCore.QRect(45, 72, 117, 31))
        self.profilelist.setObjectName(_fromUtf8("profilelist"))
        self.SaveButton = QtGui.QPushButton(self.tab_10)
        self.SaveButton.setGeometry(QtCore.QRect(3, 269, 93, 27))
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))
        self.SwapAxes = QtGui.QPushButton(self.tab_10)
        self.SwapAxes.setGeometry(QtCore.QRect(209, 17, 41, 27))
        self.SwapAxes.setObjectName(_fromUtf8("SwapAxes"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_10)
        self.groupBox_4.setGeometry(QtCore.QRect(18, 109, 319, 149))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_4)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(176, 25, 143, 120))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_38 = QtGui.QLabel(self.groupBox_4)
        self.label_38.setGeometry(QtCore.QRect(176, 5, 62, 17))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.layoutWidget10 = QtGui.QWidget(self.groupBox_4)
        self.layoutWidget10.setGeometry(QtCore.QRect(13, 26, 149, 111))
        self.layoutWidget10.setObjectName(_fromUtf8("layoutWidget10"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget10)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_26 = QtGui.QLabel(self.layoutWidget10)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_26)
        self.label_27 = QtGui.QLabel(self.layoutWidget10)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_27)
        self.label_28 = QtGui.QLabel(self.layoutWidget10)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_28)
        self.label_29 = QtGui.QLabel(self.layoutWidget10)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_29)
        self.label_30 = QtGui.QLabel(self.layoutWidget10)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_30)
        self.label_31 = QtGui.QLabel(self.layoutWidget10)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_31)
        self.label_32 = QtGui.QLabel(self.layoutWidget10)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_32)
        self.label_33 = QtGui.QLabel(self.layoutWidget10)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_33)
        self.label_34 = QtGui.QLabel(self.layoutWidget10)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_34)
        self.label_37 = QtGui.QLabel(self.layoutWidget10)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_37)
        self.ExportProfile = QtGui.QPushButton(self.tab_10)
        self.ExportProfile.setEnabled(False)
        self.ExportProfile.setGeometry(QtCore.QRect(166, 74, 53, 27))
        self.ExportProfile.setObjectName(_fromUtf8("ExportProfile"))
        self.FlipLR = QtGui.QPushButton(self.tab_10)
        self.FlipLR.setGeometry(QtCore.QRect(252, 17, 26, 27))
        self.FlipLR.setObjectName(_fromUtf8("FlipLR"))
        self.FlipUD = QtGui.QPushButton(self.tab_10)
        self.FlipUD.setGeometry(QtCore.QRect(280, 17, 43, 27))
        self.FlipUD.setObjectName(_fromUtf8("FlipUD"))
        self.tabWidget_2.addTab(self.tab_10, _fromUtf8(""))
        self.tab_12 = QtGui.QWidget()
        self.tab_12.setObjectName(_fromUtf8("tab_12"))
        self.TransportcomboBox = QtGui.QComboBox(self.tab_12)
        self.TransportcomboBox.setGeometry(QtCore.QRect(5, 7, 169, 31))
        self.TransportcomboBox.setObjectName(_fromUtf8("TransportcomboBox"))
        self.PlotTrans = QtGui.QPushButton(self.tab_12)
        self.PlotTrans.setGeometry(QtCore.QRect(174, 9, 21, 27))
        self.PlotTrans.setMouseTracking(False)
        self.PlotTrans.setAcceptDrops(False)
        self.PlotTrans.setStatusTip(_fromUtf8(""))
        self.PlotTrans.setWhatsThis(_fromUtf8(""))
        self.PlotTrans.setObjectName(_fromUtf8("PlotTrans"))
        self.ExportTransPort = QtGui.QPushButton(self.tab_12)
        self.ExportTransPort.setGeometry(QtCore.QRect(196, 9, 26, 27))
        self.ExportTransPort.setObjectName(_fromUtf8("ExportTransPort"))
        self.tabWidget_2.addTab(self.tab_12, _fromUtf8(""))
        self.tab_24 = QtGui.QWidget()
        self.tab_24.setObjectName(_fromUtf8("tab_24"))
        self.SubPlotComobo = QtGui.QComboBox(self.tab_24)
        self.SubPlotComobo.setGeometry(QtCore.QRect(52, 1, 89, 31))
        self.SubPlotComobo.setObjectName(_fromUtf8("SubPlotComobo"))
        self.AxisCombo = QtGui.QComboBox(self.tab_24)
        self.AxisCombo.setGeometry(QtCore.QRect(51, 32, 89, 31))
        self.AxisCombo.setObjectName(_fromUtf8("AxisCombo"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_24)
        self.groupBox_2.setGeometry(QtCore.QRect(4, 65, 361, 91))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.PlotScansCombo = QtGui.QComboBox(self.groupBox_2)
        self.PlotScansCombo.setGeometry(QtCore.QRect(1, 21, 150, 31))
        self.PlotScansCombo.setObjectName(_fromUtf8("PlotScansCombo"))
        self.PlotScansComboCH = QtGui.QComboBox(self.groupBox_2)
        self.PlotScansComboCH.setGeometry(QtCore.QRect(150, 20, 63, 31))
        self.PlotScansComboCH.setObjectName(_fromUtf8("PlotScansComboCH"))
        self.label_21 = QtGui.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(157, 2, 62, 17))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.AddPlotScan = QtGui.QPushButton(self.groupBox_2)
        self.AddPlotScan.setGeometry(QtCore.QRect(300, 20, 21, 27))
        self.AddPlotScan.setObjectName(_fromUtf8("AddPlotScan"))
        self.PlotScansSpinAlpha = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.PlotScansSpinAlpha.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.PlotScansSpinAlpha.setMaximum(1.0)
        self.PlotScansSpinAlpha.setSingleStep(0.05)
        self.PlotScansSpinAlpha.setProperty("value", 1.0)
        self.PlotScansSpinAlpha.setObjectName(_fromUtf8("PlotScansSpinAlpha"))
        self.label_25 = QtGui.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(222, 4, 43, 17))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.ColorMap = QtGui.QComboBox(self.groupBox_2)
        self.ColorMap.setGeometry(QtCore.QRect(61, 54, 89, 31))
        self.ColorMap.setObjectName(_fromUtf8("ColorMap"))
        self.ColorBar = QtGui.QPushButton(self.groupBox_2)
        self.ColorBar.setEnabled(True)
        self.ColorBar.setGeometry(QtCore.QRect(250, 60, 91, 27))
        self.ColorBar.setObjectName(_fromUtf8("ColorBar"))
        self.ExportScan = QtGui.QPushButton(self.groupBox_2)
        self.ExportScan.setGeometry(QtCore.QRect(330, 20, 26, 27))
        self.ExportScan.setObjectName(_fromUtf8("ExportScan"))
        self.reverse = QtGui.QCheckBox(self.groupBox_2)
        self.reverse.setGeometry(QtCore.QRect(150, 60, 91, 21))
        self.reverse.setObjectName(_fromUtf8("reverse"))
        self.groupBox = QtGui.QGroupBox(self.tab_24)
        self.groupBox.setGeometry(QtCore.QRect(10, 260, 357, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.PlotProfileComboCH = QtGui.QComboBox(self.groupBox)
        self.PlotProfileComboCH.setGeometry(QtCore.QRect(150, 20, 63, 31))
        self.PlotProfileComboCH.setObjectName(_fromUtf8("PlotProfileComboCH"))
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(150, 0, 62, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.PlotProfileCombo = QtGui.QComboBox(self.groupBox)
        self.PlotProfileCombo.setGeometry(QtCore.QRect(0, 20, 150, 31))
        self.PlotProfileCombo.setObjectName(_fromUtf8("PlotProfileCombo"))
        self.AddPlotProfile = QtGui.QPushButton(self.groupBox)
        self.AddPlotProfile.setGeometry(QtCore.QRect(290, 20, 21, 27))
        self.AddPlotProfile.setObjectName(_fromUtf8("AddPlotProfile"))
        self.PlotProfileAlpha = QtGui.QDoubleSpinBox(self.groupBox)
        self.PlotProfileAlpha.setGeometry(QtCore.QRect(216, 24, 71, 27))
        self.PlotProfileAlpha.setMaximum(1.0)
        self.PlotProfileAlpha.setSingleStep(0.05)
        self.PlotProfileAlpha.setProperty("value", 1.0)
        self.PlotProfileAlpha.setObjectName(_fromUtf8("PlotProfileAlpha"))
        self.label_23 = QtGui.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(216, 5, 62, 17))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.ExportProfile_2 = QtGui.QPushButton(self.groupBox)
        self.ExportProfile_2.setEnabled(True)
        self.ExportProfile_2.setGeometry(QtCore.QRect(330, 20, 26, 27))
        self.ExportProfile_2.setObjectName(_fromUtf8("ExportProfile_2"))
        self.PlotColorCombo = QtGui.QComboBox(self.groupBox)
        self.PlotColorCombo.setGeometry(QtCore.QRect(60, 60, 89, 31))
        self.PlotColorCombo.setObjectName(_fromUtf8("PlotColorCombo"))
        self.label_19 = QtGui.QLabel(self.tab_24)
        self.label_19.setGeometry(QtCore.QRect(0, 8, 51, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_22 = QtGui.QLabel(self.tab_24)
        self.label_22.setGeometry(QtCore.QRect(2, 39, 41, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_24)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 390, 357, 50))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.ActivePlotsCombo = QtGui.QComboBox(self.groupBox_3)
        self.ActivePlotsCombo.setGeometry(QtCore.QRect(2, 19, 150, 31))
        self.ActivePlotsCombo.setObjectName(_fromUtf8("ActivePlotsCombo"))
        self.RemovePlot = QtGui.QPushButton(self.groupBox_3)
        self.RemovePlot.setGeometry(QtCore.QRect(153, 21, 91, 27))
        self.RemovePlot.setObjectName(_fromUtf8("RemovePlot"))
        self.AddAxis = QtGui.QPushButton(self.tab_24)
        self.AddAxis.setGeometry(QtCore.QRect(145, 35, 21, 27))
        self.AddAxis.setObjectName(_fromUtf8("AddAxis"))
        self.AddSubPlot = QtGui.QPushButton(self.tab_24)
        self.AddSubPlot.setGeometry(QtCore.QRect(146, 4, 21, 27))
        self.AddSubPlot.setObjectName(_fromUtf8("AddSubPlot"))
        self.RemoveSubPlot = QtGui.QPushButton(self.tab_24)
        self.RemoveSubPlot.setEnabled(False)
        self.RemoveSubPlot.setGeometry(QtCore.QRect(171, 4, 21, 27))
        self.RemoveSubPlot.setObjectName(_fromUtf8("RemoveSubPlot"))
        self.RemoveAxis = QtGui.QPushButton(self.tab_24)
        self.RemoveAxis.setEnabled(False)
        self.RemoveAxis.setGeometry(QtCore.QRect(171, 36, 21, 27))
        self.RemoveAxis.setObjectName(_fromUtf8("RemoveAxis"))
        self.ClearAxis = QtGui.QPushButton(self.tab_24)
        self.ClearAxis.setEnabled(False)
        self.ClearAxis.setGeometry(QtCore.QRect(197, 36, 43, 27))
        self.ClearAxis.setObjectName(_fromUtf8("ClearAxis"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_24)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 160, 361, 91))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.PlotSlicesCombo = QtGui.QComboBox(self.groupBox_5)
        self.PlotSlicesCombo.setGeometry(QtCore.QRect(0, 20, 150, 31))
        self.PlotSlicesCombo.setObjectName(_fromUtf8("PlotSlicesCombo"))
        self.label_40 = QtGui.QLabel(self.groupBox_5)
        self.label_40.setGeometry(QtCore.QRect(160, 0, 62, 17))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.reverse2 = QtGui.QCheckBox(self.groupBox_5)
        self.reverse2.setGeometry(QtCore.QRect(153, 58, 91, 21))
        self.reverse2.setObjectName(_fromUtf8("reverse2"))
        self.PlotSliceSpinAlpha = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.PlotSliceSpinAlpha.setGeometry(QtCore.QRect(220, 20, 71, 31))
        self.PlotSliceSpinAlpha.setMaximum(1.0)
        self.PlotSliceSpinAlpha.setSingleStep(0.05)
        self.PlotSliceSpinAlpha.setProperty("value", 1.0)
        self.PlotSliceSpinAlpha.setObjectName(_fromUtf8("PlotSliceSpinAlpha"))
        self.label_39 = QtGui.QLabel(self.groupBox_5)
        self.label_39.setGeometry(QtCore.QRect(225, 2, 43, 17))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.ColorBar2 = QtGui.QPushButton(self.groupBox_5)
        self.ColorBar2.setEnabled(True)
        self.ColorBar2.setGeometry(QtCore.QRect(243, 58, 91, 27))
        self.ColorBar2.setObjectName(_fromUtf8("ColorBar2"))
        self.AddPlotSlice = QtGui.QPushButton(self.groupBox_5)
        self.AddPlotSlice.setGeometry(QtCore.QRect(300, 20, 21, 27))
        self.AddPlotSlice.setObjectName(_fromUtf8("AddPlotSlice"))
        self.ExportSlice = QtGui.QPushButton(self.groupBox_5)
        self.ExportSlice.setGeometry(QtCore.QRect(330, 20, 26, 27))
        self.ExportSlice.setObjectName(_fromUtf8("ExportSlice"))
        self.PlotSliceComboCH = QtGui.QComboBox(self.groupBox_5)
        self.PlotSliceComboCH.setGeometry(QtCore.QRect(156, 19, 63, 31))
        self.PlotSliceComboCH.setObjectName(_fromUtf8("PlotSliceComboCH"))
        self.ColorMap2 = QtGui.QComboBox(self.groupBox_5)
        self.ColorMap2.setGeometry(QtCore.QRect(60, 50, 89, 31))
        self.ColorMap2.setObjectName(_fromUtf8("ColorMap2"))
        self.tabWidget_2.addTab(self.tab_24, _fromUtf8(""))
        self.tabWidget_3 = QtGui.QTabWidget(self.tab_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 0, 370, 361))
        self.tabWidget_3.setMinimumSize(QtCore.QSize(250, 250))
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.TestProfile = QtGui.QPushButton(self.tab_5)
        self.TestProfile.setGeometry(QtCore.QRect(12, 166, 91, 27))
        self.TestProfile.setObjectName(_fromUtf8("TestProfile"))
        self.tabWidget_3.addTab(self.tab_5, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.getBounds_pushButton = QtGui.QPushButton(self.tab_9)
        self.getBounds_pushButton.setGeometry(QtCore.QRect(30, 10, 94, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getBounds_pushButton.sizePolicy().hasHeightForWidth())
        self.getBounds_pushButton.setSizePolicy(sizePolicy)
        self.getBounds_pushButton.setObjectName(_fromUtf8("getBounds_pushButton"))
        self.label_2 = QtGui.QLabel(self.tab_9)
        self.label_2.setGeometry(QtCore.QRect(13, 49, 16, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_9)
        self.label_3.setGeometry(QtCore.QRect(13, 78, 17, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.xstart = QtGui.QLabel(self.tab_9)
        self.xstart.setGeometry(QtCore.QRect(36, 49, 71, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xstart.sizePolicy().hasHeightForWidth())
        self.xstart.setSizePolicy(sizePolicy)
        self.xstart.setObjectName(_fromUtf8("xstart"))
        self.xdelta = QtGui.QLabel(self.tab_9)
        self.xdelta.setGeometry(QtCore.QRect(36, 78, 71, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xdelta.sizePolicy().hasHeightForWidth())
        self.xdelta.setSizePolicy(sizePolicy)
        self.xdelta.setObjectName(_fromUtf8("xdelta"))
        self.label_4 = QtGui.QLabel(self.tab_9)
        self.label_4.setGeometry(QtCore.QRect(110, 50, 16, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab_9)
        self.label_5.setGeometry(QtCore.QRect(110, 80, 17, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ystart = QtGui.QLabel(self.tab_9)
        self.ystart.setGeometry(QtCore.QRect(134, 49, 91, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ystart.sizePolicy().hasHeightForWidth())
        self.ystart.setSizePolicy(sizePolicy)
        self.ystart.setObjectName(_fromUtf8("ystart"))
        self.ydelta = QtGui.QLabel(self.tab_9)
        self.ydelta.setGeometry(QtCore.QRect(134, 78, 101, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ydelta.sizePolicy().hasHeightForWidth())
        self.ydelta.setSizePolicy(sizePolicy)
        self.ydelta.setObjectName(_fromUtf8("ydelta"))
        self.layoutWidget11 = QtGui.QWidget(self.tab_9)
        self.layoutWidget11.setGeometry(QtCore.QRect(30, 130, 321, 29))
        self.layoutWidget11.setObjectName(_fromUtf8("layoutWidget11"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ShowSlice = QtGui.QPushButton(self.layoutWidget11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowSlice.sizePolicy().hasHeightForWidth())
        self.ShowSlice.setSizePolicy(sizePolicy)
        self.ShowSlice.setObjectName(_fromUtf8("ShowSlice"))
        self.horizontalLayout.addWidget(self.ShowSlice)
        self.SliceType = QtGui.QComboBox(self.layoutWidget11)
        self.SliceType.setEnabled(False)
        self.SliceType.setObjectName(_fromUtf8("SliceType"))
        self.horizontalLayout.addWidget(self.SliceType)
        self.tabWidget_3.addTab(self.tab_9, _fromUtf8(""))
        self.tab_16 = QtGui.QWidget()
        self.tab_16.setObjectName(_fromUtf8("tab_16"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_16)
        self.layoutWidget_2.setGeometry(QtCore.QRect(6, 9, 351, 291))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.HistWidget = MplHIST(self.layoutWidget_2)
        self.HistWidget.setObjectName(_fromUtf8("HistWidget"))
        self.verticalLayout_12.addWidget(self.HistWidget)
        self.SliderVmin = QtGui.QSlider(self.layoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.SliderVmin.setPalette(palette)
        self.SliderVmin.setAutoFillBackground(False)
        self.SliderVmin.setMaximum(49)
        self.SliderVmin.setProperty("value", 0)
        self.SliderVmin.setOrientation(QtCore.Qt.Horizontal)
        self.SliderVmin.setObjectName(_fromUtf8("SliderVmin"))
        self.verticalLayout_12.addWidget(self.SliderVmin)
        self.SliderVmax = QtGui.QSlider(self.layoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.SliderVmax.setPalette(palette)
        self.SliderVmax.setMaximum(49)
        self.SliderVmax.setProperty("value", 49)
        self.SliderVmax.setOrientation(QtCore.Qt.Horizontal)
        self.SliderVmax.setObjectName(_fromUtf8("SliderVmax"))
        self.verticalLayout_12.addWidget(self.SliderVmax)
        self.tabWidget_3.addTab(self.tab_16, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.control.setWidget(self.dockWidgetContents_5)
        MplMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.control)
        self.mplactionOpen = QtGui.QAction(MplMainWindow)
        self.mplactionOpen.setObjectName(_fromUtf8("mplactionOpen"))
        self.mplactionQuit = QtGui.QAction(MplMainWindow)
        self.mplactionQuit.setObjectName(_fromUtf8("mplactionQuit"))
        self.actionSave = QtGui.QAction(MplMainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionCalibrate = QtGui.QAction(MplMainWindow)
        self.actionCalibrate.setObjectName(_fromUtf8("actionCalibrate"))
        self.actionCalibrate_2 = QtGui.QAction(MplMainWindow)
        self.actionCalibrate_2.setObjectName(_fromUtf8("actionCalibrate_2"))
        self.actionSave_2 = QtGui.QAction(MplMainWindow)
        self.actionSave_2.setObjectName(_fromUtf8("actionSave_2"))
        self.control.raise_()
        self.mplmenuFile.addAction(self.mplactionOpen)
        self.mplmenuFile.addSeparator()
        self.mplmenuFile.addAction(self.mplactionQuit)
        self.mplmenuFile.addSeparator()
        self.mplmenuFile.addAction(self.actionSave_2)
        self.menuEdit.addAction(self.actionCalibrate_2)
        self.mplmenubar.addAction(self.mplmenuFile.menuAction())
        self.mplmenubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MplMainWindow)
        self.tabImageAnalysis.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(1)
        self.analysisCh.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QObject.connect(self.PlotScansCombo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.ScanCombo.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)
        MplMainWindow.setTabOrder(self.unitsCh1, self.gainCh1)
        MplMainWindow.setTabOrder(self.gainCh1, self.labelCh1)
        MplMainWindow.setTabOrder(self.labelCh1, self.unitsCh2)
        MplMainWindow.setTabOrder(self.unitsCh2, self.gainCh2)
        MplMainWindow.setTabOrder(self.gainCh2, self.labelCh2)
        MplMainWindow.setTabOrder(self.labelCh2, self.unitsCh3)
        MplMainWindow.setTabOrder(self.unitsCh3, self.gainCh3)
        MplMainWindow.setTabOrder(self.gainCh3, self.labelCh3)
        MplMainWindow.setTabOrder(self.labelCh3, self.unitsCh4)
        MplMainWindow.setTabOrder(self.unitsCh4, self.gainCh4)
        MplMainWindow.setTabOrder(self.gainCh4, self.labelCh4)
        MplMainWindow.setTabOrder(self.labelCh4, self.unitsCh5)
        MplMainWindow.setTabOrder(self.unitsCh5, self.gainCh5)
        MplMainWindow.setTabOrder(self.gainCh5, self.labelCh5)
        MplMainWindow.setTabOrder(self.labelCh5, self.unitsCh6)
        MplMainWindow.setTabOrder(self.unitsCh6, self.gainCh6)
        MplMainWindow.setTabOrder(self.gainCh6, self.labelCh6)
        MplMainWindow.setTabOrder(self.labelCh6, self.enCh1)
        MplMainWindow.setTabOrder(self.enCh1, self.enCh2)
        MplMainWindow.setTabOrder(self.enCh2, self.enCh3)
        MplMainWindow.setTabOrder(self.enCh3, self.enCh4)
        MplMainWindow.setTabOrder(self.enCh4, self.enCh5)
        MplMainWindow.setTabOrder(self.enCh5, self.enCh6)
        MplMainWindow.setTabOrder(self.enCh6, self.tabWidget_6)
        MplMainWindow.setTabOrder(self.tabWidget_6, self.analysisCh)
        MplMainWindow.setTabOrder(self.analysisCh, self.tabWidget_4)
        MplMainWindow.setTabOrder(self.tabWidget_4, self.tabWidget)
        MplMainWindow.setTabOrder(self.tabWidget, self.hDistance)
        MplMainWindow.setTabOrder(self.hDistance, self.vDistance)
        MplMainWindow.setTabOrder(self.vDistance, self.calBounds)
        MplMainWindow.setTabOrder(self.calBounds, self.writeCalibration)
        MplMainWindow.setTabOrder(self.writeCalibration, self.imageBounds)
        MplMainWindow.setTabOrder(self.imageBounds, self.CalScan)
        MplMainWindow.setTabOrder(self.CalScan, self.ScanSize)
        MplMainWindow.setTabOrder(self.ScanSize, self.Notes)
        MplMainWindow.setTabOrder(self.Notes, self.SamplesPerPoint)
        MplMainWindow.setTabOrder(self.SamplesPerPoint, self.Mag)
        MplMainWindow.setTabOrder(self.Mag, self.Delay)
        MplMainWindow.setTabOrder(self.Delay, self.dxMicrons)
        MplMainWindow.setTabOrder(self.dxMicrons, self.updateROI)
        MplMainWindow.setTabOrder(self.updateROI, self.OScomboBox)
        MplMainWindow.setTabOrder(self.OScomboBox, self.Scan)
        MplMainWindow.setTabOrder(self.Scan, self.saveName)
        MplMainWindow.setTabOrder(self.saveName, self.SaveScan)
        MplMainWindow.setTabOrder(self.SaveScan, self.Channel)
        MplMainWindow.setTabOrder(self.Channel, self.tabWidget_7)
        MplMainWindow.setTabOrder(self.tabWidget_7, self.BeamCurrent)
        MplMainWindow.setTabOrder(self.BeamCurrent, self.KV)
        MplMainWindow.setTabOrder(self.KV, self.Aux1Spin)
        MplMainWindow.setTabOrder(self.Aux1Spin, self.Aux2Spin)
        MplMainWindow.setTabOrder(self.Aux2Spin, self.SetAux1)
        MplMainWindow.setTabOrder(self.SetAux1, self.SetAux2)
        MplMainWindow.setTabOrder(self.SetAux2, self.Aux1En)
        MplMainWindow.setTabOrder(self.Aux1En, self.Aux1Start)
        MplMainWindow.setTabOrder(self.Aux1Start, self.Aux1End)
        MplMainWindow.setTabOrder(self.Aux1End, self.Aux1VStep)
        MplMainWindow.setTabOrder(self.Aux1VStep, self.delayAux1)
        MplMainWindow.setTabOrder(self.delayAux1, self.Sweep)
        MplMainWindow.setTabOrder(self.Sweep, self.SaveSweep)
        MplMainWindow.setTabOrder(self.SaveSweep, self.SweepName)
        MplMainWindow.setTabOrder(self.SweepName, self.TransChannel)
        MplMainWindow.setTabOrder(self.TransChannel, self.TransGain)
        MplMainWindow.setTabOrder(self.TransGain, self.tabWidget_2)
        MplMainWindow.setTabOrder(self.tabWidget_2, self.ScanCombo)
        MplMainWindow.setTabOrder(self.ScanCombo, self.unloadScan)
        MplMainWindow.setTabOrder(self.unloadScan, self.profilelist)
        MplMainWindow.setTabOrder(self.profilelist, self.SaveButton)
        MplMainWindow.setTabOrder(self.SaveButton, self.SwapAxes)
        MplMainWindow.setTabOrder(self.SwapAxes, self.textEdit)
        MplMainWindow.setTabOrder(self.textEdit, self.ExportProfile)
        MplMainWindow.setTabOrder(self.ExportProfile, self.FlipLR)
        MplMainWindow.setTabOrder(self.FlipLR, self.FlipUD)
        MplMainWindow.setTabOrder(self.FlipUD, self.TransportcomboBox)
        MplMainWindow.setTabOrder(self.TransportcomboBox, self.PlotTrans)
        MplMainWindow.setTabOrder(self.PlotTrans, self.ExportTransPort)
        MplMainWindow.setTabOrder(self.ExportTransPort, self.SubPlotComobo)
        MplMainWindow.setTabOrder(self.SubPlotComobo, self.AxisCombo)
        MplMainWindow.setTabOrder(self.AxisCombo, self.PlotScansCombo)
        MplMainWindow.setTabOrder(self.PlotScansCombo, self.PlotScansComboCH)
        MplMainWindow.setTabOrder(self.PlotScansComboCH, self.AddPlotScan)
        MplMainWindow.setTabOrder(self.AddPlotScan, self.PlotScansSpinAlpha)
        MplMainWindow.setTabOrder(self.PlotScansSpinAlpha, self.ColorMap)
        MplMainWindow.setTabOrder(self.ColorMap, self.ColorBar)
        MplMainWindow.setTabOrder(self.ColorBar, self.ExportScan)
        MplMainWindow.setTabOrder(self.ExportScan, self.reverse)
        MplMainWindow.setTabOrder(self.reverse, self.PlotProfileComboCH)
        MplMainWindow.setTabOrder(self.PlotProfileComboCH, self.PlotProfileCombo)
        MplMainWindow.setTabOrder(self.PlotProfileCombo, self.AddPlotProfile)
        MplMainWindow.setTabOrder(self.AddPlotProfile, self.PlotProfileAlpha)
        MplMainWindow.setTabOrder(self.PlotProfileAlpha, self.ExportProfile_2)
        MplMainWindow.setTabOrder(self.ExportProfile_2, self.PlotColorCombo)
        MplMainWindow.setTabOrder(self.PlotColorCombo, self.ActivePlotsCombo)
        MplMainWindow.setTabOrder(self.ActivePlotsCombo, self.RemovePlot)
        MplMainWindow.setTabOrder(self.RemovePlot, self.AddAxis)
        MplMainWindow.setTabOrder(self.AddAxis, self.AddSubPlot)
        MplMainWindow.setTabOrder(self.AddSubPlot, self.RemoveSubPlot)
        MplMainWindow.setTabOrder(self.RemoveSubPlot, self.RemoveAxis)
        MplMainWindow.setTabOrder(self.RemoveAxis, self.ClearAxis)
        MplMainWindow.setTabOrder(self.ClearAxis, self.PlotSlicesCombo)
        MplMainWindow.setTabOrder(self.PlotSlicesCombo, self.reverse2)
        MplMainWindow.setTabOrder(self.reverse2, self.PlotSliceSpinAlpha)
        MplMainWindow.setTabOrder(self.PlotSliceSpinAlpha, self.ColorBar2)
        MplMainWindow.setTabOrder(self.ColorBar2, self.AddPlotSlice)
        MplMainWindow.setTabOrder(self.AddPlotSlice, self.ExportSlice)
        MplMainWindow.setTabOrder(self.ExportSlice, self.PlotSliceComboCH)
        MplMainWindow.setTabOrder(self.PlotSliceComboCH, self.ColorMap2)
        MplMainWindow.setTabOrder(self.ColorMap2, self.tabWidget_3)
        MplMainWindow.setTabOrder(self.tabWidget_3, self.TestProfile)
        MplMainWindow.setTabOrder(self.TestProfile, self.getBounds_pushButton)
        MplMainWindow.setTabOrder(self.getBounds_pushButton, self.ShowSlice)
        MplMainWindow.setTabOrder(self.ShowSlice, self.SliceType)
        MplMainWindow.setTabOrder(self.SliceType, self.SliderVmin)
        MplMainWindow.setTabOrder(self.SliderVmin, self.SliderVmax)
        MplMainWindow.setTabOrder(self.SliderVmax, self.tabWidget_5)

    def retranslateUi(self, MplMainWindow):
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "MainWindow", None))
        self.singleView.setText(_translate("MplMainWindow", "...", None))
        self.quadView.setText(_translate("MplMainWindow", "...", None))
        self.toolButton_9.setText(_translate("MplMainWindow", "...", None))
        self.toolButton_10.setText(_translate("MplMainWindow", "...", None))
        self.CrossHair.setToolTip(_translate("MplMainWindow", "Crosshair", None))
        self.CrossHair.setText(_translate("MplMainWindow", "...", "Crosshair"))
        self.toolButton_4.setText(_translate("MplMainWindow", "...", None))
        self.Sel.setToolTip(_translate("MplMainWindow", "Region of Interest", None))
        self.Sel.setText(_translate("MplMainWindow", "...", "Region of Interest"))
        self.Vis.setToolTip(_translate("MplMainWindow", "Region of Interest", None))
        self.Vis.setText(_translate("MplMainWindow", "...", "Region of Interest"))
        self.ROI.setToolTip(_translate("MplMainWindow", "Region of Interest", None))
        self.ROI.setText(_translate("MplMainWindow", "...", "Region of Interest"))
        self.ROICross.setText(_translate("MplMainWindow", "...", None))
        self.Line.setToolTip(_translate("MplMainWindow", "Line Profile", None))
        self.Line.setText(_translate("MplMainWindow", "...", "Line Profile"))
        self.toolButton.setText(_translate("MplMainWindow", "...", None))
        self.toolButton_2.setText(_translate("MplMainWindow", "...", None))
        self.toolButton_8.setText(_translate("MplMainWindow", "...", None))
        self.toolButton_3.setText(_translate("MplMainWindow", "...", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_17), _translate("MplMainWindow", "Tab1", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_18), _translate("MplMainWindow", "Tab2", None))
        self.tabImageAnalysis.setTabText(self.tabImageAnalysis.indexOf(self.tabImage), _translate("MplMainWindow", "Imaging", None))
        self.analysisCh.setTabText(self.analysisCh.indexOf(self.Ch1tab), _translate("MplMainWindow", "Tab 1", None))
        self.analysisCh.setTabText(self.analysisCh.indexOf(self.Ch2tap), _translate("MplMainWindow", "Tab 2", None))
        self.analysisCh.setTabText(self.analysisCh.indexOf(self.Ch3tab), _translate("MplMainWindow", "Tab 3", None))
        self.analysisCh.setTabText(self.analysisCh.indexOf(self.Ch4tab), _translate("MplMainWindow", "Tab 4", None))
        self.analysisCh.setTabText(self.analysisCh.indexOf(self.Ch5tab), _translate("MplMainWindow", "Tab 5", None))
        self.analysisCh.setTabText(self.analysisCh.indexOf(self.Ch6tab), _translate("MplMainWindow", "Tab 6", None))
        self.tabImageAnalysis.setTabText(self.tabImageAnalysis.indexOf(self.tabAnalysis), _translate("MplMainWindow", "Analysis", None))
        self.tabImageAnalysis.setTabText(self.tabImageAnalysis.indexOf(self.tab_4), _translate("MplMainWindow", "Transport", None))
        self.tabImageAnalysis.setTabText(self.tabImageAnalysis.indexOf(self.tab_3), _translate("MplMainWindow", "Page", None))
        self.mplmenuFile.setTitle(_translate("MplMainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MplMainWindow", "Edit", None))
        self.label_35.setText(_translate("MplMainWindow", "Units", None))
        self.label_9.setText(_translate("MplMainWindow", "Label", None))
        self.label_36.setText(_translate("MplMainWindow", "Gain", None))
        self.enCh6_2.setText(_translate("MplMainWindow", "Ch 7", None))
        self.enCh4.setText(_translate("MplMainWindow", "Ch 4", None))
        self.enCh3.setText(_translate("MplMainWindow", "Ch 3", None))
        self.enCh6_3.setText(_translate("MplMainWindow", "Ch 8", None))
        self.enCh2.setText(_translate("MplMainWindow", "Ch 2", None))
        self.enCh1.setText(_translate("MplMainWindow", "Ch 1", None))
        self.enCh5.setText(_translate("MplMainWindow", "Ch 5", None))
        self.enCh6.setText(_translate("MplMainWindow", "Ch 6", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_8), _translate("MplMainWindow", "Units and Gain", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_7), _translate("MplMainWindow", "Notes", None))
        self.calBounds.setText(_translate("MplMainWindow", "Cal Bounds", None))
        self.writeCalibration.setText(_translate("MplMainWindow", "Calibrate", None))
        self.label_13.setText(_translate("MplMainWindow", "hDistance (microns)", None))
        self.label_14.setText(_translate("MplMainWindow", "vDistance (microns)", None))
        self.calBoundsDislpay.setText(_translate("MplMainWindow", "calibration bounds", None))
        self.imageBounds.setText(_translate("MplMainWindow", "Image Bounds", None))
        self.imageBoundDisplay.setText(_translate("MplMainWindow", "image bounds", None))
        self.CalScan.setText(_translate("MplMainWindow", "Cal Scan", None))
        self.ScanSize.setItemText(0, _translate("MplMainWindow", "256x256", None))
        self.ScanSize.setItemText(1, _translate("MplMainWindow", "512x512", None))
        self.ScanSize.setItemText(2, _translate("MplMainWindow", "1024x1024", None))
        self.ScanSize.setItemText(3, _translate("MplMainWindow", "2048x2048", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_6), _translate("MplMainWindow", "Calibrate", None))
        self.updateROI.setText(_translate("MplMainWindow", "updateROI", None))
        self.label_45.setText(_translate("MplMainWindow", "# Samples", None))
        self.OScomboBox.setItemText(0, _translate("MplMainWindow", "0", None))
        self.OScomboBox.setItemText(1, _translate("MplMainWindow", "2", None))
        self.OScomboBox.setItemText(2, _translate("MplMainWindow", "4", None))
        self.OScomboBox.setItemText(3, _translate("MplMainWindow", "8", None))
        self.OScomboBox.setItemText(4, _translate("MplMainWindow", "16", None))
        self.OScomboBox.setItemText(5, _translate("MplMainWindow", "32", None))
        self.OScomboBox.setItemText(6, _translate("MplMainWindow", "64", None))
        self.label_41.setText(_translate("MplMainWindow", "OverSampling", None))
        self.label_15.setText(_translate("MplMainWindow", "dx in microns", None))
        self.Delay.setText(_translate("MplMainWindow", "5e-8", None))
        self.label_46.setText(_translate("MplMainWindow", "Delay (s) ", None))
        self.label_61.setText(_translate("MplMainWindow", "Mag", None))
        self.label_24.setText(_translate("MplMainWindow", "ROI scan size", None))
        self.label.setText(_translate("MplMainWindow", "Dwell Time", None))
        self.label_6.setText(_translate("MplMainWindow", "Scan Time", None))
        self.ROIdim.setText(_translate("MplMainWindow", "[xpoints,ypoints]", None))
        self.Scan.setText(_translate("MplMainWindow", "Scan", None))
        self.SaveScan.setText(_translate("MplMainWindow", "Save_Scan", None))
        self.StopScan.setText(_translate("MplMainWindow", "Stop", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("MplMainWindow", "ScanSetup", None))
        self.label_62.setText(_translate("MplMainWindow", "Beam Current", None))
        self.label_10.setText(_translate("MplMainWindow", "Accel. Voltage", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_20), _translate("MplMainWindow", "Microscope", None))
        self.label_47.setText(_translate("MplMainWindow", "Aux1 V", None))
        self.label_48.setText(_translate("MplMainWindow", "Aux2 V", None))
        self.SetAux1.setText(_translate("MplMainWindow", "Set", None))
        self.SetAux2.setText(_translate("MplMainWindow", "Set", None))
        self.label_49.setText(_translate("MplMainWindow", "Aux1 V", None))
        self.label_50.setText(_translate("MplMainWindow", "Aux2 V", None))
        self.Aux1Value.setText(_translate("MplMainWindow", "0", None))
        self.Aux2Value.setText(_translate("MplMainWindow", "0", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_15), _translate("MplMainWindow", "Biasing", None))
        self.label_51.setText(_translate("MplMainWindow", "Enable", None))
        self.Aux1En.setText(_translate("MplMainWindow", "Aux 1", None))
        self.delayAux1.setText(_translate("MplMainWindow", "0.4", None))
        self.label_11.setText(_translate("MplMainWindow", "delay(s)", None))
        self.SweepDir.setItemText(0, _translate("MplMainWindow", " +", None))
        self.SweepDir.setItemText(1, _translate("MplMainWindow", " -", None))
        self.label_42.setText(_translate("MplMainWindow", "Sweep direction", None))
        self.label_8.setText(_translate("MplMainWindow", "CH", None))
        self.Aux1VStep.setSuffix(_translate("MplMainWindow", " V", None))
        self.label_52.setText(_translate("MplMainWindow", "Start", None))
        self.label_53.setText(_translate("MplMainWindow", "End", None))
        self.label_54.setText(_translate("MplMainWindow", "Step V", None))
        self.label_55.setText(_translate("MplMainWindow", "Min", None))
        self.label_56.setText(_translate("MplMainWindow", "Max", None))
        self.OScomboBox_2.setItemText(0, _translate("MplMainWindow", "0", None))
        self.OScomboBox_2.setItemText(1, _translate("MplMainWindow", "2", None))
        self.OScomboBox_2.setItemText(2, _translate("MplMainWindow", "4", None))
        self.OScomboBox_2.setItemText(3, _translate("MplMainWindow", "8", None))
        self.OScomboBox_2.setItemText(4, _translate("MplMainWindow", "16", None))
        self.OScomboBox_2.setItemText(5, _translate("MplMainWindow", "32", None))
        self.OScomboBox_2.setItemText(6, _translate("MplMainWindow", "64", None))
        self.label_16.setText(_translate("MplMainWindow", "oversampling", None))
        self.label_12.setText(_translate("MplMainWindow", "samples", None))
        self.TransGain.setText(_translate("MplMainWindow", "1", None))
        self.label_17.setText(_translate("MplMainWindow", "Gain", None))
        self.Sweep.setText(_translate("MplMainWindow", "Run Sweep", None))
        self.SaveSweep.setText(_translate("MplMainWindow", "Save Sweep", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Sweep_2), _translate("MplMainWindow", "Sweep", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_14), _translate("MplMainWindow", "Experiment Variables", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MplMainWindow", "Control", None))
        self.unloadScan.setWhatsThis(_translate("MplMainWindow", "hhh", None))
        self.unloadScan.setText(_translate("MplMainWindow", "-", None))
        self.label_18.setText(_translate("MplMainWindow", "profiles", None))
        self.SaveButton.setText(_translate("MplMainWindow", "Save", None))
        self.SwapAxes.setToolTip(_translate("MplMainWindow", "swap axes", None))
        self.SwapAxes.setText(_translate("MplMainWindow", "swap", None))
        self.groupBox_4.setTitle(_translate("MplMainWindow", "Scan Info", None))
        self.label_38.setText(_translate("MplMainWindow", "Notes", None))
        self.label_26.setText(_translate("MplMainWindow", "Name:", None))
        self.label_27.setText(_translate("MplMainWindow", "TextLabel", None))
        self.label_28.setText(_translate("MplMainWindow", "Delay:", None))
        self.label_29.setText(_translate("MplMainWindow", "TextLabel", None))
        self.label_30.setText(_translate("MplMainWindow", "Mag:", None))
        self.label_31.setText(_translate("MplMainWindow", "TextLabel", None))
        self.label_32.setText(_translate("MplMainWindow", "Accel:", None))
        self.label_33.setText(_translate("MplMainWindow", "TextLabel", None))
        self.label_34.setText(_translate("MplMainWindow", "Beam:", None))
        self.label_37.setText(_translate("MplMainWindow", "TextLabel", None))
        self.ExportProfile.setText(_translate("MplMainWindow", "export", None))
        self.FlipLR.setToolTip(_translate("MplMainWindow", "flip left reft", None))
        self.FlipLR.setText(_translate("MplMainWindow", "[|]", None))
        self.FlipUD.setToolTip(_translate("MplMainWindow", "flip up down", None))
        self.FlipUD.setText(_translate("MplMainWindow", "flipud", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MplMainWindow", "Scans", None))
        self.PlotTrans.setToolTip(_translate("MplMainWindow", "plot", None))
        self.PlotTrans.setText(_translate("MplMainWindow", "+", None))
        self.ExportTransPort.setToolTip(_translate("MplMainWindow", "export iv", None))
        self.ExportTransPort.setText(_translate("MplMainWindow", "->", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MplMainWindow", "Transport", None))
        self.groupBox_2.setTitle(_translate("MplMainWindow", "Scans", None))
        self.label_21.setText(_translate("MplMainWindow", "Ch", None))
        self.AddPlotScan.setToolTip(_translate("MplMainWindow", "plot", None))
        self.AddPlotScan.setText(_translate("MplMainWindow", "+", None))
        self.label_25.setText(_translate("MplMainWindow", "alpha", None))
        self.ColorMap.setToolTip(_translate("MplMainWindow", "colormap", None))
        self.ColorBar.setText(_translate("MplMainWindow", "colorbar", None))
        self.ExportScan.setToolTip(_translate("MplMainWindow", "export", None))
        self.ExportScan.setText(_translate("MplMainWindow", "->", None))
        self.reverse.setText(_translate("MplMainWindow", "reverse", None))
        self.groupBox.setTitle(_translate("MplMainWindow", "Profiles", None))
        self.label_20.setText(_translate("MplMainWindow", "Ch", None))
        self.AddPlotProfile.setToolTip(_translate("MplMainWindow", "plot", None))
        self.AddPlotProfile.setText(_translate("MplMainWindow", "+", None))
        self.label_23.setText(_translate("MplMainWindow", "alpha", None))
        self.ExportProfile_2.setToolTip(_translate("MplMainWindow", "export", None))
        self.ExportProfile_2.setText(_translate("MplMainWindow", "->", None))
        self.label_19.setText(_translate("MplMainWindow", "subplot", None))
        self.label_22.setText(_translate("MplMainWindow", "axis", None))
        self.groupBox_3.setTitle(_translate("MplMainWindow", "ActivePlots", None))
        self.RemovePlot.setText(_translate("MplMainWindow", "remove", None))
        self.AddAxis.setToolTip(_translate("MplMainWindow", "add axis", None))
        self.AddAxis.setText(_translate("MplMainWindow", "+", None))
        self.AddSubPlot.setToolTip(_translate("MplMainWindow", "add subplot", None))
        self.AddSubPlot.setText(_translate("MplMainWindow", "+", None))
        self.RemoveSubPlot.setText(_translate("MplMainWindow", "-", None))
        self.RemoveAxis.setText(_translate("MplMainWindow", "-", None))
        self.ClearAxis.setText(_translate("MplMainWindow", "clear", None))
        self.groupBox_5.setTitle(_translate("MplMainWindow", "Slices", None))
        self.label_40.setText(_translate("MplMainWindow", "Ch", None))
        self.reverse2.setText(_translate("MplMainWindow", "reverse", None))
        self.label_39.setText(_translate("MplMainWindow", "alpha", None))
        self.ColorBar2.setText(_translate("MplMainWindow", "colorbar", None))
        self.AddPlotSlice.setToolTip(_translate("MplMainWindow", "plot", None))
        self.AddPlotSlice.setText(_translate("MplMainWindow", "+", None))
        self.ExportSlice.setToolTip(_translate("MplMainWindow", "export", None))
        self.ExportSlice.setText(_translate("MplMainWindow", "->", None))
        self.ColorMap2.setToolTip(_translate("MplMainWindow", "colormap", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_24), _translate("MplMainWindow", "Plots", None))
        self.TestProfile.setText(_translate("MplMainWindow", "LineProfile", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MplMainWindow", "Line Profile", None))
        self.getBounds_pushButton.setText(_translate("MplMainWindow", "Get Bounds", None))
        self.label_2.setText(_translate("MplMainWindow", "x", None))
        self.label_3.setText(_translate("MplMainWindow", "dx", None))
        self.xstart.setText(_translate("MplMainWindow", "0", None))
        self.xdelta.setText(_translate("MplMainWindow", "0", None))
        self.label_4.setText(_translate("MplMainWindow", "y", None))
        self.label_5.setText(_translate("MplMainWindow", "dy", None))
        self.ystart.setText(_translate("MplMainWindow", "0", None))
        self.ydelta.setText(_translate("MplMainWindow", "0", None))
        self.ShowSlice.setText(_translate("MplMainWindow", "Show Slice", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MplMainWindow", "ROI", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_16), _translate("MplMainWindow", "Hist", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MplMainWindow", "Analysis", None))
        self.mplactionOpen.setText(_translate("MplMainWindow", "Open", None))
        self.mplactionQuit.setText(_translate("MplMainWindow", "Quit", None))
        self.actionSave.setText(_translate("MplMainWindow", "Save", None))
        self.actionCalibrate.setText(_translate("MplMainWindow", "Calibrate", None))
        self.actionCalibrate_2.setText(_translate("MplMainWindow", "Calibrate", None))
        self.actionSave_2.setText(_translate("MplMainWindow", "Save", None))

from mplwidget import MplHIST, MplWidget
from src.pyqtgraph.dockarea import DockArea
import Re_rc
import style_rc
