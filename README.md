# Water Quality Clustering for Pollution Hotspot Identification  
**Machine Learning Meets UN SDG 6: Clean Water and Sanitation**

---

![Project Banner](images/project_banner.png)  

---

## Table of Contents  
- [Project Overview](#project-overview)  
- [Motivation & Problem Statement](#motivation--problem-statement)  
- [Sustainable Development Goal (SDG) Context](#sustainable-development-goal-sdg-context)  
- [Machine Learning Approach](#machine-learning-approach)  
- [Dataset Description](#dataset-description)  
- [Data Preprocessing](#data-preprocessing)  
- [Modeling & Evaluation](#modeling--evaluation)  
- [Results & Insights](#results--insights)  
- [Ethical Considerations](#ethical-considerations)  
- [Repository Structure](#repository-structure)  
- [Setup & Usage Instructions](#setup--usage-instructions)  
- [Contributing](#contributing)  
- [Author & Contact](#author--contact)  
- [Acknowledgments](#acknowledgments)  
- [License](#license)  

---

## Project Overview  
Access to safe and clean water is vital for human health and environmental sustainability. This project leverages unsupervised machine learning techniques, specifically **K-means clustering**, to analyze water quality metrics and identify regions facing water pollution challenges. The objective is to provide actionable insights that support environmental agencies and policymakers in targeting water treatment and conservation efforts, directly addressing the **UN Sustainable Development Goal 6**.

---

## Motivation & Problem Statement  
Water contamination affects billions globally, leading to health crises and ecological damage. Traditional monitoring techniques are often limited by cost and spatial coverage, causing delays in detecting pollution spikes. By applying machine learning to publicly available water quality data, we aim to cluster regions based on chemical indicators, thereby detecting pollution hotspots efficiently and aiding timely intervention.

---

## Sustainable Development Goal (SDG) Context  
This project aligns with **SDG 6: Clean Water and Sanitation**, which aims to ensure availability and sustainable management of water for all by 2030. Identifying and mitigating polluted water sources is essential to reduce waterborne diseases and protect aquatic ecosystems, promoting equitable access to clean water.

---

## Machine Learning Approach  
- **Type:** Unsupervised Learning  
- **Algorithm:** K-means Clustering  
- **Rationale:** Clustering groups regions with similar water chemistry profiles, revealing hidden patterns without labeled outputs. The elbow method determines the optimal cluster count, balancing model simplicity and performance.

---

## Dataset Description  
- **Source:** [Water Potability Dataset, Kaggle](https://www.kaggle.com/datasets/sogun3/water-potability)  
- **Features:** Includes physicochemical water properties such as:  
  - pH  
  - Hardness  
  - Solids (ppm)  
  - Chloramines  
  - Sulfate  
  - Conductivity  
  - Organic Carbon  
  - Trihalomethanes  
  - Turbidity  
- **Target:** Potability label (binary), used only for reference, **not** in clustering.

---

## Data Preprocessing  
- Removed records with missing values to ensure data integrity.  
- Selected key water quality features based on domain relevance.  
- Scaled features using **StandardScaler** to normalize data distributions and avoid bias from feature magnitude differences.  
- Verified data distributions and removed outliers where necessary.

---

## Modeling & Evaluation  
- Applied the **Elbow Method** by plotting inertia over cluster counts from 1 to 10 to identify the optimal `k` (number of clusters).  
- Selected `k=3` based on the elbow point to balance granularity and interpretability.  
- Trained K-means on scaled data and assigned cluster labels.  
- Visualized cluster separation using scatter plots of key features (e.g., pH vs. Sulfate).  
- Analyzed cluster centroids to interpret pollution levels and chemical characteristics.

---

## Results & Insights  
- Three distinct clusters emerged:  
  - **Cluster 0:** Characterized by high sulfate and turbidity levels indicating potential pollution.  
  - **Cluster 1:** Moderate contamination with intermediate chemical concentrations.  
  - **Cluster 2:** Low contamination, likely representing cleaner water sources.  
- These clusters enable environmental agencies to prioritize sampling and treatment resources effectively.  
- The unsupervised approach provides scalable, cost-effective water quality surveillance.

---

## Ethical Considerations  
- **Data Bias:** The dataset may underrepresent rural or less-monitored areas, risking unequal attention. Future work should incorporate more geographically diverse data.  
- **Fairness:** Clusters should guide support without stigmatizing communities. Transparency in communicating findings is crucial.  
- **Sustainability:** Data-driven identification promotes efficient resource allocation, aligning with equitable and sustainable water management goals.  
- **Privacy:** Dataset is anonymized and does not include sensitive personal information.

---

## Repository Structure  
