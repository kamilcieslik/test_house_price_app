import re
from PyQt5 import QtWidgets, QtCore


class DataValidation(object):

    def __init__(self):
        pass

    @staticmethod
    def text_edit_validation(data_input_widget, label, is_empty, regex=None,
                             does_not_fit=None):
        _translate = QtCore.QCoreApplication.translate

        if isinstance(data_input_widget, QtWidgets.QTextEdit) and isinstance(
                label, QtWidgets.QLabel):
            if data_input_widget.toPlainText() == "":
                label.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span "
                                         "style=\" color:#3465a4; "
                                         "\">" + is_empty
                                         + "</span></p></body></html>"))
            elif not re.match(regex, data_input_widget.toPlainText()):
                label.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span "
                                         "style=\" color:#3465a4; "
                                         "\">" + does_not_fit + ""
                                                                "</span></p"
                                                                "></body"
                                                                "></html>"))
            else:
                label.setText("")
        elif isinstance(data_input_widget, QtWidgets.QComboBox) and isinstance(
                label, QtWidgets.QLabel):
            if data_input_widget.currentText() == "":
                label.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span "
                                         "style=\" color:#3465a4; "
                                         "\">" + is_empty + ""
                                                            "</span></p"
                                                            "></body></html>"))
            else:
                label.setText("")
