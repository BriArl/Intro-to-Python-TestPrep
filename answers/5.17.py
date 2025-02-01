par = int(input())
strokes = int(input())

# Check if par is valid
if par not in [3, 4, 5]:
    print("Error")
else:
    # Determine the score name
    if strokes == par - 2:
        print("Eagle")
    elif strokes == par -1:
        print("Birdie")
    elif strokes == par:
        print("Par")
    elif strokes == par + 1:
        print("Bogey")
    else:
        print("Error")