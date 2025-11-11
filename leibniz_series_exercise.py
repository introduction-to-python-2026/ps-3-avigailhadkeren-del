def approximate_pi(n_terms):
    series_sum = 0
    for n in range(n_terms):
        series_sum = series_sum + ((-1) ** n) / (te_2 * n + 1)
    
    approximate_pi = 4 * (1 - series_sum)
    return approximare_pi

for terms in [1, 10 , 100, 1000, 10000)
  print(f"{terms}terms:
{approximate_pi(terms)}")  
