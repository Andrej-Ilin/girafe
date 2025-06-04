# Установка нужных библиотек


# Импорты
import numpy as np
import scipy.sparse as sp
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import implicit

# 1. Split data
def split_data(ratings, test_fraction=0.2):
    ratings = ratings.tocsr()
    train = ratings.copy()
    test = sp.lil_matrix(ratings.shape)

    np.random.seed(42)
    n_users = ratings.shape[0]
    users = np.random.choice(n_users, size=int(test_fraction * n_users), replace=False)

    for user in users:
        item_indices = ratings[user].indices
        if len(item_indices) == 0:
            continue
        test_item = np.random.choice(item_indices)
        train[user, test_item] = 0
        test[user, test_item] = 1

    train.eliminate_zeros()
    return train.tocsr(), test.tocsr()

# Разделяем
train_ratings, test_ratings = split_data(debug_dataset)
print("Train shape:", train_ratings.shape)
print("Test shape:", test_ratings.shape)

# 2. Train IALS
def train_ials(train_ratings, factors=64, regularization=0.1, iterations=20):
    model = implicit.als.AlternatingLeastSquares(
        factors=factors,
        regularization=regularization,
        iterations=iterations,
        use_gpu=False,
        dtype=np.float64
    )
    model.fit(train_ratings)
    return model

ials_model = train_ials(train_ratings)
print("IALS model trained.")

# 3. Calculate MRR@100
def mrr_at_k(model, train_ratings, test_ratings, k=100):
    user_ids, item_ids = test_ratings.nonzero()
    mrr_total = 0.0
    n = 0

    for user in np.unique(user_ids):
        recommended = model.recommend(user, train_ratings, N=k, filter_already_liked_items=False)
        recommended_items = [item for item, score in recommended]

        true_items = test_ratings[user].indices
        if len(true_items) == 0:
            continue

        first_hit = None
        for rank, item_id in enumerate(recommended_items, start=1):
            if item_id in true_items:
                first_hit = rank
                break

        if first_hit is not None:
            mrr_total += 1.0 / first_hit
        n += 1

    return mrr_total / n

mrr_ials = mrr_at_k(ials_model, train_ratings, test_ratings)
print(f"MRR@100 (IALS): {mrr_ials:.5f}")

# 4. Grid Search по гиперпараметрам
params_grid = {
    'factors': [32, 64, 128],
    'regularization': [0.01, 0.1, 1],
}

best_mrr = 0
best_params = None

for factors in params_grid['factors']:
    for regularization in params_grid['regularization']:
        model = train_ials(train_ratings, factors=factors, regularization=regularization)
        mrr = mrr_at_k(model, train_ratings, test_ratings)
        print(f"factors={factors}, reg={regularization} -> MRR={mrr:.5f}")

        if mrr > best_mrr:
            best_mrr = mrr
            best_params = (factors, regularization)

print("Best params:", best_params)

# 5. Item2Item Cosine Similarity
def compute_item2item_similarity(ratings):
    item_vectors = ratings.T
    similarity = cosine_similarity(item_vectors, dense_output=False)
    return similarity

i2i_similarities = compute_item2item_similarity(train_ratings)
print("Item2Item similarities computed.")

# 6. Compare similarities
# Сходства через эмбеддинги IALS
user_emb = ials_model.user_factors
item_emb = ials_model.item_factors
ials_similarity = cosine_similarity(item_emb)

# Сходства через классический item2item
i2i_similarity = i2i_similarities.toarray()

# Построим график
plt.figure(figsize=(10, 6))
plt.hist(ials_similarity.flatten(), bins=50, alpha=0.5, label='IALS similarities')
plt.hist(i2i_similarity.flatten(), bins=50, alpha=0.5, label='Item2Item similarities')
plt.legend()
plt.title('Distribution of Similarities')
plt.xlabel('Similarity')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()