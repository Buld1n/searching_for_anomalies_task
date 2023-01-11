import pandas as pd
from scipy import stats


# Определяем функцию calculate_anomaly_score, которая вычисляет значения
# аномалийных очков для каждой строки датафрейма, используя статистический метод z-score.
def calculate_anomaly_score(df, params):
    return stats.zscore(df[params])


# Определяем функцию top_anomalies, которая добавляет колонку anomaly_score в датафрейм,
# содержащую значения аномалийных очков, сортирует датафрейм по этой колонке и возвращает первые top_n строк.
def top_anomalies(df, params, top_n):
    df["anomaly_score"] = calculate_anomaly_score(df, params).sum(axis=1)
    df.sort_values(by=['anomaly_score'], ascending=False, inplace=True)
    return df.head(top_n)

# Читаем данные из файла ueba.csv и сохраняем их в переменной df.
df = pd.read_csv("ueba.csv")

# Определяем параметры, которые будем использовать для обнаружения аномалий.
params = ["logon_count", "num_logons7", "num_share7", "num_file7"]

# Используем функцию top_anomalies, чтобы найти топ-5
# аномальных записей в датафрейме, сохраняем результат в переменной anomalies.
anomalies = top_anomalies(df, params, 5)

# Выводим результат - топ-5 аномальных записей.
anomalies.to_excel("anomalies.xlsx", index=False, sheet_name="Anomalies")
