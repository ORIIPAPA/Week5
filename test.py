import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('water_potability.csv')

# Select relevant features
features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity']

# Drop missing values
df = data[features].dropna()

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Elbow method to find optimal clusters
inertia = []
for k in range(1, 10):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

plt.plot(range(1, 10), inertia, 'bo-')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# Train with chosen k (e.g., 3)
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
df['Cluster'] = clusters

# Visualize clusters
sns.scatterplot(data=df, x='ph', y='Sulfate', hue='Cluster', palette='Set1')
plt.title('Water Quality Clusters')
plt.show()
