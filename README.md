# Django List

Este repositório contém um projeto simples desenvolvido com o framework Django para praticar a criação de aplicações web. O projeto consiste em uma página com um formulário para registro de tarefas e outra página com uma tabela de listagem das tarefas.

## Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- SQLite (banco de dados padrão do Django)
- HTML/CSS (para a interface básica)
- Django Crispy Forms (para facilitar a estilização de formulários)
- Bulma (framework CSS para estilização da interface)

## Como Clonar e Configurar o Projeto

### 1. Clonar o Repositório
```bash
# Via HTTPS
git clone https://github.com/seu-usuario/django-list.git

# Via SSH
git clone git@github.com:seu-usuario/django-list.git
```

### 2. Acessar o Diretório do Projeto
```bash
cd django-list
```

### 3. Criar e Ativar um Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente no Windows
venv\Scripts\activate

# Ativar ambiente no macOS/Linux
source venv/bin/activate
```

### 4. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 5. Configurar o Banco de Dados
```bash
python manage.py migrate
```

### 6. Criar um Superusuário (Opcional)
Se desejar acessar o painel administrativo do Django, crie um superusuário:
```bash
python manage.py createsuperuser
```

### 7. Executar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```
A aplicação estará disponível em `http://127.0.0.1:8000/`


## Contribuição
Caso queira contribuir com melhorias, sinta-se à vontade para abrir um Pull Request ou sugerir melhorias na aba de Issues.

## Licença
Este projeto está sob a licença MIT. Sinta-se livre para utilizá-lo e modificá-lo conforme necessário.

