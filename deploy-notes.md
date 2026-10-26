# Deploy Notes - Práctica CI/CD Django

## Descripción

El proyecto utiliza Django, Docker, Docker Compose y PostgreSQL para simular un flujo de integración y despliegue continuo.

## Requisitos

- Docker Desktop
- Docker Compose
- Git
- Proyecto clonado desde GitHub

## Pasos para el despliegue simulado

1. Clonar el repositorio:

   git clone URL_DEL_REPOSITORIO

2. Ingresar a la carpeta del proyecto:

   cd practica-ci-cd-django

3. Construir las imágenes:

   docker compose build

4. Levantar los contenedores:

   docker compose up -d

5. Ejecutar las migraciones:

   docker compose exec web python manage.py migrate

6. Verificar los contenedores:

   docker compose ps

7. Abrir la aplicación en el navegador:

   http://localhost:8000

## Resultado esperado

La aplicación Django debe ejecutarse correctamente en un contenedor Docker y utilizar PostgreSQL como base de datos.