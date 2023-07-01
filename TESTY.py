import pandas as pd
import numpy as np

# Đọc dữ liệu từ file UI.csv và US.csv
UI_data = pd.read_csv('UI.csv')
US_data = pd.read_csv('US.csv')

# Chuyển đổi dữ liệu thành ma trận UI(u, i) và US(u, s)
UI_data = UI_data.set_index('User')
US_data = US_data.set_index('User')

# Tạo quần thể ban đầu
M = 100  # Số lượng cá thể trong quần thể
N = len(UI_data.columns)  # Số lượng sách trong thư viện
population = np.random.randint(0, 6, (M, N))  # Mỗi cá thể là một danh sách gợi ý sách

# Hàm tính điểm tương đồng giữa hai người dùng
def calculate_similarity(user1, user2):
    common_books = list(set(user1.index) & set(user2.index))
    ratings1 = user1.loc[common_books]
    ratings2 = user2.loc[common_books]
    return np.dot(ratings1, ratings2) / (np.linalg.norm(ratings1) * np.linalg.norm(ratings2))

# Hàm đề xuất sách cho new_user sử dụng SCFGA
def recommend_books(new_user, UI_data, US_data, population, top_n):
    # Tính toán điểm tương đồng giữa new_user và các users cũ
    similarities = []
    for user, ratings in UI_data.iterrows():
        similarity = calculate_similarity(new_user, ratings)
        similarities.append(similarity)

    # Lựa chọn topX cá thể tốt nhất dựa trên điểm tương đồng
    best_individuals = []
    for individual in population:
        similarity_score = np.dot(similarities, individual) / np.sum(similarities)
        best_individuals.append((individual, similarity_score))
    best_individuals.sort(key=lambda x: x[1])
    best_individuals = best_individuals[:top_n]

    # Gợi ý sách từ cá thể tốt nhất cho new_user
    recommended_books = []
    for individual, _ in best_individuals:
        for i, rating in enumerate(individual):
            if rating > 3 and UI_data.columns[i] not in recommended_books:
                recommended_books.append(UI_data.columns[i])

    return recommended_books[:top_n]  # Chỉ lấy ra top_n quyển sách có điểm rating cao nhất

# Thực hiện đề xuất sách cho new_user sử dụng SCFGA
new_user = pd.Series([4, 3, 2, 5, 1], index=US_data.columns)  # Điểm đánh giá của new_user cho 5 quyển sách phổ biến
top_n = 5  # Số lượng sách được gợi ý

recommended_books = recommend_books(new_user, UI_data, US_data, population, top_n)

# Xuất ra màn hình danh sách sách được gợi ý cho new_user
print("Recommended books for new user:")
for book in recommended_books:
    print(book)
