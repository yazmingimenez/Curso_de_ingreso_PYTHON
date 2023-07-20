import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        resultado_prompt= "si"
        suma_negativos= 0
        suma_positivos= 0
        contador= 0
        cant_positivos= 0
        cant_negativos= 0
        while(resultado_prompt != None):

            numero_ingresado = int(prompt(title="ej 8", prompt="escriba numeros"))


            if(numero_ingresado > 0):
                suma_positivos= suma_positivos + numero_ingresado
            elif(numero_ingresado < 0):
                suma_negativos= suma_negativos + numero_ingresado
            elif(cant_positivos==contador):
                cant_positivos = numero_ingresado + contador
                contador= contador + 1
            
            

            resultado_prompt=prompt(title="ej 10", prompt="desea continuar?")

        alert(title="respuesta", message="la suma acumulada de los positivos es {0} La suma acumulada de los negativos es {1} la Cantidad de números positivos ingresados son {2}".format(suma_positivos,suma_negativos, cant_positivos))

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()



