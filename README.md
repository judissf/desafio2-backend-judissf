# DESAFIO 2 - BACKEND

# # Sobre o projeto:

O projeto consiste num sistema que recebe um arquivo CNAB (o qual contém informações de transações/movimentações bancárias que empresas e bancos costumam utilizar para manipular dados financeiros), realiza a interpretação dos dados e salva as informações em um banco de dados. Além disso, as informações também podem ser consultadas e o usuário pode conferir os dados.

# # # Tecnologias utilizadas:
- Python
- Django
- Django Rest Framework

# # # Instruções para instalação e execução em ambiente de desenvolvimento (Windows):

1. Instale o ambiente virtual em seu computador utilizando o comando "python -m venv venv"
2. Execute o ambiente virtual ".\venv\Scripts\activate"
3. Instale os pacotes necessários para funcionar o projeto "pip install -r requirements.txt"
4. Exectue as migrations do projeto "python manage.py migrate"
5. Por fim, para execução do projeto use "python manage.py runserver"
6. A url para requisições é "http://127.0.0.1:8000/api/file"

# # # Instruções para instalação e execução em ambiente de desenvolvimento (Linux):

1. Instale o ambiente virtual em seu computador utilizando o comando "python -m venv venv"
2. Execute o ambiente virtual "source venv/bin/activate"
3. Instale os pacotes necessários para funcionar o projeto "pip install -r requirements.txt"
4. Exectue as migrations do projeto "python manage.py migrate"
5. Por fim, para execução do projeto use "python manage.py runserver"
6. A url para requisições é "http://127.0.0.1:8000/api/file"
