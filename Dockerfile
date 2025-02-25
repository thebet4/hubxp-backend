FROM python:latest

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./populate_mongo.py /code/populate_mongo.py
COPY ./app /code/app

# RUN python populate_mongo.py 

CMD [ "uvicorn", "app.main:app","--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-dir", "/code/app"]