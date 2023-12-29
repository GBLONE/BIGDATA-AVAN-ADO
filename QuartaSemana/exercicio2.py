from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from kneed import KneeLocator

# Cria dados sintéticos
X, _ = make_blobs(n_samples=200, random_state=42, centers=4)
# Lista_x com número de grupos (k) e lista_y com as inércias
lista_x = []
lista_y = []
# Laço variando k
for k in range(2, 11):
    # Executa kmeans para K atual
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    # Adiciona inércia e k às listas
    lista_x.append(k)
    lista_y.append(kmeans.inertia_)
# Localiza cotovelo
knee = KneeLocator(lista_x, lista_y, curve='convex', direction='decreasing')
knee.plot_knee()
melhor_k = lista_x[knee.knee-2]
print('Melhor k:', melhor_k)
