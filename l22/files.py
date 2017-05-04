f1 = open("arsen.txt","wt", encoding="utf-8")
f1.write("Арсен любит животных\n")
f1.write("Арсен молодец")
f1.close()

f1 = open("arsen.txt","rt", encoding="utf-8")
text = f1.read()
f1.close()
print(text)

supper_text = "лалалала алалалала"
with open("la.txt","wt", encoding="utf-8") as f2:
    f2.write(supper_text)