# Detecting Manipulation in Recommender Systems
### A Jacobian-based framework for identifying hidden bias and shilling attacks.

---

## Overview

Recommender systems are increasingly targeted by **shilling attacks** — where fake user profiles are injected to push specific items up the rankings. This project implements a detection system using **Jacobian Sensitivity Analysis** and **Spectral Distortion** to identify manipulation, measure system fragility, and explain which parts of the recommendation space are compromised.

Built as a Flask web dashboard, it provides both detection scores and visual explainability for user-specific recommendation health.

---

## How It Works

### 1. Jacobian Sensitivity Analysis

The system computes the Jacobian matrix **J** of the recommendation function f(**R**) with respect to the rating matrix **R**:
J_ij = ∂f_i / ∂R_j

High sensitivity means small changes in input ratings cause disproportionately large shifts in recommendations — a hallmark of successful manipulation.

### 2. SVD & Spectral Distortion

Singular Value Decomposition is applied to the Jacobian, extracting singular values σ₁, σ₂, ... σₙ. The **Spectral Distortion Score** is the condition number:
Distortion Score = σ_max / σ_min

Manipulation causes spikes in specific singular values, sharply inflating this score compared to a healthy system.

---

## Sample Output

| Metric | Normal State | Manipulated State |
|---|---|---|
| Distortion Score | ~5.2 | ~28.4 |
| Stability | High | Critical Alert |

---

## Features

- **Real-time Detection** — identifies if a recommendation list has been manipulated
- **Sensitivity Analysis** — measures system fragility via Jacobian matrices
- **Spectral Visualisation** — plots singular value distribution for normal vs manipulated states
- **Explainability** — pinpoints which latent factors are most affected
- **Web Dashboard** — Flask-based interface for per-user recommendation health analysis

---

## Project Structure
├── app.py                                          # Flask app, recommendation logic, detection algorithms

├── templates/

│   └── index.html                                  # Web interface

├── ratings.csv                                     # MovieLens ratings (userId, movieId, rating)

├── movies.csv                                      # MovieLens metadata (movieId, title)

├── requirements.txt                                # Python dependencies

├── A17_Report.pdf                                  # Theoretical report and experimental results

└── Detecting-Manipulation-in-Recommender-Systems.pdf  # Project presentation

---

## Setup & Installation

**Prerequisites:** Python 3.8+, pip

```bash
# Clone the repo
git clone https://github.com/Prakeya/Detecting-Manipulation-in-Recommender-Systems.git
cd Detecting-Manipulation-in-Recommender-Systems

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Server starts at `http://127.0.0.1:8000`

**Data:** Place `ratings.csv` and `movies.csv` (standard MovieLens format) in the root directory.

---

## Acknowledgements

Developed as part of the **Mathematics for Computing (MFC)** curriculum, applying Linear Algebra and Calculus to AI/ML safety problems.

---

## Team

**Prakeya S · Harshini Sree · Thiyaanesh N R · Yuvanidhi R**

*Developed for academic and research purposes.*
