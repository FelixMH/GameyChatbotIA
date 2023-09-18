# Pasos para conseguir ejecutar el proyecto de manera satisfactoria.

````

```
    El siguiente es el paso a paso para crear el ambiente , ejecutar y probar de manera satisfactoria
    el chatbot que hemos llamado Gamey.

    Para comenzar es importante mencionar que requerimos tener instalado Python 3.11 en nuestro sistema
    operativo,



```

````

se asume que se tiene instalado, pero en caso contrario, favor de [Descargar Python desde su web oficial](https://www.python.org/downloads/)

# Creación del ambiente virtual para mantener el proyecto.

```
    debemos tener python instalado y crear un ambiente virtual para mantener las dependencias del proyecto
    y ejecutar de manera satisfactoria el mismo.

    1.- abra una terminal de comandos, puede ser powershell si se encuentra en windows , o zsh si está
    dentro de una mac.

    2.- ejecute el siguiente comando para asegurarse de tener Python instalado, si está seguro de tenerlo
    instalado, omita y vaya al paso 3.



```

### python --version

```

    3.- Ejecute el siguiente comando : python -m venv
    "ambiente", lo marcado en comillas dobles es el
    nombre que usted desea darle a su ambiente virtual,
    en nuestro caso , le colocamos "ambiente"

    4.- una vez ejecutado, asegúrese de activar su ambiente virtual con el siguiente comando si está
    en Windows

```

### ambiente\Scripts\activate

```

    o si está en mac y linux:

```

### source ambiente/bin/activate

```

    5.- hemos dejado un archivo requerimientos.txt que le servirá para instalar todas las dependencias que el
    proyecto requiere para ejecutar satisfactoriamente,
    ejecute el siguiente comando para instalar las dependencias:

```

### pip install -r .\requerimientos.txt

```

    una vez ejecutado, deberá de esperar a que se instalen todas las dependencias, prepárese un café o
    escuche una canción mientras que el proceso termina.

    6.- una vez terminado de instalar las dependencias, ya puede ejecutar el proyecto, para ello
    ejecute el siguiente comando:

```

### py .\Main.py

```

    esto desplegará la ventana del programa, con Gamey, el chatbot inteligente programado en su
    version 1.0.0

```
