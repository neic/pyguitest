FROM python:3.6

WORKDIR /app

COPY Pipfile* /app/

RUN pip install pipenv

RUN pipenv install --system --deploy
RUN pipenv install pyinstaller

COPY . /app

CMD ["python", "main.py"]
