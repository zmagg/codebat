import math

def dvr_remote(title, width):
    menu = []
    menu_chars = "abcdefghijklmnopqrstuvwxyz "
    i = 0
    while i < math.ceil(len(menu_chars) * 1.0 / width):
        menu_row = menu_chars[len(menu) * width : (len(menu) + 1) * width]
        menu.append(menu_row)
        i+=1

def find_char(curr_char, next_char, width):
    find_char = ""
    # find row
    curr_row = math.floor(menu_chars.index(curr_char) / width)
    next_row = math.floor(menu_chars.index(next_char) / width)
    if curr_row > next_row:
        i = curr_row - next_row:
        while i > 0:
            find_char += "U"
            i-=1
    else:
        i = next_row - curr_row:
        while i > 0:
            find_char += "D"
            i-=1

    # find column
    curr_column = menu[curr_row].find(curr_char)
    next_column = menu[next_row].find(next_char)
    if curr_column > next_column:
        i = curr_column - next_column:
        while i > 0:
            find_char += "L"
            i-=1
    else:
        i = next_column - curr_column:
        while i > 0:
            find_char += "R"
            i-=1
    find_char += "@"
    print find_char

        

