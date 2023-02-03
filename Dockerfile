FROM python:3.9.10

ENV PYTHONDONTWRITEBYTECODE 1 # Pythonによる「disc, pyc files」への書き込み防止
ENV PYTHONUNBUFFERED 1 # Pythonによる標準入出力のバッファリング防止
ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir /dev-code

WORKDIR /dev-code

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ADD . /dev-code