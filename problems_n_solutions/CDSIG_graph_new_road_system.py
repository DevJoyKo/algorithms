def solution(roadRegister):
    rows, cols = len(roadRegister), len(roadRegister[0])

    for i in range(rows):
        col_items = [row[i] for row in roadRegister]
        if col_items.count(True) != roadRegister[i].count(True):
            return False
    return True