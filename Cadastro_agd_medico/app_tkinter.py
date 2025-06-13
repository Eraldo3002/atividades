import os
import django
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime  # Correção aqui

# Configura o Django para usar seus models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AtendMedic.settings")
django.setup()

from AtendimentoMed.models import Medico, Paciente, ConsultaMarcada

class AgendaMedicaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda Médica")
        self.geometry("700x500")

        # Menu
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Menu Navegação
        nav_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Navegação", menu=nav_menu)
        nav_menu.add_command(label="Médicos", command=self.mostrar_medicos)
        nav_menu.add_command(label="Pacientes", command=self.mostrar_pacientes)
        nav_menu.add_command(label="Consultas", command=self.mostrar_consultas)

        # Menu Ajuda
        ajuda_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=ajuda_menu)
        ajuda_menu.add_command(label="Sobre", command=self.sobre)

        # Frame principal para trocar as telas
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

    def limpar_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def mostrar_medicos(self):
        self.limpar_frame()
        ttk.Label(self.frame, text="Cadastro de Médicos", font=("Arial", 16)).pack(pady=10)

        form_frame = ttk.Frame(self.frame)
        form_frame.pack(pady=10)

        ttk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        nome_entry = ttk.Entry(form_frame, width=30)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Especialização:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        esp_entry = ttk.Entry(form_frame, width=30)
        esp_entry.grid(row=1, column=1, padx=5, pady=5)

        def salvar_medico():
            nome = nome_entry.get().strip()
            esp = esp_entry.get().strip()
            if not nome or not esp:
                messagebox.showerror("Erro", "Preencha todos os campos")
                return
            Medico(nome=nome, especializacao=esp).save()
            messagebox.showinfo("Sucesso", f"Médico {nome} salvo!")
            nome_entry.delete(0, tk.END)
            esp_entry.delete(0, tk.END)
            listar_medicos()

        salvar_btn = ttk.Button(form_frame, text="Salvar", command=salvar_medico)
        salvar_btn.grid(row=2, column=0, columnspan=2, pady=10)

        tree = ttk.Treeview(self.frame, columns=("Nome", "Especialização"), show="headings")
        tree.heading("Nome", text="Nome")
        tree.heading("Especialização", text="Especialização")
        tree.pack(fill=tk.BOTH, expand=True, pady=10)

        def listar_medicos():
            for i in tree.get_children():
                tree.delete(i)
            for m in Medico.objects.all():
                tree.insert("", tk.END, values=(m.nome, m.especializacao))

        listar_medicos()

    def mostrar_pacientes(self):
        self.limpar_frame()
        ttk.Label(self.frame, text="Cadastro de Pacientes", font=("Arial", 16)).pack(pady=10)

        form_frame = ttk.Frame(self.frame)
        form_frame.pack(pady=10)

        ttk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        nome_entry = ttk.Entry(form_frame, width=30)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Data de Nascimento").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        dtNas_entry = ttk.Entry(form_frame, width=30)
        dtNas_entry.grid(row=1, column=1, padx=5, pady=5)

        def salvar_pacientes():
            nome = nome_entry.get().strip()
            dtNas = dtNas_entry.get().strip()
            if not nome or not dtNas:
                messagebox.showerror("Erro", "Preencha todos os campos")
                return
            Paciente(nome=nome, data_nascimento=dtNas).save()
            messagebox.showinfo("Sucesso", f"Paciente {nome} salvo!")
            nome_entry.delete(0, tk.END)
            dtNas_entry.delete(0, tk.END)
            listar_pacientes()

        salvar_btn = ttk.Button(form_frame, text="Salvar", command=salvar_pacientes)
        salvar_btn.grid(row=2, column=0, columnspan=2, pady=10)

        tree = ttk.Treeview(self.frame, columns=("Nome", "Data de Nascimento"), show="headings")
        tree.heading("Nome", text="Nome")
        tree.heading("Data de Nascimento", text="Data de Nascimento")
        tree.pack(fill=tk.BOTH, expand=True, pady=10)

        def listar_pacientes():
            for i in tree.get_children():
                tree.delete(i)
            for m in Paciente.objects.all():
                tree.insert("", tk.END, values=(m.nome, m.data_nascimento))

        listar_pacientes()

    def mostrar_consultas(self):
        self.limpar_frame()
        ttk.Label(self.frame, text="Agendamento de Consultas", font=("Arial", 16)).pack(pady=10)

        form_frame = ttk.Frame(self.frame)
        form_frame.pack(pady=10)

        ttk.Label(form_frame, text="Médico:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        medicos = list(Medico.objects.all())
        medico_names = [m.nome for m in medicos]
        medico_var = tk.StringVar()
        medico_combo = ttk.Combobox(form_frame, textvariable=medico_var, values=medico_names, state="readonly")
        medico_combo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Paciente:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        pacientes = list(Paciente.objects.all())
        paciente_names = [p.nome for p in pacientes]
        paciente_var = tk.StringVar()
        paciente_combo = ttk.Combobox(form_frame, textvariable=paciente_var, values=paciente_names, state="readonly")
        paciente_combo.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Data e Hora (dd/mm/aaaa HH:MM):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        dt_hora_entry = ttk.Entry(form_frame, width=30)
        dt_hora_entry.grid(row=2, column=1, padx=5, pady=5)

        def salvar_consulta():
            medico_nome = medico_var.get()
            paciente_nome = paciente_var.get()
            dt_hora_str = dt_hora_entry.get().strip()

            if not medico_nome or not paciente_nome or not dt_hora_str:
                messagebox.showerror("Erro", "Preencha todos os campos")
                return

            try:
                dt_hora = datetime.strptime(dt_hora_str, "%d/%m/%Y %H:%M")
            except ValueError:
                messagebox.showerror("Erro", "Data e hora inválidas. Use o formato dd/mm/aaaa HH:MM")
                return

            medico_obj = next((m for m in medicos if m.nome == medico_nome), None)
            paciente_obj = next((p for p in pacientes if p.nome == paciente_nome), None)

            if not medico_obj or not paciente_obj:
                messagebox.showerror("Erro", "Médico ou paciente não encontrado")
                return

            ConsultaMarcada(medico=medico_obj, paciente=paciente_obj, data_hora=dt_hora).save()
            messagebox.showinfo("Sucesso", "Consulta agendada!")
            dt_hora_entry.delete(0, tk.END)
            listar_consultas()

        salvar_btn = ttk.Button(form_frame, text="Agendar Consulta", command=salvar_consulta)
        salvar_btn.grid(row=3, column=0, columnspan=2, pady=10)

        tree = ttk.Treeview(self.frame, columns=("Médico", "Paciente", "Data e Hora"), show="headings")
        tree.heading("Médico", text="Médico")
        tree.heading("Paciente", text="Paciente")
        tree.heading("Data e Hora", text="Data e Hora")
        tree.pack(fill=tk.BOTH, expand=True, pady=10)

        def listar_consultas():
            for i in tree.get_children():
                tree.delete(i)
            for c in ConsultaMarcada.objects.select_related('medico', 'paciente').all():
                dt_str = c.data_hora.strftime("%d/%m/%Y %H:%M") if c.data_hora else ""
                tree.insert("", tk.END, values=(c.medico.nome, c.paciente.nome, dt_str))

        listar_consultas()

    def sobre(self):
        messagebox.showinfo("Sobre",
               "Integrantes: Arthur Vieira Arruda De Oliveira\n"
               "Projeto: Agenda Médica\n"
               "Descrição: Sistema para cadastro de médicos, pacientes e agendamento de consultas.")

if __name__ == "__main__":
    app = AgendaMedicaApp()
    app.mainloop()