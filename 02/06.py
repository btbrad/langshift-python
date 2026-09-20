# Python 闭包
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def get_count():
        return count

    return {"increment": increment, "get_count": get_count}


counter1 = create_counter()
counter2 = create_counter()

print(counter1["increment"]())
print(counter1["increment"]())
print(counter2["increment"]())
print(counter1["get_count"]())
print(counter2["get_count"]())
