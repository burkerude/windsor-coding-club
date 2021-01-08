FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app .

CMD ["python", "routes.py"]