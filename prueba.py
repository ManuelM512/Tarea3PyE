from distributionSamples import binomSamples
from exercise import makeExercise

n = 100
p = 0.35

labels = ["100 samples", "1000 samples", "10000 samples", "100000 samples"]
binomDistributions = binomSamples(n, p, [100, 1000, 10000, 100000])
makeExercise("1", "Binom distribution", binomDistributions, labels)
