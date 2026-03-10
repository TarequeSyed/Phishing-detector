from analyser.scoring import combine_scores

score = combine_scores(
    heuristic=30,
    url=25,
    llm=80
)

print(score)