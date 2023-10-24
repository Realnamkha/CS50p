import inflect
p = inflect.engine()
word = "plural"
print("The plural of ", word, " is ", p.plural(word))
cat_count = 1
print("I saw", cat_count, p.plural("cat", cat_count))

print(
    p.plural_noun("I", N1),
    p.plural_verb("saw", N1),
    p.plural_adj("my", N2),
    p.plural_noun("saw", N2),
)