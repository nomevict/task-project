import typing
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QLabel, QScrollArea, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from tela_cadastro_tarefa import Tela_cadastroTarefa
from tela_cadastro_usuario import Tela_cadastroUsuario
from tela_login import Tela_login
from tela_inicial import Tela_inicial
from tela_buscar_tarefa import Tela_buscar_tarefa
from tela_ativar_tarefa import Tela_ativar
from tela_funcoes_tarefas import Tela_funcoes_tarefa
from datetime import datetime

import socket
ip = '192.168.18.36'
port = 9017
addr = ((ip, port))

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(addr)

class Ui_main(QtWidgets.QWidget):
    """
    Classe responsavel por configurar a interface grafica da janela principal da aplicacao.

    Representa o comportamento da janela principal da aplicacao possui atributos que representam os diferentes componentes da interface.

    Attributes:
    ----------
    tela_login : Tela_login
        Objeto da classe Tela_login para configurar a tela de login.
    tela_inicial : Tela_inicial
        Objeto da classe Tela_inicial para configurar a tela inicial.
    tela_cadastro_usuario : Tela_cadastroUsuario
        Objeto da classe Tela_cadastroUsuario para configurar a tela de cadastro de usuario.
    tela_cadastro_tarefa : Tela_cadastroTarefa
        Objeto da classe Tela_cadastroTarefa para configurar a tela de cadastro de tarefa.
    tela_buscar_tarefa : Tela_buscar_tarefa
        Objeto da classe Tela_buscar_tarefa para configurar a tela de busca de tarefa.
    tela_ativar_tarefa : Tela_ativar
        Objeto da classe Tela_ativar para configurar a tela de ativar tarefa.
    tela_funcoes_tarefa : Tela_funcoes_tarefa
        Objeto da classe Tela_funcoes_tarefa para configurar a tela de funcoes de tarefa.

    Methods:
    -------
    setupUi(Main: QtWidgets.QWidget) -> None:
        Configura a interface grafica da janela principal.
    """
    def setupUi(self, Main):
        """
        Configura a interface grafica da janela principal.

        Essa funcao e responsavel por configurar a interface grafica da janela principal da aplicacao. 

        Parameters:
        -----------
        Main : QtWidgets.QWidget
            Referencia para a janela principal da aplicacao.

        Returns:
        --------
        None
            O metodo nao possui um valor de retorno especificado e, por padrao, retorna None.
        """
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_login = Tela_login()
        self.tela_login.setupUi(self.stack0)

        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack1)

        self.tela_cadastro_usuario = Tela_cadastroUsuario()
        self.tela_cadastro_usuario.setupUi(self.stack2)

        self.tela_cadastro_tarefa = Tela_cadastroTarefa()
        self.tela_cadastro_tarefa.setupUi(self.stack3)

        self.tela_buscar_tarefa = Tela_buscar_tarefa()
        self.tela_buscar_tarefa.setupUi(self.stack4)

        self.tela_ativar_tarefa = Tela_ativar()
        self.tela_ativar_tarefa.setupUi(self.stack5)

        self.tela_funcoes_tarefa = Tela_funcoes_tarefa()
        self.tela_funcoes_tarefa.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, Ui_main):
    """
    Classe principal responsavel pela execucao da aplicacao.

    Gerencia a logica de controle da interface do usuario, como a abertura de telas, interacao com o servidor e manipulacao de eventos.

    Attributes:
    ----------
    login_atual : None or str, opcional
        O login atual do usuario. Pode ser None se nenhum login estiver atualmente ativo.
    id_usuario : None or int
        O ID do usuario logado. Pode ser None se nenhum login estiver atualmente ativo.

    Methods:
    -------
    abrir_tela_login(self)
        Abre a tela de login.

    abrir_tela_inicial(self)
        Abre a tela inicial.

    abrir_tela_cadastro_usuario(self)
        Abre a tela de cadastro de usuario.

    abrir_tela_cadastro_tarefa(self)
        Abre a tela de cadastro de tarefa.

    abrir_funcoes_tarefa(self)
        Abre a tela de funcoes de tarefa.

    abrir_tela_tarefa_concluida(self)
        Abre a tela de tarefa concluida.

    abrir_tela_buscar_tarefa(self)
        Abre a tela de busca de tarefa.

    sair(self)
        Encerra a conexao do cliente com o servidor e fecha a aplicacao.

     quantidade_tarefas_pendentes(self)
        Recebe uma mensagem do servidor e exibe uma caixa de dialogo com a quantidade de tarefas pendentes.

    cadastrar_usuario(self)
        Cadastra um novo usuario com base nos dados fornecidos.

    cadastrar_tarefa(self)
        Cadastra uma nova tarefa com base nos dados fornecidos.

    excluir_tarefa_linha(self)
        Exclui uma tarefa com base no item selecionado na lista.

    concluir_tarefa_linha(self)
        Conclui uma tarefa com base no item selecionado na lista.

    reativar_tarefa_linha(self)
        Reativa uma tarefa com base no item selecionado na lista.

    loginUser(self)
        Realiza o login do usuario com base nos dados fornecidos.
    """

    def __init__(self, login_atual=None): 
        """
        Parameters
        ----------
        login_atual : None, optional
            O login atual (default e None)
        """
        super(Main, self).__init__()
        self.setupUi(self)
        self.login_atual = login_atual
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Título", "Descrição", "Prazo"])
        # Configurar outros aspectos da tabela, se necessário
        self.id_usuario = None

        self.tela_login.login_Button.clicked.connect(self.loginUser)
        self.tela_login.nova_conta_Button.clicked.connect(self.abrir_tela_cadastro_usuario)
        self.tela_login.sair_login_Button.clicked.connect(self.sair)
        
        self.tela_inicial.cadastrar_telainicial__Button.clicked.connect(self.abrir_tela_cadastro_tarefa)
        self.tela_inicial.pushButton.clicked.connect(self.quantidade_tarefas_pendentes)
        self.tela_inicial.buscar_tarefa_telainicial_Button.clicked.connect(self.abrir_funcoes_tarefa)
        self.tela_inicial.sair_telainicial_Button_5.clicked.connect(self.abrir_tela_login)
        self.tela_inicial.buscar_tarefa_telainicial_Button_2.clicked.connect(self.sair)

        self.tela_cadastro_usuario.cadastrar_Button.clicked.connect(self.cadastrar_usuario)
        self.tela_cadastro_usuario.voltar_Button.clicked.connect(self.abrir_tela_login)
        
        self.tela_cadastro_tarefa.cadastrar_tarefa_Button.clicked.connect(self.cadastrar_tarefa)
        self.tela_cadastro_tarefa.voltar_tarefa_Button.clicked.connect(self.abrir_tela_inicial)
        
        self.tela_buscar_tarefa.excluir_tarefa_Button.clicked.connect(self.concluir_tarefa_linha) 
        self.tela_buscar_tarefa.excluir_tarefa_Button_2.clicked.connect(self.abrir_funcoes_tarefa)
        self.tela_buscar_tarefa.tableWidget.itemDoubleClicked.connect(self.editar_tarefa_linha)

        self.tela_funcoes_tarefa.cadastrar_telainicial__Button.clicked.connect(self.abrir_tela_tarefa_concluida)
        self.tela_funcoes_tarefa.buscar_tarefa_telainicial_Button.clicked.connect(self.abrir_tela_buscar_tarefa)
        self.tela_funcoes_tarefa.sair_telainicial_Button_5.clicked.connect(self.abrir_tela_inicial)

        self.tela_ativar_tarefa.excluir_tarefa_Button.clicked.connect(self.reativar_tarefa_linha) 
        self.tela_ativar_tarefa.excluir_tarefa_Button_3.clicked.connect(self.excluir_tarefa_linha)
        self.tela_ativar_tarefa.excluir_tarefa_Button_2.clicked.connect(self.abrir_funcoes_tarefa)

    def abrir_tela_tarefa_concluida(self):
        """
        Abre a tela de busca de tarefa.

        Altera o índice da pilha de widgets para exibir a tela de busca de tarefa.

        Raises
        ------
        QMessageBox
            Se ocorrer um erro ao obter a lista de tarefas.
        """
        try:
            self.QtStack.setCurrentIndex(4)
            self.tela_buscar_tarefa.tableWidget.setRowCount(0) 

            mensagem = "abrir_con"
            cliente_socket.send(mensagem.encode())

            recebida = cliente_socket.recv(1024).decode()

            if recebida == '0':
                QMessageBox.information(self, "Buscar Tarefa", "Nenhuma tarefa encontrada.")
            else:
                lista = recebida.split(";")
                if lista:
                    for item in lista:
                        if item != "":
                            linha = self.tela_buscar_tarefa.tableWidget.rowCount()
                            self.tela_buscar_tarefa.tableWidget.insertRow(linha)
                            # Preencher cada coluna da linha com os valores da tarefa
                            valores = item.split(',')
                            for coluna, valor in enumerate(valores):
                                self.tela_buscar_tarefa.tableWidget.setItem(linha, coluna, QTableWidgetItem(str(valor)))
        except Exception as e:
            QMessageBox.critical(self, "Buscar Tarefa", f"Erro ao obter a lista de tarefas: {e}")
            
    def abrir_tela_buscar_tarefa(self):
        """
        Abre a tela de busca de tarefa.

        Altera o índice da pilha de widgets para exibir a tela de busca de tarefa.

        Raises
        ------
        QMessageBox
            Se ocorrer um erro ao obter a lista de tarefas.
        """
        try:
            self.QtStack.setCurrentIndex(4)
            self.tela_buscar_tarefa.tableWidget.setRowCount(0) 

            mensagem = "abrir"
            cliente_socket.send(mensagem.encode())

            recebida = cliente_socket.recv(1024).decode()

            if recebida == '0':
                QMessageBox.information(self, "Buscar Tarefa", "Nenhuma tarefa encontrada.")
            else:
                lista = recebida.split(";")
                if lista:
                    for item in lista:
                        if item != "":
                            linha = self.tela_buscar_tarefa.tableWidget.rowCount()
                            self.tela_buscar_tarefa.tableWidget.insertRow(linha)
                            # Preencher cada coluna da linha com os valores da tarefa
                            valores = item.split(',')
                            for coluna, valor in enumerate(valores):
                                self.tela_buscar_tarefa.tableWidget.setItem(linha, coluna, QTableWidgetItem(str(valor)))
        except Exception as e:
            QMessageBox.critical(self, "Buscar Tarefa", f"Erro ao obter a lista de tarefas: {e}")
                  
    def cadastrar_tarefa(self):
        """
        Cadastra uma nova tarefa com base nos dados fornecidos.

        Envia os dados da nova tarefa para o servidor e exibe uma caixa de diálogo com o resultado do cadastro.

        Raises
        ------
        QMessageBox
            Se algum campo não for preenchido ou o formato do prazo for inválido.
        """
        try:
            titulo = self.tela_cadastro_tarefa.idtarefa_lineEdit.text()
            descricao = self.tela_cadastro_tarefa.descricao_textEdit.toPlainText()
            prazo = self.tela_cadastro_tarefa.prazo_lineEdit.text()

            if titulo and descricao and prazo:
                try:
                    datetime.strptime(prazo, "%Y-%m-%d")
                except ValueError:
                    QMessageBox(None).critical(self, 'Erro ao cadastrar a tarefa', 'Formato de prazo inválido! Utilize o formato "yyyy-mm-dd".')
                    return

                mensagem = f'cad_tarefa,{titulo},{descricao},{prazo}'
                cliente_socket.send(mensagem.encode())
                print('mensagem enviada')
                recebida = cliente_socket.recv(1024).decode()

                if recebida == '1':
                    QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    self.tela_cadastro_tarefa.idtarefa_lineEdit.setText('')
                    self.tela_cadastro_tarefa.descricao_textEdit.setPlainText('')
                    self.tela_cadastro_tarefa.prazo_lineEdit.setText('')

                elif recebida == '3':
                    QMessageBox(None).critical(self, 'Erro ao cadastrar a tarefa', 'Erro de integridade. Banco de Dados!')
                else:
                    QMessageBox(None).critical(self, 'Erro ao cadastrar a tarefa', 'Erro de conexão cliente-servidor!')

            else:
                QMessageBox(None).critical(self, 'Erro ao cadastrar a tarefa', 'Cadastro não realizado! Informe todos os campos.')
        except Exception as e:
            QMessageBox(None).critical(self, 'Erro ao cadastrar a tarefa', f'Erro ao cadastrar a tarefa: {str(e)}')

    def abrir_tela_login(self): 
        """
        Abre a tela de login.

        Altera o indice da pilha de widgets para exibir a tela de login.
        """
        self.QtStack.setCurrentIndex(0)

    def abrir_tela_inicial(self):
        """
        Abre a tela inicial.

        Altera o indice da pilha de widgets para exibir a tela inicial.
        """
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_cadastro_usuario(self):
        """
        Abre a tela de cadastro de usuario.

        Altera o indice da pilha de widgets para exibir a tela de cadastro de usuario.
        """
        self.QtStack.setCurrentIndex(2)

    def abrir_tela_cadastro_tarefa(self):
        """
        Abre a tela de cadastro de tarefa.

        Altera o indice da pilha de widgets para exibir a tela de cadastro de tarefa.
        """
        self.QtStack.setCurrentIndex(3)

    def abrir_funcoes_tarefa(self):
        """
        Abre a tela de funcoes de tarefa.

        Altera o indice da pilha de widgets para exibir a tela de funcoes de tarefa.
        """
        self.QtStack.setCurrentIndex(6)

    def sair(self):
        """
        Encerra a conexao do cliente com o servidor e fecha a aplicacao.

        Envia uma mensagem para o servidor indicando o encerramento da conexao.
        """
        try:
            mensagem = 'sair'
            cliente_socket.send(mensagem.encode())
            print('mensagem enviada')
            cliente_socket.close()
            print('ENCERRADO Conexao Cliente')
            sys.exit()
        except Exception as e:
            raise Exception(f"Erro ao encerrar a conexão com o servidor: {e}")
    
    def quantidade_tarefas_pendentes(self):
        """
        Recebe uma mensagem do servidor e exibe uma caixa de diálogo com a quantidade de tarefas pendentes.

        Essa função envia uma solicitação ao servidor para obter a quantidade de tarefas pendentes e exibe o resultado em uma caixa de diálogo personalizada.

        Returns:
        --------
        None
            O método não possui um valor de retorno especificado e, por padrão, retorna None.

        Raises:
        -------
        QMessageBox
            Se ocorrer algum erro ao obter a lista de tarefas pendentes.
        """
        try:
            # Mensagem do cliente
            mensagem = 'notificacao'
            cliente_socket.send(mensagem.encode())

            resposta = cliente_socket.recv(1024).decode()
            if resposta == '0':
                QMessageBox.warning(self, "Buscar Tarefa", "Erro ao obter a lista de tarefas.")
            else:
                valores = resposta.split(",")
                quantidade_tarefas = int(valores[0])
                vencimento_tarefas = valores[1:]

                # Criar uma caixa de diálogo personalizada
                dialog = QMessageBox(self)
                dialog.setWindowTitle("Notificação de Tarefas")  # Definir o título da caixa de diálogo

                # Criar um widget para adicionar o layout
                widget = QWidget(dialog)
                dialog.layout().addWidget(widget)

                # Criar um layout vertical para adicionar os widgets
                layout = QVBoxLayout(widget)

                # Adicionar um rótulo com a quantidade de tarefas pendentes
                label_quantidade = QLabel(f"Quantidade de Tarefas Pendentes: {quantidade_tarefas}")
                layout.addWidget(label_quantidade)

                # Criar uma área de rolagem para exibir as tarefas
                scroll_area = QScrollArea(dialog)
                scroll_area.setWidgetResizable(True)
                scroll_widget = QWidget(scroll_area)
                scroll_area.setWidget(scroll_widget)
                layout.addWidget(scroll_area)

                # Criar um layout vertical para adicionar os widgets de tarefas
                layout_tarefas = QVBoxLayout(scroll_widget)

                for i, vencimento_titulo in enumerate(vencimento_tarefas):
                    dias, titulo = vencimento_titulo.strip("[] ").split("|")
                    dias = int(dias)
                    if dias >= 0:
                        mensagem_tarefa = f"Tarefa {i+1} ({titulo}) - faltam {dias} dias"
                        estilo_tarefa = "QLabel { color: green; }"  # Estilo personalizado para tarefa pendente
                    else:
                        mensagem_tarefa = f"Tarefa {i+1} ({titulo}) - Vencida."
                        estilo_tarefa = "QLabel { color: red; }"  # Estilo personalizado para tarefa vencida

                    # Criar um rótulo com a mensagem da tarefa
                    label_tarefa = QLabel(mensagem_tarefa)
                    label_tarefa.setStyleSheet(estilo_tarefa)
                    layout_tarefas.addWidget(label_tarefa)

                # Ajustar o tamanho da caixa de diálogo
                dialog.adjustSize()

                # Exibir a caixa de diálogo personalizada
                dialog.exec_()
        except Exception as e:
            QMessageBox.information(None, 'interface', f'Erro: {str(e)}')

    def cadastrar_usuario(self):
        """
        Cadastra um novo usuario com base nos dados fornecidos.

        Envia os dados do novo usuario para o servidor e exibe uma caixa de dialogo com o resultado do cadastro.

        Raises
        ------
        QMessageBox
            Se algum campo nao for preenchido.
        """
        try:
            nome = self.tela_cadastro_usuario.nome_lineEdit.text()
            email = self.tela_cadastro_usuario.email_lineEdit.text()
            username = self.tela_cadastro_usuario.username_lineEdit.text()
            senha = self.tela_cadastro_usuario.password_lineEdit.text()

            if not (nome == '' or email == '' or username == '' or senha == ''):
                mensagem = f'cad_usuario,{nome},{username},{email},{senha}'
                cliente_socket.send(mensagem.encode())
                print('mensagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                if recebida == '1':
                    QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    self.tela_cadastro_usuario.nome_lineEdit.setText('')
                    self.tela_cadastro_usuario.email_lineEdit.setText('')
                    self.tela_cadastro_usuario.username_lineEdit.setText('')
                    self.tela_cadastro_usuario.password_lineEdit.setText('')
                elif recebida == '0':
                    QMessageBox.information(None, 'interface', 'ID ja cadastrado!')
                else:
                    raise QMessageBox("interface", 'Erro de conexao cliente-servidor!')
            else:
                raise QMessageBox(None, 'interface', 'Cadastro nao realizado! Informe todos os campos.')
        except Exception as e:
            raise QMessageBox(None, 'interface', f'Erro ao cadastrar o usuário: {str(e)}')

    def excluir_tarefa_linha(self):
        """
        Exclui uma tarefa com base no item selecionado na lista.

        Obtém o item selecionado na lista e envia uma solicitação ao servidor para excluir a tarefa. Exibe o resultado da exclusão.

        Raises
        ------
        QMessageBox
            Se nenhum item for selecionado ou ocorrer um erro durante a exclusão.
        """
        try:
            item_selecionado = self.tela_ativar_tarefa.campo_list_widget.currentItem()

            if item_selecionado is not None:
                id_tarefa = item_selecionado.text().split(" - ")[0]
                mensagem = f"excluir_tarefa,{id_tarefa}"
                cliente_socket.send(mensagem.encode())

                recebida = cliente_socket.recv(1024).decode()
                if recebida == '1':
                    self.tela_ativar_tarefa.campo_list_widget.takeItem(self.tela_ativar_tarefa.campo_list_widget.row(item_selecionado))
                    QMessageBox.information(self, "Excluir Tarefa", "Tarefa excluída com sucesso!")
                else:
                    QMessageBox.warning(self, "Excluir Tarefa", "Erro ao excluir a tarefa.")
            else:
                QMessageBox.warning(self, "Excluir Tarefa", "Selecione uma tarefa para excluí-la.")
        except Exception as e:
            QMessageBox.warning(self, "Excluir Tarefa", f"Erro ao excluir a tarefa: {e}")

    def concluir_tarefa_linha(self):
        """
        Conclui uma tarefa com base no item selecionado na lista.

        Envia uma solicitação ao servidor para concluir a tarefa selecionada na lista de busca de tarefas. Exibe o resultado da conclusão.

        Raises
        ------
        QMessageBox
            Se nenhum item for selecionado ou ocorrer um erro durante a conclusão.
        """
        try:
            item_selecionado = self.tela_buscar_tarefa.campo_list_widget.currentItem()

            if item_selecionado is not None:
                id_tarefa = item_selecionado.text().split(" - ")[0]
                mensagem = f"concluir_tarefa,{id_tarefa}"
                cliente_socket.send(mensagem.encode())

                recebida = cliente_socket.recv(1024).decode()
                if recebida == '1':
                    QMessageBox.information(self, "Concluir Tarefa", "Tarefa concluída com sucesso!")
                    self.tela_buscar_tarefa.campo_list_widget.takeItem(self.tela_buscar_tarefa.campo_list_widget.currentRow())
                else:
                    QMessageBox.warning(self, "Concluir Tarefa", "Erro ao concluir a tarefa.")
            else:
                QMessageBox.warning(self, "Concluir Tarefa", "Selecione uma tarefa para concluí-la.")
        except Exception as e:
            QMessageBox.warning(self, "Concluir Tarefa", f"Erro ao concluir a tarefa: {e}")

    def reativar_tarefa_linha(self):
        """
        Reativa uma tarefa com base no item selecionado na lista.

        Envia uma solicitação ao servidor para reativar a tarefa selecionada na lista de tarefas ativas. Exibe o resultado da reativação.

        Raises
        ------
        QMessageBox
            Se nenhum item for selecionado ou ocorrer um erro durante a reativação.
        """
        try:
            item_selecionado = self.tela_ativar_tarefa.campo_list_widget.currentItem()

            if item_selecionado is not None:
                id_tarefa = item_selecionado.text().split(" - ")[0]
                mensagem = f"reativar_tarefa,{id_tarefa}"
                cliente_socket.send(mensagem.encode())

                recebida = cliente_socket.recv(1024).decode()
                if recebida == '1':
                    QMessageBox.information(self, "Reativar Tarefa", "Tarefa reativada com sucesso!")
                    self.tela_ativar_tarefa.campo_list_widget.takeItem(self.tela_ativar_tarefa.campo_list_widget.currentRow())
                else:
                    QMessageBox.warning(self, "Reativar Tarefa", "Erro ao reativar a tarefa.")
            else:
                QMessageBox.warning(self, "Reativar Tarefa", "Selecione uma tarefa para reativá-la.")
        except Exception as e:
            QMessageBox.warning(self, "Reativar Tarefa", f"Erro ao reativar a tarefa: {e}")

    def editar_tarefa_linha(self, item):
        """
        Abre um dialogo para editar as informacoes de uma tarefa selecionada.

        Este metodo e acionado quando o usuario clica em uma tarefa na interface grafica e seleciona a opcao de editar.

        Parameters:
        ----------
        item : QTreeWidgetItem
            O item da arvore que representa a tarefa selecionada.

        Raises:
        -------
        Exception
            Se ocorrer algum erro ao editar a tarefa.
        """
        try:
            # Extrair as informações do item selecionado
            id_tarefa, titulo, descricao, prazo = item.text().split(" - ")

            # Exibir um diálogo para o usuário editar a descrição e o prazo
            titulo_editado, ok = QInputDialog.getText(self, "Editar Tarefa", "Editar título da tarefa:", QLineEdit.Normal, titulo)
            if ok:
                descricao_editada, ok = QInputDialog.getText(self, "Editar Tarefa", "Editar descrição da tarefa:", QLineEdit.Normal, descricao)
                if ok:
                    prazo_editado, ok = QInputDialog.getText(self, "Editar Tarefa", "Editar prazo da tarefa:", QLineEdit.Normal, prazo)
                    if ok:
                        # Separar a descrição, o título e o prazo editados
                        novo_titulo, nova_descricao, novo_prazo = titulo_editado.strip(), descricao_editada.strip(), prazo_editado.strip()

                        # Chamar a função para atualizar a tarefa
                        if self.atualizar_tarefa(id_tarefa, novo_titulo, nova_descricao, novo_prazo):
                            QMessageBox.information(self, "Editar Tarefa", "Tarefa atualizada com sucesso!")
                            self.abrir_tela_buscar_tarefa()  # Atualizar o campo list widget após a atualização da tarefa
                        else:
                            QMessageBox.warning(self, "Editar Tarefa", "Erro ao atualizar a tarefa.")
        except Exception as e:
            QMessageBox.warning(self, "Editar Tarefa", f"Erro ao editar a tarefa: {e}")

    def atualizar_tarefa(self, id_tarefa, novo_titulo, nova_descricao, novo_prazo):
        """
        Atualiza uma tarefa existente no banco de dados.

        Este metodo envia uma mensagem para o servidor contendo a solicitacao de atualizacao da tarefa, juntamente com as novas informacoes.

        Parameters:
        ----------
        id_tarefa : int
            O ID da tarefa a ser atualizada.
        novo_titulo : str
            O novo título da tarefa.
        nova_descricao : str
            A nova descrição da tarefa.
        novo_prazo : str
            O novo prazo da tarefa.

        Returns:
        -------
        bool
            True se a tarefa foi atualizada com sucesso, False caso contrario.

        Raises:
        -------
        Exception
            Se ocorrer algum erro ao atualizar a tarefa.
        """
        try:
            mensagem = f"atualizar_tarefa,{id_tarefa},{novo_titulo},{nova_descricao},{novo_prazo}"
            cliente_socket.send(mensagem.encode())
            recebida = cliente_socket.recv(1024).decode()
            if recebida == "1":
                return True
            else:
                return False
        except Exception as e:
            print(f"Erro ao atualizar a tarefa: {e}")
            return False

    def loginUser(self):
        """
        Realiza o login do usuario com base nos dados fornecidos.

        Envia os dados de login para o servidor e exibe uma caixa de dialogo com o resultado do login.

        Raises
        ------
        QMessageBox
            Se algum campo nao for preenchido.
        """
        username =  self.tela_login.cpf_lineEdit.text()
        senha = self.tela_login.senha_lineEdit.text()

        if not(username=='' or senha==''):
            # menssagem do cliente
            try:
                menssagem =  f'usuario,{username},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    self.abrir_tela_inicial()
                    # limpar os dados
                    self.tela_login.cpf_lineEdit.text()
                    senha = self.tela_login.senha_lineEdit.text()
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ou Senha inválidos! Nenhum Usuario cadastrado com esses campos!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                cliente_socket.close()
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Informe todos os campos para fazer o Login')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())