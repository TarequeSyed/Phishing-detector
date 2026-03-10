def combine_scores(heuristic, url, llm):
    """
    Combine all the scores to get uniformed result.
    """

    final_score = (
        0.4 * heuristic + 
        0.3 * url + 
        0.3 * llm
    )

    if final_score > 100:
        final_score = 100
    
    return int(final_score)