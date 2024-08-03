
# Comandos antes de iniciar o dev diario

## iniciar poetry
Se não entrar automaticamente no env
catalunha@pop-os:~/apps/proclinicakids.com.br/fluxus5api$ 
poetry shell

## restartar os servicos do docker compose
(fluxus5api-py3.11) catalunha@pop-os:~/myapp/proclinicakids/fluxus5api/z/docker-fluxus5$
cd z/docker-fluxus5/ && docker compose restart && cd ../..

## ativar servidos
(fluxus5api-py3.11) catalunha@pop-os:~/myapp/proclinicakids/fluxus5api$
python manage.py runserver 192.168.10.117:8000
192.168.10.117:8000

## acessar admin ou recriar senha
(fluxus5api-py3.11) catalunha@pop-os:~/apps/proclinicakids.com.br/fluxus5api$ 
python manage.py changepassword admin@gmail.com

senha atual da conta admin@gmail.com é: django@123

## aplicar migrações
(fluxus5api-py3.11) catalunha@pop-os:~/myapp/proclinicakids/fluxus5api$
python manage.py makemigrations; python manage.py migrate

# Users
## Super User
admin@gmail.com
django@123

## user 1
catalunha.mj@gmail.com
cat@1234

# Comandos após finalizar o tempo de dev diario

## Listar os servicos ativos
(fluxus5api-py3.11) catalunha@pop-os:~/myapp/proclinicakids/fluxus5api/z/docker-fluxus5$
docker compose ls

## Stop os servicos ativos deste projeto
(fluxus5api-py3.11) catalunha@pop-os:~/myapp/proclinicakids/fluxus5api/z/docker-fluxus5$
docker compose stop


# Recriando ambientes

## Criar containers
Arquivo de docker-compose.yml ja construido. O nome da pasta dá o nome do projeto no docker.
(fluxus5api-py3.11) catalunha@pop-os:~/myapp/proclinicakids/fluxus5api/z/docker-fluxus5$
docker compose up -d

## Dump dos dados remotos
(fluxus5api-py3.11) catalunha@pop-os:~/myapp/proclinicakids/fluxus5api/z/docker-fluxus5$
pg_dump -h db-fluxus-do-user-7515641-0.c.db.ondigitalocean.com -p 25060 -U fluxususer -W -Fp fluxusdb > fluxusdb_prod.txt
Password: <acessar site do digitalOcean e pegar senha para este db e user>

## Restore data em containers
### Se o data for novo
Após criado pelo volume do container
(fluxus5api-py3.11) catalunha@pop-os:~/myapp/proclinicakids/fluxus5api/z/docker-fluxus5$
psql -h localhost -U fluxususer -d fluxusdb < fluxusdb_prod.txt 
Password for user fluxususer: <informe password do database local>

### se o database ja tiver dados
Feito novo dump tem q apagar os dados atuais e restaurar novos.
Entao acessar ao database
(fluxus5api-py3.11) catalunha@pop-os:~/myapp/proclinicakids/fluxus5api/z/docker-fluxus5$
psql -h localhost -U fluxususer -d fluxusdb

Acessado o db pelos psql. precisa e recriar o database
fluxusdb=# \c postgres
postgres=# drop database fluxusdb;
postgres=# create database fluxusdb with owner fluxususer;

Sair e restaurar os dados
psql -h localhost -U fluxususer -d fluxusdb < fluxusdb_prod.txt 

# SWAGGER
http://192.168.10.117:8000/api/schema/?format=json
