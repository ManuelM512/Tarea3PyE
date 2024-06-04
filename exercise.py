from diagramMaker import boxPlotter, histogramer
from probAndStatsAuxiliar import mode


def makeExercise(exerciseNumber, distributionName, distributionSamples, labels):
    boxPlotter(distributionName, distributionSamples, labels)
    histogramer(distributionName, distributionSamples, labels)
    for distribution in distributionSamples:
        sortedDistribution = distribution.copy()
        sortedDistribution.sort()
        size = len(sortedDistribution)
        distributionMode = mode(sortedDistribution)
        median = (
            sortedDistribution[size // 2]
            if size % 2 != 0
            else (sortedDistribution[size // 2] + sortedDistribution[size // 2 - 1]) / 2
        )
        avg = sum(sortedDistribution) / len(sortedDistribution)
        data = f"Median: {median}\nMode: {distributionMode}\nAvg.: {avg}\n"
        writeToFile(
            f"Exercise{exerciseNumber}.txt",
            distributionName + f" size: {size}\n" + data + "\n",
        )


def writeToFile(filename, content):
    with open(filename, "a") as file:
        file.write(content)
