from Tkinter import as W
from time import sleep

#BLOQUE DE DEFINICIONES
#CONSTANTES
listaDiasMeses=[31,28,31,30,31,30,31,31,30,31,30,31]
listaMeses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
listaDias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
listaFeriadosDias=[1,1,21,18,19,25]
listaFeriadosMeses=[1,5,5,9,9,12]

#FUNCIONES
#FUNCION PARA SABER SI UN ANO ES BISIESTO
def esBisiesto(ano):
    if (ano%4==0) and (ano%100!=0 or ano%400==0):
        return True
    else:
        return False
#FUNCION PARA CONVERTIR UN MES A NUMERO
def numeroMes(mes):
    i = 0
    numeroMes = mes
    if isinstance(mes, str):
        mes = mes.lower()
        for e in listaMeses:
            if listaMeses[i].lower() == mes:
                numeroMes = i + 1
                break
            i += 1
    return numeroMes
#FUNCION PARA COMPROBAR SI UN DIA ES FERIADO
def esFeriado (dia,mes):
    mes = numeroMes(mes)
    i = 0
    while i < len(listaFeriadosDias):
        if dia == listaFeriadosDias[i] and mes == listaFeriadosMeses[i]:
            return True
        else:
            i += 1
    else:
        return False
#FUNCION PARA OBTENER LOS DIAS DE CIERTO MES EN UN ANO ESPECIFICO
def diasMes(mes,ano):
    mes = numeroMes(mes)
    for i in range(len(listaMeses)):
        if mes == listaMeses[i]:
            mes = i+1
    if esBisiesto(ano):
        if mes == 2:
            dias=(listaDiasMeses[mes-1])+1
        else:
            dias=(listaDiasMeses[mes-1])
    else:
        dias=(listaDiasMeses[mes-1])
    return dias
#FUNCION PARAOBTENER EL
def diaSemana(d,mes,ano):
    mes = numeroMes(mes)
    for i in range(len(listaMeses)):
        if mes == listaMeses[i]:
            if mes=="enero":
                mes=13
                ano=ano-1
            if mes=="febrero":
                mes=14
                ano=ano-1
            else:
                mes = i+1
    n=(d+2*mes+(3*(mes+1)/5)+ano+(ano/4)-(ano/10)+(ano/400)+2)%7-2
    if n <= 0:
        n = 7+n
    return n
#FUNCION QUE CREA LA MATRIZ DEL MES DADO
def matMes(mes,ano):
    matMes = [[],[],[],[],[],[]]
    i = 0
    j = 0
    d = 1
    while j < 6:
        while i < diaSemana(1,mes,ano)-1 and j == 0:
            matMes[j].append("  ")
            i += 1
        while i < 7:
            if d <= diasMes(mes,ano):
                matMes[j].append(d)
            else:
                matMes[j].append("  ")
            d += 1
            i += 1
        j += 1
        i = 0
    return matMes
#PRINTEA LA MATRIZ MES
def printMes(dia,mes,ano):
    lista = matMes(mes,ano)
    i = 0
    j = 0
    linea = " LU   MA   MI   JU   VI   SA   DO\n\n "
    posX = 262
    posY = 30
    if lista[0][6] == "  ":
        j = 1
    while j < 6:
        while i < 7:
            if lista[j][i] < 10:
                if lista[j][i] == dia:
                    linea += " (" + str(lista[j][i])
                else:
                    linea += "  " + str(lista[j][i])
            else:
                if lista[j][i] == dia:
                    linea += "(" + str(lista[j][i])
                else:
                    linea += " " + str(lista[j][i])
            if lista[j][i] == dia:
                linea += ") "
            else:
                linea += "  "
            i += 1
        i = 0
        j += 1
        linea += "\n\n "
    texto6=Label(W,text=linea,font=("Consolas", 10)).place(x=posX,y=posY+j*5)
def diasUp():
    if var1.get()+1 <= diasMes(numeroMes(var2.get()),var3.get()):
        var1.set(var1.get()+1)
    else:
        var1.set(1)
        mesesUp()
    todo()
