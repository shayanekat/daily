from tkinter import *
import time
import os

#fonction de verif du fichier du jour
def checkfile():
    L = os.listdir("./data/")
    if time.strftime("%a %d %b %Y")+".txt" in L:
        return False
    else:
        return True

#fonction du premier bouton interface1
def entrer():
    #fonction du 2eme bouton interface1
    def createfile():
        f = open("./data/"+time.strftime("%a %d %b %Y")+".txt","w")
        f.write("to do,duration,done,\n")
        for i in range(n):
            a = LL[i].get()
            m = LR[i].get()
            f.write(a+","+m+",,\n")
        f.close()
        interface1.destroy()

    n = int(entrer1.get())

    l4 = Label(interface1,text="Titre")
    l4.grid(row=3,column=0)

    l5 = Label(interface1,text="Durée (min)")
    l5.grid(row=3,column=1)

    #creation des Entry
    LL,LR = [],[]
    for i in range(4,n+4):
        LL.append(Entry(interface1))
        LL[i-4].grid(row=i,column=0)

        LR.append(Entry(interface1))
        LR[i-4].grid(row=i,column=1)
    
    #bouton 2 interface1
    b2 = Button(interface1,text="Save",command=createfile)
    b2.grid(row=n+5,column=1)

#fonction du bouton interface2 pas encore fini
#on cherche a sauvegarder la position des checkbutton
def sauve():
    #lecture du fichier
    f = open("./data/"+time.strftime("%a %d %b %Y")+".txt","r")
    #enregistrement dans une liste
    L = []
    out = []
    for i in f:
        L.append(str(i).split(","))
    for i in range(len(var)):
        out.append(var[i].get())
        L[i+1][-2] = str(out[i])
    f.close()

    #réecriture du fichier
    f2 = open("./data/"+time.strftime("%a %d %b %Y")+".txt","w")
    for i in L:
        f2.write(i[0]+","+i[1]+","+i[2]+",\n")
    f2.close()

#verifie si le fichier du jour a déja été créé
if checkfile() :
    #premiere interface
    interface1 = Tk()
    interface1.title("Daily")

    l1 = Label(interface1,text="Date :")
    l1.grid(row=0,column=0)

    l2 = Label(interface1,text=time.strftime("%a %d %b %Y"))
    l2.grid(row=0,column=1)

    l3 = Label(interface1,text="nb de chose à faire :")
    l3.grid(row=1,column=0)

    entrer1 = Entry(interface1)
    entrer1.grid(row=1,column=1)

    b1 = Button(interface1,text="entrer",command=entrer)
    b1.grid(row=2,column=1)

    interface1.mainloop()

#deuxième interface
interface2 = Tk()
interface2.title("Daily")

#creation des checkbutton
f = open("./data/"+time.strftime("%a %d %b %Y")+".txt","r")
f.readline()
L = []
cases = []
var = []
for l in f.readlines():
    L.append(l.split(","))
for i in range(len(L)):
    var.append(IntVar())
    cases.append(Checkbutton(interface2,text=L[i][0]+" en "+L[i][1]+"min",variable=var[i]))
    if L[i][-2] == "1":
        cases[i].select()
    cases[i].grid(row=i,column=0)
f.close()

b = Button(interface2,text="save",command=sauve)
b.grid(row=len(L)+1,column=0)

interface2.mainloop()