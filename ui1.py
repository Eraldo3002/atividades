import tkinter as tk

def salvar_nome():
    nome = entry_nome.get()
    endereco = entry_endereco.get()

    if nome and endereco:
        with open ("nomes.txt","a") as arquivo:
            arquivo.write(f"Nome: {nome} | endereço: {endereco}\n")
                          
        label_status.config(text=f'nome "{nome}" salvo com sucesso', fg="green")
    else:
        label_status.config(text="Digite um nome.", fg="read")
root = tk.Tk()
root.title("Nomes")
root.geometry("300x200")

label_instrucao = tk.Label(root, text="digite um nome:")
label_instrucao.pack(pady=10)

entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

label_instrucao2 = tk.Label(root, text="digite seu enderço:")
label_instrucao2.pack(pady=10)

entry_endereco =  tk.Entry(root)
entry_endereco.pack(pady=5)

botao_salvar = tk.Button(root, text="salvar", command=salvar_nome)
botao_salvar.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)
root.mainloop()