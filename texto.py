def leer():
    with open("invitados.txt", "r", encoding="UTF-8") as f:
        invitado = [linea[:-1] for linea in f]
        print(invitado)
        
def escribir():
    invitados1=  ["Jose", "Angel", "Ericka", "Stalin", "Juan"]
    invitados2= ["Andres", "Xiomara", "Victor", "Maria", "Dalia"]

    with open("invitados.txt", "w", encoding="UTF-8") as f:
        for nombre in invitados2:
            f.write(nombre)
            f.write("\n")

def run():
    escribir()
    leer()

if __name__ =="__main__":
    run()