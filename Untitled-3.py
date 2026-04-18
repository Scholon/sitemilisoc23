text = "Sandu"
trans = str.maketrans("Sandu", "abcde")  
new_text = text.translate(trans)
print(new_text)