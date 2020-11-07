def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}
    # process files
    for file in files:
        # add each file in the files
        s = file.rpartition("/")
        s = s[-1]
        if s not in cache:
            cache[s] = []
        cache[s].append(file)
    # process queries
    for query in queries:
        if query in cache:
            for file in cache[query]:
                result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
