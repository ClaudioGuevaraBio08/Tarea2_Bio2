import random
from Bio.pairwise2 import format_alignment
from Bio import pairwise2
import sys
from time import time

print("ALINEAMIENTO DE LAS SECUENCIAS DADAS EN LA TAREA\n")
if(len(sys.argv) > 2):
	tiempo_inicial = time()
	print "Primera secuencia : " + sys.argv[1]
	print "Seguna secuencia : " + sys.argv[2] + "\n"
	#Biopython: Se entregan las secuencias creadas al azar y se alinean, ademas de entregar un puntaje.
	alignments = pairwise2.align.globalxx(sys.argv[1], sys.argv[2])
	print("Alineamiento entre la secuencia 1 y 2 : \n")
	print(format_alignment(*alignments[0]))
	print("#################################################################################################\n")
    
	tamano_muestra = 1
	while tamano_muestra < 351:#Este valor se explica en el informe  
		print "ciclo", tamano_muestra
		print("\n")
		secuencia_1 = ""#Se almacena la primera secuencia al azar.
		secuencia_2 = ""#Se almacena la segunda secuencia al azar.
		caso_secuencia = 1#Variable para distinguir una secuencia de la otra dentro del for, dependiendo del ciclo. Primero parte por la secuencia 1.
		
		lista_aminoacidos = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
		
		for i in range(2):#Rango 2, donde primera se crea un secuencia y luego la otra. 
			for i in range(17):#17 hace referencia al largo de las secuencias
				posicion = random.randrange(0,20)#Posicion indica un lugar al azar de la lista de aminoacidos 
				
				aminoacido = lista_aminoacidos[posicion]
				
				if caso_secuencia == 1:#Se crea la secuencia 1 agregando el nucleotido establecido anteriormente.
					secuencia_1 += aminoacido
				if caso_secuencia == 2:#Se crea la secuencia 2 agregando el nucleotido establecido anteriormente
					secuencia_2 += aminoacido
			
			caso_secuencia = 2#La variable cambia a 2 una vez terminado el primer ciclo del for. Ahora se creara la segunda secuencia al azar.
		
		print("ALINEAMIENTO DE LAS SECUENCIAS GENERADAS AL AZAR\n")
		print("Secuencia 1 : " + secuencia_1)
		print("\n")
		print("Secuencia 2 : " + secuencia_2)
		print("\n")
		
	    #Biopython: Se entregan las secuencias creadas al azar y se alinean, ademas de entregar un puntaje.
		alignments = pairwise2.align.globalxx(secuencia_1, secuencia_2)
		print("Alineamiento entre la secuencia 1 y 2 : \n")
		print(format_alignment(*alignments[0]))
		print("//////////////////////////////////////////////////////////////////////////////////////////////////////\n")

		tamano_muestra = tamano_muestra + 1
		
	tiempo_final = time() - tiempo_inicial
	print("\n")
	print "Tiempo de ejecucion : ", tiempo_final, " segundos"
else:
    print "Necesario ejecutar con al menos dos parametros"
    print "python simulacion.py seq1 seq2"

