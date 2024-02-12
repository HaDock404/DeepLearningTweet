# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

EXPOSE 8000

WORKDIR /app
COPY . /app
COPY production/api/cleaning.py /app

COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN pip install gunicorn UvicornWorker

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "production.api.app:app"]
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "production.api.app:app"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "production.api.app:app"]


# run % docker build -t mldockerimg:v1 .
# run % docker run -dp 8081:8000 -ti --name mlContainer mldockerimg:v1