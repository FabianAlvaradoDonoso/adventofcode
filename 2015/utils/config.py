from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Ahora puedes acceder a las variables de entorno
AOC_SESSION = os.getenv("AOC_SESSION")
AOC_HEADERS = os.getenv("AOC_HEADERS")
