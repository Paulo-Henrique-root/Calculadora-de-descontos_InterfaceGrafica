from tkinter import *
import tkinter #PAra poder chamar a função toplevel.
from tkinter import messagebox

def sobredados():
    app2 = tkinter.Toplevel() #Utilizado quando for uma segunda janela, para poder usar junto com o app2.grab_set().
    app2.title("Sobre")
    app2.geometry("250x250+550+245")
    app2.configure(background="#062F4F")
    app2.grab_set() #Não permitir mexer na janela abaixo dessa.
    app2.resizable(width=False, height=False)  #Proibe modificar o tamanho da janela.

    framesobre = Frame(app2, borderwidth=2, relief="solid")
    framesobre.place(x=10, y=10, width=230, height=230)
    framesobre.configure(background="#062F4F")

    Label(framesobre, text="Calculadora de descontos BRCOM\n Versão - 1.0", background="#062F4F", foreground="#fff", font="arial 9 bold").place(x=15, y=8, width=200, height=30)
    Label(framesobre, text="Desenvolvedor: Paulo Henrique", background="#062F4F", foreground="#fff", font="arial 9 bold").place(x=15, y=177, width=200, height=20)
    Label(framesobre, text="Contato: paulo.junior.ph@gmail.com", background="#062F4F", foreground="#fff", font="arial 9 bold").place(x=10, y=201, width=205, height=20)
    app2.mainloop()

def novo():
    principal()

