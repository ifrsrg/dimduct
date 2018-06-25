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
   L_1 = float(ed3.get())
   Q_1 = float(ed4.get())
   Q_2 = float(ed5.get())
   theta = float(ed6.get())
   epsilon = float(ed12.get())
   Tipo = float(ed13.get())
   rho = 101303 /(286.9 *(temp + 273.15))
   mu = ((13 + 0.1 * temp)* 0.000001)* rho
   if Tipo == 1:
       Q_1L = Q_1*1000.0  #[l/s]
       D_1 = 32.0*(math.pow(Q_1L, 0.38))/1000
       A_1 = (math.pi*D_1**2.0)/4.0
       u_1 = Q_1/A_1
       Q_2L = Q_2*1000.0 #[l/s]
       D_2 = 32.0*(math.pow(Q_2L, 0.38))/1000
       A_2 = (math.pi*D_2**2.0)/4.0
       u_2 = Q_2/A_2

   if Tipo == 2:
       Q_1L = Q_1*1000.0  #[l/s]
       D_1 = 25.0*(math.pow(Q_1L, 0.38))/1000
       A_1 = (math.pi*D_1**2.0)/4.0
       u_1 = Q_1/A_1
       Q_2L = Q_2*1000.0 #[l/s]
       D_2 = 25.0*(math.pow(Q_2L, 0.38))/1000
       A_2 = (math.pi*D_2**2.0)/4.0
       u_2 = Q_2/A_2
       
   Re = rho * u_1 * D_1 / mu
   f_0 = math.pow(-1.8 * math.log10(math.pow(epsilon / (3.7 * D_1), 1.11) + 6.9 / Re), -2.0)
   f = math.pow(-2.0 * math.log10(epsilon / (3.7 * D_1) + 2.51 / (Re * math.sqrt(f_0))), -2.0)
   dP_m = (f * L_1 / D_1 + 0.1 * theta / 90.0) * u_1 ** 2.0 * rho
   
   lb7["text"] = "D_1 =" + str(math.floor(D_1 * 1000)/1000) + "[m]"
   lb8["text"] = "u_1 = " + str(math.floor(u_1 * 1000)/1000) + "[m/s]"
   lb9["text"] = "A_1 =" + str(math.floor(A_1 * 1000)/1000) + "[m²]"
   lb10["text"] = "D_2 =" + str(math.floor(D_2 * 1000)/1000) + "[m]"
   lb11["text"] = "u_2 =" + str(math.floor(u_2 * 1000)/1000) + "[m/s]" 
   lb12["text"] = "A_2 =" + str(math.floor(A_2 * 1000)/1000) + "[m²]"
   lb13b["text"] = "dP_m =" + str(math.floor(dP_m * 1000)/1000) + "[Pa/m]" 
