# Book Recommender using CF and GA
 A Recommender System using Collaborative Filtering and Genetic Algorithm. We implemented a paper with a novel approach in building a robust recommender system named BLIGA to solve problems commonly seen in such systems, such as cold-start and sparsity.
 
 The BLIGA consists of 2 main filtering levels:
 1. Semantic similarity. This is the level of similarity between features of items in a recommended list.
 2. Total predicted score. This is the fitness value of each recommended list, calculated by using the similarity between users and the AU (active user).

We modified the original BLIGA and tuned the hyperparameters. We also made some experiments to test the performance of the system.

Then we implemented a hyperparameter combination with top performance in a UI representing a book recommendation system in a digital library. The UI design is based on that of [UEH Smart Digital Library](https://smartlib.ueh.edu.vn/), a key service of UEH University in Vietnam.

We have reported our process of designing, implementing, and testing the system and related problems in our final report.
(Note: The content of the report is written entirely in Vietnamese)

## Some related concepts

1. User to Product Filtering
---
![image](https://github.com/Neyung/UEH500/assets/120383829/119fd016-d0c6-4b30-9076-97f9572f0675)
---

2. Content-Based Filtering
---
![image](https://github.com/Neyung/UEH500/assets/120383829/24c672e8-b2e3-433e-bcb3-09615b7e0eb8)
---

3. Hybrid Filtering
---
![image](https://github.com/Neyung/UEH500/assets/120383829/2bc25b09-55ee-472e-92e3-1fd3f39f5099)
---

4. BLIGA
---
![image](https://github.com/Neyung/UEH500/assets/120383829/f4d57a1e-0892-444b-ad72-e0c80b8bd182)
---

# DEMO
To be able to use the interface, please use: main.py - [[Here](https://github.com/Neyung/UEH500/blob/main/UI/main.py)]

---

https://github.com/Neyung/UEH500/assets/120383829/02313703-c270-4c83-81ad-c76d4778303d

---

# GUIDELINES
Our final Report - [[Here](https://drive.google.com/file/d/1yQ1gsgIAjDEdUfG6A45Dg8vtQQ_4VkCH/view?usp=sharing)]

[BLIGA](Algorithm/main.ipynb)

[The UI for BLIGA](UI/main.py)

[Statistical Analysis of datasets](Algorithm/statistics.ipynb)
