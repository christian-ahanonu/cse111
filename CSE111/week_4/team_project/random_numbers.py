from random import uniform, choice


def main():
    words = [
    "arm", "car", "cloud", "head", "heal", "hydrogen", "jog"
    ] 
    numbers = [15.2, 23.9, 80]
    print(f"Here is the list {numbers}")

    append_random_numbers(numbers)
    print(f"After random numbers function {numbers}")

    append_random_numbers(numbers, 3)
    print(f"After adding 3 numbers {numbers}")
    
    append_random_words(words)
    print(f"words {words}")
    append_random_words(words, 5)
    print(f"words {words}")

def append_random_numbers(numbers_list,quantity=1):
    for i in range(0,quantity):
        random_number = uniform(0,100)
        numbers_list.append(round(random_number,1))


def append_random_words(words_list, quantity=1):
    random_words = ['bus','plane','tank','desert']
    for word in range(quantity):
        word = choice(random_words)
        words_list.append(word)

    
if __name__ == '__main__':
    main()