def approximate_pi(n_terms):
    series sum = 0
    for n = 1 to n_terms:
        series_sum = series_sum + ((-1) ** n) / (2 * n + 1)
approximate_pi = 4 * (1 - series_sum)
return
