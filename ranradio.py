#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ranradio.py
#
# Creative Commons Josi Guaimas <info@gdotg.com> 2015
# 
# El siguiente código escrito en el lenguaje python se utilizó para la 
# instalación. Detecta ondas de radio en el aire de manera aleatoria a 
# través de un receptor de radio SDR y produce como resultado archivos .mp3
#
#

import random
import decimal
import subprocess
from time import sleep

"""Rango de frecuencias de FM Interesantes de captar en Oberá (Mhz)"""
frec_min = 80  
frec_max = 150

def bash_command(cmd):
	subprocess.Popen(['/bin/bash', '-c', cmd])
	
def obtener_frecuencia(minima, maxima):
	"""Sortea una frecuencia entre la mínima y la máxima ej. 99.7M"""
	return str(decimal.Decimal(random.randint(minima*100, maxima*100,))/100)

def play(frec):
	"""Reproduce una frecuencia de radio"""
	comando = 'rtl_fm -f %sM -M fm -s 192.161k -A std  -l 0 -E deemp -r 44.1k \
	            | play -r 32k -t raw -e s -b 16 -c 1 -V1 -' % (frec)
	bash_command(comando)

def grabar(frec):
	"""Graba el audio obtenido de la frecuencia a un archivo .mp3"""
	comando = 'rtl_fm -f %sM  -M fm -s 170k -A std  -l 0 -E deemp -r 44.1k  \
	           | lame -s 22.0 -r -h -V 0 -b 128 - %s.mp3' % (frec, frec)
	bash_command(comando)

def stop():
	"""Detiene la reproducción o grabación"""
	bash_command('killall rtl_fm')

while True:
	"""Reproduce o graba durante 5 segundos y repite la
	secuencia hasta que el usuario presione ctrl + c"""
	frecuencia = obtener_frecuencia(frec_min, frec_max)
	grabar(frecuencia)
	sleep(5)
	stop()

