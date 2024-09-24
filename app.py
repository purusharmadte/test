def compress_string(input_string):
    if not input_string:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed.append(f"{input_string[i - 1]}{count}")
            count = 1

    compressed.append(f"{input_string[-1]}{count}")
    return ''.join(compressed)

input_string = "ccaaaabbzzx"
result = compress_string(input_string)
print(result)

def my_decorator(func):
    def wrapper():
        print("something is happening before function called ")
        func()
        print("something is happening after function called")

    return wrapper


@my_decorator
def say_hello():
    print("hello")


say_hello()

nums = [1,2,3,4,5]
result = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(result)


