# Gerenciador de tarefas
Gerenciador de tarefas em Django

Servicos necessarios:
- Python >= 3.3  
- Git  

# Steps para utilizar o projeto
Steps para configuralo no windows

## Clonando repositorio
```sh
git clone https://github.com/VStahelin/gerenciador-de-tarefas.git  
```

## Configurando settings.py do Django 
Projeto/  
├─ gerenciador/  
│⠀⠀└─ gerenciador/  
│⠀⠀⠀⠀└─ settings.py  


Primeiro vamos configurar o banco de dados, neste projeto esta configurado para
MySql, caso utilize outro sera nessario atualizar o porjeto com o modulo 
respectivo do seu banco de dados.

### Em de DATABASES:   
```NAME``` sera atribuido o nome do banco de dados  
```USER``` sera atribuido o usuario  
```PASSWORD``` sera atribuido a sua respectiva senha  
```HOST``` sera atribuido o dominio do seu banco de dados (localhost no nosso caso)  
```PORT``` sera atribuido a para acessar o banco de dados

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
Esta variavel define qual a linguagem padrao da sua aplicacao  
[Confira os codigos de linguaguem](http://www.i18nguy.com/unicode/language-identifiers.html)

#### Exemplo
``` 
LANGUAGE_CODE = 'pt-br'
```

### Em TIME_ZONE
Esta variavel define qual fuso horario que a aplicacao deve se basear  
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


## Instalando dependencias
Dentro da pasta do projeto
```sh
pip3 install -r requirements.txt
python manage.py migrate
```


## Atualizando ambiente do Django 
Projeto/  
├─ gerenciador/  
│⠀⠀└─ manage.py  


### Aplicando migracoes 
Dentro da pasta "gerenciador" 
```sh
python manage.py makemigrations
python manage.py migrate
```

### Startando a aplicacao
Sempre usando o ambiente virtual
```sh
python manage.py runserserver
```