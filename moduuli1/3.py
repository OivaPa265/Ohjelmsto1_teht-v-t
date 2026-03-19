# vastaukset
Ala = "teidän hemoglobiini lukunne on alhainen"
nor ="Teidän hemoglobiini lukunne on normaali"
kor = "teidän hemoglobiini lukunne on liian korkea"

# kysyy sukupuolen ja hemoglobiini määrän
Suku = input(f"sukupuolenne M jos mies ja W jos nainen")
Hemo = int(input("kirjoitakaa hemoglobiini lukunne\n"))

#muuttaa teksin isoiksi kirjaimiksi
Suku = Suku.upper()

# MIEHEN VASTAUKSET
if Suku == "M"  and Hemo >=134 and Hemo <=195 :
    print(f"{nor}")
elif Suku == "M"  and  Hemo <134 :
    print(f"{Ala}")
elif  Suku == "M"  and  Hemo >=196 :
    print(f"{kor}")

# NAISEN VASTAUKSET
if Suku == "W" and Hemo >= 117 and Hemo <= 175:
    print(f"{nor}")
elif Suku == "W" and Hemo <117:
    print(f"{Ala}")
elif Suku == "W" and Hemo >= 176:
    print(f"{kor}")