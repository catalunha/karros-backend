catalunha@pop-os:~/apps/karros-backend$ pyenv versions
  system
* 3.11.0 (set by /home/catalunha/.pyenv/version)
  3.12.2
catalunha@pop-os:~/apps/karros-backend$ pyenv install 3.12.0
catalunha@pop-os:~/apps/karros-backend$ pyenv versions
  system
  3.11.0
  3.12.0
* 3.12.2 (set by /home/catalunha/apps/karros-backend/.python-version)
catalunha@pop-os:~/apps/karros-backend$ pyenv local 3.12.0

poetry init

Would you like... no
Would you like... no

poetry shell

poetry config --list

poetry config virtualenvs.create = true
poetry config virtualenvs.in-project = true


poetry add django
poetry add djangorestframework
poetry add djangorestframework-simplejwt
poetry add pillow
poetry add python-decouple
poetry add dj-database-url
poetry add django-cors-headers
poetry add psycopg2-binary
poetry add gunicorn
poetry add django-storages[s3]
poetry add boto3


django-admin startproject backend .
cd backend
django-admin startapp users
django-admin startapp core

python manage.py makemigrations; python manage.py migrate

python manage.py createsuperuser

admin@gmail.com
django@123

# acessar db no docean
Localmente
(karros-backend-py3.12) catalunha@pop-os:~/apps/karros-backend/backend$ psql postgresql://doadmin:AVNS_hC3sRyHIfULxX7NdbIp@db-fluxus-do-user-7515641-0.c.db.ondigitalocean.com:25060/karrosdb?sslmode=require
psql (15.7 (Ubuntu 15.7-1.pgdg22.04+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

karrosdb=> 


REVOKE ALL ON DATABASE karrosdb FROM karrosuser;
GRANT ALL ON DATABASE karrosdb TO karrosuser;
GRANT ALL ON ALL TABLES IN SCHEMA public TO karrosuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO karrosuser;
ALTER DATABASE karrosdb OWNER TO karrosuser;
