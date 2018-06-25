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
   L_23 = float(ed3.get())
   Q_23 = float(ed4.get())
   theta = float(ed5.get())
   epsilon = float(ed6.get())
   Q_1 = float(ed12.get())
   u_1 = float(ed13.get())
   Trecho = float(ed14.get())
   dP_m1 = float(ed15.get())
   D_23_i = float(ed16.get())
   rho = 101303 /(286.9 *(temp + 273.15))
   mu = ((13 + 0.1 * temp)* 0.000001)* rho
   if Trecho == 1:
      D_1 = math.sqrt((4.0 * Q_1) / (math.pi * u_1)) 
      Re_i = rho * u_1 * D_1 / mu
      f_0_i = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_1), 1.11) + 6.9 / Re_i), -2.0)
      f_i = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_1) + 2.51 / (Re_i * math.sqrt(f_0_i))), -2.0)
      dP_m1 = (f_i * L_23 / D_1 + 0.1 * theta / 90.0) * u_1 ** 2.0 * rho
      D_23_i = D_1
      u_23_i = u_1 

   u_23_i = u_1
   def residuals(initial):
    D_23 = initial[0]
    u_23 = initial[1]
    residual = [0.0, 0.0]
    global Re
    global f
    Re = rho * u_23 * D_23 / mu
    f_0 = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_23), 1.11) + 6.9 / Re), -2.0)
    f = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_23) + 2.51 / (Re * math.sqrt(f_0))), -2.0)
    residual[0] = (f * L_23 / D_23 + 0.1 * theta / 90.0)*u_23**2.0 - dP_m1    
    residual[1] = D_23 - math.sqrt((4.0 * Q_23) / (math.pi * u_23))
    return residual
    
   D_23, u_23 = fsolve(residuals, [D_23_i, u_23_i])

   lb7["text"] = "D_2-3 =" + str(math.floor(D_23 * 1000)/1000) + "[m]"
   lb8["text"] = "u_2-3 = " + str(math.floor(u_23 * 1000)/1000) + "[m/s]"
   if Trecho == 1 : lb9["text"] = "D_1 =" + str(math.floor(D_1 * 1000)/1000) + "[m]"
   lb10["text"] = "dP_m1 =" + str(math.floor(dP_m1 * 1000)/1000) + "[Pa/m]"
#METODO DA JANELA DE INFORMAÇÕES 
def bt1_onclick() :
    janela1 = Tk()
    lb100 = Label(janela1, text="Informações", bg="green")
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
    lb32 = Label(janela1, text="temp = 30 [°C]")
    lb32.place(x=70,y=90)
    lb33 = Label(janela1, text="L_23 = 1.0 [m]")
    lb33.place(x=70,y=110)
    lb34 = Label(janela1, text="Q_23 = 0.800 -> ESTA É A VAZÃO DO TRECHO EM QUE SE ESTÁ FAZENDO OS CÁLCULOS")
    lb34.place(x=70,y=130)
    lb35 = Label(janela1, text="theta = 0.0 [deg] -> ÂNGULO TOTAL DE CURVAS NO TRECHO")
    lb35.place(x=70,y=150)
    lb36 = Label(janela1, text="epsilon = 0.0001 [m] -> RUGOSIDADE ABSOLUTA")
    lb36.place(x=70,y=170)
    lb37 = Label(janela1, text="Q_1 = 1.000 [m³/s] -> ESTA É A VAZÃO ANTERIOR AO TRECHO")
    lb37.place(x=70,y=190)
    lb38 = Label(janela1, text="u_1 = 6.32 [m/s] -> PARA A PRIMEIRA ETAPA, COLOCA-SE O VALOR DA VELOCIDADE INICAL")
    lb38.place(x=70,y=210)
    lb39 = Label(janela1, text="u_1 -> NOS DEMAIS COLOCA-SE O CALCULADO NO TRECHO ANTERIOR")
    lb39.place(x=70,y=230)
    lb40 = Label(janela1, text="dP_m1 = 1.54 [Pa/m] -> COLOCA-SE O VALOR CALCULADO NO PRIMEIRO TRECHO!")
    lb40.place(x=70,y=250)
    lb41 = Label(janela1, text="dP_m1 -> NO TRECHO 1 DEVE SE INICIAR COM (0) NO VALOR")
    lb41.place(x=70,y=270)
    lb42 = Label(janela1, text="D_23_i = 0.449 [m] -> AQUI, COLCA-SE O VALOR CALCULADO NA ETAPA ANTERIOR")
    lb42.place(x=70,y=290)
    lb43 = Label(janela1, text="D_23_i -> NO TRECHO 1 DEVE SE INICIAR COM (0) NO VALOR")
    lb43.place(x=70,y=310)
    lb44 = Label(janela1, text="Trecho = (1,2,3,4,5) -> DIGA O TRECHO ATUAL QUE ESTA CALCULANDO")
    lb44.place(x=70,y=340)

    janela1.geometry("600x550+400+100")
    janela1.mainloop()
