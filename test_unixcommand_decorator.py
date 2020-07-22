def unixcommand(f):
    def g(filenames):
        printlines(out for line in readlines(filenames) for out in f(line))
    return g

@unixcommand
def cat(line):
    yield line

@unixcommand
def lowercase(line):
    yield line.lower()