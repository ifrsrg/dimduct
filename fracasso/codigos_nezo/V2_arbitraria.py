# -*-encoding:utf-8-*-
try:
  from Tkinter import *
except ImportError:
  from tkinter import *
import math
#Para Usar o programa voce so precisa executar o codigo apertando a tecla F5 ou clicando Run.
#METODO PRINCIPAL
def bt_onclick() :
   temp = float(ed1.get())
   epsilon = float(ed2.get())
   L = float(ed3.get())
   Q = float(ed4.get())
   theta = float(ed5.get())
   u = float(ed6.get())
   rho = 101303 /(286.9 *(temp + 273.15))
   mu = ((13 + 0.1 * temp)* 0.000001)* rho
   D = math.sqrt((4.0 * Q) / (math.pi * u))
   Re = rho * u * D / mu
   f_0 = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D), 1.11) + 6.9 / Re), -2.0)
   f = math.pow(-2.0 * math.log10(epsilon / (3.7 * D) + 2.51 / (Re * math.sqrt(f_0))), -2.0)
   dP = rho*((f*L/D+0.1*(theta/90.0)))*((u**2.0)/2.0)
   A = (math.pi*D**2)/4.0
   D = math.floor(D * 1000)/1000
   dP = math.floor(dP * 1000)/1000
   A = math.floor(A * 1000)/1000
   lb7["text"] = "D(Diâmetro) = " + str(D) + " [m]"
   lb8["text"] = "u(Velocidade) = "+  str(u) + " [m/s]"
   lb9["text"] = "dP(Perda de Carga) = " + str(dP) + " [Pa]"
   lb10["text"] = "A(Área) = " + str(A) + " [m²]"
#METODO DA JANELA DE INFORMAÇÕES 
def bt1_onclick() :
    janela1 = Tk()
    lb100 = Label(janela1, text="Informações", bg="gold")
    lb101 = Label(janela1, text="", bg="black")
    lb102 = Label(janela1, text="", bg="black")
    lb100.pack(side=TOP, fill=X)
    lb101.pack(side=LEFT, fill=Y)
    lb102.pack(side=RIGHT, fill=Y)
    janela1.title("Info")
    lb30 = Label(janela1, text="Algumas dicas, exemplos e instruções de como preencher.")
    lb30.place(x=50,y=30)
    lb31 = Label(janela1, text="Exemplo/Instruções")
    lb31.place(x=245,y=60)
    lb32 = Label(janela1, text="temp = 30  [°C]")
    lb32.place(x=70,y=110)
    lb34 = Label(janela1, text="L = 10.0  [m]")
    lb34.place(x=70,y=130)
    lb35 = Label(janela1, text="Q = 1.330  [m³/s]  <---- ESTA É A VAZÃO DO TRECHO EM QUE SE ESTÁ FAZENDO OS CÁLCULOS")
    lb35.place(x=70,y=150)
    lb36 = Label(janela1, text="theta = 0.0  [deg] = ÂNGULO TOTAL DE CURVAS NO TRECHO")
    lb36.place(x=70,y=170)
    lb37 = Label(janela1, text="epsilon = 0.0001  [m] = RUGOSIDADE ABSOLUTA")
    lb37.place(x=70,y=190)
    lb38 = Label(janela1, text="u = 6.0  [m/s] <--- VALOR DE VELOCIDADE NO CONDUTO PRINCIPAL")
    lb38.place(x=70,y=210)
    janela1.geometry("600x400+400+100")
    janela1.mainloop()

janela = Tk()
janela.title("Arbitraria")
#JANELA PRINCIPAL
lb11 = Label(janela, text="Arbitraria", bg="gold")
lb12 = Label(janela, text="", bg="black")
lb13 = Label(janela, text="", bg="black")

lb11.pack(side=TOP, fill=X)
lb12.pack(side=LEFT, fill=Y)
lb13.pack(side=RIGHT, fill=Y)
#ENTRADA NO SISTEMA
lb1 = Label(janela, text="temp [°C]: ")
lb1.place(x=182,y=20)
ed1 = Entry(janela)#USADO PARA PEGAR O VALOR
ed1.place(x=250,y=20)
lb21 = Label(janela, text="(temperatura)")
lb21.place(x=370,y=20)

lb2 = Label(janela, text="Epsilon [m]: ")
lb2.place(x=175,y=50)
ed2 = Entry(janela)
ed2.place(x=250,y=50)
lb22 = Label(janela, text="(Rugosidade Absoluta)")
lb22.place(x=370,y=50)

lb3 = Label(janela, text="L [m]: ")
lb3.place(x=208,y=80)
ed3 = Entry(janela)
ed3.place(x=250,y=80)
lb23 = Label(janela, text="(Comprimento do Trecho)")
lb23.place(x=370,y=80)

lb4 = Label(janela, text="Q [m³/s]: ")
lb4.place(x=193,y=110)
ed4 = Entry(janela)
ed4.place(x=250,y=110)
lb24 = Label(janela, text="(Vazão no Trecho)")
lb24.place(x=370,y=110)

lb5 = Label(janela, text="Theta [deg]: ")
lb5.place(x=177,y=140)
ed5 = Entry(janela)
ed5.place(x=250,y=140)
lb25 = Label(janela, text="(Angulo Total de Curvas)")
lb25.place(x=370,y=140)

lb6 = Label(janela, text="u [m/s]: ")
lb6.place(x=200,y=170)
ed6 = Entry(janela)
ed6.place(x=250,y=170)
lb26 = Label(janela, text="(Velocidade)")
lb26.place(x=370,y=170)
#AREA PARA ESCREVER AS RESPOSTAS
bt = Button(janela, width=25, height=1, text="Resultado", command=bt_onclick)
bt.place(x=200,y=200)
lb7 = Label(janela, text="")
lb7.place(x=200,y=240)
lb8 = Label(janela, text="")
lb8.place(x=200,y=270)
lb9 = Label(janela, text="")
lb9.place(x=200,y=300)
lb10 = Label(janela, text="")
lb10.place(x=200,y=330)

bt1 = Button(janela, width=10, height=2, text="Info", command=bt1_onclick)
bt1.place(x=10,y=357)

janela.geometry("600x400+400+100")
janela.mainloop()
