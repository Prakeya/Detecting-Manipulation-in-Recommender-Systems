# Detecting-Manipulation-in-Recommender-Systems

A Jacobian-based framework for detecting manipulation and hidden bias in recommender systems. This project provides a robust methodology to identify and analyze how malicious injections or biases in the rating matrix affect recommendation outcomes.

## 🚀 Overview

Recommender systems are increasingly targeted by "shilling attacks" or "push attacks," where fake user profiles are created to bias recommendations towards specific items. This project implements a cutting-edge detection system based on **Jacobian sensitivity analysis** and **Spectral Distortion**, providing both detection scores and visual explainability.

---

## ✨ Features

- **Real-time Detection**: Identify if a user's recommendation list has been manipulated.
- **Sensitivity Analysis**: Measures the "fragility" of the recommender system using Jacobian matrices.
- **Spectral Visualization**: Plots the singular value distribution to visually distinguish between normal and manipulated states.
- **Explainability**: Identifies which latent factors in the recommendation space are most affected by the detected manipulation.
- **Web Dashboard**: An intuitive Flask-based interface for analyzing user-specific recommendation health.

---

## 🛠️ Project Structure

- `app.py`: Core Flask application containing the recommendation logic and detection algorithms.
- `templates/index.html`: Modern, responsive web interface for the detector.
- `A17_Report.pdf`: Comprehensive theoretical report detailing the mathematical foundation and experimental results.
- `Detecting-Manipulation-in-Recommender-Systems.pdf`: Official project presentation/slide deck.
- `requirements.txt`: Python package dependencies.

---

## 🧪 Methodology

The core of the detection logic rests on two advanced mathematical concepts:

### 1. Jacobian Sensitivity Analysis
The system calculates the **Jacobian matrix** $(\mathbf{J})$ of the recommendation function $f(\mathbf{R})$ with respect to the rating matrix $\mathbf{R}$.
$$J_{ij} = \frac{\partial f_i}{\partial R_j}$$
A high sensitivity indicates that small changes in the input ratings lead to disproportionately large changes in recommendations, a hallmark of successful manipulation.

### 2. SVD and Spectral Distortion
By applying **Singular Value Decomposition (SVD)** to the Jacobian matrix, we extract the singular values $S = \{\sigma_1, \sigma_2, \dots, \sigma_n\}$. The **Spectral Distortion Score** is calculated as the condition number:
$$\text{Distortion Score} = \frac{\sigma_{\text{max}}}{\sigma_{\text{min}}}$$
Manipulation typically causes "spikes" in specific singular values, significantly increasing the distortion score compared to a healthy, balanced system.

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- `pip` package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Prakeya/Detecting-Manipulation-in-Recommender-Systems.git
   cd Detecting-Manipulation-in-Recommender-Systems
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Data Requirements**:
   Place your `ratings.csv` and `movies.csv` (standard MovieLens format) in the root directory. The app expects columns:
   - `ratings.csv`: `userId`, `movieId`, `rating`
   - `movies.csv`: `movieId`, `title`

### Running the App
```bash
python app.py
```
The server will start at `http://127.0.0.1:8000`.

---

## 📊 Sample Output
| Metric | Normal State | Manipulated State |
| :--- | :--- | :--- |
| Distortion Score | $\sim 5.2$ | $\sim 28.4$ |
| Stability | High | Critical Alert |

---

## 📜 Acknowledgments
Developed as part of the **Mathematics for Computing (MFC)** curriculum, focusing on the application of Linear Algebra and Calculus in AI/ML safety.
