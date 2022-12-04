from classes import *
from funcoes import *
import pandas as pd
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk, filedialog



nome_adm = 'devteam4'
senha_adm = 'devteam4'



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tela de Login')
        self.geometry('751x776')
        #self.config(background='#008')

        self.bg = PhotoImage(file="LOGO 1.png")
        self.label = Label(self, image=self.bg, width=751, height=776, bg='silver')
        self.label.place(x=0, y=0)

        self.lb_usuario = Label(self, text="Usuario", anchor=W, bg='silver')
        self.lb_usuario.place(x=10, y=200, width=100, height=20)

        self.usuario = Entry(self, bg='silver')
        self.usuario.place(x=10, y=220, width=150, height=20)

        self.lb_senha = Label(self, text="Senha", anchor=W, bg='silver')
        self.lb_senha.place(x=10, y=250, width=100, height=20)

        self.senha = Entry(self, bg='silver')
        self.senha.place(x=10, y=270, width=150, height=20)

        self.botao3 = Button(self, text="Login", bg='silver', anchor=W, command=self.abrir_jan_cf)
        self.botao3.place(x=10, y=300, width=100, height=20)

    def abrir_jan_cf(self):
        Jan_Cf()

# DESATIVEI PARA FAZER OS TESTES SEM PRECISAR POR LOGIN E SENHA

    # def abrir_jan_cf(self):
    #     if self.usuario.get() == 'devteam4' and self.senha.get() == 'devteam4':
    #        Jan_Cf()
    #     else:
    #         messagebox.showinfo(title='Usuario ou senha invalidos', message='Usuario ou senha invalidos')



