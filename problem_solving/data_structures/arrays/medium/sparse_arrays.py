def matchingStrings(stringList, queries):
    results = []
    [results.append(stringList.count(i)) for i in queries]
    return results
