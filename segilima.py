from polygon import Polygon

class Segilima(Polygon):
	def __init__(self):
		Polygon.__init__(self,5) 
		
	def hitungKeliling(self):
		self.sisi = a,b,c,d,e
		k = a+b+c+d+e
		print("Keliling Segilima adalah",k)

result = Segilima(5)
print(result.hitungKeliling())