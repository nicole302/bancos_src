from tkinter import *
import services

def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.enviar_dados(nome, email, senha)

        # Para limpar os campos

        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        senhaEntry.delete(0, END)

    def listar_usuario():
        usuarios = services.listar_usuario()

        #criar uma janela para mostrar a lista de usuario
        janela_listar = Toplevel(janela)
        janela_listar.title('Lista de Usuarios')
        janela_listar.geometry('600x300')

        #criar uma Treeview (view, visualizacão) da lista de usuario, show='headings para limpar o cabeçalho
        tree = Tk.Treeview(janela_listar, columns=('ID', 'Nome', 'Email'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')
    
    #criar botao de voltar que iras fechar a tela de lista de usuario
        voltar = Button(janela_listar, text='Voltar', width=10, command=janela_listar.detroy)
        voltar.pack(fill=BOTH, expand=True, side=BOTTOM)
    
        tree.pack(fill=BOTH, expand=True)
    
        #inserir os daods dos usuarios na Treeview
        for usuario in usuario:
            # END vai inserir o item no final da tabela
            tree.insert

    janela = Tk()
    janela.geometry('400x300')
    janela.title('Sistema de Gerenciamento de Usuário')


    titulo = Label(janela, text='CRUD', font=('Arial', 20))
    titulo.pack(pady=30)

    # Componentes de entrada
    # Nome
    nome = Label(janela, text='Nome:')
    nome.place(x=50, y=100)

    global nomeEntry  
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=100, y=100)

    # Email
    email = Label(janela, text='Email:')
    email.place(x=50, y=130)

    global emailEntry
    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=100, y=100)

    # Senha
    senha = Label(janela, text='Senha:')
    senha.place(x=50, y=160)

    # comando shor para esconder a senha
    global senhaEntry
    senhaEntry = Entry(janela, width=30, show='*')
    senhaEntry.place(x=50, y=160)


    enviar = Button(janela, text='Cadastrar', width=10, command= on_enviar)
    enviar.place(x=100, y=200)

    listar = Button(janela, text ='Listar Usuarios', width=15, command=listar_usuario)
    listar.place(x=200, y=200)

    janela.mainloop()

    if __name__== '_main_':
      main()




