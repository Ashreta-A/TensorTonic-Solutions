def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    recommended_k = recommended[:k]

    relevant_set = set(relevant)
    recommended_set = set(recommended_k)

    true_positives = len(recommended_set & relevant_set)

    precision = true_positives / len(recommended_k) if recommended_k else 0.0
    recall = true_positives / len(relevant_set) if relevant_set else 0.0

    return [precision, recall]