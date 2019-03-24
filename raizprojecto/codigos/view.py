import sys
import compute
#entrada= float r
#salida= "hola sen(r)"

def get_input():
	#recibe datos de la linea de comandos
	r = float(sys.argv[1])
	return r

def present_output(r):
	"""imprime resultados en la linea de comandos"""
	s = compute.compute(r)
	print 'Hola: sen(%g)=%g' % (r, s)