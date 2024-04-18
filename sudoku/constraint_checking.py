import random
import time


def cross(items_a, items_b):
    """Cross product of elements in A and elements in B."""
    return [a + b for a in items_a for b in items_b]


digits = "123456789"
rows = "ABCDEFGHI"
cols = digits
squares = cross(rows, cols)
unitlist = (
    [cross(rows, c) for c in cols]
    + [cross(r, cols) for r in rows]
    + [cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")]
)
units = {s: [u for u in unitlist if s in u] for s in squares}
peers = {s: set(sum(units[s], [])) - {s} for s in squares}


def test():
    """A set of unit tests."""
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units["C2"] == [
        ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2"],
        ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
        ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"],
    ]
    assert peers["C2"] == {
        "A2",
        "B2",
        "D2",
        "E2",
        "F2",
        "G2",
        "H2",
        "I2",
        "C1",
        "C3",
        "C4",
        "C5",
        "C6",
        "C7",
        "C8",
        "C9",
        "A1",
        "A3",
        "B1",
        "B3",
    }
    print("All tests pass.")


def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or return False if a
    contradiction is detected."""
    values = {s: digits for s in squares}
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False
    return values


def grid_values(grid):
    """Convert grid into a dict of {square: char} with '0' or '.' for empties."""
    chars = [c for c in grid if c in digits or c in "0."]
    assert len(chars) == 81
    return dict(zip(squares, chars))


def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.

    Return values, except return False if a contradiction is detected.
    """
    other_values = values[s].replace(d, "")
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.

    Return values, except return False if a contradiction is detected.
    """
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, "")
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1 and not assign(values, dplaces[0], d):
            return False
    return values


def display(values):
    """Display these values as a 2-D grid."""
    width = 1 + max(len(values[s]) for s in squares)
    line = "+".join(["-" * (width * 3)] * 3)
    for r in rows:
        print("".join(values[r + c].center(width) + ("|" if c in "36" else "") for c in cols))
        if r in "CF":
            print(line)


def solve(grid):
    return search(parse_grid(grid))


def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e:
            return e
    return False


def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in sorted(values[s]))


def solve_all(grids, name="", showif=0.0):
    """Attempt to solve a sequence of grids.

    Report results. When showif is a number of seconds, display puzzles that take longer. When
    showif is None, don't display any puzzles.
    """

    def time_solve(grid):
        start = time.monotonic()
        values = solve(grid)
        t = time.monotonic() - start
        if showif is not None and t > showif:
            display(grid_values(grid))
            if values:
                display(values)
            print("(%.5f seconds)\n" % t)
        return (t, solved(values))

    times, results = zip(*[time_solve(grid) for grid in grids])
    if (n := len(grids)) > 1:
        print(
            "Solved %d of %d %s puzzles (avg %.2f secs (%d Hz), max %.2f secs)."
            % (sum(results), n, name, sum(times) / n, n / sum(times), max(times))
        )


def solved(values):
    "A puzzle is solved if each unit is a permutation of the digits 1 to 9."

    def unitsolved(unit):
        return {values[s] for s in unit} == set(digits)

    return values is not False and all(unitsolved(unit) for unit in unitlist)


def from_file(filename, sep="\n"):
    "Parse a file into a list of strings, separated by sep."
    return open(filename).read().strip().split(sep)


def random_puzzle(assignments=17):
    """Make a random puzzle with N or more assignments.

    Restart on contradictions. Note the resulting puzzle is not guaranteed to be solvable, but
    empirically about 99.8% of them are solvable. Some have multiple solutions.
    """
    values = {s: digits for s in squares}
    for s in shuffled(squares):
        if not assign(values, s, random.choice(values[s])):
            break
        ds = [values[s] for s in squares if len(values[s]) == 1]
        if len(ds) >= assignments and len(set(ds)) >= 8:
            return "".join(values[s] if len(values[s]) == 1 else "." for s in squares)
    return random_puzzle(assignments)


def shuffled(seq):
    "Return a randomly shuffled copy of the input sequence."
    seq = list(seq)
    random.shuffle(seq)
    return seq


grid1 = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
grid2 = "400000805030000000000700000020000060000080400000010000000603070500200000104000000"
hard1 = "000006000059000008200008000045000000003000000006003054000325006000000000000000000"

if __name__ == "__main__":
    test()
    solve_all([random_puzzle() for _ in range(99)], "random", 100.0)
    for puzzle in (grid1, grid2, hard1):
        start = time.monotonic()
        result = "".join(solve(puzzle).values())
        display(parse_grid(result))
        t = time.monotonic() - start
        print("Solved: %.5f sec" % t)
