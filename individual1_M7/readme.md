-	Crear ambiente virtual
    python –m venv nombreAmbiente
-	Activar el ambiente en termianl:
    ambiente\Scripts\activate
-   Instalación de frameworks
	pip install django
-   Creación del proyecto
	django-admin startproject nombre_project 
-	Creación de la aplicación: 
	python manage.py startapp nombre_aplicacion

-   Para crear el archivo con los requerimientos 
    pip freeze > requirements.txt 



    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bdPrueba',
        'USER' : 'postgres',
        'PASSWORD' : 'root',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

En la consola del proyecto, dentro del ambiante virtual:
		1	 	pip install psycopg2



-	Migraciones 
    python manage.py migrate
    python manage.py makemigrations 
-	Creación del super usuario 
	python manage.py createsuperuser

    admin
    123



