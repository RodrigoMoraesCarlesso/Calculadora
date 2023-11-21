from tkinter import *

def n1():
    visor["text"] += '1'

def n2():
    visor["text"] += '2'

def n3():
    visor["text"] += '3'

def n4():
    visor["text"] += '4'

def n5():
    visor["text"] += '5'

def n6():
    visor["text"] += '6'

def n7():
    visor["text"] += '7'

def n8():
    visor["text"] += '8'

def n9():
    visor["text"] += '9'

def n0():
    visor["text"] += '0'

def nvirg():
    visor['text'] += '.'

def mais():
    global produto, adicao, subtracao, multiplicacao, divisao
    if visor['text'] != '':
        prod()
    adicao = True
    subtracao = multiplicacao = divisao = False
    if produto == 0:
        produto += float(visor['text'])
    elif visor['text'] != '':
        produto += float(visor['text'])
    visoreq['text'] = produto
    visor['text'] = ''


def menos():
    global produto, adicao, subtracao, multiplicacao, divisao
    if visor['text'] != '':
        prod()
    subtracao = True
    adicao = multiplicacao = divisao = False
    if produto == 0:
        produto += float(visor['text'])
    elif visor['text'] != '':
        produto -= float(visor['text'])
    visoreq['text'] = produto
    visor['text'] = ''


def mult():
    global produto, adicao, subtracao, multiplicacao, divisao
    if visor['text'] != '':
        prod()
    multiplicacao = True
    adicao = divisao = subtracao = False
    if produto == 0:
        produto += float(visor['text'])
    elif visor['text'] != '':
        produto *= float(visor['text'])
    visoreq['text'] = produto
    visor['text'] = ''


def div():
    global produto, adicao, subtracao, multiplicacao, divisao
    if visor['text'] != '':
        prod()
    divisao = True
    adicao = multiplicacao = subtracao = False
    if produto == 0:
        produto += float(visor['text'])
    elif visor['text'] != '':
        produto /= float(visor['text'])
    visoreq['text'] = produto
    visor['text'] = ''


def prod():
    global produto, adicao, subtracao, multiplicacao, divisao
    if adicao == True:
        produto += float(visor['text'])
        visor['text'] = ''
        visoreq['text'] = produto
    elif subtracao == True:
        produto -= float(visor['text'])
        visor['text'] = ''
        visoreq['text'] = produto
    elif multiplicacao == True:
        produto *= float(visor['text'])
        visor['text'] = ''
        visoreq['text'] = produto
    elif divisao == True:
        produto /= float(visor['text'])
        visor['text'] = ''
        visoreq['text'] = produto


def limpar():
    global adicao, multiplicacao, divisao, subtracao, produto
    visor['text'] = ''
    visoreq['text'] = ''
    produto = 0
    adicao = multiplicacao = divisao = subtracao = False


def but(n, x=''):
    global janela
    fim = Button(janela, text=n, command=x, width=5, borderwidth=4, bg='#00CED1', font=('Verdana', 15), justify=CENTER)
    return fim


adicao = False
subtracao = False
multiplicacao = False
divisao = False
produto = 0

janela = Tk()

#Janela

janela.geometry('600x250')
janela.configure(background='#483D8B')

#TÍTULO

janela.title('Calculadora')

#VISOR

visoreq = Label(janela, text='', width=20, borderwidth=4, bg='#00CED1', font=('Verdana', 15), justify=CENTER)
visoreq.grid(column=4, row=0)

visor = Label(janela, text='', width=20, borderwidth=4, bg='#00CED1', font=('Verdana', 15), justify=CENTER)
visor.grid(column=4, row=1)

#BOTÕES

button1 = but(1, n1)
button1.grid(column=0, row=2)

button2 = but(2, n2)
button2.grid(column=1, row=2)

button3 = but(3, n3)
button3.grid(column=2, row=2)

button4 = but(4, n4)
button4.grid(column=0, row=1)

button5 = but(5,n5)
button5.grid(column=1, row=1)

button6 = but(6, n6)
button6.grid(column=2, row=1)

button7 = but(7, n7)
button7.grid(column=0, row=0)

button8 = but(8, n8)
button8.grid(column=1, row=0)

button9 = but(9, n9)
button9.grid(column=2, row=0)

button0 = Button(janela, text='0', command=n0, width=11, borderwidth=4, bg='#00CED1', font=('Verdana', 15), justify=CENTER)
button0.grid(column=0, row=3, columnspan=2)

buttonp = but('=', prod)
buttonp.grid(column=3, row=4)

buttonc = Button(janela, text='C', command=limpar, width=17, borderwidth=4, bg='#00CED1', font=('Verdana', 15), justify=CENTER)
buttonc.grid(column=0, row=4, columnspan=3)

buttonvirg = but('.', nvirg)
buttonvirg.grid(column=2, row=3)

buttonmais = but('+', mais)
buttonmais.grid(column=3, row=3)

buttonmenos = but('-', menos)
buttonmenos.grid(column=3, row=2)

buttondiv = but('/', div)
buttondiv.grid(column=3, row=0)

buttonmult = but('X', mult)
buttonmult.grid(column=3, row=1)

#FIM

janela.mainloop()