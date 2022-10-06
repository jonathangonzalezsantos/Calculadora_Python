# Calculadora

## Entorno virtual 

Para la ejecución de este programa, le recomendamos la creación de un entorno virtual de Python. 

Este, es un ambiente creado con el objetivo de aislar los recursos que tenga instalados (librerías, entornos de ejecución, ...) y así poder ejecutar la Calculadora sin crear ningún tipo de conflicto con su equipo actual.

### Primera ejecución del programa

Para llevar a cabo la primera ejecución del programa en un entorno virtual, debe de seguir los siguientes pasos en su equipo Linux:

1. Ejecute el terminal desde la carpeta del proyecto. Si ha accedido a la terminal 
desde otra ubicación, podrá situarse en la carpeta del proyecto con el siguiente comando (sustituya "ruta" por su ubicación del proyecto):
```$ cd ruta```

2. Instale las dependencias del sistema, necesarias para ejecutar la aplicación:
   
    ```
    sudo apt-get install python3 python3-pip
    sudo apt-get install python-virtualenv virtualenv
    sudo pip install --upgrade autopep8
    ```
3. Instale virtualenv:
   
   ```sudo pip3 install virtualenv```

4. Cree el entorno virtual en el que ejecutará la calculadora:
   
    ```$ virtualenv --python=python3 .venv```

    ".venv" representa donde se instalarán las dependencias necesarias de la aplicación. El punto (".") nos permite crear esta carpeta de forma oculta en Linux para que no le sean molestos. El nombre "venv" puede ser modificado si así lo desea.

5. Active el entorno virtual recién creado:
   ```$ source .venv/bin/activate```

6. Desde este momento, ya está dentro del entorno virtual. Todas aquellas dependencias que instale desde ahora no afectarán a la configuración local de su equipo.
   
7. Instale los paquetes necesarios para el correcto funcionamiento de la aplicación y que están ubicados en el archivo "dependencias.txt", con la siguiente sentencia:
   ```$ pip install -r conf/dependencias.txt```

8. A partir de este momento, ya puede ejecutar el programa de la Calculadora en el entorno virtual
   ```$ python main.py```

9.  En el caso de que en el futuro quiera añadir más dependencias al programa, puede actualizar el archivo con la siguiente sentencia:
    ```$ pip freeze > conf/dependencias.txt```

10. Una vez finalizado el trabajo con la aplicación, recuerde salir del entorno virtual:
    ```deactivate```

**Nota**: En la carpeta "docs" hay un video de demostración en el que se simula el primer uso en un nuevo equipo sin configurar. Se aplican todos estos puntos indicados (excepto el 9).


### Siguientes ejecuciones

Una vez haya realizado la primera ejecución, si quiere volver a abrir el programa en un entorno virtual del mismo equipo, bastará con realizar los siguientes puntos:

1. Ejecute el terminal desde la carpeta del proyecto. Si ha accedido a la terminal 
desde otra ubicación, podrá situarse en la carpeta del proyecto con el siguiente comando (sustituya "ruta" por su ubicación del proyecto):
    ```$ cd ruta```

2. Active el entorno virtual creado anteriormente (Si quiere crear otro entorno diferente, por favor siga las instrucciones del punto 4 del apartado anterior):
   ```$ source .venv/bin/activate```

3. A partir de este momento, ya puede ejecutar el programa de la Calculadora en el entorno virtual
   ```$ python main.py```

4. Una vez finalizado el trabajo con la aplicación, recuerde salir del entorno virtual:
    ```deactivate```

Recuerde que si hacee cambios, añadiendo o modificando dependencias, ha de actualizar el archivo "dependencias.txt" siguiendo los pasos del punto 9 del apartado anterior.