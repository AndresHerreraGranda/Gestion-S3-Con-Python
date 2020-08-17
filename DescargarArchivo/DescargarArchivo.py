# ==== LIBRERIAS ====
import boto3


# ==== CREDENCIALES S3 ==== 
id = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
clave_secreta = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
nombre_bucket = 'XXXXXXXXX'

# ==== DATOS DE DESCARGA ====
archivo = 'XXXXXX.jpg'
ruta = 'XXXXXXXX\XXXXXXXXXX\XXXXXXXXXX'

# ==== FUNCION ====
def descargar_archivos(ID_LLAVE_ACCESO ,LLAVE_SECRETA_ACCESO ,NOMBRE_BUCKET ,ARCHIVO ,RUTA):

    s3 = boto3.client('s3', aws_access_key_id=ID_LLAVE_ACCESO,
                      aws_secret_access_key=LLAVE_SECRETA_ACCESO)
    
    s3.download_file(Bucket= NOMBRE_BUCKET, Key = ARCHIVO, Filename = RUTA)
    
# ==== EJECUCCION ====
descargar_archivos(id ,clave_secreta ,nombre_bucket ,archivo ,ruta)
