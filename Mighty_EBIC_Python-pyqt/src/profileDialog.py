# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profileDialog.ui'
#
# Created: Wed Sep 18 12:01:15 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_profiler(object):
    def setupUi(self, profiler):
        profiler.setObjectName(_fromUtf8("profiler"))
        profiler.setEnabled(True)
        profiler.resize(508, 454)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(profiler.sizePolicy().hasHeightForWidth())
        profiler.setSizePolicy(sizePolicy)
        profiler.setModal(False)
        self.widget = MplWidget(profiler)
        self.widget.setGeometry(QtCore.QRect(8, 8, 486, 323))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(profiler)
        self.label.setGeometry(QtCore.QRect(398, 388, 82, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.addprofile = QtGui.QPushButton(profiler)
        self.addprofile.setGeometry(QtCore.QRect(395, 406, 91, 27))
        self.addprofile.setObjectName(_fromUtf8("addprofile"))
        self.ProfileName = QtGui.QLineEdit(profiler)
        self.ProfileName.setGeometry(QtCore.QRect(3, 357, 357, 27))
        self.ProfileName.setObjectName(_fromUtf8("ProfileName"))
        self.label_2 = QtGui.QLabel(profiler)
        self.label_2.setGeometry(QtCore.QRect(4, 337, 83, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(profiler)
        self.label_3.setGeometry(QtCore.QRect(4, 404, 62, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(profiler)
        self.label_4.setGeometry(QtCore.QRect(87, 378, 131, 17))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.viewCH_comboBox = QtGui.QComboBox(profiler)
        self.viewCH_comboBox.setGeometry(QtCore.QRect(396, 353, 89, 31))
        self.viewCH_comboBox.setObjectName(_fromUtf8("viewCH_comboBox"))
        self.label_5 = QtGui.QLabel(profiler)
        self.label_5.setGeometry(QtCore.QRect(398, 334, 90, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ParentName = QtGui.QLabel(profiler)
        self.ParentName.setGeometry(QtCore.QRect(77, 405, 281, 17))
        self.ParentName.setObjectName(_fromUtf8("ParentName"))

        self.retranslateUi(profiler)
        QtCore.QMetaObject.connectSlotsByName(profiler)

    def retranslateUi(self, profiler):
        profiler.setWindowTitle(QtGui.QApplication.translate("profiler", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("profiler", "Add to Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.addprofile.setText(QtGui.QApplication.translate("profiler", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.ProfileName.setText(QtGui.QApplication.translate("profiler", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("profiler", "profileName", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("profiler", "Parent:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("profiler", "view channel", None, QtGui.QApplication.UnicodeUTF8))
        self.ParentName.setText(QtGui.QApplication.translate("profiler", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import MplWidget
