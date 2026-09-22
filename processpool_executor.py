from concurrent.futures import ProcessPoolExecutor

def square(number):
    return number * number

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(square, [1, 2, 3, 4]))

    print("Results:", results)