def principal():
    def cores():
        app3 = tkinter.Toplevel() #Utilizado quando for uma segunda janela, para poder usar junto com o app2.grab_set().
        app3.title("Cores")
        app3.geometry("80x180+912+200")
        app3.configure(background="#062F4F")
        app3.grab_set() #Não permitir mexer na janela abaixo dessa.
        app3.resizable(width=False, height=False)


        azul = StringVar()
        verde = StringVar()
        amarelo = StringVar()
        padrao = StringVar()

        def cliqueazul(value):
            app3.configure(background=azul.get())
            app.configure(background=azul.get())
            v3.configure(background=azul.get())
            vv3.configure(background=azul.get())
            v4.configure(background=azul.get())
            vv4.configure(background=azul.get())
            v5.configure(background=azul.get())
            vv5.configure(background=azul.get())

        def cliqueverde(value):
            app3.configure(background=verde.get())
            app.configure(background=verde.get())
            v3.configure(background=verde.get())
            vv3.configure(background=verde.get())
            v4.configure(background=verde.get())
            vv4.configure(background=verde.get())
            v5.configure(background=verde.get())
            vv5.configure(background=verde.get())

        def cliqueamarelo(value):
            app3.configure(background=amarelo.get())
            app.configure(background=amarelo.get())
            v3.configure(background=amarelo.get())
            vv3.configure(background=amarelo.get())
            v4.configure(background=amarelo.get())
            vv4.configure(background=amarelo.get())
            v5.configure(background=amarelo.get())
            vv5.configure(background=amarelo.get())

        def cliquepadrao(value):
            app3.configure(background=padrao.get())
            app.configure(background=padrao.get())
            v3.configure(background=padrao.get())
            vv3.configure(background=padrao.get())
            v4.configure(background=padrao.get())
            vv4.configure(background=padrao.get())
            v5.configure(background=padrao.get())
            vv5.configure(background=padrao.get())

        azul.set("#191970")
        verde.set("#007849")
        amarelo.set("#FECE00")
        padrao.set("#062F4F")

        Button(app3, text="", background="#191970", command=lambda: cliqueazul(azul.get())).place(x=15, y=10, width=50,height=35)  # lambda: cliked(vcor.get()))

        Button(app3, text="", background="#007849", command=lambda: cliqueverde(verde.get())).place(x=15, y=53,width=50,height=35)

        Button(app3, text="", background="#FECE00", command=lambda: cliqueamarelo(amarelo.get())).place(x=15, y=95,width=50,height=35)

        Button(app3, text="", background="#062F4F", command=lambda: cliquepadrao(padrao.get())).place(x=15, y=137,width=50,height=35)

        app3.mainloop()

    def resetar():  # Função para resetar todos os campos.
        res = messagebox.askyesno("Limpar",
                                  "Deseja limpar todos os campos?")  # Primeiro é passado o titulo e depois a mensagem.
        if (res == True):
            #v1.delete(0, END)
            #v2.delete(0, END)
            #v1.focus()  # Vai focar o curso no widget da variavel v1 que é o valor do plano.
            #v3.place_forget()
            # v3.delete(0, END)
            # v4.delete(0, END)
            # v5.delete(0, END)
            app.destroy()
            principal()

    def impdados():
        try:
            mes = 30
            planocl = int(v1.get())
            diasu = int(v2.get())
            plano = planocl / mes
            valor = plano * diasu
            desconto = planocl - valor
            descontofloat = float("{0:.2f}".format(desconto))  # Arredonda para 2 casas decimais.
            valorfloat = "%.2f" % valor  # Ainda não sei qual a melhor forma de arrendondar para 2 casas decimais.
            if diasu <= 30:
                vv3["text"] = "DESCONTO DE"
                v3["text"] = "RS", descontofloat
                vv4["text"] = "VALOR A SER PAGO"
                v4["text"] = "R$", valorfloat
                v5["text"] = "Sucesso!!"
            else:
                v5["text"] = "Dias utilizados não pode ser maior que 30."
        except ValueError:
            messagebox.showerror(title="Erro", message="Digite somente números inteiros.")

    app = Tk()
    app.title("BRCOM")
    app.geometry("470x350+440+180")
    app.configure(background="#062F4F")
    app.resizable(width=False, height=False) #Proibe modificar o tamanho da janela.

    frameprincipal = Frame(app, borderwidth=1, relief="solid", background="#191970")
    frameprincipal.place(x=10, y=10, width=450, height=170)

    Label(frameprincipal, text="INFORME O VALOR DO PLANO", background="#191970", foreground="#fff", font=("arial", 13, "bold")).place(x=70, y=10, width=300, height=20)#anchor=W Deixa o label para esquedar.

    v1 = Entry(frameprincipal, font= "verdana 12 bold") #Variavel do plano.
    v1.place(x=200, y=33, width=50, height=21)

    Label(frameprincipal, text="INFORME QUANTOS DIAS FORAM UTILIZADOS", background="#191970", foreground="#fff", font="arial 13 bold").place(x=40, y=70, width=370, height=20)

    v2 = Entry(frameprincipal, font= "verdana 12 bold") #Variavel de dias utilizados.
    v2.place(x=200, y=93, width=50, height=21)

    vv3 = Label(app, text="", background="#062F4F", foreground="#fff", font="arial 13")
    vv3.place(x=135, y=270, width=200, height=20)

    v3 = Label(app, text="", background="#062F4F", foreground="#fff", font="arial 13", anchor=W) #Print o desconto.
    v3.place(x=202, y=290, width=250, height=25)

    vv4 = Label(app, text="", background="#062F4F", foreground="#fff", font="arial 15 bold")
    vv4.place(x=134, y=190, width=200, height=20)

    v4 = Label(app, text="", background="#062F4F", foreground="#fff", font="arial 20 bold", anchor=W) #Print o valor a ser pago.
    v4.place(x=185, y=215, width=270, height=23)

    vv5 = Label(app, text="Status:", background="#062F4F", foreground="#fff", anchor=W)
    vv5.place(x=7, y=330, width=50, height=20)

    v5 = Label(app, text="", background="#062F4F", foreground="#fff", anchor=W) #Print "status".
    v5.place(x=44, y=330, width=350, height=20)

    btncalcular = Button(frameprincipal, text="Calcular", background="#07889B", command=impdados, font="arial 13 bold").place(x=185, y=130, width=80, height=30)  # Botão de "calcular".

    btnreset = Button(frameprincipal, text="Limpar", command=resetar)  # Botão de limpar.
    btnreset.place(x=398, y=136, width=45, height=25)

    btnsobre = Button(app, text="Sobre", background="#07889B", command=sobredados, font=("verdana", 8, "")).place(x=416, y=320, width=43, height=25) #Botão de "sobre".

    #####Barra de menu#####
    barramenus = Menu(app) #Cria uma barra de menus.

    arquivomenu = Menu(barramenus) #Cria uma coluna dentro do menu.
    arquivomenu = Menu(arquivomenu, tearoff=0) #Tira um tracejado que vem por padrão nos menu.
    barramenus.add_cascade(label="Arquivo", menu=arquivomenu) #Da um nome a o menu e diz que vai ser em forma de cascata.
    arquivomenu.add_command(label="Novo", command=principal) #Cria submenus.

    arquivomenu.add_separator()
    arquivomenu.add_command(label="Fechar", command=app.quit)

    confmenu = Menu(barramenus)
    confmenu = Menu(confmenu, tearoff=0) #Tira um tracejado que vem por padrão nos menu.
    barramenus.add_cascade(label="Configurações", menu=confmenu)
    confmenu.add_command(label="Cores", command=cores)

    sobremenu = Menu(barramenus)
    sobremenu = Menu(sobremenu, tearoff=0) #Tira um tracejado que vem por padrão nos menu.
    barramenus.add_cascade(label="Sobre", menu=sobremenu)
    sobremenu.add_command(label="Empresa", command=sobredados)

    app.config(menu=barramenus)
    ######################

    v1.focus() #Vai focar o curso no widget da variavel v1 que é o valor do plano.

    app.mainloop() #Faz a execução do programa em modo gráfico.

principal()
