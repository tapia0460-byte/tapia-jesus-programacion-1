Programacion 1
Nombre del alumno: Tapia Hernandez Jesus Adrian
Curso: Programacion 1
Grupo: V2213

# Proposito del repositorio
Este repositorio servira para resguardar practicas y proyectos futuros que se hagan en clase

# Estructura de carpetas
tapia-jesus-programacion-1/

 practicas/
 proyectos/
 .gitignore
 README.md

# practicas/
En esta carpeta se guardan las practicas y ejercicios de la clase.

# proyectos/
En esta carpeta se guardan los proyectos realizados durante el curso

# .gitignore
Aqui estan los archivos que deben ser ignorados para evitar subir cosas innecesarias.

# README.md
Este archivo tiene documentacion e informacion general del repositorio.

# Bitacora de instalacion del IDE

IDE utilizado: Visual studio code

Version: 1.138.0

Fecha de instalacion: 21/09/26

Primero descargue el IDE desde la pagina oficial y simplemente lo abri para instalarlo.

No tuve problemas para instalarlo

Para clonar el repositorio en otra computadora:
1. Instalar Git.
2. Abrir Git Bash o una terminal.
3. Copiar la URL del repositorio desde GitHub.
4. Ejecutar el comando:

git clone URL-DEL-REPOSITORIO

5. Entrar a la carpeta del repositorio:

cd apellido-nombre-programacion-1

6. Hacer modificaciones o agregar las practicas y proyectos hechos.
7. Guardar los cambios.
8. Agregar los archivos a Git:

```bash
git add .
```

9. Crear un commit:

```bash
git commit -m "Descripcion de los cambios"
```

10. Subir los cambios a GitHub:

```bash
git push
```

# Scratch y Python

Link del proyecto en Scratch:
https://scratch.mit.edu/projects/1378434231/

Porcion traducida a Python:
def when_program_starts_1(self):
    while True:
        self.go_to_x_y(-11.0, -36.0)
        self.switch_costume_to("kris")
        while not (self.answer() == "element_1_: data_itemoflist"):
            pass

        self.go_to_x_y(30.0, -36.0)
        while not (self.answer() == "element_3_: data_itemoflist"):
            pass

        self.wait(5.0)
        self.switch_costume_to("kris_down")
        self.start_sound("dead")
        self.wait(3.0)

Autor:
Tapia Hernandez Jesus Adrian