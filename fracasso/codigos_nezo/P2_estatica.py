# -*-encoding:utf-8-*-
try:
  from Tkinter import *
except ImportError:
  from tkinter import *
import math
from scipy.optimize import fsolve
#Para Usar o programa voce so precisa executar o codigo apertando a tecla F5 ou clicando Run.
#METODO PRINCIPAL
def bt_onclick() :
   temp = float(ed1.get())
   L_23 = float(ed3.get()) # Comprimento do Trecho Atual
   Q_23 = float(ed4.get()) # Vazão do Trecho Atual
   u_12 = float(ed5.get())
   theta = float(ed6.get())
   R = float(ed12.get())
   epsilon = float(ed13.get()) #Rugosidade
   D_23_i = float(ed14.get())
   u_23_i = float(ed15.get())
   Trecho = float(ed16.get())
   D_12 = float(ed17.get())
   rho = 101303 /(286.9 *(temp + 273.15))
   mu = ((13 + 0.1 * temp)* 0.000001)* rho
   def residuals(initial):
       D_23 = initial[0]
       u_23 = initial[1]
       residual = [0.0, 0.0]
       global Re
       global f
       Re = rho * u_23 * D_23 / mu
       f_0 = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_23), 1.11) + 6.9 / Re), -2.0)
       f = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_23) + 2.51 / (Re * math.sqrt(f_0))), -2.0)
       residual[0] = (f * L_23 / D_23 + 0.1 * theta / 90.0 + R) * u_23 ** 2.0 - R * u_12 ** 2.0
       residual[1] = D_23 - math.sqrt((4.0 * Q_23) / (math.pi * u_23))
       return residual
       

   D_23, u_23 = fsolve(residuals, [D_23_i, u_23_i])
   if Trecho == 1: dP = (rho*f*L_23*u_23**2.0/(D_23*2.0))
   A = (math.pi*D_23**2.0)/4.0
   lb7["text"] = "D_2-3 =" + str(math.floor(D_23 * 1000)/1000) + "[m]" # 3 casas
   lb8["text"] = "u_2-3 = " + str(math.floor(u_23 * 100)/100) + "[m/s]" #2 casas
   lb9["text"] = "A =" + str(math.floor(A * 1000)/1000) + "[m²]" # 3 casas
   lb10["text"] = "f =" + str(math.floor(f * 10000)/10000) + "[]" # 4 casas
   lb11["text"] = "dP =" + str(math.floor(dP * 1000)/1000) + "[Pa]" # 3 casas  
#METODO DA JANELA DE INFORMAÇÕES 
def bt1_onclick() :
    janela1 = Tk()
    lb100 = Label(janela1, text="Informações", bg="red")
    lb101 = Label(janela1, text="", bg="black")
    lb102 = Label(janela1, text="", bg="black")
    lb100.pack(side=TOP, fill=X)
    lb101.pack(side=LEFT, fill=Y)
    lb102.pack(side=RIGHT, fill=Y)
    janela1.title("Info")
    lb30 = Label(janela1, text="Algumas dicas, exemplos e instruções de como preencher.")
    lb30.place(x=50,y=30)
    lb31 = Label(janela1, text="Exemplo/Instruções)")
    lb31.place(x=245,y=60)
    lb32 = Label(janela1, text="temp = 30  [°C])")
    lb32.place(x=70,y=90)
    lb33 = Label(janela1, text="L_23 = 10.0  [m]")
    lb33.place(x=70,y=110)
    lb34 = Label(janela1, text="Q_23 = 1.33  [m³/s]")
    lb34.place(x=70,y=130)
    lb35 = Label(janela1, text="u_12 = 6.0  [m/s] (VELOCIDADE NO TRECHO ANTERIOR)")
    lb35.place(x=70,y=150)
    lb36 = Label(janela1, text="theta = 0.0  [deg] (ANGULO TOTAL EM CURVAS NO TRECHO)")
    lb36.place(x=70,y=170)
    lb37 = Label(janela1, text="R = 1.0 # [ ] (FATOR DE RECUPERAÇÃO (75% - 100%))")
    lb37.place(x=70,y=190)
    lb38 = Label(janela1, text="epsilon = 0.0  [m]")
    lb38.place(x=70,y=210)
    lb39 = Label(janela1, text="D_23_i = 0.7  [m]<---- CHUTE INICIAL DO DIÂMETRO DO TRECHO")
    lb39.place(x=70,y=230)
    lb40 = Label(janela1, text="u_23_i = 5.0  [m/s]<---- CHUTE INICIAL DA VELOCIDADE DO TRECHO")
    lb40.place(x=70,y=250)
    janela1.geometry("600x400+400+100")
    janela1.mainloop()
