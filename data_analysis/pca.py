import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_pca_2d(X_scaled, df):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    print("Explained variance ratio for 2 components:", pca.explained_variance_ratio_)

    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['Sex'], cmap='plasma', alpha=0.75)
    plt.xlabel('First principal component')
    plt.ylabel('Second principal component')
    plt.title('PCA of Suicide Rates Dataset')
    plt.colorbar(label='Sex (0: Female, 1: Male)')
    plt.show()

def plot_pca_3d(X_scaled, df):
    pca = PCA(n_components=3)
    X_pca = pca.fit_transform(X_scaled)
    print("Explained variance ratio for 3 components:", pca.explained_variance_ratio_)
    print("Total variance captured by 3 components:", sum(pca.explained_variance_ratio_))

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    colors = ['blue', 'red']  # Blue for Female, Red for Male
    markers = ['o', '^']

    for sex, color, marker in zip(df['Sex'].unique(), colors, markers):
        ax.scatter(X_pca[df['Sex'] == sex, 0], X_pca[df['Sex'] == sex, 1], X_pca[df['Sex'] == sex, 2], 
                   c=color, marker=marker, alpha=0.75, label='Male' if sex == 1 else 'Female')

    ax.set_xlabel('First principal component')
    ax.set_ylabel('Second principal component')
    ax.set_zlabel('Third principal component')
    ax.set_title('3 Component PCA of Suicide Rates Dataset')
    ax.legend()
    plt.show()



