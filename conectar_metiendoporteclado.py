#!/usr/bin/python
import os
import sys
usuario=raw_input("Introduce el usuario ")
contr=raw_input("Introduce la password ")
bd=raw_input("Introduce la base de datos ")
print "Vamos a conectarnos a mysql"
acceder="mysql -u "+usuario+" -p"+contr+" "+bd
os.system(acceder)
