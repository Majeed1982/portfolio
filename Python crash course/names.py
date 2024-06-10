from name_function import get_formatted_name
print("enter 'q' to quit.")
while True:
    first = input("\nplease give me frist name: ")
    if first == 'q':
        break
    last = input("please give me last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tneatly formatted name is: {formatted_name}")
    
    python -m pip install --user pytest