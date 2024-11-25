# info de la materia: ST0263-242
# Proyecto 3 – Automatización del Proceso de Captura, Ingesta, Procesamiento y Salida de Datos COVID en Colombia

## Estudiante(s): 
Jonathan Betancur, jbetancur3@eafit.edu.co  
Esteban Vergara Giraldo, evergarag@eafit.edu.co  
Miguel Angel Cock Cano, macockc@eafit.edu.co

## Profesor: 
Alvaro Enrique Ospina SanJuan, aeospinas@eafit.edu.co  

---

## 1. Descripción de la Actividad

Este proyecto implementa una arquitectura batch para big data, automatizando el ciclo de vida completo de gestión de datos relacionados con COVID-19 en Colombia. Las etapas incluyen:

- **Captura de datos**: Obtención de información desde archivos y APIs proporcionadas por el Ministerio de Salud.
- **Ingesta**: Transferencia de datos desde una base de datos relacional (MySQL/Postgres) hacia Amazon S3.
- **Procesamiento**: Uso de Amazon EMR con Spark para realizar procesos ETL y análisis de datos.
- **Salida de datos**: Almacenamiento de resultados procesados y analíticos en S3, con acceso mediante Amazon Athena y una API.

### 1.1 Aspectos Cumplidos

- **Requerimientos funcionales**:
  - Captura automática de datos desde archivos y APIs del Ministerio de Salud.
  - Ingesta de datos desde una base de datos relacional hacia S3 utilizando herramientas como Hadoop Sqoop.
  - Procesamiento ETL con Spark en EMR para preparar y unir datos, almacenándolos en la zona Trusted de S3.
  - Análisis descriptivo y creación de pipelines analíticos con SparkSQL y SparkML, con resultados almacenados en la zona Refined de S3.
  - Exposición de resultados mediante consultas en Amazon Athena y una API.

- **Requerimientos no funcionales**:
  - Automatización completa de los procesos sin intervención humana.
  - Implementación de mejores prácticas para el manejo de datos en entornos distribuidos.
  - Compatibilidad con múltiples nubes, utilizando AWS como principal y explorando alternativas en GCP y Azure.

### 1.2 Aspectos No Cumplidos

- No se implementaron modelos avanzados de aprendizaje automático, ya que eran opcionales.
- La herramienta AWS DMS no se utilizó debido a limitaciones de permisos; se optó por Hadoop Sqoop como alternativa.

---

## 2. Información General de Diseño

### Arquitectura de Alto Nivel

- **Fuente de datos**: Archivos y APIs del Ministerio de Salud, base de datos relacional (MySQL/Postgres).
- **Almacenamiento**: Amazon S3 con zonas Raw, Trusted y Refined.
- **Procesamiento**: Amazon EMR con Spark para tareas ETL y análisis.
- **Consulta y visualización**: Amazon Athena y una API para acceso a los resultados.

### Patrones y Mejores Prácticas Utilizadas

- **Patrón Lambda**: División en zonas Raw, Trusted y Refined para asegurar la trazabilidad y calidad de los datos.
- **Automatización**: Uso de scripts para la creación de clústeres, ejecución de procesos ETL y análisis de datos.
- **Seguridad**: Configuración de roles y políticas de IAM para controlar el acceso a los recursos.

---

## 3. Ambiente de Desarrollo

### Tecnologías Utilizadas

- **Lenguaje de programación**: Python 3.10.
- **Librerías y paquetes**:
  - `boto3` para interacción con servicios de AWS.
  - `pyspark` para procesamiento de datos con Spark.
  - `requests` para consumo de APIs.
  - `sqlalchemy` para conexión con bases de datos relacionales.
- **Herramientas adicionales**: Hadoop Sqoop para ingesta de datos desde bases de datos hacia S3.

### Pasos para Compilar y Ejecutar

1. 

## detalles del desarrollo.
## detalles técnicos
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 

EJEMPLO CLOUD9
![1](fotos/1.png)
![2](fotos/2.png)

STEPS EJECUTADOS
![4](fotos/4.png)

RESULTADO DE API
![5](fotos/5.png)

RESULTADO DE ARCHIVO
![6](fotos/6.png)

RESULTADO DE SQL HIVE
![7](fotos/7.png)

ARVHIDO DESCARGADO CON EL STEP DE SHELL
![8](fotos/8.png)

CARPETA CON CODIGOS
![9](fotos/9.png)

CARPETA CON RESULTADOS
![10](fotos/10.png)

RESULTADO EXITOSO DE API
![11](fotos/11.png)

RESULTADO EXITOSO DE ARCHIVO
![12](fotos/12.png)

CREACION DE TABLA EN ATENA DE RESULTADO DE API
![13](fotos/13.png)
![14](fotos/14.png)
![15](fotos/15.png)

CREACION DE TABLA EN ATENA DE RESULTADO DE API
![16](fotos/16.png)
![17](fotos/17.png)
![18](fotos/18.png)

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
## 4. Ambiente de Ejecución

### Tecnologías

- **Lenguaje de programación**: Python 3.10.
- **Librerías y paquetes**: Mismas que en el ambiente de desarrollo.
- **Servicios en la nube**:
  - **Almacenamiento**: Amazon S3.
  - **Procesamiento**: Amazon EMR con Spark.
  - **Consulta**: Amazon Athena.

### Configuración

- **IP o nombres de dominio**: Configuración automática para clústeres y buckets de S3.
- **Parámetros**: Mismos que en el ambiente de desarrollo.

### Lanzamiento del Servidor

1. **Iniciar la API para consulta de resultados**:
   ```bash
   python api.py

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto
