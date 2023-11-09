import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime


from tarefa_model import Tarefa
from tarefa_data import TarefaData


class App:
    def __init__(self):
        self.retorno: int

        self.db = TarefaData()

        self.janela = Tk()
        self.janela.title('Stark Industries - Tarefas')
        self.janela.state('zoomed')

        self.logo = PhotoImage(file='logo.png')
        self.janela.iconbitmap("logo.ico")


        # Label
        self.label_id = Label(self.janela, text="Id",
                                     font="Tahoma 14 bold", fg="red")
        self.label_id.grid(row=0, column=0)

        # Entry
        self.txt_id = Entry(self.janela, font="Tahoma 14",
                                   width=27, state=DISABLED)
        self.txt_id.grid(row=0, column=1)

        # Label
        self.label_logo = Label(self.janela, image=self.logo)
        self.label_logo.grid(row=0, column=2, columnspan=2)

        self.label_blank1 = Label(self.janela, text="",
                                     font="Tahoma 14 bold", fg="red")

        self.label_blank1.grid(row=1, column=0)

        # Label
        self.label_tarefa = Label(self.janela, text="Tarefa",
                                     font="Tahoma 14 bold", fg="red")
        self.label_tarefa.grid(row=2, column=0)

        # Entry
        self.txt_tarefa = Entry(self.janela, font="Tahoma 14",
                                   width=27)
        self.txt_tarefa.grid(row=2, column=1)

        # Label
        self.label_descricao = Label(self.janela, text="Descricao",
                                font="Tahoma 14 bold", fg="red")
        self.label_descricao.grid(row=2, column=2)

        # Entry
        self.txt_descricao = Entry(self.janela, font="Tahoma 14",
                              width=27)
        self.txt_descricao.grid(row=2, column=3)

        self.label_blank2 = Label(self.janela, text="",
                                     font="Tahoma 14 bold", fg="red")

        self.label_blank2.grid(row=3, column=0)

        self.ini = tkinter.StringVar(self.janela, str(datetime.date.today()))
        self.fim = tkinter.StringVar(self.janela, str(datetime.date.today()))


        #Label
        self.label_dtini = Label(self.janela, text="Data Inicial",
                                 font="Tahoma 14 bold", fg="red")
        self.label_dtini.grid(row=4, column=0)

        # Calendar
        self.cal_dtini = DateEntry(locale="pt_BR", date_pattern="DD/MM/YYYY", font="Tahoma 14 bold")
        self.cal_dtini.grid(row=4, column=1)

        # Label
        self.label_dtfim = Label(self.janela, text="Data Final",
                                 font="Tahoma 14 bold", fg="red")
        self.label_dtfim.grid(row=4, column=2)


        # Calendar
        self.cal_dtfim = DateEntry(locale="pt_BR", date_pattern="DD/MM/YYYY", font="Tahoma 14 bold")

        self.cal_dtfim.grid(row=4, column=3)

        self.label_blank3 = Label(self.janela, text="",
                                     font="Tahoma 14 bold", fg="red")

        self.label_blank3.grid(row=5, column=0)

        # Label
        self.label_status = Label(self.janela, text="Status",
                                 font="Tahoma 14 bold", fg="red")
        self.label_status.grid(row=6, column=0)

        self.status = ['A fazer', 'Em andamento', 'Concluído']
        self.cb_status = ttk.Combobox(self.janela, values=self.status, width=28,
                                      font="Tahoma 14 bold")
        self.cb_status.grid(row=6, column=1)

        self.label_blank4 = Label(self.janela, text="",
                                     font="Tahoma 14 bold", fg="red")


        self.label_blank4.grid(row=7, column=0)

        # botões
        self.button_adicionar = Button(self.janela, font="Tahoma 12 bold", width=7,
                                       text="Adicionar", fg="red",
                                       command=self.adicionarTarefa)

        self.button_adicionar.grid(row=8, column=0)

        # botões
        self.button_editar = Button(self.janela, font="Tahoma 12 bold", width=7,
                                    text="Atualizar", fg="red",
                                    command=self.editarTarefa)
        self.button_editar.grid(row=8, column=1)

        # botões
        self.button_deletar = Button(self.janela, font="Tahoma 12 bold", width=7,
                                     text="Deletar", fg="red",
                                     command=self.deletarTarefa)
        self.button_deletar.grid(row=8, column=2)

        # botões
        self.button_deletarconcluidas = Button(self.janela, font="Tahoma 12 bold", width=15,
                                     text="Deletar Concluídas", fg="red",
                                     command=self.deletarTarefasConcluidas)
        self.button_deletarconcluidas.grid(row=9, column=2)

        # botões
        self.button_fechar = Button(self.janela, font="Tahoma 12 bold", width=7,
                                     text="Fechar", fg="red",
                                     command=self.janela.destroy)
        self.button_fechar.grid(row=8, column=3)

        # botões
        self.button_limpar = Button(self.janela, font="Tahoma 12 bold", width=7,
                                     text="Limpar", fg="red",
                                     command=self.limparCampos)
        self.button_limpar.grid(row=9, column=3)

        self.label_blank5 = Label(self.janela, text="",
                                     font="Tahoma 14 bold", fg="red")


        self.label_blank5.grid(row=10, column=0)

        # frame
        self.frame = Frame(self.janela)
        self.frame.grid(row=11, column=0, columnspan=4)

        self.colunas = ['Id','Tarefa', 'Descricao', 'Dt Ini', 'Dt Fim', 'Status']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show='headings')
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
        self.tabela.pack()
        self.tabela.bind('<ButtonRelease-1>', self.selecionarTarefa)
        self.atualizarTabela()
        self.janela.mainloop()


    def verificarPreenchimento(self):
        tarefa_txt = self.txt_tarefa.get()
        descricao_txt = self.txt_descricao.get()
        status_txt = self.cb_status.get()
        dtini = self.cal_dtini.get_date()
        dtfim = self.cal_dtfim.get_date()
        self.retorno = 1
        if (tarefa_txt == ''):
            messagebox.showinfo("Atenção!", "Preencher a tarefa!")
            self.retorno = 0
        if (descricao_txt == ''):
            messagebox.showinfo("Atenção!", "Preencher a descrição!")
            self.retorno = 0
        if (status_txt == ''):
            messagebox.showinfo("Atenção!", "Preencher o status!")
            self.retorno = 0
        if dtini > dtfim:
            messagebox.showinfo("Atenção!", "A data inicial não pode ser maior que a data final!")
            self.retorno = 0
    def limparCampos(self):
        self.txt_tarefa.delete(0, END)
        self.txt_descricao.delete(0, END)
        self.cal_dtini.set_date(datetime.date.today())
        self.cal_dtfim.set_date(datetime.date.today())
        self.cb_status.set("")
        self.txt_id.config(state=NORMAL)
        self.txt_id.delete(0, END)
        self.txt_id.config(state=DISABLED)

    def atualizarTabela(self):
        # Limpa a tabela
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        tarefas = self.db.selectTarefas()
        for tarefa in tarefas:
            dtini = datetime.datetime.strptime(str(tarefa['dtini']), '%Y-%m-%d %H:%M:%S')
            dtfim = datetime.datetime.strptime(str(tarefa['dtfim']), '%Y-%m-%d %H:%M:%S')
            self.tabela.insert("",END, values=(tarefa['id'],
                                               tarefa['tarefa'],
                                               tarefa['descricao'],
                                               dtini.strftime('%d/%m/%Y'),
                                               dtfim.strftime('%d/%m/%Y'),
                                               tarefa['status']))

    def selecionarTarefa(self, event):
        linha_selecionada = self.tabela.selection()[0]
        item = self.tabela.item(linha_selecionada)['values']
        self.limparCampos()
        self.txt_id.config(state=NORMAL)
        self.txt_id.insert(0, item[0])
        self.txt_id.config(state=DISABLED)
        self.txt_tarefa.insert(0, item[1])
        self.txt_descricao.insert(0, item[2])
        self.cal_dtini.set_date(datetime.datetime.strptime(item[3], '%d/%m/%Y'))
        self.cal_dtfim.set_date(datetime.datetime.strptime(item[4], '%d/%m/%Y'))
        self.cb_status.set(item[5])

    def criarTarefa(self):
        tarefa = self.txt_tarefa.get()
        descricao = self.txt_descricao.get()
        dtini = self.cal_dtini.get_date()
        dtfim = self.cal_dtfim.get_date()
        status = self.cb_status.get()

        return Tarefa(tarefa,descricao,dtini,dtfim,status)

    def adicionarTarefa(self):
        self.verificarPreenchimento()
        if self.retorno == 1:
            tarefa= self.criarTarefa()
            self.db.insertTarefa(tarefa)
            self.limparCampos()
            self.atualizarTabela()
            messagebox.showinfo("Sucesso!", "Tarefa adicionada com sucesso!")
    def editarTarefa(self):
        self.verificarPreenchimento()
        if self.retorno == 1:
            id = self.txt_id.get()
            tarefa = self.criarTarefa()
            self.db.updateTarefa(tarefa, id)
            self.limparCampos()
            self.atualizarTabela()
            messagebox.showinfo("Sucesso!", "Tarefa atualizada com sucesso!")

    def deletarTarefa(self):
        id = self.txt_id.get()
        status = self.cb_status.get()
        retorno = self.db.deleteTarefa(status, id)
        if retorno == 1:
            messagebox.showinfo("Sucesso!", "Tarefa deletada com sucesso!")
            self.atualizarTabela()
            self.limparCampos()
        elif retorno == 2:
            messagebox.showinfo("Erro!", "Tarefa não está concluída!")
        else:
            messagebox.showinfo("Erro!", "Tarefa não pode ser excluída!")


    def deletarTarefasConcluidas(self):
        self.db.deletarTarefasConcluidas()
        messagebox.showinfo("Sucesso!", "Todas as tarefas concluídas foram excluídas!")
        self.atualizarTabela()
        self.limparCampos()

if __name__ == "__main__":
    app = App()