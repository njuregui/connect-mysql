#!/usr/bin/python
import os
import sys
print "Se va a crear una base de datos, introduzca sus credenciales: "
usuario=raw_input("Introduce el usuario ")
contr=raw_input("Introduce la password ")
base_de_datos=raw_input("Introduce la base de datos ")
backup="mysql -u "+usuario+" -p"+contr+" "+base_de_datos+ " | gzip > "+base_de_datos+".sql.gz"
os.system(backup)
print "Copia de seguridad creada"