class Jan_Cf(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('CF logado')
        self.geometry('1000x600')


        # Criar um notebook (pai dos demais) que ocupa toda a tela. O pai do notebook é a class Jan_Cf
        # ou seja, 'self'

        my_note = ttk.Notebook(self)
        my_note.place(x=0, y=0, width=1000, height=600)


        def del_tvbd():
            if not treeProdutos.selection():
                messagebox.showinfo(title='erro', message='Selecione o elemento a ser deletado')
            else:
                index = treeProdutos.index(treeProdutos.selection()[0])
                treeProdutos.delete(treeProdutos.selection()[0])
                #print(Bd.tabela_funcionarios)
                Bd.tabela_funcionarios = Bd.tabela_funcionarios.drop([index])
                Bd.tabela_funcionarios = Bd.tabela_funcionarios.reset_index()
                #print(Bd.tabela_funcionarios)
                Bd.tabela_funcionarios = Bd.tabela_funcionarios.drop(['index'], axis=1)
                Bd.tabela_funcionarios.to_csv(r'lista_funcionarios.csv')

        def validation():
            name = vnome.get()
            turno = vturno.get()
            equipe = vequipe.get()
            cpf = vcpf.get()
            fone = vfone.get()
            msg = ''

            if len(name) == 0:
                return 'Nome não pode estar vazio'
            if len(turno) == 0:
                return 'Turno vazio'
            if len(equipe) == 0:
                return 'equipe vazio'
            if len(cpf) == 0:
                return 'cpf vazio'
            if len(fone) == 0:
                return 'fone vazio'
            else:
                try:
                    if any(ch.isdigit() for ch in name):
                        return 'Nome nao pode conter numeros'
                    if any(ch.isdigit() for ch in turno):
                        return 'Turno nao pode conter numeros'
                    # if any(ch is not int for ch in cpf):
                    #     return 'CPF nao pode conter letras'
                    # if any(ch.isdigit() for ch in fone):
                    #     return 'Fone nao pode conter letras'
                    elif len(name) <= 5: # elif len(name) <= 5 or len(name) >40: return 'O nome deve ser entre 05 a 40 caracteres'
                        return 'Nome é muito curto. O nome deve ser entre 05 a 40 caracteres'
                    elif len(name) > 40:
                        return 'Nome é muito longo. O nome deve ser entre 05 a 40 caracteres'
                    elif len(turno) <= 4: # Podem ser as opções para escolher uma (manha, tarde, noite)
                        return 'Turno é muito curto. O turno deve ser entre 05 a 06 caracteres'
                    elif len(turno) > 6:676\
                        return 'Turno é muito longo. O nome deve ser entre 05 a 06 caracteres'
                    elif len(equipe) <= 1:
                        return 'Equipe é muito curto. A equipe deve ser entre 02 a 30 caracteres'
                    elif len(equipe) > 30:
                        return 'Equipe é muito longo. Equipe deve ser entre 02 a 30 caracteres'
                    elif len(cpf) != 11:
                        return 'CPF deve conter 11 caracteres. Sem traço nem ponto nem barras'
                    # TEM QUE INSERIR AQUI A FUNÇÃO DE VALIDAR DIGITOS VERIFICADORES DO CPF
                    elif len(fone) != 9:
                        return 'Fone deve conter 9 caracteres. Sem traço nem ponto nem barras'
                    # TEM QUE INSERIR AQUI ALGO PARA VERIFICAR SE FOR RADIO (8 CHAR) OU TELEFONE(9 CHAR)
                    else:
                        return 'Sucess!'
                except Exception as ep:
                    messagebox.showerror('Error', ep)
            #messagebox.showinfo('message', msg)

        def add_tvbd():
            if validation() != 'Sucess!':
                #or vturno.get() =='' or vequipe.get() =='' or vcpf.get() =='' or vfone.get() =='':
                messagebox.showinfo('erro', message=validation())
            else:
                treeProdutos.insert('', tk.END,
                values=(vnome.get(), vturno.get(), vequipe.get(), vcpf.get(), vfone.get()))
                lista_add = [vnome.get(), vturno.get(), vequipe.get(), vcpf.get(), vfone.get()]
                #print(Bd.tabela_funcionarios)
                Bd.tabela_funcionarios.loc[len(Bd.tabela_funcionarios)] = lista_add
                #print(Bd.tabela_funcionarios)
                Bd.tabela_funcionarios.to_csv(r'lista_funcionarios.csv')
                vnome.delete(0, END),
                vturno.delete(0, END),
                vequipe.delete(0, END),
                vcpf.delete(0, END),
                vfone.delete(0, END),
                vnome.focus()

        def download():
            arquivo = filedialog.asksaveasfile(mode='w', defaultextension=".csv",
                                                filetypes=[('Arquivo csv', '*.csv')])
            # ("Texto", "*.txt"),
            # ('Excel Sheets','*.xlsx')
            if arquivo is not None:
                messagebox.showinfo(message='Download realizado com sucesso')
                Bd.tabela_funcionarios.to_csv(arquivo)
            else:
                messagebox.showinfo(message='Download cancelado')

        def del_tvbd2():
            if not treeFer.selection():
                messagebox.showinfo(title='erro', message='Selecione o elemento a ser deletado')
            else:
                index = treeFer.index(treeFer.selection()[0])
                #print(index)
                treeFer.delete(treeFer.selection()[0])
                #print(Bd.tabela_ferramentas)
                Bd.tabela_ferramentas = Bd.tabela_ferramentas.drop([index])
                Bd.tabela_ferramentas = Bd.tabela_ferramentas.reset_index()
                #print(Bd.tabela_ferramentas)
                Bd.tabela_ferramentas = Bd.tabela_ferramentas.drop(['index'], axis=1)
                #print(Bd.tabela_ferramentas)
                Bd.tabela_ferramentas.to_csv(r'lista_ferramentas.csv', sep=';')

        def add_tvbd2():
            if vid.get()=='' or vdesc.get() =='' or vfab.get() =='' or vvolt.get() =='' \
                    or vtam.get() =='' or vuni.get() =='' or vtipo.get() =='' or vmat.get() ==''\
                    or vpn.get() =='':
                messagebox.showinfo('erro', message='Preencha todos os campos')
            else:
                treeFer.insert('', tk.END,
                values=(vid.get(), vdesc.get(), vfab.get(), vvolt.get(), vtam.get(), vuni.get(),
                vtipo.get(),vmat.get(),vpn.get()))
                lista_add = [vid.get(), vdesc.get(), vfab.get(), vvolt.get(), vtam.get(), vuni.get(),
                vtipo.get(),vmat.get(),vpn.get()]
                #print(Bd.tabela_ferramentas)
                Bd.tabela_ferramentas.loc[len(Bd.tabela_ferramentas)] = lista_add
                #print(Bd.tabela_ferramentas)
                Bd.tabela_ferramentas.to_csv(r'lista_ferramentas.csv', sep=';')
                vid.delete(0, END),
                vdesc.delete(0, END),
                vfab.delete(0, END),
                vvolt.delete(0, END),
                vtam.delete(0, END),
                vuni.delete(0, END),
                vtipo.delete(0, END),
                vmat.delete(0, END),
                vpn.delete(0, END),
                vnome.focus()

        def download2():
            arquivo = filedialog.asksaveasfile(mode='w', defaultextension=".csv",
                                                filetypes=[('Arquivo csv', '*.csv')])
            # ("Texto", "*.txt"),
            # ('Excel Sheets','*.xlsx')
            if arquivo is not None:
                messagebox.showinfo(message='Download realizado com sucesso')
                Bd.tabela_ferramentas.to_csv(arquivo, sep=';')
            else:
                messagebox.showinfo(message='Download cancelado')

#----------------Adicionando abas ao notebook(self.nb)---------------------------------------


        tb2 = Frame(my_note, background='#008',width=250, height=150, bg='silver')
        my_note.add(tb2, text='Gerenciar Ferramentas')

        tb4 = Frame(my_note, bg='silver',width=250, height=150)
        my_note.add(tb4, text='Gerenciar Tecnicos')

        tb5 = Frame(my_note, bg='silver', width=250, height=150)
        my_note.add(tb5, text='Gerenciar Reservas')
    ##---------------- ADICIONANDO IMAGEM DE FUNDO na aba tb4-------------------------------------------

        # self.bg2 = PhotoImage(file="LOGO 1.png")
        # self.label = Label(tb4, image=self.bg2, width=1000, height=600, bg='silver')
        # self.label.place(x=0, y=0)
    #-----------------------------------------------------------------------------------------

    # ------------------Adicionando Widgets a aba tb4 (botes, labels, etc)--------------------


        lbnome_tb4 = Label(tb4, text='NOME', anchor=W)
        vnome = Entry(tb4)
        lbturno_tb4 = Label(tb4, text='TURNO', anchor=W)
        vturno = Entry(tb4)
        lbequipe_tb4 = Label(tb4, text='EQUIPE', anchor=W)
        vequipe = Entry(tb4)
        lbcpf_tb4 = Label(tb4, text='CPF', anchor=W)
        vcpf = Entry(tb4)
        lbfone_tb4 = Label(tb4, text='TELEFONE', anchor=W)
        vfone = Entry(tb4)

        # ------------------Adicionando Widgets a aba tb2 (botes, labels, etc)--------------------

        lbid_tb2 = Label(tb2, text='ID', anchor=W)
        vid = Entry(tb2)
        lbdesc_tb2 = Label(tb2, text='DESCRIÇÃO', anchor=W)
        vdesc = Entry(tb2)
        lbfab_tb2 = Label(tb2, text='fabricantes', anchor=W)
        vfab = Entry(tb2)
        lbvolt_tb2 = Label(tb2, text='voltagem', anchor=W)
        vvolt = Entry(tb2)
        lbtam_tb2 = Label(tb2, text='tamanho', anchor=W)
        vtam = Entry(tb2)
        lbuni_tb2 = Label(tb2, text='unidade', anchor=W)
        vuni = Entry(tb2)
        lbtipo_tb2 = Label(tb2, text='tipo', anchor=W)
        vtipo = Entry(tb2)
        lbmat_tb2 = Label(tb2, text='material', anchor=W)
        vmat = Entry(tb2)
        lbpn_tb2 = Label(tb2, text='part_number', anchor=W)
        vpn = Entry(tb2)

        # ------------------Adicionando Widgets a aba tb5 (botes, labels, etc)--------------------

        lbidfer_tb5 = Label(tb5, text='ID Ferramenta', anchor=W)
        vidfer = Entry(tb5)
        lbdesc_tb5 = Label(tb5, text='DESCRIÇÃO da solicitação', anchor=W)
        vdescres = Entry(tb5)
        lbdtret_tb5 = Label(tb5, text='Data da Retirada', anchor=W)
        vdtret = Entry(tb5)
        lbhrret_tb5 = Label(tb5, text='Hora retirada', anchor=W)
        vhrret = Entry(tb5)
        lbdtdev_tb5 = Label(tb5, text='Data devolução', anchor=W)
        vdtdev = Entry(tb5)
        lbhrdev_tb5 = Label(tb5, text='Hora devolução', anchor=W)
        vhrdev = Entry(tb5)
        lbnmtec_tb5 = Label(tb5, text='Nome tecnico', anchor=W)
        vnmtec = Entry(tb5)


        # self.nome_tecnico = nome_tecnico

        #-Botao para executar a funcao de adicionar dados ao treeview e ao BD pelo formulario--------------------------

        btn_adicionar_tb4 = Button(tb4, text='Adicionar',
        command= add_tvbd)

        btn_adicionar_tb2 = Button(tb2, text='Adicionar', command=add_tvbd2)

        #-----------------------------------------------------------------------------------

        #-Botao para executar a funcao de Excluir dados do treeview e do BD selecionando o item-----------------------

        btn_excluir_tb4 = Button(tb4, text='Deletar',
        command=del_tvbd)

        btn_excluir_tb2 = Button(tb2, text='Deletar', command=del_tvbd2)

        #------------------------------------------------------------------------------------

        #------------Obtendo dados do treeview selecionando o item----------------

        # btn_carregar_tb4 = Button(tb4, text='Carregar',
        # command=lambda: messagebox.showinfo(title='erro', message='Selecione o elemento a ser mostrado')
        # if not treeProdutos.selection()
        # else print(
        #     "Nome: " + treeProdutos.item(treeProdutos.selection()[0], "values")[0] + ' \n',
        #     "Turno: " + treeProdutos.item(treeProdutos.selection()[0], "values")[1] + ' \n',
        #     "Equipe: " + treeProdutos.item(treeProdutos.selection()[0], "values")[2] + ' \n',
        #     "CPF: " + treeProdutos.item(treeProdutos.selection()[0], "values")[3] + ' \n',
        #     "Celular: " + treeProdutos.item(treeProdutos.selection()[0],"values")[4]
        #           ))
        # --------------------------------------------------------------------------

        # --------------------------Download --------------------------------------------------

        btn_down_tb4 = Button(tb4, text='Fazer download', command=download)

        btn_down_tb2 = Button(tb2, text='Fazer download', command=download2)

        #--------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------

        ##-----------Adicionando o treeview na aba4 e carregando dados do bd-------------------------

        dadosColunas = [item for item in Bd.tabela_funcionarios.columns]

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview', background='silver', foreground='black', rowheight=25,
                        fieldbackground='silver')
        style.map('Treeview', background=[('selected', 'red')])

        treeProdutos = ttk.Treeview(tb4,
                                    columns=dadosColunas,
                                    show='headings')

        # Adding a scrollbar to Treeview widget
        ytreeScroll2 = ttk.Scrollbar(tb4)
        ytreeScroll2.configure(command=treeProdutos.yview)

        xtreeScroll2 = ttk.Scrollbar(tb4, orient='horizontal')
        xtreeScroll2.configure(command=treeProdutos.xview)

        treeProdutos.configure(yscrollcommand=ytreeScroll2.set, xscrollcommand=xtreeScroll2.set)

        xtreeScroll2.pack(side=BOTTOM, fill='x')
        ytreeScroll2.pack(side=RIGHT, fill=BOTH)


        for i in dadosColunas:
            treeProdutos.heading(f"{i}", text=f"{i}")

        for n in Bd.tabela_funcionarios.values:
            treeProdutos.insert('', tk.END, values=list(n))

        treeProdutos.place(x=4, y=100, width=1000, height=200)

        #-----------Treeview da aba de ferramentas --------------

        dadosColunas2 = [item2 for item2 in Bd.tabela_ferramentas.columns]

        treeFer = ttk.Treeview(tb2, columns=dadosColunas2, show='headings')

        # Adding a scrollbar to Treeview widget
        ytreeScroll = ttk.Scrollbar(tb2)
        ytreeScroll.configure(command=treeFer.yview)

        xtreeScroll = ttk.Scrollbar(tb2, orient='horizontal')
        xtreeScroll.configure(command=treeFer.xview)

        treeFer.configure(yscrollcommand=ytreeScroll.set, xscrollcommand=xtreeScroll.set)

        xtreeScroll.pack(side=BOTTOM, fill='x')
        ytreeScroll.pack(side=RIGHT, fill=BOTH)


        for i2 in dadosColunas2:
            treeFer.heading(f"{i2}", text=f"{i2}")

        for n2 in Bd.tabela_ferramentas.values:
            treeFer.insert('', tk.END, values=list(n2))

        treeFer.place(x=4, y=100, width=1000, height=200)

        #----------------------------------------------------------

        # -----------Treeview da aba de Reservas --------------

        dadosColunas3 = [item3 for item3 in Bd.tabela_reservas.columns]

        treeRes = ttk.Treeview(tb5, columns=dadosColunas3, show='headings')

        # Adding a scrollbar to Treeview widget
        ytreeScroll = ttk.Scrollbar(tb5)
        ytreeScroll.configure(command=treeRes.yview)

        xtreeScroll = ttk.Scrollbar(tb5, orient='horizontal')
        xtreeScroll.configure(command=treeRes.xview)

        treeRes.configure(yscrollcommand=ytreeScroll.set, xscrollcommand=xtreeScroll.set)

        xtreeScroll.pack(side=BOTTOM, fill='x')
        ytreeScroll.pack(side=RIGHT, fill=BOTH)

        for i3 in dadosColunas3:
            treeRes.heading(f"{i3}", text=f"{i3}")

        for n3 in Bd.tabela_reservas.values:
            treeRes.insert('', tk.END, values=list(n3))

        treeRes.place(x=4, y=100, width=1000, height=200)

        #---------------------------------------------------------
        #---------------------------------------------------------------------------------------------

    # -------------------Posicionando os elementos na aba tb4----------------------

        lbnome_tb4.place(x=10, y=10, width=80, height=20)
        vnome.place(x=10, y=30, width=80, height=20)
        lbturno_tb4.place(x=100, y=10, width=80, height=20)
        vturno.place(x=100, y=30, width=80, height=20)
        lbequipe_tb4.place(x=190, y=10, width=70, height=20)
        vequipe.place(x=190, y=30, width=70, height=20)
        lbcpf_tb4.place(x=270, y=10, width=70, height=20)
        vcpf.place(x=270, y=30, width=70, height=20)
        lbfone_tb4.place(x=360, y=10, width=80, height=20)
        vfone.place(x=360, y=30, width=80, height=20)
        btn_adicionar_tb4.place(x=10, y=300, width=80, height=20)
        btn_excluir_tb4.place(x=100, y=300, width=80, height=20)
        #btn_carregar_tb4.place(x=190, y=300, width=80, height=20)
        btn_down_tb4.place(x=190, y=300, width=100, height=20)

    # --------------------------------------------------------------------------

        # -------------------Posicionando os elementos na aba tb2----------------------

        lbid_tb2.place(x=10, y=10, width=80, height=20)
        vid.place(x=10, y=30, width=80, height=20)
        lbdesc_tb2.place(x=100, y=10, width=80, height=20)
        vdesc.place(x=100, y=30, width=80, height=20)
        lbfab_tb2.place(x=190, y=10, width=70, height=20)
        vfab.place(x=190, y=30, width=70, height=20)
        lbvolt_tb2.place(x=270, y=10, width=70, height=20)
        vvolt.place(x=270, y=30, width=70, height=20)
        lbtam_tb2.place(x=350, y=10, width=70, height=20)
        vtam.place(x=350, y=30, width=70, height=20)
        lbuni_tb2.place(x=430, y=10, width=70, height=20)
        vuni.place(x=430, y=30, width=70, height=20)
        lbtipo_tb2.place(x=510, y=10, width=70, height=20)
        vtipo.place(x=510, y=30, width=70, height=20)
        lbmat_tb2.place(x=590, y=10, width=70, height=20)
        vmat.place(x=590, y=30, width=70, height=20)
        lbpn_tb2.place(x=670, y=10, width=70, height=20)
        vpn.place(x=670, y=30, width=70, height=20)
        btn_adicionar_tb2.place(x=10, y=300, width=80, height=20)
        btn_excluir_tb2.place(x=100, y=300, width=80, height=20)
        btn_down_tb2.place(x=190, y=300, width=100, height=20)

        # --------------------------------------------------------------------------

        # -------------------Posicionando os elementos na aba tb5----------------------

        lbidfer_tb5.place(x=10, y=10, width=80, height=20)
        vidfer.place(x=10, y=30, width=80, height=20)
        lbdesc_tb5.place(x=100, y=10, width=80, height=20)
        vdescres.place(x=100, y=30, width=80, height=20)
        lbdtret_tb5.place(x=190, y=10, width=70, height=20)
        vdtret.place(x=190, y=30, width=70, height=20)
        lbhrret_tb5.place(x=270, y=10, width=70, height=20)
        vhrret.place(x=270, y=30, width=70, height=20)
        lbdtdev_tb5.place(x=350, y=10, width=70, height=20)
        vdtdev.place(x=350, y=30, width=70, height=20)
        lbhrdev_tb5.place(x=430, y=10, width=70, height=20)
        vhrdev.place(x=430, y=30, width=70, height=20)
        lbnmtec_tb5.place(x=510, y=10, width=70, height=20)
        vnmtec.place(x=510, y=30, width=70, height=20)

        # --------------------------------------------------------------------------

        #------------------Adicionando Widgets as demais abas (botes, labels, etc)--------------------

        lbl_tb2 = Label(tb2, text='Gerenciar Ferramentas')
        lbl_tb2.place(x=350, y=70, width=200, height=20)

        lbl_tb4 = Label(tb4, text='Gerenciar Tecnicos')
        lbl_tb4.place(x=350, y=70, width=200, height=20)

        lbl_tb5 = Label(tb5, text='Gerenciar Reservas')
        lbl_tb5.place(x=350, y=70, width=200, height=20)

        #----------------------------------------------------------------------------------

## ----------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = App()
    root.mainloop()