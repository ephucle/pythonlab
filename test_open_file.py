path = "running.txt"
finish_lines = [line for line in open(path) if "finish" in line]
print(len(finish_lines))