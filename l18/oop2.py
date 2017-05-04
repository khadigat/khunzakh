class Book:
	def __init__(self,pages,color,author):
	self,pages = pages
	self,color = color
	self,author = author
    def make_clever(self):
    	print("Ты стал умнее")


holms = Book(500,"Серый","Артур Конан Дойл")
holms.pages -= 1
print(holms.pages)