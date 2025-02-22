frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

try:
        index = int(input().strip())
        print(frameworks[index])
except (IndexError, ValueError):
    print("Error")