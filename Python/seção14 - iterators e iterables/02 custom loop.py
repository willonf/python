def custom_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


custom_for([1, 2, 3, 4, 5])
word = 'Willon'
custom_for(word)
