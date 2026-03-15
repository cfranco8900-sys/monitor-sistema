# Monitor de Recursos del Sistema con Django y Psutil

## Descripción

Este proyecto es una aplicación web desarrollada con **Django** que permite monitorear en tiempo real los recursos del sistema utilizando la librería **psutil**.

La aplicación muestra información sobre:

* Uso del CPU
* Uso de memoria RAM
* Uso del disco duro
* Información del sistema operativo
* Número de núcleos del procesador

Los datos se actualizan automáticamente cada **2 segundos** en la interfaz web.

---

## Tecnologías utilizadas

* Python
* Django
* Psutil
* Chart.js
* Docker

---

## Información monitoreada

La aplicación muestra:

* Porcentaje de uso del CPU
* Uso de memoria RAM (porcentaje)
* Uso del disco duro (porcentaje)
* Sistema operativo
* Versión del sistema
* Núcleos del CPU
* Temperatura del CPU (simulada)

---

## Estructura del proyecto

monitor/
│
├── monitor/
├── sistema/
├── templates/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

---

## Instalación y ejecución local

### Clonar el repositorio

git clone https://github.com/cfranco8900-sys/monitor-sistema.git

### Entrar al proyecto

cd monitor-sistema

### Crear entorno virtual

python -m venv venv

### Activar entorno virtual

Windows:

venv\Scripts\activate

### Instalar dependencias

pip install -r requirements.txt

### Ejecutar servidor

python manage.py runserver

Abrir en el navegador:

http://localhost:8000

---

## Ejecutar con Docker

Construir contenedor

docker compose build

Ejecutar aplicación

docker compose up

Abrir en el navegador:

http://localhost:8000

---

## Autor

C. Franco
Cuenta: 201111110063
