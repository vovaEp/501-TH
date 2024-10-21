FROM python:3.8-alpine
 RUN apk add g++ jpeg-dev zlib-dev libjpeg make
 RUN pip3 install matplotlib
 COPY . /app
 WORKDIR /app
 CMD ["python", "lab18_kostenko.py"]