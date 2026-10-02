import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate descriptive statistics for a dataset.
    
    Args:
        data: List or NumPy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, std, percentiles, IQR
    """
    # Chuyển về numpy array để tính toán
    arr = np.asarray(data, dtype=float)
    N = len(arr)
    
    # 1. Mean - giá trị trung bình
    mean = float(np.mean(arr))
    
    # 2. Median - trung vị
    median = float(np.median(arr))
    
    # 3. Mode - giá trị xuất hiện nhiều nhất
    values, counts = np.unique(arr, return_counts=True)
    mode = float(values[np.argmax(counts)])
    
    # 4. Population variance - phương sai (chia cho N)
    variance = float(np.var(arr, ddof=0))
    
    # 5. Standard deviation - độ lệch chuẩn
    standard_deviation = float(np.sqrt(variance))
    
    # 6. Percentiles - tứ phân vị
    q25 = float(np.percentile(arr, 25))
    q50 = float(np.percentile(arr, 50))
    q75 = float(np.percentile(arr, 75))
    
    # 7. Interquartile Range (IQR)
    iqr = q75 - q25
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        'standard_deviation': standard_deviation,
        '25th_percentile': q25,
        '50th_percentile': q50,
        '75th_percentile': q75,
        'interquartile_range': iqr
    }