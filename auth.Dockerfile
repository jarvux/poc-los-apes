FROM python:3.10

EXPOSE 5005/tcp

COPY auth-requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r auth-requirements.txt

COPY . .

CMD [ "flask", "--app", "./authentication/api", "--debug", "run", "--host=0.0.0.0"]
