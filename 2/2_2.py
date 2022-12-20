# A,X - ROCK
# B,Y - PAPER
# C,Z - SCISSORS

file = open("2.txt","r")
points_dict = {"X" : 1, "Y" : 2, "Z" : 3}
decider_dict = {
    tuple(["A","X"]): 3,
    tuple(["A","Y"]): 6,
    tuple(["A","Z"]): 0,
    tuple(["B","X"]): 0,
    tuple(["B","Y"]): 3,
    tuple(["B","Z"]): 6,
    tuple(["C","X"]): 6,
    tuple(["C","Y"]): 0,
    tuple(["C","Z"]): 3
}
conversion_dict = {
    tuple(["A","X"]): "Z",
    tuple(["A","Y"]): "X",
    tuple(["A","Z"]): "Y",
    tuple(["B","X"]): "X",
    tuple(["B","Y"]): "Y",
    tuple(["B","Z"]): "Z",
    tuple(["C","X"]): "Y",
    tuple(["C","Y"]): "Z",
    tuple(["C","Z"]): "X"
}

points = 0

def count_points(r, o):
    r = conversion_dict[o,r]
    print(o,r, decider_dict[o,r] + points_dict[r])
    return decider_dict[o,r] + points_dict[r]

    

for line in file:
    opponent = line.split(" ")[0]
    response = line.split(" ")[1][0:1]
    points += count_points(response, opponent)

print(points)