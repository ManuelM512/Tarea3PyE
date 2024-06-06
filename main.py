from distributionSamples import binomSamples, geomSamples, poissonSamples
from exercise import makeExercise


def main():
    n = 100
    sizes = [100, 1000, 10000, 100000]
    labels = ["100 samples", "1000 samples", "10000 samples", "100000 samples"]

    # Ejercicio 1 - Binomial
    p = 0.35
    binomDistributions = binomSamples(n, p, sizes)
    resultsBinom = makeExercise(1, "Binom", binomDistributions, labels)
    print(resultsBinom)

    # Ejercicio 2 - Geométrica
    p = 0.08
    geomDistributions = geomSamples(p, sizes)
    resultsGeom = makeExercise(2, "Geom", geomDistributions, labels)
    print(resultsGeom)

    # Ejercicio 3 - Poisson
    mu = 30
    poissonDistributions = poissonSamples(mu, sizes)
    resultsPoisson = makeExercise(3, "Poisson", poissonDistributions, labels)
    print(resultsPoisson)


main()
