# Imagen base de Python
FROM python:3.10

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto de Flask
EXPOSE 5000

# Comando para correr Flask
CMD ["python", "app.py"]
