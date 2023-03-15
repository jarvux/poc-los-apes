FROM python:3.10

EXPOSE 50052/tcp

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./entrega/app.py"]