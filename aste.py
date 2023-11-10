def lasit_datni():
    # Pajautāsim ievadīt datnes nosaukumu
    datnes_nosaukums=input("Ieavadīt datnes nosaukumu:")
    try:

    # Kā ielādēt datnes saturu?
        with open(datnes_nosaukums, 'r') as ff:
            saturs=ff.read()
            # print(saturs) pārliecinājāmies par to, ka datnē ir skaitļi
            # Izvadi simbolu skaitu datnē
            print(f"Simbolu skaits datnē ir {len(saturs)}")

            # Izvadi pirmos 10 simbolus
            print(f"Pirmie 10 simboli ir: {saturs[:10]}")

            # Izvadi pirmo un pēdējo simbolu
            print(f"Izvadōt pirmo un pēdējo simbolu:{saturs[0]} un {saturs[-1]}")
    except FileNotFoundError:
        print("Datne nav atrasta!")
    except ValueError:
        print("Datu kļūda!")



if __name__=="__main__":
    lasit_datni()