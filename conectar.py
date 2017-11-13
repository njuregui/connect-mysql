#!/usr/bin/python
import os
import sys
usuario=sys.argv[1]
contr=sys.argv[2]
bd=sys.argv[3]
print "Vamos a conectarnos a mysql con"
acceder_mysql="mysql -u "+usuario+" -p"+contr+" "+bd
os.system(acceder_mysql)
