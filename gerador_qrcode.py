import os
import qrcode
from tkinter import * 
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror,showinfo

def center(win):
    # :param win: the main window or Toplevel window to center

    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    win.update_idletasks()  # Update "requested size" from geometry manager

    # define window dimensions width and height
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Get the window position from the top dynamically as well as position from left or right as follows
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()




def directory():

    # diretorio selecionado pelo usuario
    filepath= askdirectory(title="Selecione a pasta: ")
    if filepath =="":
        return
    return filepath

def criarQR():
    
    nomeArquivo = nome.get()
    if (nomeArquivo=="" or nomeArquivo ==" "):
        showerror("ERRO","Insira um nome válido no nome do arquivo")
    else:
        rota = directory()
        if rota !=None:
            rotaNova = rota+"/"+nomeArquivo+".jpg"
            if (rota ==None):
                showerror("ERRO","Insira um nome válido no nome do arquivo")
            else:
                qr=qrcode.make(link.get())
                if(os.path.exists(rotaNova)==False):
                    qr.save(rotaNova)
                    showinfo("QR Code","QR Code criado com sucesso!")
                else:
                    showerror("ERRO","Arquivo já existente, escolha outro nome!")

    

janela = Tk()
janela.title("Gerador de QRCode ")
janela.iconbitmap(None)
janela.geometry("640x200")
janela.resizable(0,0)
janela.configure(bg="#ECECEC")
center(janela)

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
labelNome.grid(column=0, row=1, padx=5, pady=5)
#   input
nome =StringVar()
entradaNome = Entry(janela,textvariable=nome,width=55)
entradaNome.grid(column=1, row=1, padx=5, pady=5)

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
