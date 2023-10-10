import random
import matplotlib.pyplot as plt
import networkx as nx

class Graphe:
    def __init__(self, n):
        self.n = n
        self.matrice_adjacence = [[0] * n for _ in range(n)]
        self.coloriage = []

    def ajouter_arete(self, u, v):
        self.matrice_adjacence[u][v] = 1
        self.matrice_adjacence[v][u] = 1

    def genererGraphe3Coloriable(self):
        couleurs = ["red", "green", "blue"]
        
        # Étape 1 : Assigner une couleur aléatoire à chaque nœud
        self.coloriage = [random.choice(couleurs) for _ in range(self.n)]

        # Étape 2 : Générer la matrice d'adjacence
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.coloriage[i] != self.coloriage[j]:
                    # Relier les nœuds avec une probabilité de 1/2
                    tirage = random.random()
                    if tirage < 0.5:
                        self.ajouter_arete(i, j)

        return self
    
    def afficher_graphe(self):
        print("Matrice d'adjacence du graphe :")
        for ligne in self.matrice_adjacence:
            print(ligne)

        
        print("Tableau des couleurs :")
        print(graphe.coloriage)

        print("\nColoriage du graphe :")
        for i, couleur in enumerate(self.coloriage):
            print(f"Sommet {i + 1}: {couleur}")
    
    def afficher_graphe_graphiquement(self):
        G = nx.Graph()
        for i in range(self.n):
            G.add_node(i, color=self.coloriage[i])

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.matrice_adjacence[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.spring_layout(G)
        node_colors = [G.nodes[node]['color'] for node in G.nodes]

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, font_color='white')
        plt.title("Graphe 3-Coloriable")
        plt.show()

# Exemple d'utilisation
n = 20
graphe = Graphe(n).genererGraphe3Coloriable()

# Afficher le graphe avec les couleurs correspondantes
graphe.afficher_graphe()

# Afficher le graphe avec les couleurs correspondantes
graphe.afficher_graphe_graphiquement()