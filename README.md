# Wycena mieszkań - House Price Calc

Aplikacja desktopowa umożliwiająca wycenę domów/mieszkań w Polsce.
Wykorzystywana biblioteka - [House Price Calculator Library](https://github.com/kamilcieslik/house_price_calculator_library)

### Autor:

- Kamil Cieślik <br />

### Wykorzystane technologie i dodatkowe API:

- Python 3.6 <br /> 

- Qt Designer <br /> 

- Google Maps API <br /> 

- Python Client for Google Maps Services <br /> 

### Wykorzystane narzędzia:

- PyCharm Professional IDEA 2018.1.3 <br />

### Wykorzystane programy wraz z komendami:

Konwersja interfejsu graficznego w formacie .xml (Qt Designer) do pliku .py:

```
pyuic5 main.ui -o main_gui.py 
```

Konwersja pliku z ścieżkami do zasobów wykorzystywanych w Qt Designerze:

```
pyrcc5 resource.qrc -o resource_rc.py
```