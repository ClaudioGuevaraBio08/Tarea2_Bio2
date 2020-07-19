Fasta 1: MIEVFLFGIVLGLIPIT
Fasta 2: MVEPILLGIVLGLVPVT
Fasta 3: MVEALLSGIVLGLIPITL

Si desea ver en detalle de todos los alineamientos entre las secuencias, ejecute en la terminal el comando:

	python tarea2.py secuencia1 secuencia2


Si solo quiere saber el resultado de los alineamientos (score), ejecute por la terminal:

	1. python tarea2.py secuencia1 secuencia 2 | grep "Score" | awk 'BEGIN{OFS="\t"}{print $1}' > score_secuencias.txt
	2. vim score_secuencias.txt
	3. En vim ejecutar => :%s/Score=//g
	4. En vim ejecutar => :wq

*Lo anterior creara el archivo score_secuencias.txt.

	4. Luego abrimos R y cargamos los datos con: datos <- read.table("ruta donde este el archivo", header = FALSE).
	*En mi caso sería => datos <- read.table("/home/claudio/Documentos/Bio 2/Tarea/score_secuencias.txt", header = FALSE)
	5. histograma => hist (x=datos$V1, col=456, main="Frecuencia de puntajes de las secuencias", xlab="Score", ylab="Frecuencia")
	6. Calcular los p-value => datos$valorp <- 1 - ecdf(datos$V1)(datos$V1)
	7. Filtrar los p-value menores que 0.01 => datos[which(datos$valorp<=0.01),]



