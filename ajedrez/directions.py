def get_directions(piece_type):
    if piece_type == "queen":
        return [
            (-1, -1), (-1, 1), (1, -1), (1, 1), 
            (-1, 0), (1, 0), (0, -1), (0, 1) 
        ]
    elif piece_type == "knight":
        return [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
    elif piece_type == "king":
        return [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
    return []
