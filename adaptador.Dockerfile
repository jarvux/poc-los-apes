FROM python:3

EXPOSE 50051/tcp

COPY sidecar-requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r sidecar-requirements.txt

COPY . .

CMD [ "python3", "./sidecar/main.py" ]