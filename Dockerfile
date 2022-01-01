FROM python:3.8-slim
COPY main.py /deploy/
COPY config.yaml /deploy/
WORKDIR /deploy/
RUN apt update
RUN apt install -y git
RUN apt-get install -y libglib2.0-0
RUN pip install git+https://github.com/AndrewWalker251/lightbulb_app.git
RUN wget  -O lightbulb_app/image_classifier/weights/model_weights_4.pth "https://github.com/AndrewWalker251/lightbulb_app/releases/download/v0.0.1/model_weights_4.pth"
EXPOSE 8080

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1