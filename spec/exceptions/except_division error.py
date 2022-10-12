# Example
nbre1 = input("Entrez le nombre1: ")
nbre2 = input("Entrez le nombre: ")

while True:
    try:
        division = int(nbre1) / int(nbre2)
    except ZeroDivisionError:
        print("Je ne peux pas diviser par zéro.")
        nbre1 = input("Entrez le nombre1: ")
        nbre2 = input("Entrez le nombre: ")
    except ValueError:
        print("Données invalide!")
        nbre1 = input("Entrez le nombre1: ")
        nbre2 = input("Entrez le nombre: ")
    except Exception as e:
        print(e)
    else:
        print(division)
        break
        
print("Bonjour")