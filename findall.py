def find_all(a_str, sub, start, end):
    res = ""
    while True:
        start = a_str.find(sub, start, end)

        if start == -1:
            return res
        res += str(start) + "/"
        start += 1