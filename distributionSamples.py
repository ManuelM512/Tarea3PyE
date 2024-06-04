from scipy.stats import binom, geom, poisson


def binomSamples(n, p, sizes):
    return [binom.rvs(n, p, size=size) for size in sizes]


def poissonSamples(L, sizes):
    return [poisson.rvs(L, size=size) for size in sizes]


def geomSamples(p, sizes):
    return [geom.rvs(p, size=size) for size in sizes]
