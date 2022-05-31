import random
import json
from numpy import array


def create_reward_matrix(goal):  # Return a matrix of rewards for the agent
    global cells
    index = str(goal).split('.')
    index = [int(i) for i in index]
    all_reward = [[80, 80, 80, 80, 80, 80, 80, 80, 80],
                  [80, 85, 85, 85, 85, 85, 85, 85, 80],
                  [80, 85, 90, 90, 90, 90, 90, 85, 80],
                  [80, 85, 90, 95, 95, 95, 90, 85, 80],
                  [80, 85, 90, 95, 100, 95, 90, 85, 80],
                  [80, 85, 90, 95, 95, 95, 90, 85, 80],
                  [80, 85, 90, 90, 90, 90, 90, 85, 80],
                  [80, 85, 85, 85, 85, 85, 85, 85, 80],
                  [80, 80, 80, 80, 80, 80, 80, 80, 80]]
    reward_matrixf = all_reward[(4 - (index[0] - 1)):((4 - (index[0] - 1)) + 5)]
    for i, k in enumerate(reward_matrixf):
        reward_matrixf[i] = k[(4 - index[1]):((4 - index[1]) + 5)]
    return reward_matrixf


def update_records(data, end):  # Update info in PathFinder.json with what the agent has learned
    with open("PathFinder.json") as file:
        positions = json.loads(file.read())
    check = True
    for i in positions["positions"]:
        if i["goal"] == end:
            check = False
            index = positions["positions"].index(i)

    if check:
        raise Exception()

    positions["positions"][index] = data

    with open("PathFinder.json", "w") as file:
        file.write(json.dumps(positions))


def paths(s, e):  # Function to return the already existing information about the current start and end position
    with open("PathFinder.json") as file:
        positions = json.loads(file.read())
    for i in positions["positions"]:
        if i["goal"] == e and i["start"] == s:
            return i
    positions["positions"].append({"start": s, "goal": e, "rewards": [[0, 0, 0, 0, 0],
                                                                      [0, 0, 0, 0, 0],
                                                                      [0, 0, 0, 0, 0],
                                                                      [0, 0, 0, 0, 0],
                                                                      [0, 0, 0, 0, 0]],
                                   "moves": [[0.1, 1, -0.1, -0.1, -0.1],
                                             [0.1, 1, 1, -0.1, -1],
                                             [0.1, 1, 1, -1, -1],
                                             [0.1, 0.1, 0.1, -1, -1],
                                             [0.1, 0.1, 0.1, 0.1, -1]], "optralen": 100, "optra": []})
    with open("PathFinder.json", "w") as file:
        file.write(json.dumps(positions))

    return {"start": s, "goal": e, "rewards": [[0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0]], "moves": [[0.1, 1, -0.1, -0.1, -0.1],
                                                                           [0.1, 1, 1, -0.1, -1],
                                                                           [0.1, 1, 1, -1, -1],
                                                                           [0.1, 0.1, 0.1, -1, -1],
                                                                           [0.1, 0.1, 0.1, 0.1, -1]], "optralen": 100,
            "optra": []}


start_position = float(input('Starting Position: '))
goal = float(input('Ending Position: '))
cells = [1.0, 1.1, 1.2, 1.3, 1.4, 2.0, 2.1, 2.2, 2.3, 2.4, 3.0, 3.1, 3.2, 3.3, 3.4, 4.0, 4.1, 4.2, 4.3, 4.4, 5.0, 5.1,
         5.2, 5.3, 5.4]
movable_cells = [-1, 1, -0.1, 0.1]  # Possible moves
reward_matrix = create_reward_matrix(goal)
epochs = 100
rewards = 0
current_position = start_position
previous_position = 0
steps = 0
trajectory = [current_position]
info = paths(current_position, goal)

for i in range(epochs):  # Training
    while True:
        while True:
            move = random.choice(movable_cells)
            if round((current_position + move), 1) in cells and not ((current_position + move) == previous_position):
                break

        previous_position = current_position
        current_position = round(current_position + move, 1)
        index = str(current_position).split('.')
        index[0] = int(index[0])
        index[1] = int(index[1])
        index[0] = index[0] - 1

        reward = reward_matrix[index[0]][index[1]]
        rewards += reward

        index = str(previous_position).split('.')
        index[0] = int(index[0])
        index[1] = int(index[1])
        index[0] = index[0] - 1

        if info["rewards"][index[0]][index[1]] < reward:
            info["moves"][index[0]][index[1]] = move
            info["rewards"][index[0]][index[1]] = reward

        steps += 1
        trajectory.append(current_position)

        if current_position == goal:
            break
        print(1)

    if info["optralen"] > steps:
        info["optralen"] = steps
        info["optra"] = trajectory

    current_position = start_position
    previous_position = 0
    steps = 0
    trajectory = [current_position]

update_records(info, goal)
