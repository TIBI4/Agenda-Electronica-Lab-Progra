from Tkinter import *
listaDiasMeses=[31,28,31,30,31,30,31,31,30,31,30,31]
listaMeses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
def bisiesto(ano):
    if (ano%4==0) and (ano%100!=0 or ano%400==0):
        return True
    else:
        return False
def compruebaFeriado (dia):
    if dia == ("1 enero") or dia == ("1 mayo") or dia == ("21 mayo") or dia == ("18 septiembre") or dia == ("19 septiembre") or dia == ("25 diciembre"):
        return True
    else:
        return False
def cuentaDias(mes,ano):
    for i in range(len(listaMeses)):
        if mes == listaMeses[i]:
            mes = i+1
    if bisiesto(ano)==True:
        if mes == 2:
            dias=(listaDiasMeses[mes-1])+1
        else:
            dias=(listaDiasMeses[mes-1])
    else:
        dias=(listaDiasMeses[mes-1])
    return dias
def diaAno(d,mes,ano):
    Diasemana=["sabado","domingo","lunes","martes","miercoles","jueves","viernes"]
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
    n=(d+2*mes+(3*(mes+1)/5)+ano+(ano/4)-(ano/10)+(ano/400)+2)%7
    return Diasemana[n-1]
def todo():
    dia=varbase1.get()
    ano=varbase2.get()
    mes=dia[3:]
    if dia=="29 febrero" and bisiesto(ano)==True:
        d=int(dia[:2])
        if bisiesto(ano)==True:
            print ano,"es bisiesto"
        else:
            print ano,"no es bisiesto"
        B=compruebaFeriado(dia)
        if B==True:
            print dia,"es feriado"
        else:
            print dia,"no es feriado"
        C=cuentaDias(mes,ano)
        print mes,"tiene",C,"dias"
        D=diaAno(d,mes,ano)
        print dia,"de",ano,"es un",D
    if dia=="29 febrero" and bisiesto(ano)==False:
        print ano,"no es un ano bisiesto"
    if dia!="29 febrero":
        d=int(dia[:2])
        A=bisiesto(ano)
        if A==True:
            print ano,"es bisiesto"
        else:
            print ano,"no es bisiesto"
        B=compruebaFeriado(dia)
        if B==True:
            print dia,"es feriado"
        else:
            print dia,"no es feriado"
        C=cuentaDias(mes,ano)
        print mes,"tiene",C,"dias"
        D=diaAno(d,mes,ano)
        print dia,"de",ano,"es un",D
W=Tk()
W.geometry("540x550")
W.title("Agenda Grupo 1")
l=Label(W,text="-----------------ingrese la fecha que busca------------------")
l.pack()
varPizarra=StringVar()
l1=Label(W,text="Fecha:").place(x=20,y=30)
l2=Label(W,text="Ingrese dia y mes:").place(x=10,y=50)
varbase1=StringVar()
e1=Entry(W,textvariable=varbase1,width=15).place(x=12,y=70)
l3=Label(W,text="Ingrese ano:").place(x=150,y=50)
varbase2=IntVar()
e2=Entry(W,textvariable=varbase2,width=15).place(x=152,y=70)
b1=Button(W,text="procesar fecha",width=15,height=1,command=todo).place(x=340,y=70)
pizarra1=Label(W,text="Pizarra:").place(x=20,y=200)
pizarra2=Label(W,textvariable=varPizarra).place(x=20,y=220)
W.mainloop()
