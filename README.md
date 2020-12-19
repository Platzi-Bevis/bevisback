# Platzi-bevis - bevisback

### Backend para una aplicación que permite evaluar código hecho en python, regresa si el código ejecutado entrega la salida esperada.

  

## Documentación:

> La documentación fué hecha usando la herramienta que proporciona Swagger.
> Puede leerla aquí: https://docs.hardmakers.com/

## Arquitectura
> Usamos el concepto de microservicios para entregar un backend modular, y así poder escalar los servicios que más demanda tengan.
> Se uso Docker para modularizar nuestros servicios.

## Tecnologías usadas
>- El API se desarrollo con Python - Django
>- El servicio de evaluación del código se desarrollo con Python - Flask
>- La documentación se entrega con un servicio desarrollado con JavaScript - NodeJS
>- Base de datos: PostgreSQL

## Despliegue
>El despliegue se realizo usando un droplet de DigitalOcean, con Docker y Traefik
>Puede verlo aquí: 
>https://api.hardmakers.com/api/v1/course/12/material/2/tests