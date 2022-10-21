def intsum( *ints ):
    print(ints)
    sum = 0
    for s in ints:
        sum += s
    return sum

print(intsum(input()))
