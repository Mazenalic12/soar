# Gebruik een lichte Python image
FROM python:3.10-slim

# Werkdirectory in de container
WORKDIR /app

# Kopieer de bestanden
COPY . .

# Installeer Flask
RUN pip install flask

# Start de app
CMD ["python", "app.py"]
