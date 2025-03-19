def Add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    if numbers.find(",,") < -1:
        return -1
    if numbers.endswith(",") or numbers.startswith(","):
        return -1

    x = numbers.split(",")

    sum = 0
    for i in x:
        sum += int(i)
    return sum
