from polygon import Polygon
from segitiga import Segitiga 
from segilima import Segilima

#menunjukan bahwa file ini merupakan kelas main

if __name__ == "__main__":
	#s4 adalah objek dari kelas segiempat

	s3 = Segitiga()

	#method inputsisi() dan dispSisi() dimiliki polygon (kelas induk)
	s3.inputSisi()
	s3.dispSisi()

	#method hitung keliling() dimiliki oleh kelas segiempat (kelas anak)

	s3.hitungLuas()

	s5 = Segilima.Segilima()

	#method inputsisi() dan dispSisi() dimiliki polygon (kelas induk)
	s5.inputSisi()
	s5.dispSisi()

	#method hitung keliling() dimiliki oleh kelas segiempat (kelas anak)

	s5.hitungKeliling()

	poly = Polygon()

	poly.inputSisi()
	poly.dispSisi()

	# poly adalah objek dari kelas polygon
	