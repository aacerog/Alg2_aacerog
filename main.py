import math
import csv
import time


class HeapMin:

    
    def __init__(self):
        self.nos = 0
        self.heap = []

    def adicional(self, u, indice):
        self.heap.append([u, indice])
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def mostra_heap(self):
        print("la estructura es la siguiente:")
        nivel = int(math.log(self.nos, 2))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(self.heap[a])
                a += 1
            print("")
        for i in range(self.nos-a):
            print(self.heap[a])
            a += 1
        print("")

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                p = f
        return x

    def tamano(self):
        return self.nos

    def menor_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return "esta vacio"

    def hijo_izquierda(self, u):
        if self.nos >= 2*u:
            return self.heap[2*u-1]
        return "no tiene un hijo"

    def hijo_derecha(self, u):
        if self.nos >= 2*u+1:
            return self.heap[2*u]
        return "no tiene un hijo"

    def pai(self, u):
        return self.heap[u // 2]


class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adicionar_arista(self, u, v, peso):
        self.grafo[u-1][v-1] = peso

    def mostrar_matriz(self):
        print("Matriz de adyacencia:")
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origen):
        costo = [[-1, 0] for i in range(self.vertices)]
        costo[origen - 1] = [0, origen]
        h = HeapMin()
        h.adicional(0, origen)
        while h.tamano() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:
                    if costo[i][0] == -1 or costo[i][0] > dist + self.grafo[v-1][i]:
                        costo[i] = [dist + self.grafo[v-1][i], v]
                        h.adicional(dist + self.grafo[v-1][i], i+1)
        return costo




archivoDistancia="distancia.csv"
archivoTiempo="tiempo.csv"

aristas=[]
matrizDistancia=[]
matrizTiempo=[]
lista_abierta=["Bogota","Cali", "Medellin", "Barranquilla", "Cartagena", 
"Cucuta", "Bucaramanga", "Pereira", "Santa Marta", "Ibague", "Pasto","Manizales",
"Neiva", "Villavicencio", "Armenia"]

with open(archivoTiempo, "r") as archivo:
    lector=csv.reader(archivo, delimiter=",")
    for i in lector:
        if aristas==[]:
            aristas=i[1:]
        else:
            matrizTiempo.append(i[1:])

with open(archivoDistancia, "r") as archivo:
    lector=csv.reader(archivo, delimiter=",")
    next(archivo, None)
    for i in lector:
      matrizDistancia.append(i[1:])

def hstomin(tiempo):
    tm=tiempo.split(":")
    min=(int(tm[0])*60)+int(tm[1])
    return min
  
def mintohs(tiempo):
    hs=tiempo/60
    mn=tiempo%60
    tm=str(hs)+":"+str(mn)
    return tm


g = Grafo(15)
for i in range (15):
    for j in range(15):
        if(i==j):
            pass
        else:
            g.adicionar_arista(i+1,j+1,int(matrizDistancia[i][j]))

t = Grafo(15)
for i in range (15):
    for j in range(15):
        if(i==j):
            pass
        else:
            t.adicionar_arista(i+1,j+1,int(hstomin(matrizTiempo[i][j])))



inicio=str(input("Origen: "))
destino=str(input("Destino: "))

start=time.time()

resultado_dijkstra = g.dijkstra(lista_abierta.index(inicio)+1)
print(resultado_dijkstra[lista_abierta.index(destino)][0])
stop=time.time()
print("Tiempo 1: "+ str(stop-start))



aristas=[]
matrizDistancia=[]
matrizTiempo=[]
lista_abierta=["Bogota","Cali", "Medellin", "Barranquilla", "Cartagena", 
"Cucuta", "Bucaramanga", "Pereira", "Santa Marta", "Ibague", "Pasto","Manizales",
"Neiva", "Villavicencio", "Armenia"]


start=time.time()


resultado_dijkstra2 = t.dijkstra(lista_abierta.index(inicio)+1)

print(resultado_dijkstra2[lista_abierta.index(destino)][0])

stop=time.time()
print("Tiempo 2: "+ str(stop-start))