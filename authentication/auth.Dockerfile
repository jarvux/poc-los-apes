FROM python:3
EXPOSE 5000/tcp
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "flask", "--app", "./api", "--debug", "run", "--host=0.0.0.0"]
