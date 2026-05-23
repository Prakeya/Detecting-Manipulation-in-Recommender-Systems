from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import io, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

# -------------------------------
# LOAD DATA
# -------------------------------
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

ratings = ratings.sample(n=30000, random_state=42)

top_users = ratings['userId'].value_counts().head(150).index
top_movies = ratings['movieId'].value_counts().head(200).index
ratings = ratings[ratings['userId'].isin(top_users)]
ratings = ratings[ratings['movieId'].isin(top_movies)]

user_item_matrix = ratings.pivot_table(
    index="userId",
    columns="movieId",
    values="rating"
).fillna(0)

R = user_item_matrix.values
user_ids = list(user_item_matrix.index)
movie_ids = list(user_item_matrix.columns)

similarity = cosine_similarity(R)

# -------------------------------
# FUNCTIONS
# -------------------------------
def get_user_index(user_id):
    return user_ids.index(user_id) if user_id in user_ids else 0

def recommend(Rmat, sim, user_id):
    return sim[get_user_index(user_id)] @ Rmat

def jacobian(Rmat, sim, user_id, k=30, eps=1e-3):
    base = recommend(Rmat, sim, user_id)
    idx = np.argsort(base)[-k:]

    def f(x):
        Rcopy = Rmat.copy()
        ui = get_user_index(user_id)
        Rcopy[ui, idx] = x
        sim_new = cosine_similarity(Rcopy)
        return (sim_new[ui] @ Rcopy)[idx]

    x0 = base[idx].copy()
    n = len(x0)
    J = np.zeros((n,n))

    for i in range(n):
        x1, x2 = x0.copy(), x0.copy()
        x1[i]+=eps; x2[i]-=eps
        J[:,i]=(f(x1)-f(x2))/(2*eps)

    return J

def distortion(J):
    _, S, _ = np.linalg.svd(J)
    return (np.max(S)+1e-8)/(np.min(S)+1e-8), S

def explain(Sn, Sm):
    Sn, Sm = np.array(Sn), np.array(Sm)
    diff = Sm - Sn
    top = np.argsort(np.abs(diff))[-3:]
    return [
        f"Latent factor {i} heavily affected" for i in top
    ]

def manipulate(R):
    fake = np.zeros((15, R.shape[1]))
    fake[:, :10] = 5
    return np.vstack([R, fake])

def plot_graph(S1, S2):
    plt.figure()
    plt.plot(S1, label="Normal")
    plt.plot(S2, label="Manipulated")
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

# -------------------------------
# ROUTE
# -------------------------------
@app.route('/', methods=['GET','POST'])
def index():
    result=None

    if request.method=='POST':
        uid=int(request.form['user_id'])

        rec = recommend(R, similarity, uid)
        J = jacobian(R, similarity, uid)
        n_score, S1 = distortion(J)

        Rm = manipulate(R)
        sim_m = cosine_similarity(Rm)
        Jm = jacobian(Rm, sim_m, uid)
        m_score, S2 = distortion(Jm)

        is_manip = m_score > n_score*1.2

        result = {
            "normal": round(n_score,3),
            "manip": round(m_score,3),
            "status": "Manipulation Detected" if is_manip else "Normal",
            "plot": plot_graph(S1,S2),
            "is_manip": is_manip,
            "explain": explain(S1,S2) if is_manip else []
        }

    return render_template("index.html", result=result, users=user_ids[:50])

if __name__=='__main__':
    app.run(port=8000, debug=True)
