FROM arm32v7/python:2.7.13-jessie

WORKDIR /DevOps

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY ./src ./src

EXPOSE 5000

CMD ["python", "./src/app.py"]