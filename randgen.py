import scipy.stats as stats
a, b = 0, 650
mu, sigma = 250, 100
dist = stats.truncnorm((a-mu)/sigma, (b-mu)/sigma, loc=mu, scale=sigma)
values=dist.rvs(5)
print(values)