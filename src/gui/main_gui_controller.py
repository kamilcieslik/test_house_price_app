import sys
from PyQt5 import QtWidgets
from src.gui.main_gui import GuiMainWindow
from src.gui.widgets_data_validation import DataValidation
from calculator.prices_calculator import PricesCalculator
from calculator.exception.construction_year_violation_exception \
    import ConstructionYearViolationException
from googlemaps.exceptions import TransportError


class MainGuiController(object):

    def __init__(self, google_api_key):
        self._prices_calculator = PricesCalculator(google_api_key)
        self._data_validation = DataValidation

        # Inicjalizacja komponentów GUI.
        self._ui = GuiMainWindow()
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self._ui.setup_ui(MainWindow)

        # Inicjacja listenerów komponentów GUI.
        self.init_listeners()

        # Inicjacja kontroli wprowadzanych danych.
        self.init_data_validation()

        # Wypełnienie combo-boxów danymi.
        self.fill_combo_boxes_with_data()

        # Zresetowanie wartości komponentów (nadpisanie przykładowych).
        self.reset_components_values()

        # Wyświetlenie GUI.
        MainWindow.show()
        sys.exit(app.exec_())

    def init_data_validation(self):
        self \
            ._ui.text_edit_construction_year \
            .textChanged \
            .connect(lambda: self
                     ._data_validation
                     .text_edit_validation(self._ui
                                           .text_edit_construction_year,
                                           self._ui.
                                           label_construction_year_message,
                                           "Podaj rok budowy.",
                                           "^[1-9]{1}[0-9]{3}$",
                                           "Niepoprawny format."))
        self \
            ._ui.text_edit_meters \
            .textChanged.connect(lambda: self
                                 ._data_validation
                                 .text_edit_validation(self._ui
                                                       .text_edit_meters,
                                                       self._ui.
                                                       label_meters_message,
                                                       "Podaj il. metrów kw.",
                                                       "^[1-9]{1}[0-9]{1,2}$",
                                                       "Niepoprawny format."))
        self\
            ._ui.combo_box_address.\
            currentTextChanged\
            .connect(lambda: self._data_validation
                     .text_edit_validation(self._ui
                                           .combo_box_address,
                                           self._ui.label_address_message,
                                           "Wybierz adres."))
        self\
            ._ui.combo_box_market_type\
            .currentTextChanged\
            .connect(lambda: self._data_validation
                     .text_edit_validation(self._ui
                                           .combo_box_market_type,
                                           self._ui.label_market_type_message,
                                           "Wybierz rynek."))
        self._ui.combo_box_building_type \
            .currentTextChanged\
            .connect(lambda: self._data_validation
                     .text_edit_validation(self._ui
                                           .combo_box_building_type,
                                           self._ui
                                           .label_building_type_message,
                                           "Wybierz rodzaj zabudowy."))
        self._ui.combo_box_building_material \
            .currentTextChanged\
            .connect(lambda: self._data_validation
                     .text_edit_validation(self._ui
                                           .combo_box_building_material,
                                           self._ui
                                           .label_building_material_message,
                                           "Wybierz materiał budynku."))

    def init_listeners(self):
        self._ui.push_button_calculate.clicked.connect(
            self.push_button_calculate_on_click)
        self._ui.push_button_reset.clicked.connect(
            self.push_button_reset_on_click)
        self._ui.push_button_search_address.clicked.connect(
            self.push_button_search_address_on_click)
        self._ui.combo_box_address.currentIndexChanged.connect(
            self.combo_box_address_on_index_changed)

    def fill_combo_boxes_with_data(self):
        self._ui.combo_box_building_type.addItem("")
        self._ui.combo_box_building_type.addItems(
            self._prices_calculator.building_types)

        self._ui.combo_box_market_type.addItem("")
        self._ui.combo_box_market_type.addItems(
            self._prices_calculator.market_types)

        self._ui.combo_box_building_material.addItem("")
        self._ui.combo_box_building_material.addItems(
            self._prices_calculator.building_materials)

    def reset_components_values(self):
        self._ui.text_edit_search_address.setText("")

        if self._prices_calculator.autocomplete_addresses:
            self._prices_calculator.autocomplete_addresses = []

        self._ui.combo_box_address.setCurrentIndex(0)
        self._ui.combo_box_market_type.setCurrentIndex(0)
        self._ui.text_edit_construction_year.setText("")
        self._ui.text_edit_meters.setText("")
        self._ui.combo_box_building_type.setCurrentIndex(0)
        self._ui.combo_box_building_material.setCurrentIndex(0)

        self._ui.check_box_balcony.setChecked(False)
        self._ui.chech_box_cellar.setChecked(False)
        self._ui.check_box_garden.setChecked(False)
        self._ui.check_box_terrace.setChecked(False)
        self._ui.check_box_elevator.setChecked(False)
        self._ui.check_box_separate_kitchen.setChecked(False)
        self._ui.check_box_guarded_estate.setChecked(False)

        self._ui.label_reference_city_data.setText("------")
        self._ui.label_reference_city_price_per_meter_data.setText("------")
        self._ui.label_distance_data.setText("------")
        self._ui.label_basic_price_per_meter_data.setText("------")
        self._ui.label_final_price_data.setText("------")
        self._ui.label_final_price_per_meter_data.setText("------")

    def push_button_calculate_on_click(self):
        if self._ui.label_address_message.text() == "" and self \
                ._ui.label_building_type_message.text() == "" \
                and self._ui.label_market_type_message.text() == "" \
                and self._ui.label_construction_year_message.text() == "" \
                and self._ui.label_meters_message.text() == "" \
                and self._ui.label_building_material_message.text() == "":
            try:
                calculator_result = self._prices_calculator \
                    .calculate_house_price(self._ui.combo_box_building_type # TUTAJ
                                           .currentText(),
                                           self._ui.combo_box_market_type
                                           .currentText(),
                                           self._ui.combo_box_building_material
                                           .currentText(),
                                           self._ui.text_edit_construction_year
                                           .toPlainText(),
                                           self._ui.text_edit_meters
                                           .toPlainText(),
                                           self._ui.check_box_balcony
                                           .isChecked(),
                                           self._ui.chech_box_cellar
                                           .isChecked(),
                                           self._ui.check_box_garden
                                           .isChecked(),
                                           self._ui.check_box_terrace
                                           .isChecked(),
                                           self._ui.check_box_elevator
                                           .isChecked(),
                                           self._ui.check_box_separate_kitchen
                                           .isChecked(),
                                           self._ui.check_box_guarded_estate
                                           .isChecked())

                self._ui.label_reference_city_data.setText(
                    calculator_result.nearest_reference_city.name)

                if self._ui.combo_box_market_type.currentText() == "pierwotny":
                    self._ui.label_reference_city_price_per_meter_data \
                        .setText(str(round(calculator_result
                                           .nearest_reference_city
                                           .price_per_meter_on_primary_market,
                                           2)) + " zł")
                else:
                    self._ui.label_reference_city_price_per_meter_data \
                        .setText(str(round(calculator_result
                                           .nearest_reference_city
                                           .price_per_meter_on_aftermarket, 2))
                                 + " zł")

                self._ui.label_distance_data.setText(
                    str(round(calculator_result
                              .distance_from_flat_to_nearest_reference_city /
                              1000,
                              2))
                    + " km")

                self._ui.label_basic_price_per_meter_data.setText(
                    str(round(calculator_result.basic_price_per_meter, 2))
                    + " zł")
                self._ui.label_final_price_data.setText(
                    str(round(calculator_result.house_price, 2)) + " zł")
                self._ui.label_final_price_per_meter_data.setText(
                    str(round(calculator_result.final_price_per_meter, 2))
                    + " zł")

                self._ui.browser.page().runJavaScript("drawFlatMarker=true;")
                self._ui.browser.page().runJavaScript(
                    "drawReferenceCity=true;")
                self._ui.browser.page().runJavaScript(
                    "yourFlatLat=" + str(
                        self._prices_calculator.selected_address.latitude))
                self._ui.browser.page().runJavaScript(
                    "yourFlatLng=" + str(
                        self._prices_calculator.selected_address.longitude))
                self._ui.browser.page().runJavaScript(
                    "referenceCityLat=" + str(
                        calculator_result.nearest_reference_city.latitude))
                self._ui.browser.page().runJavaScript(
                    "referenceCityLng=" + str(
                        calculator_result.nearest_reference_city.longitude))
                self._ui.browser.page().runJavaScript("initMap();")
            except ConstructionYearViolationException as e:
                msgBox = QtWidgets.QMessageBox(self._ui.widget_central)
                msgBox.about(self._ui.widget_central, "Ostrzeżenie",
                             "Operacja oszacowania wartości nie powiedzie się."
                             "\n"
                             "Powód: {}.".format(str(e)))
        else:
            msgBox = QtWidgets.QMessageBox(self._ui.widget_central)
            msgBox.about(self._ui.widget_central, "Ostrzeżenie",
                         "Operacja oszacowania wartości nie powiedzie się.\n"
                         "Powód: Nie wszystkie wartości mają poprawny format.")

    def push_button_reset_on_click(self):
        self.reset_components_values()
        self._ui.browser.page().runJavaScript("drawFlatMarker=false;")
        self._ui.browser.page().runJavaScript("drawReferenceCity=false;")
        self._ui.browser.page().runJavaScript("initMap();")

    def push_button_search_address_on_click(self):
        try:
            self._ui.combo_box_address.clear()
            self._prices_calculator.autocomplete_addresses = \
                self._ui.text_edit_search_address.toPlainText()
            if self._prices_calculator.autocomplete_addresses:
                self._ui.combo_box_address.addItem("")
                for address in self._prices_calculator.autocomplete_addresses:
                    self._ui.combo_box_address.addItem(str(address))

                self._ui.browser.page().runJavaScript("drawFlatMarker=false;")
                self._ui.browser.page().runJavaScript(
                    "drawReferenceCity=false;")
                self._ui.browser.page().runJavaScript("initMap();")
        except TransportError as e:
            msgBox = QtWidgets.QMessageBox(self._ui.widget_central)
            msgBox.about(self._ui.widget_central, "Ostrzeżenie",
                         "Operacja typowania adresów nie powiodła się.\n"
                         "Powód: {}.".format(str(e)))

    def combo_box_address_on_index_changed(self):
        if self._ui.combo_box_address.currentText() != "":
            self._prices_calculator.selected_address = \
                self._ui.combo_box_address.currentIndex() - 1
            self._ui.browser.page().runJavaScript("drawFlatMarker=true;")
            self._ui.browser.page().runJavaScript("drawReferenceCity=false;")
            self._ui.browser.page().runJavaScript(
                "yourFlatLat=" + str(
                    self._prices_calculator.selected_address.latitude))
            self._ui.browser.page().runJavaScript(
                "yourFlatLng=" + str(
                    self._prices_calculator.selected_address.longitude))
            self._ui.browser.page().runJavaScript("initMap();")
