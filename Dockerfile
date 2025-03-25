# Use an official Python image
FROM python:3.12

# Expose port 8501 for the application
EXPOSE 8501

# Install system dependencies for PyAudio
RUN apt-get update && apt-get install -y gcc portaudio19-dev

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Copy the rest of the application
COPY . .


# Start the application using Uvicorn
CMD ["streamlit", "run", "app.py"]