#JANELA PRINCIPAL
janela = Tk()
janela.title("Constante2")

lb11 = Label(janela, text="Constante2", bg="green")
lb12 = Label(janela, text="", bg="black")
lb13 = Label(janela, text="", bg="black")

lb11.pack(side=TOP, fill=X)
lb12.pack(side=LEFT, fill=Y)
lb13.pack(side=RIGHT, fill=Y)
#ENTRADA NO SISTEMA
lb1 = Label(janela, text="temp em [°C]: ")
lb1.place(x=163,y=30)
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
lb4.place(x=153,y=90)
ed4 = Entry(janela)
ed4.place(x=250,y=90)
lb23 = Label(janela, text="(Vazão do Trecho Atual)")
lb23.place(x=373,y=90)

lb5 = Label(janela, text="theta em [deg]: ")
lb5.place(x=157,y=120)
ed5 = Entry(janela)
ed5.place(x=250,y=120)
lb24 = Label(janela, text="(Angulo total de curvas no trecho)")
lb24.place(x=373,y=120)

lb6 = Label(janela, text="epsilon em [m]: ")
lb6.place(x=155,y=150)
ed6 = Entry(janela)
ed6.place(x=250,y=150)
lb25 = Label(janela, text="(Rugurosidade)")
lb25.place(x=373,y=150)

lb12 = Label(janela, text="Q_1 em [m³/s]: ")
lb12.place(x=159,y=180)
ed12 = Entry(janela)
ed12.place(x=250,y=180)
lb26 = Label(janela, text="(Vazão ao trecho anterior)")
lb26.place(x=373,y=180)

lb13 = Label(janela, text="u_1 em [m/s]:")
lb13.place(x=166,y=210)
ed13 = Entry(janela)
ed13.place(x=250,y=210)
lb27 = Label(janela, text="(Descrito em info com detalhes)")
lb27.place(x=373,y=210)

lb14 = Label(janela, text="Trecho:")
lb14.place(x=198,y=240)
ed14 = Entry(janela)
ed14.place(x=250,y=240)
lb28 = Label(janela, text="(Descrito em info com detalhes)")
lb28.place(x=373,y=240)

lb15 = Label(janela, text="dP_m1 em [Pa/m]:")
lb15.place(x=140,y=270)
ed15 = Entry(janela)
ed15.place(x=250,y=270)
lb29 = Label(janela, text="(Descrito em info com detalhes)")
lb29.place(x=373,y=270)

lb16 = Label(janela, text="D_23_i em [m]:")
lb16.place(x=161,y=300)
ed16 = Entry(janela)
ed16.place(x=250,y=300)
lb30 = Label(janela, text="(Descrito em info com detalhes)")
lb30.place(x=373,y=300)
#AREA PARA ESCREVER AS RESPOSTAS
bt = Button(janela, width=25, height=1, text="Resultado", command=bt_onclick)
bt.place(x=200,y=335)
lb7 = Label(janela, text="")
lb7.place(x=200,y=365)
lb8 = Label(janela, text="")
lb8.place(x=200,y=395)
lb9 = Label(janela, text="")
lb9.place(x=200,y=425)
lb10 = Label(janela, text="")
lb10.place(x=200,y=455)
lb11 = Label(janela, text="")
lb11.place(x=200,y=485)
lb12 = Label(janela, text="")
lb12.place(x=200,y=515)
lb13b = Label(janela, text="")
lb13b.place(x=200,y=535)

bt1 = Button(janela, width=10, height=2, text="Info", command=bt1_onclick)
bt1.place(x=10,y=550)

janela.geometry("600x590+400+100")
janela.mainloop()