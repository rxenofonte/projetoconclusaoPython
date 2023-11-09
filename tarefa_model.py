import uuid


class Tarefa:
    def __init__(self, tarefa, descricao, dtini, dtfim, status):
        self.id = uuid.uuid1()
        self.tarefa = tarefa
        self.descricao = descricao
        self.dtini = dtini
        self.dtfim = dtfim
        self.status = status

    def __repr__(self):
        return (f"Id: {self.id} \n" \
               f"Tarefa: {self.tarefa} \n" \
               f"Descricao: {self.descricao} \n" \
               f"DataIni: {self.dtini} \n" \
               f"DataFim: {self.dtfim} \n" \
               f"Status: {self.status}")

# if __name__ == "__main__":
#     t1 = Tarefa("Teste","teste","12/11/2023","12/11/2023", "Teste")
#     print(t1)