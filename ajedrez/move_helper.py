class MoveHelper:
    @staticmethod
    def generate_moves(directions, row, col, max_steps=8):
        moves = []
        for direction_r, direction_c in directions:
            r, c = row + direction_r, col + direction_c
            steps = 0
            while 0 <= r < 8 and 0 <= c < 8 and steps < max_steps:
                moves.append((r, c))
                r += direction_r
                c += direction_c
                steps += 1
        return moves
