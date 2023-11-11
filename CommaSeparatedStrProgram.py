# Program that accepts comma separated sequence of words and sorts the unique words alphabetically
items=input("input comma separated sequence of words:")
words=[word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))