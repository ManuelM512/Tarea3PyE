from diagramMaker import boxPlotter, histogramer
from probAndStatsAuxiliar import mode, median


def makeExercise(exerciseNumber, distributionName, distributionSamples, labels):
    boxPlotter(distributionName, distributionSamples, labels)
    histogramer(distributionName, distributionSamples, labels)
    text = ""
    for distribution in distributionSamples:
        sortedDistribution = distribution.copy()
        sortedDistribution.sort()

        size = len(sortedDistribution)
        distributionMode = mode(sortedDistribution)
        distributionMedian = median(sortedDistribution)
        avg = sum(sortedDistribution) / len(sortedDistribution)

        data = (
            f"Median: {distributionMedian}\n"
            + f"Mode: {distributionMode}\nAvg.: {avg}\n"
        )
        content = distributionName + f" size: {size}\n" + data + "\n"
        writeToFile(f"Exercise{exerciseNumber}.txt", content)
        text += content
    return text


def writeToFile(filename, content, folder="Diagrams"):
    with open(folder + "/" + filename, "a") as file:
        file.write(content)
