import xml.etree.ElementTree as ET
import os

existeix_fitxer = os.path.exists("game.xml")
if not existeix_fitxer:
    f1 = open("game.xml", "w")
    f1.write("<data></data>")
    f1.close()
tree = ET.parse("game.xml")
root = tree.getroot()
cont = 0
while (True):
    print(
        "Elegeix una d'aquestes opcions: \n1.Insertar un nou joc\n2.Llistar els jocs\n3.Mostrar totes les dades d'un joc\n"
        "4.Modificar un joc\n5.Eliminar un joc\n6.Sortir")
    print("La teva elecció es:")

    eleccio = input()
    if (eleccio == "1"):
        for element in root.findall('game'):
            ids= int(element.get('id'))
            if ids>cont:
                cont=ids
        cont += 1

        id = str(cont)
        game = ET.SubElement(root, "game")
        game.set('id', id)
        name = ET.SubElement(game, "name")
        print("Escriu el nom del videojoc:")
        textname = input()
        name.text = textname
        year = ET.SubElement(game, "year")
        print("Escriu el any del videojoc:")
        textyear = input()
        year.text = textyear
        systems = ET.SubElement(game, "systems")
        print("Escriu la consola on es pot jugar el videojoc:")
        textsyst = input()
        systems.text = textsyst
        developer = ET.SubElement(game, "developer")
        print("Escriu el desarrolador d'aquest videojoc:")
        textdeveloper = input()
        developer.text = textdeveloper
        genre = ET.SubElement(game, "genre")
        print("Escriu el genere del videojoc:")
        textgenre = input()
        genre.text = textgenre
        description = ET.SubElement(game, "description")
        print("Escriu la descripcio del videojoc:")
        textdescrip = input()
        description.text = textdescrip
        imatgeURL = ET.SubElement(game, "imatgeURL")
        print("Escriu l'enllaç de una imatge del videojoc:")
        textimatge = input()
        imatgeURL.text = textimatge
        tree.write("game.xml")
        continue
    elif (eleccio == "2"):
        tree = ET.parse("game.xml")
        root = tree.getroot()
        for child in root.iter('game'):
            nom=child.find('name').text.strip()
            any=child.find('year').text.strip()
            desenvolupador=child.find('developer').text.strip()
            id=child.get('id')
            print("ID:", id)
            print("Name: ", nom)
            print("Year:", any)
            print("Developer:", desenvolupador)
            print(" ")
        continue
    elif (eleccio == "3"):
        print("De quin joc vols veure les dades?")
        joc=input()
        tree = ET.parse("game.xml")
        root = tree.getroot()
        for child in root.iter('game'):
            id = child.get('id')
            if (joc==id):
                id = child.get('id')
                nom = child.find('name').text.strip()
                any = child.find('year').text.strip()
                sistema=child.find('systems').text.strip()
                genere=child.find('genre').text.strip()
                desenvolupador = child.find('developer').text.strip()
                descripcio = child.find('description').text.strip()
                imatge=child.find('imatgeURL').text.strip()
                print("ID:", id)
                print("Name: ", nom)
                print("Year:", any)
                print("System:", sistema)
                print("Developer:", desenvolupador)
                print("Genre: ", genere)
                print("Description: ", descripcio)
                print("ImatgeURL: ", imatge)
                print(" ")

        continue

    elif (eleccio == "4"):
        print("Quin joc vols modificar? (Indrodueix la ID del joc)")
        jocedit=input()
        tree = ET.parse("game.xml")
        root = tree.getroot()
        for element in root.findall('game'):
            id = element.get('id')
            if (jocedit == id):
                id = element.get('id')
                root.remove(element)
                id = str(id)
                game = ET.SubElement(root, "game")
                game.set('id', id)
                name = ET.SubElement(game, "name")
                print("Escriu el nom del videojoc:")
                textname = input()
                name.text = textname
                year = ET.SubElement(game, "year")
                print("Escriu el any del videojoc:")
                textyear = input()
                year.text = textyear
                systems = ET.SubElement(game, "systems")
                print("Escriu la consola on es pot jugar el videojoc:")
                textsyst = input()
                systems.text = textsyst
                developer = ET.SubElement(game, "developer")
                print("Escriu el desarrolador d'aquest videojoc:")
                textdeveloper = input()
                developer.text = textdeveloper
                genre = ET.SubElement(game, "genre")
                print("Escriu el genere del videojoc:")
                textgenre = input()
                genre.text = textgenre
                description = ET.SubElement(game, "description")
                print("Escriu la descripcio del videojoc:")
                textdescrip = input()
                description.text = textdescrip
                imatgeURL = ET.SubElement(game, "imatgeURL")
                print("Escriu l'enllaç de una imatge del videojoc:")
                textimatge = input()
                imatgeURL.text = textimatge
                tree.write("game.xml")
        continue
    elif (eleccio == "5"):
        print("Ficar la id del joc que vols eliminar:")
        jocF=input()
        tree = ET.parse("game.xml")
        root = tree.getroot()
        for element in root.findall('game'):
            id = element.get('id')
            if (jocF == id):
                id = element.get('id')
                root.remove(element)
        tree.write("game.xml")
        continue

    elif (eleccio == "6"):
        print("Fins un altra!")
        break
