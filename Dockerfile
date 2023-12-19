FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN python3 -m venv venv

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-w", "4","pancake:app"]
#CMD ["python3","-m","flask", "--app=app","run","--host=0.0.0.0"]
