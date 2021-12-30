FROM python:3.8-slim
COPY main.py /deploy/
COPY config.yaml /deploy/
WORKDIR /deploy/
RUN apt update
RUN apt install -y git
RUN apt-get install -y libglib2.0-0
RUN pip install git+https://github.com/AndrewWalker251/lightbulb_app.git
EXPOSE 8080

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1