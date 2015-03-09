#!/usr/bin/python


fichero = open('/etc/passwd','r')
lectura = fichero.readlines()
fichero.close()


for linea in lectura
    shell = linea.split(":")[-1]
    usuario = linea.split(":)[0]
    print usuario, shell

print "Hay " + str(len(lectura)) + " usuarios"
