import numpy as np

def detect_outliers_zscore(values, threshold=2.0):
    data = np.array(values)

    mean = np.mean(data)
    std = np.std(data)

    z_scores = abs((data - mean) / std)

    outliers = data[z_scores > threshold]

    return outliers.tolist()


metrics = [10.0, 12.0, 12.0, 13.0, 12.0, 11.0, 14.0, 100.0, 12.0]

outliers = detect_outliers_zscore(metrics, threshold=2.0)

print(outliers)