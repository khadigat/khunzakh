capitals = {
  "Эпилог":"Заключительная часть произведения",
  "Монолог":"Речь одного лица",
  "Абзац":"Отступ в начале строки"
  }
print(capitals)
print(capitals["Монолог"])
capitals["Эпилог"] = "монолог" # изменить значение 
print(capitals["Абзац"])
capitals["Эпилог"] = "Абзац"