FROM python:3.10-slim

EXPOSE 8000

WORKDIR /app
COPY . /app
COPY production/api/cleaning.py /app

COPY packages/requirements.txt .
RUN pip install -r packages/requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "production.api.main:app"]


# run % docker build -t hadock404/mldockerimg:v1 .
# run % docker run -dp 8081:8000 -ti --name mlContainer hadock404/mldockerimg:v1
# run % docker push hadock404/mldockerimg:v1