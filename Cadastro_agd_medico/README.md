# 🏥 Agenda Médica - Django + Tkinter e Banco de Dados. 

## Descrição: 

A Agenda Médica é uma aplicação desenvolvida com Django e Tkinter para realizar o cadastro de médicos, pacientes e agendamento de consultas. Ela une um backend robusto com o Django e uma interface gráfica simples usando Tkinter, permitindo uma experiência prática e funcional para pequenos consultórios ou aprendizado de desenvolvimento full-stack com Python.

## 🧠 Funcionalidades: 

Interface Gráfica com Tkinter: Tela amigável que facilita a interação com os dados cadastrados.

Cadastro de Médicos: Nome e especialização dos profissionais de saúde.

Cadastro de Pacientes: Nome e data de nascimento.

Agendamento de Consultas: Associação entre médicos e pacientes, com data e hora marcadas.

Listagens Dinâmicas: Todos os dados cadastrados são exibidos em tabelas de fácil leitura com atualizações em tempo real.

## 💻 Tecnologias Usadas: 

Backend: Django 4.x

Frontend (Interface Gráfica): Tkinter

Banco de Dados: MySQL WorkBanch.

Outras bibliotecas: datetime, os, ttk, messagebox

## 🚀 Como Executar o Projeto
**1. Clone o repositório:**
git clone https://github.com/seu-usuario/agenda-medica.git 
**2. Crie e ative um ambiente virtual (recomendado):**
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate 
**3. Instale as dependências:**
pip install django
**4. Execute as migrações do Django:**
python manage.py makemigrations
python manage.py migrate
**5. Crie um superusuário para acessar o admin (opcional):**
python manage.py createsuperuser
**6. Inicie o servidor para testar o backend (opcional):**
python manage.py runserver
**7. Execute o sistema com interface gráfica:**
python app_tkinter.py 

## 🧑‍💻 Sobre o Projeto:
Este projeto foi criado com o objetivo de integrar os conhecimentos de backend com Django e frontend com Tkinter. É um exemplo prático de como é possível unir uma interface gráfica tradicional com um ORM robusto para aplicações desktop que utilizam banco de dados.

## 📌 Como Funciona: 
**Modelos (Django):**
Medico: nome, especialização.

Paciente: nome, data de nascimento.

ConsultaMarcada: médico, paciente, data/hora da consulta.

**Interface com Tkinter:**
Menu superior com navegação entre telas (médicos, pacientes, consultas).

Formulários para inserção dos dados.

Tabelas para visualização imediata das informações cadastradas.

Validação de campos e feedback ao usuário via messagebox.

**Funcionalidade Extra:**
Formato de data e hora para agendamento: dd/mm/aaaa HH:MM.


## 💬 Contato:
Para dúvidas, sugestões ou colaborações:

Email: [eraldoalves715@gmail.com]

LinkedIn: https://www.linkedin.com/in/eraldo-alves-filho 

## 👌 Considerações finais:
Este projeto serve como uma base sólida para aplicações desktop com persistência de dados usando Django e interface gráfica com Tkinter. Ideal para fins educacionais, testes em clínicas locais ou aprendizado de desenvolvimento Python completo.

Obrigado por acessar! 🚀

