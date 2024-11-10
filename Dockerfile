# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY main.py /app

# Instalar las dependencias
RUN pip install requests

# Definir el comando para ejecutar la aplicación
CMD ["python", "main.py"]
