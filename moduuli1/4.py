#vastaukset
on = " on karkaus vuosi"
ei =  "ei ole karkaus vuosi"
#pyytää käyttäjältä Vuoden
Vuosi =int(input("mikä vuosi\n"))
#laskee jos vuosi on jaettava 4 100 taikka 400
if (Vuosi %4==0) and (Vuosi%100!=0 or Vuosi %400==0):
# jso vuosi on karkaus vuosi printaa tämän
    print (f"{Vuosi} {on}")
else:
# jos ei ole printaa tämän
    print(f"{Vuosi} {ei}")