def diasDown():
    if var1.get()-1 > 0:
        var1.set(var1.get()-1)
    else:
        var1.set(listaDiasMeses[numeroMes(var2.get())-2])
        mesesDown()
    todo()
def mesesUp():
    if numeroMes(var2.get())+1 > 12:
        var2.set("Enero")
        anosUp()
    else:
        var2.set(listaMeses[numeroMes(var2.get())])
    todo()
def mesesDown():
    if numeroMes(var2.get()) == 1:
        var2.set("Diciembre")
        anosDown()
    else:
        var2.set(listaMeses[numeroMes(var2.get())-2])
    todo()
def anosUp():
    var3.set(var3.get()+1)
    todo()
def anosDown():
    var3.set(var3.get()-1)
    todo()
def todo():
    dia=var1.get()
    mes=var2.get()
    ano=var3.get()
    printMes(dia,mes,ano)
    #Info
    if esBisiesto(ano):
        esbisiesto = "El ano es bisiesto "
    else:
        esbisiesto = "El ano no es bisiesto "
        
    if esFeriado(dia,mes):
        esferiado = "y el dia seleccionado es feriado "
    else:
        esferiado = "y el dia seleccionado no es feriado "
    textoInfo = esbisiesto + esferiado + "ademas cae dia " + listaDias[diaSemana(dia,mes,ano)-1].lower() + "."
    texto5 = Label(W,text=textoInfo).place(x=50,y=500)

#Ventana x,y
W.geometry("540x550")
#Titulo del programa
W.title("Agenda Grupo 1")
#Texto
texto=Label(W,text="- - - - - - - - - - - - - - - - -          Ingrese la fecha que busca          - - - - - - - - - - - - - - - - - -")
texto.pack() # No se.. xD
#SubTexto
varPizarra=StringVar()
texto=Label(W,text="Rellene la informacion pertinente.").place(x=20,y=30)
#Ingresar dia
texto2=Label(W,text="Dia:").place(x=20,y=65)
var1=IntVar()
var1.set("25")
caja1=Entry(W,textvariable=var1,width=5).place(x=60,y=66)
#Ingresar mes
texto4=Label(W,text="Mes:").place(x=110,y=66)
var2 = StringVar()
var2 = StringVar(W)
var2.set('Diciembre')
cajaSeleccion = OptionMenu(W, var2, *listaMeses).place(x=150,y=62)
#Ingresar ano
texto3=Label(W,text="Ano:").place(x=20,y=100)
var3=IntVar()
var3.set("1999")
caja2=Entry(W,textvariable=var3,width=5).place(x=60,y=101)
#Boton procesar
boton1=Button(W,text=" Actualizar >>",width=10,height=1,command=todo).place(x=20,y=140)
#Botones recorrer anos
boton2=Button(W,text="<",width=2,height=1,command=diasDown).place(x=130,y=110)
texto2=Label(W,text="DIAS",font=(None, 10,"italic")).place(x=170,y=111)
boton3=Button(W,text=">",width=2,height=1,command=diasUp).place(x=222,y=110)
#Botones recorrer meses
boton2=Button(W,text="<",width=2,height=1,command=mesesDown).place(x=130,y=140)
texto2=Label(W,text="MESES",font=(None, 10,"italic")).place(x=162,y=141)
boton3=Button(W,text=">",width=2,height=1,command=mesesUp).place(x=222,y=140)
#Botones recorrer dias
boton2=Button(W,text="<",width=2,height=1,command=anosDown).place(x=130,y=170)
texto2=Label(W,text="ANOS",font=(None, 10,"italic")).place(x=167,y=171)
boton3=Button(W,text=">",width=2,height=1,command=anosUp).place(x=222,y=170)
#Pizarra
#pizarra1=Label(W,text="Pizarra:").place(x=20,y=200)
#pizarra2=Label(W,textvariable=varPizarra).place(x=20,y=220)

#INICIAL
todo()

#Iniciar ventana
W.mainloop()


