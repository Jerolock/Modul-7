def all_variants(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            yield string[i:j]


a = all_variants('abc')
for substr in a:
    print(substr)
