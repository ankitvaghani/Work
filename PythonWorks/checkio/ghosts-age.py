def checkio(opacity):

    #fibonaci
    fib_numbers = [1, 1]
    for i in range(2, 10 + 1):
    	fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])


    ghosts_age = 0
    opacity_left = 10000

    while opacity != opacity_left:
        ghosts_age += 1
        if ghosts_age in fib_numbers:
            opacity_left -= ghosts_age
        else:
            opacity_left += 1
    return ghosts_age

    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
    print ("Done! time for check")
