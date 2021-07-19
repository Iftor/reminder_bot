FROM python:3.9

WORKDIR /reminder_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./Application.py"]
