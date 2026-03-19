#vastaukset
Pie = "Kuhanne on liian pieni. laittakaa kuha takaisin järveen"
kay ="Onnitelut kuhanne on  ainakin minimitan kokoinen onnitelut saate pitää sen"
Min = "Minimi kuhan koosta puuuit"

# pättaa sallitun minimi koon
Minimi_koko = 37

# kun käyttäjä käynistää ohjelman hän pistää kuhan koon (en keksinyt miten saada ohjelmaa tunnistamaan cm päätettttä)
fisu = float(input(" Mikä on kuhan pituus  "))

# Tarkistaa onko kuha tarpeeksi pitkä
if fisu< 37:
    puutuu = Minimi_koko - fisu
    print(f"{Pie}.") # jos kuha ei ole tarpeeksi iso printaa tämän
    print(f"{Min}, {puutuu}cm. ")

else:
    print(f"{kay}") # jos on tarpeeksi iso printaa tämän