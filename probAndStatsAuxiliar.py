"""
This module contains a function for finding the mode in a sorted distribution.

Functions:
- mode(sortedDistribution): Finds the mode in a sorted distribution and returns a list of the most frequent elements.
- compareMode(actual, tempMax): Auxiliar to mode. Compares Actual value to the temporaries maximum values. 

"""


def mode(sortedDistribution):
    """
    Finds the mode in a sorted distribution and returns a list of the most frequent elements.

    Args:
        sortedDistribution (list): A sorted list representing a distribution.

    Returns:
        list: A list of the most frequent elements in the distribution.

    """
    tempMax = [["Actual max number", 0]]
    actual = ["Actual number", 1]
    for i in range(len(sortedDistribution)):
        if sortedDistribution[i] == actual[0]:
            actual[1] += 1
        else:
            compareMode(actual, tempMax)
            if i != len(sortedDistribution) - 1:
                actual[0] = sortedDistribution[i]
                actual[1] = 1
    compareMode(actual, tempMax)
    return [tempMax[i][0] for i in range(len(tempMax))]


def compareMode(actual, tempMax):
    """
    Compare the mode of a given number with the current maximum mode.

    Parameters:
    actual (list): A list containing the number and its frequency.
    tempMax (list): A list containing the current maximum/s mode, with it's frequency/ies

    Returns:
    None: Returns None if the frequency of the given number is less than the current maximum mode, otherwise returns None.

    """
    actualNumber = actual[0]
    actualAmount = actual[1]
    if actualAmount < tempMax[0][1]:
        return None
    if actualAmount > tempMax[0][1]:
        tempMax.clear()
    tempMax.append([actualNumber, actualAmount])
