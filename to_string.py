
def board_to_string(board):
    line = ' - - - - - '
    return line + "\n" + ("\n" + line + "\n").join(list(map(lambda row: '|' + (' '.join(row)) + '|', board))) + "\n" + line

def compass_to_string(compass):
    out = ''
    if (compass['nw']):
        out += '\\'
    else:
        out += ' '
    if (compass['no']):
        out += '|'
    else:
        out += ' '
    if (compass['ne']):
        out += '/'
    else:
        out += ' '
    out += "\n"
    if (compass['we']):
        out += '-'
    else:
        out += ' '
    out += '+'
    if (compass['ea']):
        out += '-'
    else:
        out += ' '
    out += "\n"
    if (compass['sw']):
        out += '/'
    else:
        out += ' '
    if (compass['so']):
        out += '|'
    else:
        out += ' '
    if (compass['se']):
        out += '\\'
    else:
        out += ' '
    return out
