import requests
from datetime import datetime

# 1. Mostrar mensaje
print("Hola Mundo Cruel!!!")

# 2. Mostrar día y hora actual
ahora = datetime.now()
print("Fecha y hora actual:", ahora.strftime("%d/%m/%Y %H:%M:%S"))

# 3. Obtener temperatura actual en Barcelona usando Open-Meteo
# Coordenadas de Barcelona: 41.3888, 2.159
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 41.3888,
    "longitude": 2.159,
    "current_weather": "true"
}

try:
    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    
    temperatura = datos["current_weather"]["temperature"]
    print(f"La temperatura actual en Barcelona es: {temperatura}°C")
except Exception as e:
    print("No se pudo obtener la temperatura:", e)
