from collections import defaultdict


def group_points(points: list[tuple[int, int]]) -> list[list[int]]:
    groupped_points = defaultdict(list)

    for x, y in points:
        groupped_points[y].append(x)

    for group in groupped_points.values():
        group.sort()

    return groupped_points.values()


def check_middle_points(points: list[list[int]]) -> bool:
    middle_points = []

    for group in points:
        left = 0
        right = len(group) - 1

        while left <= right:
            middle = (group[left] + group[right]) / 2

            middle_points.append(middle)

            left += 1
            right -= 1

    return any([middle - middle_points[0] for middle in middle_points])


def check_symmetry(points: list[tuple[int, int]]) -> bool:
    groupped_points = group_points(points)

    return not check_middle_points(groupped_points)


if __name__ == "__main__":
    symmetric_points = [(1, 1), (3, 1)]
    symmetric_points2 = [(4, 5), (6, 5), (3, 3), (7, 3), (2, 1), (8, 1)]
    asymmetric_points = [(1, 1), (3, 3)]

    print(symmetric_points)
    print(f"Symmetry for points: {symmetric_points}\n{check_symmetry(symmetric_points)}")

    print(symmetric_points2)
    print(f"Symmetry for points: {symmetric_points2}\n{check_symmetry(symmetric_points2)}")

    print(asymmetric_points)
    print(f"Symmetry for points: {asymmetric_points}\n{check_symmetry(asymmetric_points)}")
