FROM continuumio/miniconda3

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

EXPOSE 5000

RUN ["python", "manager.py", "-db", "start"]

CMD [ "python", "app.py" ] 
