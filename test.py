def robot_collisions(N, A):
    # Create a list of robots with their health and direction
    robots = [(health, direction) for health, direction in A]

    while True:
        collisions = []
        for i in range(N - 1):
            if robots[i][1] == 1 and robots[i + 1][1] == 0:
                # Robots facing right collide with robots facing left
                if robots[i][0] > robots[i + 1][0]:
                    collisions.append(i + 1)
                elif robots[i][0] < robots[i + 1][0]:
                    collisions.append(i)
                else:
                    collisions.extend([i, i + 1])

        if not collisions:
            break   # No more collisions

        # Remove robots involved in collisions
        robots = [robot for index, robot in enumerate(
            robots) if index not in collisions]
        N = len(robots)  # Update the number of robots

    return robots

print(robot_collisions(4, [(39,1),(20, 0), (21,0), (12,0)]))