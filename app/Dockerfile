FROM python:3.9

#EXPOSE 5000
#ARG APPDIR=/usr/src/app
#ARG SRCDIR=/usr/src
#RUN mkdir -p $APPDIR
#WORKDIR $SRCDIR
#COPY app $APPDIR
#COPY requirements.txt .
#COPY wsgi.py .
#COPY config.py .
#RUN pip install -r requirements.txt --upgrade pip
#CMD python wsgi.py

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt --upgrade pip

COPY . /app
CMD python wsgi.py

