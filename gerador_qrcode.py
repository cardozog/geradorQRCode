import qrcode
from tkinter import * 
from tkinter.filedialog import askdirectory


def directory():
    # diretorio selecionado pelo usuario
    global filepath 
    filepath= askdirectory(title="Salvar QRCode")
    entradaCaminho = Label(janela,width=55,text=filepath,bg="#ECECEC")
    entradaCaminho.grid(column=1, row=2, padx=0, pady=5)
    return filepath

def criarQR():

    nomeArquivo = nome.get()
    if (nomeArquivo=="" ||nomeArq):
        print('uauuu')
    codigo = qrcode.make(link.get())
    codigo.save("teste.jpg")

texto= str

janela = Tk()
janela.title("Validar resposta")
janela.geometry("640x320")
janela.resizable(0,0)
janela.configure(bg="#ECECEC")

#LINK
#   label
labelLink= Label(janela, text="Link",bg="#ECECEC",fg="black",font=("11"))
labelLink.grid(column=0, row=0, padx=15, pady=5)


#   input
link = StringVar()
entradaLink = Entry(janela,textvariable=link,width=60)
entradaLink.grid(column=1, row=0, padx=5, pady=5)

#NOME DO ARQUIVO
#   label
labelNome = Label(janela, text="Nome do arquivo",bg="#ECECEC",fg="black",font=("7"))
labelNome.grid(column=0, row=1, padx=0, pady=5)
#   input
nome =StringVar()
entradaNome = Entry(janela,textvariable=nome,width=55)
entradaNome.grid(column=1, row=1, padx=0, pady=5)

#LOCAL A SER SALVO
#   label
#labelSalvar= Label(janela, text="Salvar em: ",bg="#ECECEC",fg="black",font=("11"))
#labelSalvar.grid(column=0, row=2, padx=15, pady=5)

#   BOTAO CAMINHO
#botaoCaminho = Button(janela, text="Salvar...",command=directory(teste))
#botaoCaminho.grid(column=2, row=2, padx=0, pady=5)

# BOTAO CRIAR QR CODE
botaoCriar = Button(janela,height=2,width=35,text="Criar QR Code",command=criarQR)
botaoCriar.grid(column=1, row=3, padx=0, pady=5)

janela.mainloop()
