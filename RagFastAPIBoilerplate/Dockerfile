FROM python:3.11-slim
RUN pip install uv
WORKDIR /code
COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt
COPY . /code
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
