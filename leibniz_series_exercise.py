def approximate_pi(n_terms):
    series sum = 0
    for n in range(n_terms):
        series_sum = series_sum + ((-1) ** n) / (2 * n + 1)
    
    approximate_pi = 4 * (1 - series_sum)
    return
for terms in [1, 10 , 100, 1000, 10000)
  print(f"{terms}terms:
{approximate_pi(terms)}")  
