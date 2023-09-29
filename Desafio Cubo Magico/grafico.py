import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d

# Definindo as coordenadas dos vértices do cubo
vertices = [
    (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),  # Face frontal (z = 0)
    (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)   # Face traseira (z = 1)
]

# Definindo as arestas do cubo
arestas = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Arestas da face frontal
    (4, 5), (5, 6), (6, 7), (7, 4),  # Arestas da face traseira
    (0, 4), (1, 5), (2, 6), (3, 7)    # Arestas que conectam as duas faces
]

# Definindo as cores para cada face do cubo
cores = [
    'red', 'green', 'blue', 'yellow', 'cyan', 'magenta'
]

# Criando uma figura e um objeto Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhando as faces do cubo com cores
for i in range(6):
    face = art3d.Polygon3D([vertices[j] for j in range(4)], alpha=0.5)
    face.set_facecolor(cores[i])
    ax.add_collection3d(face)

# Desenhando as arestas do cubo
for a in arestas:
    ax.plot([vertices[a[0]][0], vertices[a[1]][0]],
            [vertices[a[0]][1], vertices[a[1]][1]],
            [vertices[a[0]][2], vertices[a[1]][2]], c='black')

# Configurando os limites dos eixos
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])

# Exibindo a figura
plt.show()