from spillebrett import Spillebrett
def main():
    print("Oppgi dimensjoner paa spillebrettet med to heltall:")
    x = int(input("X= "))
    y = int(input("Y= "))

    myBoard = Spillebrett(x,y)
    cont = ""
    while not cont == "q":
        myBoard.update()
        print(myBoard)
        print("Antall levende celler:", myBoard.aliveCounter())
        print("Generasjon:", myBoard.genCounter())
        cont = input("Skriv inn q for aa avslutte eller enter for ny generasjon: ")

main()
