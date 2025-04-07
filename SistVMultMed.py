from datetime import datetime
import time

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=0
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__caninos = {}
        self.__felinos = {}
    
    def verificarExiste(self,historia):
        return historia in self.__caninos or historia in self.__felinos
        
    def verNumeroMascotas(self):
       return len(self.__caninos) + len(self.__felinos)
    
    def ingresarMascota(self, mascota):
        if self.verNumeroMascotas() >= 10:
            return "No hay espacio"
        historia = mascota.verHistoria()
        if self.verificarExiste(historia):
            return "Ya existe la mascota"
        if mascota.verTipo().lower() == "canino":
            self.__caninos[historia] = mascota
        else:
            self.__felinos[historia] = mascota
        return "Mascota ingresada con éxito"
   

    def verFechaIngreso(self,historia):
        mascota = self.__caninos.get(historia) or self.__felinos.get(historia)
        if mascota:
            return mascota.verFecha().strftime("%d/%m/%Y")
        return "La mascota no está en el sistema"
    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        mascota = self.__caninos.get(historia) or self.__felinos.get(historia)
        if mascota:
            return mascota.verLista_Medicamentos()
        return None
    
    def eliminarMascota(self, historia):
        if historia in self.__caninos:
            del self.__caninos[historia]
            return True
        elif historia in self.__felinos:
            del self.__felinos[historia]
            return True
        return False
    def eliminarMedicamentoMascota(self, historia, nombre_med):
        mascota = self.__caninos.get(historia) or self.__felinos.get(historia)
        if mascota:
            return mascota.eliminarMedicamento(nombre_med)
        


def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        
        print(f"\nActualmente hay {servicio_hospitalario.verNumeroMascotas()}/10 mascotas hospitalizadas")
        try:
            menu = int(input('''\nIngrese una opción: 
1- Ingresar una mascota 
2- Ver fecha de ingreso 
3- Ver número de mascotas en el servicio 
4- Ver medicamentos que se están administrando
5- Eliminar mascota 
6- Eliminar medicamento de una mascota
7- Salir 
Usted ingresó la opción: '''))
        except ValueError:
            print("Ingrese un número válido.")
            print("-" * 50)
            continue

        if menu == 1:
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio disponible.")
                print("-" * 50)
                continue

            try:
                historia = int(input("Ingrese la historia clínica: "))
            except ValueError:
                print("Debe ingresar un número válido para historia clínica.")
                print("-" * 50)
                continue

            if servicio_hospitalario.verificarExiste(historia):
                print("Ya existe una mascota con ese número de historia clínica.")
                print("-" * 50)
                continue

            nombre = input("Ingrese el nombre de la mascota: ")
            tipo = input("Ingrese el tipo de mascota (canino o felino): ").strip().lower()
            if tipo not in ["canino", "felino"]:
                print("Tipo de mascota no válido.")
                print("-" * 50)
                continue

            try:
                peso = float(input("Ingrese el peso: "))
            except ValueError:
                print("Peso inválido.")
                print("-" * 50)
                continue

            fecha_str = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
            try:
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            except ValueError:
                print("Formato de fecha incorrecto. Use dd/mm/aaaa.")
                print("-" * 50)
                continue

            try:
                nm = int(input("¿Cuántos medicamentos se van a registrar?: "))
            except ValueError:
                print("Ingrese un número válido.")
                print("-" * 50)
                continue

            nombres_meds = set()
            lista_med = []
            for i in range(nm):
                nombre_medicamento = input(f"Nombre del medicamento {i+1}: ").strip().lower()
                if nombre_medicamento in nombres_meds:
                    print("Ese medicamento ya fue ingresado. Intente con otro.")
                    continue
                try:
                    dosis = float(input("Ingrese la dosis: "))
                except ValueError:
                    print("Dosis inválida. Intente nuevamente.")
                    continue

                medicamento = Medicamento()
                medicamento.asignarNombre(nombre_medicamento)
                medicamento.asignarDosis(dosis)
                lista_med.append(medicamento)
                nombres_meds.add(nombre_medicamento)

            mascota = Mascota()
            mascota.asignarNombre(nombre)
            mascota.asignarHistoria(historia)
            mascota.asignarTipo(tipo)
            mascota.asignarPeso(peso)
            mascota.asignarFecha(fecha)
            mascota.asignarLista_Medicamentos(lista_med)
            resultado = servicio_hospitalario.ingresarMascota(mascota)
            print(resultado)
            print("-" * 50)

        elif menu==2: # Ver fecha de ingreso
                q = int(input("Ingrese la historia clínica de la mascota: "))
                fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
                if fecha != None:
                 print("La fecha de ingreso de la mascota es: " + fecha)
                else:
                 print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
                 print("-" * 50)
            
        elif menu==3: # Ver número de mascotas en el servicio 
                numero=servicio_hospitalario.verNumeroMascotas()
                print("El número de pacientes en el sistema es: " + str(numero))
                print("-" * 50)

        elif menu == 4:
            try:
                historia = int(input("Ingrese la historia clínica: "))
            except ValueError:
                print("Número inválido.")
                continue
            medicamentos = servicio_hospitalario.verMedicamento(historia)
            if medicamentos is not None:
                print("\nMedicamentos administrados:")
                for med in medicamentos:
                    print(f"- {med.verNombre().capitalize()} (Dosis: {med.verDosis()})")
            else:
                print("La mascota no está en el sistema.")
                print("-" * 50)
            
        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
                print("-" * 50)
        
        elif menu == 6:
            try:
                historia = int(input("Ingrese la historia clínica: "))
                nombre_medicamento = input("Nombre del medicamento a eliminar: ").strip()
                resultado = servicio_hospitalario.eliminarMedicamentoMascota(historia, nombre_medicamento)
                print("Medicamento eliminado" if resultado else "No se encontró el medicamento o la mascota")
            except:
                print("Error al eliminar el medicamento.")
                print("-" * 50)
        elif menu == 7:
            print("Cerrando el programa")
            time.sleep(0.3)
            print("...")
            time.sleep(0.3)
            print("...")
            time.sleep(0.3)
            print("...")
            time.sleep(0.3)
            print("-" * 50)
            break

        else:
            print("Opción inválida. Intente nuevamente.")
            print("-" * 50)

if __name__ == '__main__':
    main()
        
        

if __name__=='__main__':
    main()





            

                

