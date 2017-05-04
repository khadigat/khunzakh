class Book:
	def __init__(self,pages,color,author):
		self.pages = pages
		self.color = color
		self.author = author
    def make_clever(self):
    	print(self.author, "Сделал тебя умнее")


holms = Book(500,"Серый","Артур Конан Дойл")
holms.pages -= 1
print(holms.pages)
holms.make_clever()
omar = Book(500,"красный","Омар Омар Омар")
omar.make_clever()