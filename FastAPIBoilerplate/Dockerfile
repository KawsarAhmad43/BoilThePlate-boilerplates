# Use the official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file first to cache the pip install step
COPY ./requirements.txt /code/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the application code
COPY ./app /code/app

# Start the FastAPI server using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
