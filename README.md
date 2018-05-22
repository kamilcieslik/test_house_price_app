# Wycena mieszkań - House Price Calc

Aplikacja desktopowa umożliwiająca wycenę domów/mieszkań w Polsce. <br />
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

### Zrzuty ekranu prezentujące działanie aplikacji:
<p align="center">
1. Typowanie adresów.
</p>
<p align="center">
<img height="480" width="814" src="https://image.ibb.co/gTwE6T/1.png" />
</p>
<p align="center">

<p align="center">
2. Wycena mieszkań.
</p>
<p align="center">
<img height="480" width="814" src="https://image.ibb.co/kBwst8/2.png" />
</p>
<p align="center">