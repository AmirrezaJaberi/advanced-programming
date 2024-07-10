def test(m):
    if len(m) == 1:
        return m[0]
    else:
        print(list)
        return m[0] + test(m[1:])


k = [10, 20, 9, 5]
print(test(k))
