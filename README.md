# Gerenciador de tarefas
Gerenciador de tarefas em Django

Serviços necessários:
- Python >= 3.3

# Steps para utilizar o projeto
Steps para configura-lo no windows

## Clonando repositório
```sh
git clone https://github.com/VStahelin/gerenciador-de-tarefas.git  
```

## Configurando settings.py do Django 
Projeto/  
├─ gerenciador/  
│⠀⠀└─ gerenciador/  
│⠀⠀⠀⠀└─ settings.py  


Primeiro vamos configurar o banco de dados, neste projeto esta configurado para
MySql, caso utilize outro sera mesário atualizar o projeto com o respectivo
Modulo do seu banco de dados.

### Em de DATABASES:   
```NAME``` sera atribuído o nome do banco de dados  
```USER``` sera atribuído o usuario  
```PASSWORD``` sera atribuído a sua respectiva senha  
```HOST``` sera atribuído o domínio do seu banco de dados (localhost no nosso caso)  
```PORT``` sera atribuído a para acessar o banco de dados

#### Exemplo
Atualmente esta configurado assim
``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gerenciador',
        'USER': 'root',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Em LANGUAGE_CODE
Esta variável define qual a linguagem padrão da sua aplicação  
[Confira os códigos de linguagem](http://www.i18nguy.com/unicode/language-identifiers.html)

#### Exemplo
``` 
LANGUAGE_CODE = 'pt-br'
```

### Em TIME_ZONE
Esta variável define qual fuso horário que a aplicação deve se basear  
[Confira as zonas suportadas](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568)

#### Exemplo
``` 
TIME_ZONE = 'America/Sao_Paulo'
```

## Criando ambiente virtual
Dentro da pasta do projeto
```sh
mkdir venv
python -m venv venv/
```

Para ativar o ambiente virtual
```sh
source venv/Scripts/activate
```
Para desativar o ambiente virtual
```sh
deactivate
```

Projeto/  
├─ Venv/  
│⠀⠀├─ Include/  
│⠀⠀├─ Lib/  
│⠀⠀└─ Scripts/  
|⠀⠀⠀⠀⠀└─ activate


## Instalando dependências
Dentro da pasta do projeto
```sh
pip3 install -r requirements.txt
python manage.py migrate
```


## Atualizando ambiente do Django 
Projeto/  
├─ gerenciador/  
│⠀⠀└─ manage.py  


### Aplicando migrações 
Dentro da pasta "gerenciador" 
```sh
python manage.py makemigrations
python manage.py migrate
```

### Startando a aplicação
Sempre usando o ambiente virtual
```sh
python manage.py runserver
```

Observação: O app sera acessível pela porta 8000
Exemplo:
```
http://127.0.0.1:8000/
```
