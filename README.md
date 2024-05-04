# meu primeiro projeto Django
esse é o meu primeiro projeto Django, que aborda as bases do framework

## instrução para baixar, editar e executar local
1. clone o projeto
```bash
git clone https://github.com/cassio-ksim/projeto1.git
```
2. entre na pasta do projeto e crie um ambiente vitual python   
```bash
cd projeto1
```
```bash
python -m venv .venv
```
3. ative o ambiente virtual no windows:
```bash
.venv\Scripts\activate
```
no Linux:
```bash
source .venv/bin/activate
```
4. instale as dependencias 
```bash
pip install -r requirements-dev.txt
```
5. execute as migrações 
```bash
python manage.py migrate
```
6. execute o servidor
```bash
python manage.py runserver
```