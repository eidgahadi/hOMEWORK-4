def nucleo_game(a,t,c,g):
    total = a+t+c+g
    vals =[]            # an empty list that is available to add nucleotide numbers
    if a != 0:
        vals.append(a)
    if t != 0:
        vals.append(t)
    if c != 0:
        vals.append(c)
    if g != 0:
        vals.append(g)

    if total <= 2:
        print("Impossible game")

    if total%3 == 0:
        print("Player one loses anyway")

    if total%3 == 1:    #Since we should put the second player in a position of total%3== 0 we decrease one nucleotide which is the minimum
        minvals = min(vals)
        if a == minvals:
            a -= 1
        if t == minvals:
            t -= 1
        if c == minvals:
            c -= 1
        if g == minvals:
            g -= 1
    if total%3 == 2:     #Since we should put the second player in the particular situation, we decrase 2 nucleotides of th maximum nucleotide
        if a and (t + c + g) == 4:
            a -= 1
            t -= 1
        if t and (a + c + g) == 4:
            t -= 1
            c -= 1
        if c and (a + c + g) == 4:
            c -= 1
            g -= 1
        if g and (a + t + c) == 4:
            g -= 1
            a -= 1
        maxval = max(vals)
        if a == maxval:
            a -= 2
        if t == maxval:
            t -= 2
        if c == maxval:
            c -= 2
        if g == maxval:
            g -= 2
    return (a, t, c, g)

    nucleo_game(a,t,c,g)

