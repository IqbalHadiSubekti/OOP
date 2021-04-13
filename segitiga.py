from polygon import Polygon

class Segitiga(Polygon):
	def __init__(self):
		Polygon.__init__(self,1) 
		
	def hitungLuas(self):
		self.t = int(input("Masukkan tinggi: "))
		self.a = int(input("Masukkan alas: "))
		l = 0.5*self.a*self.t
		print("Luas segitiga adalah ",l)

hasil = Segitiga()
print(hasil.hitungLuas())




