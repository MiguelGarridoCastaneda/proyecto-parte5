from numpy import save
from algorithms import *
import random
from graph import *


# g = gridGraph(3)
# g = erdosRenyiGraph(200, 8500)
g = dorogovtsevMendesGraph(200)
# g = gilbertGraph(30, p=0.4)
# tree = DFS_R(g, 5)
# saveGraph(tree, g.typee)
# tree = DFS_I(g, 5)
# tree.typee = 8
# saveGraph(tree, g.typee)

# saveGraph(tree, g.typee)

# g = barasiAlbertGraph(30, 4)
# g = dorogovtsevMendesGraph(300)
# g = erdosRenyiGraph(30, 330)
# print(f"Número de aristas: {len(g.edges)}")
# m = g.createAdjMat()
# print(f"Matriz de adyacencia de dimensión: {m.shape}")
# print(m)
# dg = g.Dijkstra(5)
# saveGraph(dg, g.typee)
# print(g.edges.keys())
# kg = g.KruskalD()
# # print(kg.nodes)
# # print(kg.edges.keys())
# print(f"MST value: {kg.mst}")
# saveGraph(kg, g.typee)
# print(set(g.getNodes()))
# kg = g.KruskalI()# pendiente Kruskal inverso
pg = g.KruskalI()
# print()
# saveGraph(pg, g.typee)
