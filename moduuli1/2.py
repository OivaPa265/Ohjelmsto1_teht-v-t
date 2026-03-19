#Vastaukset
LUX ="LUX on parvekkeellinen hytti yläkannella."
A = "A on ikkunallinen hytti autokannen yläpuolella."
B = "B on ikkunaton hytti autokannen yläpuolella."
C = "C on ikkunaton hytti autokannen alapuolella."

#kysyy hyttiluokan
print("terve millaisen hytin haluaisitte LUX, A, B taikka C?")

#Käyttäjä kirjoitaa tähän haluamansa hytti luokan
hytti =input("valitkaa hyttinne\n")

#muuttaa kirjaimet isoiksi kirjaimiksi
hytti = hytti.upper()

# tarkistaa jos valita on hyväksyttävä printaa vastaavan tekstin
if hytti == "A" or hytti == "a":
    print(f"{A}")
elif hytti == "B" or hytti == "b":
    print(f"{B}")
elif hytti == "C" or hytti == "c":
    print(f"{C}")
elif hytti == "LUX":
    print(f"{LUX}")

    # jos valinta ei ole hyväksyttävä printaa tämän
else:
    print("Virheellinen hyttiluokka \n")