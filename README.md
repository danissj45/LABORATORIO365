# LABORATORIO365 
INSTALACCION
### 1. Configuración de Termux

Primero, asegúrate de tener Python y Flask instalados en Termux. Si no lo has hecho, ejecuta los siguientes comandos:

```bash
pkg install python
pkg install python2
pkg install python3
pip install Flask
pip install requests colorama
```

### 2. CLONA EL REPOSITORIO

git clone https://github.com/danissj45/LABORATORIO365 


### Instrucciones de Uso para BruteForcesRed

1. **Configuración Inicial**:
   - Primero, asegúrate de tener Python instalado en Termux. Si no lo tienes, puedes instalarlo con:
     ```bash
     pkg install python
     pkg install python2
     pkg install python3
     ```
   - Luego, instala las dependencias necesarias ejecutando:
     ```bash
     pip install requests colorama
     ```
   - Es importante que coloques el archivo de diccionario de contraseñas (por ejemplo, `diccionario.txt`) en la misma carpeta que el script `brute_force.py`.

2. **Ejecución del Script**:
   - Abre Termux y navega hasta la carpeta donde guardaste tu archivo `brute_force.py`.
   - Para ejecutar el script, simplemente escribe:
     ```bash
     python3 brute_force.py
     ```

3. **Menú Principal**:
   - Una vez que inicie el programa, verás un menú con varias opciones:
     1. **Iniciar Brute Force**: Comienza un ataque de fuerza bruta utilizando el diccionario que elegiste.
     2. **Iniciar RED FAST BRUTE FORCE**: Comienza un ataque de fuerza bruta a diferentes velocidades. Tendrás la opción de elegir entre varias velocidades (2x, 3x, 4x o sin pausa).
     3. **Ingresar contraseña manualmente**: Si prefieres, puedes probar una contraseña específica ingresándola manualmente.
     4. **Ver diccionario de contraseñas**: Si deseas, puedes revisar el contenido del archivo del diccionario.
     5. **Instrucciones de uso**: Si en algún momento necesitas recordar cómo usar el programa, selecciona esta opción.
     6. **Usar otro diccionario**: Si quieres cambiar el archivo de diccionario, puedes hacerlo aquí (recuerda que debe estar en la misma carpeta).
     7. **Cambiar IP**: Si necesitas cambiar la dirección IP que utilizarás para el ataque, elige esta opción.
     8. **Cambiar Puerto**: Puedes cambiar el puerto que usarás para el ataque con esta opción.
     9. **Salir**: Cuando termines, selecciona esta opción para cerrar el programa.

4. **Atacar con Fuerza Bruta**:
   - Al seleccionar "Iniciar Brute Force", el programa comenzará a probar las contraseñas del diccionario en la URL que has especificado (con la IP y el puerto que elegiste).
   - Verás mensajes que indican si cada contraseña es correcta o incorrecta, junto con un símbolo que lo refleja (✓ para correcta y X para incorrecta).

5. **Configuración de IP y Puerto**:
   - Puedes cambiar la IP y el puerto en cualquier momento seleccionando las opciones 7 y 8 en el menú.
   - Antes de cambiar, se mostrará la IP o puerto actual para que sepas lo que estás modificando.

6. **Finalizando el Programa**:
   - Puedes salir del programa en cualquier momento seleccionando la opción 9.
   - Al hacerlo, aparecerá un mensaje que dice: *"The Termux Syndicate - "EXPLORAMOS CON ÉTICA, PROTEGEMOS CON UNIDAD"*.

### Recomendaciones
- Recuerda siempre usar este programa de manera ética y solo en sistemas donde tengas permiso para realizar pruebas de penetración.
- Asegúrate de que la URL y las credenciales que estás probando sean legítimas y que estés autorizado para hacerlo.

  
