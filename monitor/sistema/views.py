from django.shortcuts import render
from django.http import JsonResponse
import psutil
import platform


def index(request):

    try:
        procesador = platform.processor()
        sistema = platform.system()
        version = platform.release()
        nucleos = psutil.cpu_count()

    except Exception:
        procesador = "No disponible"
        sistema = "No disponible"
        version = ""
        nucleos = "N/A"

    return render(request, "index.html", {
        "procesador": procesador,
        "sistema": sistema,
        "version": version,
        "nucleos": nucleos
    })


def datos_sistema(request):

    try:

        # CPU
        cpu = psutil.cpu_percent(interval=None)

        # RAM
        memoria = psutil.virtual_memory()
        ram_porcentaje = memoria.percent
        ram_total = round(memoria.total / (1024**3), 2)
        ram_usada = round(memoria.used / (1024**3), 2)

        # DISCO
        disco = psutil.disk_usage('/')
        disk_porcentaje = disco.percent
        disco_total = round(disco.total / (1024**3), 2)
        disco_usado = round(disco.used / (1024**3), 2)
        disco_libre = round(disco.free / (1024**3), 2)

        temperatura = 39  # simulada

    except Exception:

        cpu = 0
        ram_porcentaje = 0
        ram_total = 0
        ram_usada = 0

        disk_porcentaje = 0
        disco_total = 0
        disco_usado = 0
        disco_libre = 0

        temperatura = 39

    data = {
        "cpu": cpu,

        "ram_porcentaje": ram_porcentaje,
        "ram_total": ram_total,
        "ram_usada": ram_usada,

        "disk_porcentaje": disk_porcentaje,
        "disco_total": disco_total,
        "disco_usado": disco_usado,
        "disco_libre": disco_libre,

        "temperatura": temperatura
    }

    return JsonResponse(data)