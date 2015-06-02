#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ranradio.py
#  
#  Copyright 2015 jositux <info@gdotg.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import threading
import subprocess
import random

index = 0;

def bash_command(cmd):
	subprocess.Popen(['/bin/bash', '-c', cmd])

def capturar():
	global index
	threading.Timer(5.0, capturar).start()
	aleatorio = random.randint(1, 11)
	print "Captura %i seg. - posición %i" % (index, aleatorio)
	comando = 'a="Comando hacia bash con variable random = %i" && echo "${a}"' % (aleatorio)
	bash_command(comando)
	index = index + 5

capturar()
