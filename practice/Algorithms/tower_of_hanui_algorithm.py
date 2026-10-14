def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]

    moves_history = [f"{rods[0]} {rods[1]} {rods[2]}"]

    def move(k, source, target, auxiliary):
        if k > 0:
            move(k - 1, source, auxiliary, target)

            rods[target].append(rods[source].pop())

            moves_history.append(f"{rods[0]} {rods[1]} {rods[2]}")

            move(k - 1, auxiliary, target, source)

    move(n, 0, 2, 1)

    return "\n".join(moves_history)