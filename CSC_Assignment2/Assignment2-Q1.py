def sqrt(n):
    lastGuess=1
    nextGuess=(lastGuess+(n/lastGuess))/2
    while abs(lastGuess-nextGuess)>=0.0001:
        lastGuess=nextGuess
        nextGuess=(lastGuess+(n/lastGuess))/2
    square_root=nextGuess
    return square_root


if __name__ == '__main__':
    ans1 = sqrt(5)
    ans2 = sqrt(37)