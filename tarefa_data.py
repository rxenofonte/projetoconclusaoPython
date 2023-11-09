import pymysql.cursors
from tarefa_model import Tarefa


class TarefaData:
    def __init__(self):
        self.conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='C@med.2023',
            database='starkind',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conexao.cursor()

    def insertTarefa(self, tarefa: Tarefa):
        try:
            sql = "insert into tarefas " \
                  "(id, tarefa, descricao, dtini, dtfim, status) values " \
                  "(%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (tarefa.id,
                                      tarefa.tarefa,
                                      tarefa.descricao,
                                      tarefa.dtini,
                                      tarefa.dtfim,
                                      tarefa.status))
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao cadastrar tarefa: {error}")

    def updateTarefa(self, tarefa: Tarefa, id: str):
        try:
            sql = "update tarefas set tarefa = %s, descricao = %s, " \
                  "dtini = %s, dtfim = %s, status = %s where id = %s"
            self.cursor.execute(sql, (tarefa.tarefa,
                                      tarefa.descricao,
                                      tarefa.dtini,
                                      tarefa.dtfim,
                                      tarefa.status,
                                      id))
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao atualizar a tarefa: {error}")

    def deleteTarefa(self, status: str, id: str):
        if status == "Concluído":
            try:
                sql = "delete from tarefas where id = %s"
                self.cursor.execute(sql, id)
                self.conexao.commit()
                return 1
            except Exception as error:
                print(f"Erro ao apagar a terfa: {error}")
                return 0
        else:
            print('A tarefa não está concluida.')
            return 2

    def deletarTarefasConcluidas(self):
        try:
            sql = "delete from tarefas where status = %s"
            self.cursor.execute(sql, 'Concluído')
            self.conexao.commit()
            print('Tarefas concluídas excluidas com sucesso!')
        except Exception as error:
            print(f"Erro ao deletar as tarefas concluidas: {error}")

    def selectTarefas(self):
        try:
            sql = "select * from tarefas"
            self.cursor.execute(sql)
            tarefas = self.cursor.fetchall()
            return tarefas
        except Exception as error:
            print(f"Erro ao buscar as tarefas: {error}")


# if __name__ == "__main__":
#      db = TarefaData()