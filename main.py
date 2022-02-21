
class Alumno:
    Codigo = ""
    Nombre = ""
    Carrera = ""

    def setCodigo(self,codigo):
        self.Codigo = codigo
    def setNombre(self,nombre):
        self.Nombre = nombre
    def setCarrera(self,carrera):
        self.Carrera = carrera

    def getCodigo(self):
        return self.Codigo
    def getNombre(self):
        return self.Nombre
    def getCarrera(self):
        return self.Carrera


class Agenda():
    def cargarAgenda(self):
        self.archivo = open("Agenda.txt", 'a')

    def guardarAgenda(self):
        self.archivo.close()

    def agregar(self,Alumno):
        Codigo = Alumno.getCodigo()
        Nombre = Alumno.getNombre()
        Carrera = Alumno.getCarrera()

        self.archivo.write(Codigo + ", " + Nombre + ", " + Carrera + '\n')

    def buscar_codigo(self):
        archivo = open("Agenda.txt", 'r')
        codigo = input("Inserte el codigo a buscar: ")
        Noencontrado = True
        for element in archivo:
            arreglo = element.split(',')
            if codigo in arreglo[0]:
                print("\nCodigo: " + arreglo[0])
                print("Nombre: " + arreglo[1])
                print("Carrera: " + arreglo[2])

                Noencontrado = False
        if Noencontrado == True:
            print("Estudiante no encontrado")
        archivo.close()

    def buscar_nombre(self):
        archivo = open("Agenda.txt", 'r')
        nombre = input("Inserte el nombre a buscar: ")
        Noencontrado = True
        for element in archivo:
            arreglo = element.split(',')
            if nombre in arreglo[1]:
                print("\nCodigo: " + arreglo[0])
                print("Nombre: " + arreglo[1])
                print("Carrera: " + arreglo[2])

                Noencontrado = False
        if Noencontrado == True:
            print("Estudiante no encontrado")
        archivo.close()

    def eliminar_codigo(self):
        archivo = open("Agenda.txt", 'r')
        archivo2 = open("Respaldo.txt", 'w')
        codigo = input("Inserte el codigo a eliminar: ")
        Noencontrado = True
        while(True):
            eliminar = input("\nEsta seguro que quiere eliminar al estudiante? 1=Si 2=No: ")
            if eliminar == "1":
                for element in archivo:
                    arreglo = element.split(',')
                    if not codigo in arreglo[0]:
                        archivo2.write(arreglo[0]+','+arreglo[1]+','+arreglo[2])
                    else:
                        Noencontrado = False
                if Noencontrado == True:
                    print("\nEstudiante no encontrado")
                    break
                archivo.close()
                archivo2.close()
                archivo = open("Respaldo.txt",'r')
                archivo2 = open("Agenda.txt", 'w')
                for element in archivo:
                    archivo2.write(element)
                archivo.close()
                archivo2.close()
                print("Estudiante eliminado exitosamente\n")
                break
            elif eliminar == "2":
                print("No se elimino al estudiante")
                break
            else:
                print("Opcion incorrecta, repita de nuevo \n")

    def eliminar_nombre(self):
        archivo = open("Agenda.txt", 'r')
        archivo2 = open("Respaldo.txt", 'w')
        nombre = input("Inserte el nombre a eliminar: ")
        Noencontrado = True
        while (True):
            eliminar = input("\nEsta seguro que quiere eliminar al estudiante? 1=Si 2=No: ")
            if eliminar == "1":
                for element in archivo:
                    arreglo = element.split(',')
                    if not nombre in arreglo[1]:
                        archivo2.write(arreglo[0] + ',' + arreglo[1] + ',' + arreglo[2] )
                    else:
                        Noencontrado = False
                if Noencontrado == True:
                    print("\nEstudiante no encontrado")
                    break
                archivo.close()
                archivo2.close()
                archivo = open("Respaldo.txt", 'r')
                archivo2 = open("Agenda.txt", 'w')
                for element in archivo:
                    archivo2.write(element)
                archivo.close()
                archivo2.close()
                print("Estudiante eliminado exitosamente\n")
                break
            elif eliminar == "2":
                print("No se elimino al estudiante")
                break
            else:
                print("Opcion incorrecta, repita de nuevo :)\n")

    def mostrar_agenda(self):
        archivo = open("Agenda.txt", 'r')
        for element in archivo:
            arreglo = element.split(',')
            print("Codigo: " + arreglo[0])
            print("Nombre: " + arreglo[1])
            print("Carrera: " + arreglo[2])

        archivo.close()

def main():
    agenda = Agenda()
    agenda.cargarAgenda()
    while True:
        print("AGENDA VERSION 2\n1. Agregar estudiante \n2. Buscar estudiante\n3. Borrar estudiante\n4. Mostrar agenda \n0. Salir")
        try:
            opc = int(input("Elige la opción deseada: "))
            if opc == 1:
                Estudiante = Alumno()
                codigo = str(input("Codigo del estudiante: "))
                nombre = str(input("Nombre del estudiante: "))
                carrera = str(input("Carrera: "))

                Estudiante.setNombre(nombre)
                Estudiante.setCodigo(codigo)
                Estudiante.setCarrera(carrera)

                agenda.agregar(Estudiante)
                agenda.guardarAgenda()
                agenda.cargarAgenda()
                print("")
            elif opc == 2:
                while True:
                    print("1. Buscar por codigo \n2. Buscar por nombre completo\n3. Regresar al menu")
                    try:
                        opc = int(input("Elige una opcion: "))
                        if opc == 1:
                            agenda.buscar_codigo()
                        elif opc == 2:
                            agenda.buscar_nombre()
                        elif opc == 3:
                            print("")
                            break
                        else:
                            print("Opcion incorrecta, repita de nuevo)")
                    except:
                        print("Tipo de dato no valido\n")
            elif opc == 3:
                while True:
                    print("1. Eliminar por codigo \n2. Eliminar por nombre completo\n3. Regresar al menu")
                    try:
                        opc = int(input("Elige una opcion: "))
                        if opc == 1:
                            agenda.eliminar_codigo()
                            print("")
                        elif opc == 2:
                            agenda.eliminar_nombre()
                            print("")
                        elif opc == 3:
                            print("")
                            break
                        else:
                            print("Opcion incorrecta, repita de nuevo ")
                    except:
                        print("ERROR!!\n")
            elif opc == 4:
                agenda.mostrar_agenda()
                print("")
            elif opc == 0:
                print("Saliendo...")
                break
            else:
                print("Opcion incorrecta, repita de nuevo :)")
        except:
            print("ERROR!!\n")

main()