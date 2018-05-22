# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
# noinspection PyUnresolvedReferences
import resources.resource_rc

del resources.resource_rc


# noinspection PyAttributeOutsideInit,PyArgumentList
class GuiMainWindow(object):

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1600, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        self.widget_central = QtWidgets.QWidget(main_window)
        self.widget_central.setObjectName("widget_central")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_central)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_app_theme = QtWidgets.QWidget(self.widget_central)
        self.widget_app_theme.setMinimumSize(QtCore.QSize(0, 140))
        self.widget_app_theme.setMaximumSize(QtCore.QSize(16777215, 200))
        self.widget_app_theme.setBaseSize(QtCore.QSize(0, 200))
        self.widget_app_theme.setStyleSheet(
            "background-image: url(:/app_main_theme.jpg);\n"
            "border: 1px solid #000000;\n"
            "background-repeat: no-repeat;\n"
            "background-attachment: fixed;\n"
            "background-position: center;\n")
        self.widget_app_theme.setObjectName("widget_app_theme")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_app_theme)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_app_logo = QtWidgets.QWidget(self.widget_app_theme)
        self.widget_app_logo.setMinimumSize(QtCore.QSize(310, 115))
        self.widget_app_logo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_app_logo.setStyleSheet(
            "background-image: url(:/logo.png);\n"
            "background-repeat: no-repeat;\n"
            "background-position: center; \n"
            "border: none;")
        self.widget_app_logo.setObjectName("widget_app_logo")
        self.gridLayout_3.addWidget(self.widget_app_logo, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_app_theme)
        self.widget_label_title = QtWidgets.QWidget(self.widget_central)
        self.widget_label_title.setEnabled(True)
        self.widget_label_title.setMinimumSize(QtCore.QSize(0, 17))
        self.widget_label_title.setMaximumSize(QtCore.QSize(16777215, 17))
        self.widget_label_title.setBaseSize(QtCore.QSize(66, 17))
        self.widget_label_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_label_title.setAutoFillBackground(False)
        self.widget_label_title.setStyleSheet(
            "background-color: rgb(0, 0, 0);")
        self.widget_label_title.setObjectName("widget_label_title")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_label_title)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_title = QtWidgets.QLabel(self.widget_label_title)
        self.label_title.setMinimumSize(QtCore.QSize(0, 15))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_label_title)
        self.widget_app_center = QtWidgets.QWidget(self.widget_central)
        self.widget_app_center.setObjectName("widget_app_center")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_app_center)
        self.horizontalLayout.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_app_left = QtWidgets.QWidget(self.widget_app_center)
        self.widget_app_left.setMaximumSize(QtCore.QSize(550, 16777215))
        self.widget_app_left.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_app_left.setObjectName("widget_app_left")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_app_left)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_calculator = QtWidgets.QWidget(self.widget_app_left)
        self.widget_calculator.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget_calculator.setStyleSheet(
            "background-color: rgb(186, 189, 182);")
        self.widget_calculator.setObjectName("widget_calculator")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_calculator)
        self.horizontalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_calculator = QtWidgets.QLabel(self.widget_calculator)
        self.label_calculator.setMinimumSize(QtCore.QSize(0, 20))
        self.label_calculator.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_calculator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_calculator.setObjectName("label_calculator")
        self.horizontalLayout_2.addWidget(self.label_calculator)
        self.verticalLayout_3.addWidget(self.widget_calculator)
        self.widget_enter_data_outer = QtWidgets.QWidget(self.widget_app_left)
        self.widget_enter_data_outer.setStyleSheet(
            "background-color: rgb(42, 42, 42);")
        self.widget_enter_data_outer.setObjectName("widget_enter_data_outer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.widget_enter_data_outer)
        self.verticalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_enter_data_inner = QtWidgets.QWidget(
            self.widget_enter_data_outer)
        self.widget_enter_data_inner.setObjectName("widget_enter_data_inner")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.widget_enter_data_inner)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_enter_data = QtWidgets.QLabel(self.widget_enter_data_inner)
        self.label_enter_data.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_enter_data.setObjectName("label_enter_data")
        self.verticalLayout_5.addWidget(self.label_enter_data)
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.widget_search_address = QtWidgets.QWidget(
            self.widget_enter_data_inner)
        self.widget_search_address.setObjectName("widget_search_address")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(
            self.widget_search_address)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_search_address = QtWidgets.QLabel(
            self.widget_search_address)
        self.label_search_address.setMinimumSize(QtCore.QSize(120, 0))
        self.label_search_address.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_search_address.setObjectName("label_search_address")
        self.horizontalLayout_10.addWidget(self.label_search_address)
        self.widget_search_address_inner = QtWidgets.QWidget(
            self.widget_search_address)
        self.widget_search_address_inner.setMinimumSize(QtCore.QSize(0, 42))
        self.widget_search_address_inner.setMaximumSize(
            QtCore.QSize(16777215, 60))
        self.widget_search_address_inner.setObjectName(
            "widget_search_address_inner")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(
            self.widget_search_address_inner)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.text_edit_search_address = QtWidgets.QTextEdit(
            self.widget_search_address_inner)
        self.text_edit_search_address.setMinimumSize(QtCore.QSize(0, 27))
        self.text_edit_search_address.setMaximumSize(
            QtCore.QSize(16777215, 26))
        self.text_edit_search_address.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.text_edit_search_address.setObjectName("text_edit_search_address")
        self.verticalLayout_13.addWidget(self.text_edit_search_address)
        self.horizontalLayout_10.addWidget(self.widget_search_address_inner)
        self.push_button_search_address = QtWidgets.QPushButton(
            self.widget_search_address)
        self.push_button_search_address.setMaximumSize(QtCore.QSize(27, 27))
        self.push_button_search_address.setStyleSheet(
            "background-image: url(:/search_icon.png);")
        self.push_button_search_address.setText("")
        self.push_button_search_address.setObjectName(
            "push_button_search_address")
        self.horizontalLayout_10.addWidget(self.push_button_search_address)
        self.verticalLayout_5.addWidget(self.widget_search_address)
        self.widget_address = QtWidgets.QWidget(self.widget_enter_data_inner)
        self.widget_address.setObjectName("widget_address")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_address)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_address = QtWidgets.QLabel(self.widget_address)
        self.label_address.setMinimumSize(QtCore.QSize(120, 0))
        self.label_address.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_address.setObjectName("label_address")
        self.horizontalLayout_9.addWidget(self.label_address)
        self.widget_address_inner = QtWidgets.QWidget(self.widget_address)
        self.widget_address_inner.setMinimumSize(QtCore.QSize(0, 63))
        self.widget_address_inner.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_address_inner.setObjectName("widget_address_inner")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(
            self.widget_address_inner)
        self.verticalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.combo_box_address = QtWidgets.QComboBox(self.widget_address_inner)
        self.combo_box_address.setMinimumSize(QtCore.QSize(0, 27))
        self.combo_box_address.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.combo_box_address.setObjectName("combo_box_address")
        self.verticalLayout_12.addWidget(self.combo_box_address)
        self.label_address_message = QtWidgets.QLabel(
            self.widget_address_inner)
        self.label_address_message.setObjectName("label_address_message")
        self.verticalLayout_12.addWidget(self.label_address_message)
        self.horizontalLayout_9.addWidget(self.widget_address_inner)
        self.verticalLayout_5.addWidget(self.widget_address)
        self.widget_building_type = QtWidgets.QWidget(
            self.widget_enter_data_inner)
        self.widget_building_type.setObjectName("widget_building_type")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(
            self.widget_building_type)
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_building_type = QtWidgets.QLabel(self.widget_building_type)
        self.label_building_type.setMinimumSize(QtCore.QSize(250, 0))
        self.label_building_type.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_building_type.setObjectName("label_building_type")
        self.horizontalLayout_14.addWidget(self.label_building_type)
        self.widget_building_type_inner = QtWidgets.QWidget(
            self.widget_building_type)
        self.widget_building_type_inner.setMinimumSize(QtCore.QSize(0, 63))
        self.widget_building_type_inner.setMaximumSize(
            QtCore.QSize(16777215, 60))
        self.widget_building_type_inner.setObjectName(
            "widget_building_type_inner")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(
            self.widget_building_type_inner)
        self.verticalLayout_17.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.combo_box_building_type = QtWidgets.QComboBox(
            self.widget_building_type_inner)
        self.combo_box_building_type.setMinimumSize(QtCore.QSize(0, 27))
        self.combo_box_building_type.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.combo_box_building_type.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.combo_box_building_type.setObjectName("combo_box_building_type")
        self.verticalLayout_17.addWidget(self.combo_box_building_type)
        self.label_building_type_message = QtWidgets.QLabel(
            self.widget_building_type_inner)
        self.label_building_type_message.setObjectName(
            "label_building_type_message")
        self.verticalLayout_17.addWidget(self.label_building_type_message)
        self.horizontalLayout_14.addWidget(self.widget_building_type_inner)
        self.verticalLayout_5.addWidget(self.widget_building_type)
        self.widget_market_type = QtWidgets.QWidget(
            self.widget_enter_data_inner)
        self.widget_market_type.setObjectName("widget_market_type")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(
            self.widget_market_type)
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_market_type = QtWidgets.QLabel(self.widget_market_type)
        self.label_market_type.setMinimumSize(QtCore.QSize(250, 0))
        self.label_market_type.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_market_type.setObjectName("label_market_type")
        self.horizontalLayout_13.addWidget(self.label_market_type)
        self.widget_market_type_inner = QtWidgets.QWidget(
            self.widget_market_type)
        self.widget_market_type_inner.setMinimumSize(QtCore.QSize(0, 63))
        self.widget_market_type_inner.setMaximumSize(
            QtCore.QSize(16777215, 60))
        self.widget_market_type_inner.setObjectName("widget_market_type_inner")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(
            self.widget_market_type_inner)
        self.verticalLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.combo_box_market_type = QtWidgets.QComboBox(
            self.widget_market_type_inner)
        self.combo_box_market_type.setMinimumSize(QtCore.QSize(0, 27))
        self.combo_box_market_type.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.combo_box_market_type.setObjectName("combo_box_market_type")
        self.verticalLayout_16.addWidget(self.combo_box_market_type)
        self.label_market_type_message = QtWidgets.QLabel(
            self.widget_market_type_inner)
        self.label_market_type_message.setObjectName(
            "label_market_type_message")
        self.verticalLayout_16.addWidget(self.label_market_type_message)
        self.horizontalLayout_13.addWidget(self.widget_market_type_inner)
        self.verticalLayout_5.addWidget(self.widget_market_type)
        self.widget_construction_year = QtWidgets.QWidget(
            self.widget_enter_data_inner)
        self.widget_construction_year.setObjectName("widget_construction_year")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(
            self.widget_construction_year)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_construction_year = QtWidgets.QLabel(
            self.widget_construction_year)
        self.label_construction_year.setMinimumSize(QtCore.QSize(250, 0))
        self.label_construction_year.setMaximumSize(
            QtCore.QSize(250, 16777215))
        self.label_construction_year.setObjectName("label_construction_year")
        self.horizontalLayout_12.addWidget(self.label_construction_year)
        self.widget_construction_year_inner = QtWidgets.QWidget(
            self.widget_construction_year)
        self.widget_construction_year_inner.setMinimumSize(QtCore.QSize(0, 63))
        self.widget_construction_year_inner.setMaximumSize(
            QtCore.QSize(16777215, 60))
        self.widget_construction_year_inner.setObjectName(
            "widget_construction_year_inner")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(
            self.widget_construction_year_inner)
        self.verticalLayout_15.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.text_edit_construction_year = QtWidgets.QTextEdit(
            self.widget_construction_year_inner)
        self.text_edit_construction_year.setMinimumSize(QtCore.QSize(0, 27))
        self.text_edit_construction_year.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.text_edit_construction_year.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.text_edit_construction_year.setObjectName(
            "text_edit_construction_year")
        self.verticalLayout_15.addWidget(self.text_edit_construction_year)
        self.label_construction_year_message = QtWidgets.QLabel(
            self.widget_construction_year_inner)
        self.label_construction_year_message.setObjectName(
            "label_construction_year_message")
        self.verticalLayout_15.addWidget(self.label_construction_year_message)
        self.horizontalLayout_12.addWidget(self.widget_construction_year_inner)
        self.verticalLayout_5.addWidget(self.widget_construction_year)
        self.widget_meters = QtWidgets.QWidget(self.widget_enter_data_inner)
        self.widget_meters.setObjectName("widget_meters")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_meters)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_meters = QtWidgets.QLabel(self.widget_meters)
        self.label_meters.setMinimumSize(QtCore.QSize(250, 0))
        self.label_meters.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_meters.setObjectName("label_meters")
        self.horizontalLayout_11.addWidget(self.label_meters)
        self.widget_meters_inner = QtWidgets.QWidget(self.widget_meters)
        self.widget_meters_inner.setMinimumSize(QtCore.QSize(0, 63))
        self.widget_meters_inner.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_meters_inner.setObjectName("widget_meters_inner")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(
            self.widget_meters_inner)
        self.verticalLayout_14.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.text_edit_meters = QtWidgets.QTextEdit(self.widget_meters_inner)
        self.text_edit_meters.setMinimumSize(QtCore.QSize(0, 27))
        self.text_edit_meters.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text_edit_meters.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.text_edit_meters.setObjectName("text_edit_meters")
        self.verticalLayout_14.addWidget(self.text_edit_meters)
        self.label_meters_message = QtWidgets.QLabel(self.widget_meters_inner)
        self.label_meters_message.setObjectName("label_meters_message")
        self.verticalLayout_14.addWidget(self.label_meters_message)
        self.horizontalLayout_11.addWidget(self.widget_meters_inner)
        self.verticalLayout_5.addWidget(self.widget_meters)
        self.widget_building_material = QtWidgets.QWidget(
            self.widget_enter_data_inner)
        self.widget_building_material.setObjectName("widget_building_material")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(
            self.widget_building_material)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_building_material = QtWidgets.QLabel(
            self.widget_building_material)
        self.label_building_material.setMinimumSize(QtCore.QSize(250, 0))
        self.label_building_material.setMaximumSize(
            QtCore.QSize(250, 16777215))
        self.label_building_material.setObjectName("label_building_material")
        self.horizontalLayout_8.addWidget(self.label_building_material)
        self.widget_building_material_inner = QtWidgets.QWidget(
            self.widget_building_material)
        self.widget_building_material_inner.setMinimumSize(QtCore.QSize(0, 63))
        self.widget_building_material_inner.setMaximumSize(
            QtCore.QSize(16777215, 60))
        self.widget_building_material_inner.setObjectName(
            "widget_building_material_inner")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(
            self.widget_building_material_inner)
        self.verticalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.combo_box_building_material = QtWidgets.QComboBox(
            self.widget_building_material_inner)
        self.combo_box_building_material.setMinimumSize(QtCore.QSize(0, 27))
        self.combo_box_building_material.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.combo_box_building_material.setObjectName(
            "combo_box_building_material")
        self.verticalLayout_11.addWidget(self.combo_box_building_material)
        self.label_building_material_message = QtWidgets.QLabel(
            self.widget_building_material_inner)
        self.label_building_material_message.setObjectName(
            "label_building_material_message")
        self.verticalLayout_11.addWidget(self.label_building_material_message)
        self.horizontalLayout_8.addWidget(self.widget_building_material_inner)
        self.verticalLayout_5.addWidget(self.widget_building_material)
        self.widget_check_boxes = QtWidgets.QWidget(
            self.widget_enter_data_inner)
        self.widget_check_boxes.setObjectName("widget_check_boxes")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.widget_check_boxes)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.widget_check_boxes_inner_left = QtWidgets.QWidget(
            self.widget_check_boxes)
        self.widget_check_boxes_inner_left.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_check_boxes_inner_left.setStyleSheet("")
        self.widget_check_boxes_inner_left.setObjectName(
            "widget_check_boxes_inner_left")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(
            self.widget_check_boxes_inner_left)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.check_box_balcony = QtWidgets.QCheckBox(
            self.widget_check_boxes_inner_left)
        self.check_box_balcony.setStyleSheet("color: rgb(255, 255, 255);")
        self.check_box_balcony.setObjectName("check_box_balcony")
        self.verticalLayout_7.addWidget(self.check_box_balcony)
        self.chech_box_cellar = QtWidgets.QCheckBox(
            self.widget_check_boxes_inner_left)
        self.chech_box_cellar.setStyleSheet("color: rgb(255, 255, 255);")
        self.chech_box_cellar.setObjectName("chech_box_cellar")
        self.verticalLayout_7.addWidget(self.chech_box_cellar)
        self.check_box_garden = QtWidgets.QCheckBox(
            self.widget_check_boxes_inner_left)
        self.check_box_garden.setStyleSheet("color: rgb(255, 255, 255);")
        self.check_box_garden.setObjectName("check_box_garden")
        self.verticalLayout_7.addWidget(self.check_box_garden)
        self.check_box_terrace = QtWidgets.QCheckBox(
            self.widget_check_boxes_inner_left)
        self.check_box_terrace.setStyleSheet("color: rgb(255, 255, 255);")
        self.check_box_terrace.setObjectName("check_box_terrace")
        self.verticalLayout_7.addWidget(self.check_box_terrace)
        self.horizontalLayout_3.addWidget(self.widget_check_boxes_inner_left)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.widget_check_boxes_inner_right = QtWidgets.QWidget(
            self.widget_check_boxes)
        self.widget_check_boxes_inner_right.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_check_boxes_inner_right.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.widget_check_boxes_inner_right.setStyleSheet("")
        self.widget_check_boxes_inner_right.setObjectName(
            "widget_check_boxes_inner_right")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(
            self.widget_check_boxes_inner_right)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.check_box_elevator = QtWidgets.QCheckBox(
            self.widget_check_boxes_inner_right)
        self.check_box_elevator.setStyleSheet("color: rgb(255, 255, 255);")
        self.check_box_elevator.setObjectName("check_box_elevator")
        self.verticalLayout_6.addWidget(self.check_box_elevator)
        self.check_box_separate_kitchen = QtWidgets.QCheckBox(
            self.widget_check_boxes_inner_right)
        self.check_box_separate_kitchen.setStyleSheet(
            "color: rgb(255, 255, 255);")
        self.check_box_separate_kitchen.setObjectName(
            "check_box_separate_kitchen")
        self.verticalLayout_6.addWidget(self.check_box_separate_kitchen)
        self.check_box_guarded_estate = QtWidgets.QCheckBox(
            self.widget_check_boxes_inner_right)
        self.check_box_guarded_estate.setStyleSheet(
            "color: rgb(255, 255, 255);")
        self.check_box_guarded_estate.setObjectName("check_box_guarded_estate")
        self.verticalLayout_6.addWidget(self.check_box_guarded_estate)
        self.horizontalLayout_3.addWidget(self.widget_check_boxes_inner_right)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.widget_check_boxes)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.verticalLayout_4.addWidget(self.widget_enter_data_inner)
        self.verticalLayout_3.addWidget(self.widget_enter_data_outer)
        self.widget_buttons = QtWidgets.QWidget(self.widget_app_left)
        self.widget_buttons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_buttons.setStyleSheet(
            "background-color: rgb(84, 84, 105);")
        self.widget_buttons.setObjectName("widget_buttons")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_buttons)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.push_button_calculate = QtWidgets.QPushButton(self.widget_buttons)
        self.push_button_calculate.setStyleSheet(
            "background-color: rgb(38, 135, 152);")
        self.push_button_calculate.setObjectName("push_button_calculate")
        self.gridLayout_2.addWidget(self.push_button_calculate, 0, 0, 1, 1)
        self.push_button_reset = QtWidgets.QPushButton(self.widget_buttons)
        self.push_button_reset.setStyleSheet(
            "background-color: rgb(38, 135, 152);")
        self.push_button_reset.setObjectName("push_button_reset")
        self.gridLayout_2.addWidget(self.push_button_reset, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_buttons)
        self.horizontalLayout.addWidget(self.widget_app_left)
        self.widget_app_right = QtWidgets.QWidget(self.widget_app_center)
        self.widget_app_right.setMinimumSize(QtCore.QSize(450, 0))
        self.widget_app_right.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_app_right.setObjectName("widget_app_right")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.widget_app_right)
        self.verticalLayout_25.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_25.setSpacing(3)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.widget_reference_city = QtWidgets.QWidget(self.widget_app_right)
        self.widget_reference_city.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget_reference_city.setStyleSheet(
            "background-color: rgb(186, 189, 182);")
        self.widget_reference_city.setObjectName("widget_reference_city")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(
            self.widget_reference_city)
        self.horizontalLayout_6.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_reference_city = QtWidgets.QLabel(
            self.widget_reference_city)
        self.label_reference_city.setMinimumSize(QtCore.QSize(0, 20))
        self.label_reference_city.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_reference_city.setAlignment(QtCore.Qt.AlignCenter)
        self.label_reference_city.setObjectName("label_reference_city")
        self.horizontalLayout_6.addWidget(self.label_reference_city)
        self.verticalLayout_25.addWidget(self.widget_reference_city)
        self.widget_reference_city_data = QtWidgets.QWidget(
            self.widget_app_right)
        self.widget_reference_city_data.setStyleSheet(
            "background-color: rgb(84,84,105);")
        self.widget_reference_city_data.setObjectName(
            "widget_reference_city_data")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(
            self.widget_reference_city_data)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_reference_city_2 = QtWidgets.QLabel(
            self.widget_reference_city_data)
        self.label_reference_city_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_reference_city_2.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_reference_city_2.setObjectName("label_reference_city_2")
        self.verticalLayout_9.addWidget(self.label_reference_city_2)
        self.label_reference_city_data = QtWidgets.QLabel(
            self.widget_reference_city_data)
        self.label_reference_city_data.setMinimumSize(QtCore.QSize(0, 0))
        self.label_reference_city_data.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_reference_city_data.setStyleSheet(
            "border: 1px solid #000000;")
        self.label_reference_city_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_reference_city_data.setObjectName(
            "label_reference_city_data")
        self.verticalLayout_9.addWidget(self.label_reference_city_data)
        self.label_reference_city_price_per_meter = QtWidgets.QLabel(
            self.widget_reference_city_data)
        self.label_reference_city_price_per_meter.setMinimumSize(
            QtCore.QSize(120, 0))
        self.label_reference_city_price_per_meter.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_reference_city_price_per_meter.setObjectName(
            "label_reference_city_price_per_meter")
        self.verticalLayout_9.addWidget(
            self.label_reference_city_price_per_meter)
        self.label_reference_city_price_per_meter_data = QtWidgets.QLabel(
            self.widget_reference_city_data)
        self.label_reference_city_price_per_meter_data.setMinimumSize(
            QtCore.QSize(0, 0))
        self.label_reference_city_price_per_meter_data.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_reference_city_price_per_meter_data.setStyleSheet(
            "border: 1px solid #000000;")
        self.label_reference_city_price_per_meter_data.setAlignment(
            QtCore.Qt.AlignCenter)
        self.label_reference_city_price_per_meter_data.setObjectName(
            "label_reference_city_price_per_meter_data")
        self.verticalLayout_9.addWidget(
            self.label_reference_city_price_per_meter_data)
        self.verticalLayout_25.addWidget(self.widget_reference_city_data)
        self.widget_map = QtWidgets.QWidget(self.widget_app_right)
        self.widget_map.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_map.setObjectName("widget_map")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_map)
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.browser = QtWebEngineWidgets.QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 "../../resources/map.html"))
        local_url = QtCore.QUrl.fromLocalFile(file_path)
        self.browser.setUrl(local_url)
        self.verticalLayout_8.addWidget(self.browser)
        self.verticalLayout_25.addWidget(self.widget_map)
        self.widget_result = QtWidgets.QWidget(self.widget_app_right)
        self.widget_result.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget_result.setStyleSheet(
            "background-color: rgb(186, 189, 182);")
        self.widget_result.setObjectName("widget_result")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_result)
        self.horizontalLayout_4.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_result = QtWidgets.QLabel(self.widget_result)
        self.label_result.setMinimumSize(QtCore.QSize(0, 20))
        self.label_result.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.horizontalLayout_4.addWidget(self.label_result)
        self.verticalLayout_25.addWidget(self.widget_result)
        self.widget_result_data = QtWidgets.QWidget(self.widget_app_right)
        self.widget_result_data.setStyleSheet(
            "background-color: rgb(84,84,105);")
        self.widget_result_data.setObjectName("widget_result_data")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_result_data)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_distance = QtWidgets.QLabel(self.widget_result_data)
        self.label_distance.setMinimumSize(QtCore.QSize(120, 0))
        self.label_distance.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_distance.setObjectName("label_distance")
        self.verticalLayout_10.addWidget(self.label_distance)
        self.label_distance_data = QtWidgets.QLabel(self.widget_result_data)
        self.label_distance_data.setMinimumSize(QtCore.QSize(0, 0))
        self.label_distance_data.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_distance_data.setStyleSheet("border: 1px solid #000000;")
        self.label_distance_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_distance_data.setObjectName("label_distance_data")
        self.verticalLayout_10.addWidget(self.label_distance_data)
        self.label_basic_price_per_meter = QtWidgets.QLabel(
            self.widget_result_data)
        self.label_basic_price_per_meter.setMinimumSize(QtCore.QSize(120, 0))
        self.label_basic_price_per_meter.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_basic_price_per_meter.setObjectName(
            "label_basic_price_per_meter")
        self.verticalLayout_10.addWidget(self.label_basic_price_per_meter)
        self.label_basic_price_per_meter_data = QtWidgets.QLabel(
            self.widget_result_data)
        self.label_basic_price_per_meter_data.setMinimumSize(
            QtCore.QSize(0, 0))
        self.label_basic_price_per_meter_data.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_basic_price_per_meter_data.setStyleSheet(
            "border: 1px solid #000000;")
        self.label_basic_price_per_meter_data.setAlignment(
            QtCore.Qt.AlignCenter)
        self.label_basic_price_per_meter_data.setObjectName(
            "label_basic_price_per_meter_data")
        self.verticalLayout_10.addWidget(self.label_basic_price_per_meter_data)
        self.label_final_price = QtWidgets.QLabel(self.widget_result_data)
        self.label_final_price.setMinimumSize(QtCore.QSize(120, 0))
        self.label_final_price.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_final_price.setObjectName("label_final_price")
        self.verticalLayout_10.addWidget(self.label_final_price)
        self.label_final_price_data = QtWidgets.QLabel(self.widget_result_data)
        self.label_final_price_data.setMinimumSize(QtCore.QSize(0, 0))
        self.label_final_price_data.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_final_price_data.setStyleSheet("border: 1px solid #000000;")
        self.label_final_price_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_final_price_data.setObjectName("label_final_price_data")
        self.verticalLayout_10.addWidget(self.label_final_price_data)
        self.label_final_price_per_meter = QtWidgets.QLabel(
            self.widget_result_data)
        self.label_final_price_per_meter.setMinimumSize(QtCore.QSize(120, 0))
        self.label_final_price_per_meter.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_final_price_per_meter.setObjectName(
            "label_final_price_per_meter")
        self.verticalLayout_10.addWidget(self.label_final_price_per_meter)
        self.label_final_price_per_meter_data = QtWidgets.QLabel(
            self.widget_result_data)
        self.label_final_price_per_meter_data.setMinimumSize(
            QtCore.QSize(0, 0))
        self.label_final_price_per_meter_data.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_final_price_per_meter_data.setStyleSheet(
            "border: 1px solid #000000;")
        self.label_final_price_per_meter_data.setAlignment(
            QtCore.Qt.AlignCenter)
        self.label_final_price_per_meter_data.setObjectName(
            "label_final_price_per_meter_data")
        self.verticalLayout_10.addWidget(self.label_final_price_per_meter_data)
        self.verticalLayout_25.addWidget(self.widget_result_data)
        self.widget_reference_city.raise_()
        self.widget_map.raise_()
        self.widget_result.raise_()
        self.widget_reference_city_data.raise_()
        self.widget_result_data.raise_()
        self.horizontalLayout.addWidget(self.widget_app_right)
        self.verticalLayout_2.addWidget(self.widget_app_center)
        main_window.setCentralWidget(self.widget_central)

        self.translate_user_interface(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_user_interface(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(
            _translate("MainWindow", "House Price Calc"))
        self.label_title.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span "
                                            "style=\" font-weight:600; "
                                            "color:#ffffff;\" "
                                            ">KALKULATOR CEN ZAKUPU MIESZKAŃ "
                                            "W "
                                            "POLSCE</span></p></body></html>"))
        self.label_calculator.setText(_translate("MainWindow",
                                                 "<html><head/><body><p"
                                                 "><span style=\" "
                                                 "color:#ffffff; "
                                                 "\">Kalkulator "
                                                 "ceny</span></p></body"
                                                 "></html>"))
        self.label_enter_data.setText(_translate("MainWindow",
                                                 "<html><head/><body><p"
                                                 "><span style=\" "
                                                 "color:#ffffff; "
                                                 "\">Uzupełnij dane dot. "
                                                 "nieruchomości</span></p"
                                                 "></body></html>"))
        self.label_search_address.setText(_translate("MainWindow",
                                                     "<html><head/><body><p"
                                                     "><span style=\" "
                                                     "color:#ffffff; "
                                                     "\">Wyszukaj "
                                                     "adres:</span></p"
                                                     "></body></html>"))
        self.label_address.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span "
                                              "style=\" color:#ffffff; "
                                              "\">Wybrany "
                                              "adres:</span></p></body></html>"
                                              ))
        self.label_address_message.setText(_translate("MainWindow",
                                                      "<html><head/><body><p"
                                                      "><span style=\" "
                                                      "color:#3465a4; "
                                                      "\">Wybierz "
                                                      "adres.</span></p"
                                                      "></body></html>"))
        self.label_building_type.setText(_translate("MainWindow",
                                                    "<html><head/><body><p"
                                                    "><span style=\" "
                                                    "color:#ffffff; "
                                                    "\">Rodzaj "
                                                    "zabudowy:</span></p"
                                                    "></body></html>"))
        self.label_building_type_message.setText(_translate("MainWindow",
                                                            "<html><head"
                                                            "/><body><p"
                                                            "><span style=\" "
                                                            "color:#3465a4; "
                                                            "\">Wybierz "
                                                            "rodzaj "
                                                            "zabudowy.</span"
                                                            "></p></body"
                                                            "></html>"))
        self.label_market_type.setText(_translate("MainWindow",
                                                  "<html><head/><body><p"
                                                  "><span style=\" "
                                                  "color:#ffffff; "
                                                  "\">Rynek:</span></p"
                                                  "></body></html>"))
        self.label_market_type_message.setText(_translate("MainWindow",
                                                          "<html><head"
                                                          "/><body><p><span "
                                                          "style=\" "
                                                          "color:#3465a4; "
                                                          "\">Wybierz "
                                                          "rynek.</span></p"
                                                          "></body></html>"))
        self.label_construction_year.setText(_translate("MainWindow",
                                                        "<html><head/><body"
                                                        "><p><span style=\" "
                                                        "color:#ffffff; "
                                                        "\">Rok "
                                                        "budowy:</span></p"
                                                        "></body></html>"))
        self.label_construction_year_message.setText(_translate("MainWindow",
                                                                "<html><head"
                                                                "/><body><p"
                                                                "><span "
                                                                "style=\" "
                                                                "color"
                                                                ":#3465a4; "
                                                                "\">Podaj "
                                                                "rok "
                                                                "budowy"
                                                                ".</span></p"
                                                                "></body"
                                                                "></html>"))
        self.label_meters.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span "
                                             "style=\" color:#ffffff; "
                                             "\">Ilość mkw:</span></p></body"
                                             "></html>"))
        self.label_meters_message.setText(_translate("MainWindow",
                                                     "<html><head/><body><p"
                                                     "><span style=\" "
                                                     "color:#3465a4; "
                                                     "\">Podaj ilość metrów "
                                                     "kw.</span></p></body"
                                                     "></html>"))
        self.label_building_material.setText(_translate("MainWindow",
                                                        "<html><head/><body"
                                                        "><p><span style=\" "
                                                        "color:#ffffff; "
                                                        "\">Materiał "
                                                        "budynku:</span></p"
                                                        "></body></html>"))
        self.label_building_material_message.setText(_translate("MainWindow",
                                                                "<html><head"
                                                                "/><body><p"
                                                                "><span "
                                                                "style=\" "
                                                                "color"
                                                                ":#3465a4; "
                                                                "\">Wybierz "
                                                                "materiał "
                                                                "budynku. "
                                                                "</span></p"
                                                                "></body"
                                                                "></html>"))
        self.check_box_balcony.setText(_translate("MainWindow", "balkon"))
        self.chech_box_cellar.setText(_translate("MainWindow", "piwnica"))
        self.check_box_garden.setText(_translate("MainWindow", "ogródek"))
        self.check_box_terrace.setText(_translate("MainWindow", "taras"))
        self.check_box_elevator.setText(_translate("MainWindow", "winda"))
        self.check_box_separate_kitchen.setText(
            _translate("MainWindow", "oddzielna kuchnia"))
        self.check_box_guarded_estate.setText(
            _translate("MainWindow", "strzeżone osiedle"))
        self.push_button_calculate.setText(_translate("MainWindow", "Oszacuj"))
        self.push_button_reset.setText(_translate("MainWindow", "Reset"))
        self.label_reference_city.setText(_translate("MainWindow",
                                                     "<html><head/><body><p"
                                                     "><span style=\" "
                                                     "color:#ffffff; "
                                                     "\">Najbliższe duże "
                                                     "miasto "
                                                     "odniesienia:</span></p"
                                                     "></body></html>"))
        self.label_reference_city_2.setText(_translate("MainWindow",
                                                       "<html><head/><body"
                                                       "><p><span style=\" "
                                                       "color:#ffffff; "
                                                       "\">Nazwa "
                                                       "miasta:</span></p"
                                                       "></body></html>"))
        self.label_reference_city_data.setText(_translate("MainWindow",
                                                          "<html><head"
                                                          "/><body><p><span "
                                                          "style=\" "
                                                          "color:#ffffff; "
                                                          "\">Warszawa</span"
                                                          "></p></body></html>"
                                                          ))
        self.label_reference_city_price_per_meter.setText(
            _translate("MainWindow",
                       "<html><head/><body><p><span style=\" color:"
                       "#ffffff;\">Średnia cena za mkw:"
                       "</span></p></body></html>"))
        self.label_reference_city_price_per_meter_data.setText(
            _translate("MainWindow",
                       "<html><head/><body><p><span style=\" color:"
                       "#ffffff;"
                       "\">6762 zł</span></p></body></html>"))
        self.label_result.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span "
                                             "style=\" color:#ffffff; "
                                             "\">Wynik:</span></p></body"
                                             "></html>"))
        self.label_distance.setText(_translate("MainWindow",
                                               "<html><head/><body><p><span "
                                               "style=\" color:#ffffff; "
                                               "\">Odległość od centrum "
                                               "miasta "
                                               "odniesienia:</span></p"
                                               "></body></html>"))
        self.label_distance_data.setText(_translate("MainWindow",
                                                    "<html><head/><body><p"
                                                    "><span style=\" "
                                                    "color:#ffffff; "
                                                    "\">42 km</span></p"
                                                    "></body></html>"))
        self.label_basic_price_per_meter.setText(_translate("MainWindow",
                                                            "<html><head"
                                                            "/><body><p"
                                                            "><span style=\" "
                                                            "color:#ffffff; "
                                                            "\">Cena za mkw "
                                                            "(na podstawie "
                                                            "odl. od miasta "
                                                            "odniesienia): "
                                                            "</span></p"
                                                            "></body></html>"))
        self.label_basic_price_per_meter_data.setText(_translate("MainWindow",
                                                                 "<html"
                                                                 "><head"
                                                                 "/><body><p"
                                                                 "><span "
                                                                 "style=\" "
                                                                 "color"
                                                                 ":#ffffff; "
                                                                 "\">5982 "
                                                                 "zł</span"
                                                                 "></p"
                                                                 "></body"
                                                                 "></html>"))
        self.label_final_price.setText(_translate("MainWindow",
                                                  "<html><head/><body><p"
                                                  "><span style=\" "
                                                  "color:#ffffff; "
                                                  "\">Cena mieszkania:</span"
                                                  "></p></body></html>"))
        self.label_final_price_data.setText(_translate("MainWindow",
                                                       "<html><head/><body"
                                                       "><p><span style=\" "
                                                       "color:#ffffff; "
                                                       "\">250212 "
                                                       "zł</span></p></body"
                                                       "></html>"))
        self.label_final_price_per_meter.setText(_translate("MainWindow",
                                                            "<html><head"
                                                            "/><body><p"
                                                            "><span style=\" "
                                                            "color:#ffffff; "
                                                            "\">Ostateczna "
                                                            "cena za "
                                                            "mkw:</span></p"
                                                            "></body></html>"))
        self.label_final_price_per_meter_data.setText(_translate("MainWindow",
                                                                 "<html"
                                                                 "><head"
                                                                 "/><body><p"
                                                                 "><span "
                                                                 "style=\" "
                                                                 "color"
                                                                 ":#ffffff; "
                                                                 "\">6120 "
                                                                 "zł</span"
                                                                 "></p"
                                                                 "></body"
                                                                 "></html>"))
