from diagramMaker import boxPlotter, histogramer
from probAndStatsAuxiliar import mode, median, variance


def makeExercise(exerciseNumber, distributionName, distributionSamples, labels):
    boxPlotter(distributionName, distributionSamples, labels)
    histogramer(distributionName, distributionSamples, labels)
    text = ""
    for distribution in distributionSamples:
        sortedDistribution = distribution.copy()
        sortedDistribution.sort()

        size = len(sortedDistribution)
        distributionMode = mode(sortedDistribution)
        dModeStr = list2str(distributionMode, ", ")
        distributionMedian = median(sortedDistribution)
        avg = sum(sortedDistribution) / len(sortedDistribution)
        empVariance = variance(distribution)

        data = (
            f"Median: {distributionMedian}\n"
            + f"Mode: {dModeStr}\nAvg.: {avg}\n"
            + f"Empirical variance: {empVariance}\n"
        )
        content = distributionName + f" size: {size}\n" + data + "\n"
        writeToFile(f"Exercise{exerciseNumber}.txt", content)
        text += content
    return text


def writeToFile(filename, content, folder="Diagrams"):
    with open(folder + "/" + filename, "a") as file:
        file.write(content)


def list2str(list, concatText=" "):
    values2str = [str(value) for value in list]
    resultStr = concatText.join(values2str)
    return resultStr
