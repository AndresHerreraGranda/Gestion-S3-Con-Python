# Gestión de AWS S3 con python

## Introducción
[AWS S3](https://aws.amazon.com/es/s3/) es un servició de almacenamiento de objetos en la nube, al cual se puede subir, descargar, modificar y guardar archivos de diferentes formas. Una de ellas es mediante Python utilizando el [SDK](https://es.wikipedia.org/wiki/Kit_de_desarrollo_de_software#:~:text=Un%20kit%20de%20desarrollo%20de,de%20software%2C%20entornos%20de%20trabajo%2C) predefinido por Amazon [Boto3](https://aws.amazon.com/es/sdk-for-python/).
Se debe tener claro como crear un [bucket](https://docs.aws.amazon.com/es_es/AmazonS3/latest/dev/UsingBucket.html#create-bucket-intro) en S3, ya que solo se configura la clave de acceso al S3, y mediante esta clave poder gestionar los archivos con python.

## Desarrollo
### 1. Configuración de clave de acceso 
Una vez ingrese en su consala de administración continue con los siguientes pasos:

  - Haga clic en su nombre de usuario en la parte superior derecha de la página para abrir el menú desplegable.

  - Haga clic en 'Mis credenciales de seguridad'.
  
  - Haga clic en "Panel de control" en el lado izquierdo de la página.
  
  - Haga clic en 'Rotar sus claves de acceso' en la sección 'Estado de seguridad'.
  
  - Haga clic en el botón 'Administrar claves de usuario'.
  
  - Haga clic en la pestaña 'Credenciales de seguridad' para ver sus claves de acceso.
  
  - Para crear una nueva clave de acceso, haga clic en el botón 'Crear clave de acceso'.
  
  - Descargue el archivo .csv que contiene su clave de acceso . Manténgalo seguro.
  
### 2. Instale el SKD Boto3

Se utilizar el paquete de instalación de python **PIP**, se debe asegurar que este actualizado:
```
python -m pip install --upgrade pip
```

Se instala [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation):
```
pip install boto3
```
