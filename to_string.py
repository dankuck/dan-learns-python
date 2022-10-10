
def board_to_string(board):
    line = ' - - - - - '
    row_strings = map(
        lambda row: '|' + (' '.join(row)) + '|',
        board
    )
    out = line + "\n"
    out += ("\n" + line + "\n").join(row_strings)
    out += "\n" + line
    return out

def compass_to_string(compass):
    out = ''
    out += '\\' if compass['nw'] else ' '
    out += '|' if compass['no'] else ' '
    out += '/' if compass['ne'] else ' '
    out += "\n"
    out += '-' if compass['we'] else ' '
    out += '+'
    out += '-' if compass['ea'] else ' '
    out += "\n"
    out += '/' if compass['sw'] else ' '
    out += '|' if compass['so'] else ' '
    out += '\\' if compass['se'] else ' '
    return out