#METODO DA JANELA DE INFORMAÇÕES 
def bt1_onclick() :
    janela1 = Tk()
    lb100 = Label(janela1, text="Informações", bg="pink")
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
    lb33 = Label(janela1, text="L_1 = 1.0  [m])")
    lb33.place(x=70,y=110)
    lb34 = Label(janela1, text="Q_1 = 1.000  [m³/s]")
    lb34.place(x=70,y=130)
    lb35 = Label(janela1, text="Q_2 = 0.800  [m³/s]")
    lb35.place(x=70,y=150)
    lb36 = Label(janela1, text="theta = 0.0  [deg]")
    lb36.place(x=70,y=170)
    lb37 = Label(janela1, text="epsilon = 0.0001  [m]")
    lb37.place(x=70,y=190)
    lb38 = Label(janela1, text="Tipo = 1  (DE ACORDO COM O TIPO DE SISTEMA. CONFORME DESCRITO ABAIXO)")
    lb38.place(x=70,y=210)
    lb39 = Label(janela1, text="TIPO DE SISTEMAS:")
    lb39.place(x=70,y=230)
    lb40 = Label(janela1, text="- (1) BAIXA VELOCIDADE (CONFORTO) :")
    lb40.place(x=70,y=250)
    lb41 = Label(janela1, text="- PERDA DE CARGA UNITÁRIA EM TORNO DE 1.2 - 2.2 Pa/m")
    lb41.place(x=70,y=270)
    lb42 = Label(janela1, text="- VELOCIDADE MÁX.: 12 m/s")
    lb42.place(x=70,y=290)
    lb43 = Label(janela1, text="- (2) ALTA VELOCIDADE (INDUSTRIAL) :")
    lb43.place(x=70,y=320)
    lb44 = Label(janela1, text="- PERDA DE CARGA UNITÁRIA EM TORNO DE 4.0 - 6.0 Pa/m")
    lb44.place(x=70,y=340)
    lb45 = Label(janela1, text="- VELOCIDADE MÁX.: 20 m/s")
    lb45.place(x=70,y=360)
    lb46 = Label(janela1, text="PARA DIMENSIONAR TODOS OS TRECHOS A PARTIR DA VAZÃO, TENDO A VELOCIDADE")
    lb46.place(x=70,y=390)
    lb47 = Label(janela1, text="COMO CONSEQUÊNCIA,A ROTINA DE CÁLCULOS ABAIXO É UTILIZADA.")
    lb47.place(x=70,y=410)
    lb48 = Label(janela1, text="É NECESSÁRIO VERIFICAR, NESTE CASO, SE A VELOCIDADE")
    lb48.place(x=70,y=430)
    lb49 = Label(janela1, text="RESULTANTE NÃO ESTÁ MUITO ACIMA DO RECOMENDADO PARA O CONFORTO (< 12m/s)")
    lb49.place(x=70,y=450)
    janela1.geometry("600x550+400+100")
    janela1.mainloop()
#JANELA PRINCIPAL
janela = Tk()
janela.title("Constante1")

lb11 = Label(janela, text="Constante1", bg="pink")
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

lb3 = Label(janela, text="L_1 em [m]: ")
lb3.place(x=177,y=60)
ed3 = Entry(janela)
ed3.place(x=250,y=60)
lb22 = Label(janela, text="()")
lb22.place(x=373,y=60)

lb4 = Label(janela, text="Q_1 em [m³/s]: ")
lb4.place(x=160,y=90)
ed4 = Entry(janela)
ed4.place(x=250,y=90)
lb23 = Label(janela, text="()")
lb23.place(x=373,y=90)

lb5 = Label(janela, text="Q_2 em [m³/s]: ")
lb5.place(x=160,y=120)
ed5 = Entry(janela)
ed5.place(x=250,y=120)
lb24 = Label(janela, text="()")
lb24.place(x=373,y=120)

lb6 = Label(janela, text="theta em [deg]: ")
lb6.place(x=157,y=150)
ed6 = Entry(janela)
ed6.place(x=250,y=150)
lb25 = Label(janela, text="(Angulo total de curvas no trecho)")
lb25.place(x=373,y=150)

lb12 = Label(janela, text="epsilon em [m]: ")
lb12.place(x=155 ,y=180)
ed12 = Entry(janela)
ed12.place(x=250,y=180)
lb26 = Label(janela, text="(Rugurosidade)")
lb26.place(x=373,y=180)

lb13 = Label(janela, text="Tipo (1 ou 2):")
lb13.place(x=168,y=210)
ed13 = Entry(janela)
ed13.place(x=250,y=210)
lb27 = Label(janela, text="Descrito em info com detalhes")
lb27.place(x=373,y=210)
#AREA PARA ESCREVER AS RESPOSTAS
bt = Button(janela, width=25, height=1, text="Resultado", command=bt_onclick)
bt.place(x=200,y=250)
lb7 = Label(janela, text="")
lb7.place(x=200,y=280)
lb8 = Label(janela, text="")
lb8.place(x=200,y=310)
lb9 = Label(janela, text="")
lb9.place(x=200,y=340)
lb10 = Label(janela, text="")
lb10.place(x=200,y=370)
lb11 = Label(janela, text="")
lb11.place(x=200,y=400)
lb12 = Label(janela, text="")
lb12.place(x=200,y=430)
lb13b = Label(janela, text="")
lb13b.place(x=200,y=460)

bt1 = Button(janela, width=10, height=2, text="Info", command=bt1_onclick)
bt1.place(x=10,y=490)

janela.geometry("600x530+400+100")
janela.mainloop()