L = [6, 3, 46, 7, 3]
e = 6

def liner_search(L, e):
    found = False

    for i in L:
        if i == e:
            found = True

    return found


def better_liner_search(L, e):
    for i in L:
        if i == e:
            return True

    return False

