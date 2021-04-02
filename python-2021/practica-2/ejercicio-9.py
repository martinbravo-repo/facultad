word = input("Ingrese una palabra: ")
format_pattern = "{: <20} ==> {: <20}"
no_spaces = word.replace(" ", "")
if len(set(no_spaces)) == len(no_spaces):
    print(format_pattern.format(word, "Es Heterograma"))
else:
    print(format_pattern.format(word, "NO es Heterograma"))
