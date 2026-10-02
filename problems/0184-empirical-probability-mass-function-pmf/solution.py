from collections import Counter

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    
    Args:
        samples: Iterable of integer samples
    
    Returns:
        List of (value, probability) tuples sorted by value ascending
    """
    # Chuyển về list để đếm được (và xử lý trường hợp generator)
    samples = list(samples)
    
    # Xử lý trường hợp rỗng
    if not samples:
        return []
    
    # Đếm tần suất xuất hiện của từng giá trị
    counts = Counter(samples)
    total = len(samples)
    
    # Tính xác suất và sắp xếp theo giá trị tăng dần
    pmf = [(value, count / total) for value, count in sorted(counts.items())]
    
    return pmf