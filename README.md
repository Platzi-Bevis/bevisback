# Platzi-bevis - bevisback

### Backend para una aplicación web que permite evaluar código hecho en python, regresa información de la ejecución del código, además provee un dashboard/admin para agregar los tests/pruebas que se entregarán al usuario.

  

## Documentación:

> La documentación fué hecha usando la herramienta que proporciona Swagger.
> Puede leer la documentación aquí: https://docs.hardmakers.com/

## Arquitectura
> Usamos el concepto de microservicios para entregar un backend modular, y así poder escalar los servicios que más demanda tengan.
> Se uso Docker para modularizar nuestros servicios.

## Tecnologías usadas
>- El API se desarrolló con Python - Django
>- El servicio de evaluación del código se desarrolló con Python - Flask
>- La documentación se entrega con un servicio desarrollado con JavaScript - NodeJS
>- Base de datos: PostgreSQL

## Despliegue
>El despliegue se realizo usando un droplet de DigitalOcean, con Docker y Traefik
>Puede verlo aquí:
>- Endpoint: https://api.hardmakers.com/api/v1/course/12/material/2/tests
>- Dashboard - Admin: https://api.hardmakers.com/admin/