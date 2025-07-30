# Biodiversity Endangerment Analysis

This project analyses biodiversity data from national parks in the United States to explore how species are distributed across conservation statuses and biological categories, with a specific focus on endangered species.

## 🔍 Objective

To investigate species endangerment patterns by:
- Conservation status
- Biological category (e.g., mammal, bird, plant)
- National park

## 📊 Key Insights

### 1. Species by Conservation Status

| Conservation Status     | Count     |
|-------------------------|-----------|
| Not Endangered          | 24,752     |
| Species of Concern      | 732       |
| Endangered              | 80        |
| Threatened              | 44        |
| In Recovery             | 24        |

Most species observed are not endangered.

### 2. Endangered Species by Category

| Category          | Endangered Count |
|------------------|------------------|
| Vascular Plant    | 19,560           |
| Bird              | 2,364            |
| Nonvascular Plant | 1,332            |
| Mammal            | 1,200            |
| Fish              | 524              |
| Amphibian         | 328              |
| Reptile           | 324              |

> Vascular plants dominate both the overall dataset.

### 3. Percentage Insights

- **Percentage of Endangered Observations**: 0.31%  
- **Percentage of Observations that are Vascular Plants**: 76.31%

### 4. Endangered Observations per National Park

Each park has 20 endangered species observations:

- Bryce National Park  
- Great Smoky Mountains National Park  
- Yellowstone National Park  
- Yosemite National Park  

This suggests a balanced distribution in observation effort.

## 📈 Visualisations

- Bar chart of species by conservation status
- Bar chart of endangered species by category

## ✅ Requirements

- Python 3.10+
- pandas
- matplotlib
- seaborn

Install dependencies with:

```bash
pip install -r requirements.txt