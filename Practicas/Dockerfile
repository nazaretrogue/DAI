FROM python:3.7
# WORKDIR /Ejs
WORKDIR /flask

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development

RUN apt-get install libjpeg-dev \
                    zlib1g-dev \
                    libfreetype6-dev \
                    liblcms2-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["flask", "run"]