#JANELA PRINCIPAL
janela = Tk()
janela.title("Estatica")

lb11 = Label(janela, text="Estatica", bg="red")
lb12 = Label(janela, text="", bg="black")
lb13 = Label(janela, text="", bg="black")

lb11.pack(side=TOP, fill=X)
lb12.pack(side=LEFT, fill=Y)
lb13.pack(side=RIGHT, fill=Y)
#ENTRADA NO SISTEMA
lb1 = Label(janela, text="temp [°C]: ")
lb1.place(x=182,y=30)
ed1 = Entry(janela)#USADO PARA PEGAR O VALOR
ed1.place(x=250,y=30)
lb21 = Label(janela, text="(Temperatura)")
lb21.place(x=373,y=30)

lb3 = Label(janela, text="L_23 em [m]: ")
lb3.place(x=170,y=60)
ed3 = Entry(janela)
ed3.place(x=250,y=60)
lb22 = Label(janela, text="(Comprimento do Trecho Atual)")
lb22.place(x=373,y=60)

lb4 = Label(janela, text="Q_23 em [m³/s]: ")
lb4.place(x=152,y=90)
ed4 = Entry(janela)
ed4.place(x=250,y=90)
lb23 = Label(janela, text="(Vazão do Trecho Atual)")
lb23.place(x=373,y=90)

lb5 = Label(janela, text="u_12 em [m/s]: ")
lb5.place(x=158,y=120)
ed5 = Entry(janela)
ed5.place(x=250,y=120)
lb24 = Label(janela, text="(Velocidade no trecho anterior)")
lb24.place(x=373,y=120)

lb6 = Label(janela, text="theta em [deg]: ")
lb6.place(x=155,y=150)
ed6 = Entry(janela)
ed6.place(x=250,y=150)
lb25 = Label(janela, text="(Angulo total de curvas no trecho)")
lb25.place(x=373,y=150)

lb12 = Label(janela, text="R em [ ]: ")
lb12.place(x=191,y=180)
ed12 = Entry(janela)
ed12.place(x=250,y=180)
lb26 = Label(janela, text="(Fator de recuperacao)")
lb26.place(x=373,y=180)

lb13 = Label(janela, text="epsilon em [m]: ")
lb13.place(x=152,y=210)
ed13 = Entry(janela)
ed13.place(x=250,y=210)
lb27 = Label(janela, text="(Rugurosidade)")
lb27.place(x=373,y=210)

lb14 = Label(janela, text="D_23_i em [m]: ")
lb14.place(x=156,y=240)
ed14 = Entry(janela)
ed14.place(x=250,y=240)
lb24 = Label(janela, text="(Chute inicial do diametro)")
lb24.place(x=373,y=240)

lb15 = Label(janela, text="u_23_i em [m/s]: ")
lb15.place(x=147,y=270)
ed15 = Entry(janela)
ed15.place(x=250,y=270)
lb24 = Label(janela, text="(Chute inicial da velocidade)")
lb24.place(x=373,y=270)

lb16 = Label(janela, text="Trecho(1,2,3 etc): ")
lb16.place(x=147,y=300)
ed16 = Entry(janela)
ed16.place(x=250,y=300)
lb25 = Label(janela, text="(Inserir o trecho que esta calculando)")
lb25.place(x=373,y=300)

lb17 = Label(janela, text="D_12 ")
lb17.place(x=147,y=330)
ed17 = Entry(janela)
ed17.place(x=250,y=330)
lb26 = Label(janela, text="(Inserir o diâmetro do primeiro Trecho)")
lb26.place(x=373,y=330)
#AREA PARA ESCREVER AS RESPOSTAS
bt = Button(janela, width=25, height=1, text="Resultado", command=bt_onclick)
bt.place(x=200,y=360)
lb7 = Label(janela, text="")
lb7.place(x=200,y=400)
lb8 = Label(janela, text="")
lb8.place(x=200,y=440)
lb9 = Label(janela, text="")
lb9.place(x=200,y=470)
lb10 = Label(janela, text="")
lb10.place(x=200,y=500)
lb11 = Label(janela, text="")
lb11.place(x=200,y=530)
lb12 = Label(janela, text="")
lb12.place(x=200,y=560)

bt1 = Button(janela, width=10, height=2, text="Info", command=bt1_onclick)
bt1.place(x=10,y=600)

janela.geometry("600x620+400+100")
janela.mainloop()
