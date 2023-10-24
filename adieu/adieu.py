import inflect
p = inflect.engine()
word = "plural"
print("The plural of ", word, " is ", p.plural(word))
cat_count = 1
print("I saw", cat_count, p.plural("cat", cat_count))