# poc-los-alpes
Repo con el POCs que contiene los microservicios de entregas Los Alpes

## EntregaDelosAlpes

### Estructura del proyecto

Este repositorio sigue la siguiente estructura:
- **authentication**: En este directorio encuentra el microservicio de authentication EntregaDelosAlpes.
- **entregadelosalpes**: En este directorio encuentra el microservicio de orden EntregaDelosAlpes.
- **entrega**: En este directorio encuentra el microservicio de consumidor de eventos desde el Apache Pulsar.
- **sidecar**: En este directorio encuentra el código para el adaptador gRPC de EntregaDelosAlpes. En el, podrá encontrar el módulo `entregadelosalpes`, el cual cuenta con la definición de los servicios gRPC y mensajes Protobuf en el directorio `protos`. Por otra parte, el módulo `servicios` implementa las interfaces definidas en los archivos proto anteriomente descritos. Finalmente el módulo `pb2py` aloja los archivos compilados `.proto` en Python (para ver como compilarlos lea la siguientes secciones). El archivo `main.py` corre el servidor y `cliente.py` un cliente que crea una reserva usando un mensaje en JSON definido en el directorio `mensajes`.
- **.Dockerfile**: Cada servicio cuenta con un Dockerfile para la creación de la imagen y futura ejecución de la misma. El archivo `adaptador.Dockerfile` es el encargado de instalar las dependencias de nuestro servicio en gRPC y los comandos de ejecución. Mientras que el archivo `entregadelosalpes.Dockerfile` es el encargado de definir nuestro backend. El `auth.Dockerfile` es el encargado de definir nuestro servicio de autenticación
- **docker-compose.yml**: Este archivo nos define la forma de componer nuestros servicios. En este caso usted puede ver como creamos el Sidecar/adaptador por medio del uso de una red común para la comunicación entre contenedoras. En el caso de desplegar esta topología en un orquestador de contenedoras, el concepto va a ser similar.

### Escenarios probar
En el siguiente enlace se encuentran los escenarios a probar [PPT](https://uniandes-my.sharepoint.com/:p:/g/personal/z_alarcon_uniandes_edu_co/Edn078mbwttJkCMHlDPYdXwBbf29RYQgqMDmh6ld9eUeRg?e=a3sTmu)

### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app entregadelosalpes/api --debug run
```

```bash
flask --app authentication/api --debug run
```

### Utilizar una imagen Docker

Desde la carpeta raiz ejecutar el siguiente comando.

```bash
docker build . -f entregadelosalpes.Dockerfile -t entregadelosalpes
```

```bash
docker build . -f auth.Dockerfile -t auth
```

### Ejecutar la imagen docker

Para arrancar la imagen creada en el paso anterior ejecute el siguiente comando.

```bash
docker run -p 5000:5000 entregadelosalpes
```

```bash
docker run -p 5001:5001 auth
```

## Sidecar/Adaptador
### Instalar dependencias

En el archivo `sidecar-requirements.txt`, se encuentran las dependencias de Python para el servidor y el cliente gRPC.

```bash
pip3 install -r sidecar-requirements.txt
```

### Compilar gRPC

Desde la carpeta `sidecar/entregadelosalpes` se ejecuta el siguiente comando.

```bash
python3 -m grpc_tools.protoc -I ./protos --python_out=./pb2py --pyi_out=./pb2py --grpc_python_out=./pb2py ./protos/orden.proto
```
Este genera unos archivos .py y .pyi

### Como ejecutar server

Ingresar a la carpeta sidecar y ejecutar el siguiente comando, en una terminal.

```bash
python3 main.py 
```

### Como ejecutar client (ejemplo)

Ingresar a la carpeta sidecar y ejecutar el siguiente comando, abrir otra terminal.
Este consume un archivo JSON(crear un orden mock) ubicado en la carpeta mensajes

```bash
python3 cliente.py 
```

### Utilizar Docker para ejecutar gRPC

Desde la carpeta raiz ejecutar el siguiente comando.

```bash
docker build . -f adaptador.Dockerfile -t adaptador
```

### Ejecutar la imagen docker con gRPC

Para arrancar la imagen creada en el paso anterior ejecute el siguiente comando.

```bash
docker run -p 50051:50051 adaptador
```

## Docker-compose

Para desplegar todo con `docker-compose`:

```bash
docker-compose up
```
## Probar el consumo gRPC desde Postman

1. Seleccione en Crear Nueva `gRPC Request`, ver imagen
![image info](./docs/postman1.png)

2. Ingrese en hostname y el puerto (localhost:5000)
![image info](./docs/postman2.png)

3. En la opción Service Definition, importe el archivo .proto (sidecar/entregadelosalpes/protos/orden.proto)
![image info](./docs/postman3.png)

4. Una vez importado en la casilla de method se listan aquellos que fueron creados
![image info](./docs/postman4.png)

5. Puedes enviar un mensaje de ejemplo haciendo click en `Generate example message` y luego dar click en el boton Invoke
![image info](./docs/postman5.png)
