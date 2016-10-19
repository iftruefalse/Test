import psycopg2 as db

con = db.connect(database='def', user='postgres', password='tujuh117', host='127.0.0.1', port='5433')
cur = con.cursor()
slct = cur.execute('select * from pegawai')
show = cur.fetchall()

class Crud:
	def __init__(self):
		self.data = show

	def tambah(self):
		self.data.append(valt)

	def hapus(self, vald):
		self.data.remove(vald)

	def edit(self, vale):
		self.data.remove(vale)
		self.data.append(vale)

	def fungsi(self):
		self.data
		inp = raw_input("Pilih T untuk Tambah data, D untuk hapus data, E untuk edit data : ")
		if(inp == 'T'):
			print "Masukan data"
			tid = raw_input('id = ')
			tnam = raw_input('nama = ')
			talam = raw_input('alamat = ')
			valt = cur.execute("insert into pegawai(id, nama, alamat) values(%s, %s, %s)", (tid, tnam, talam))
#				(raw_input("id = "), raw_input("nama = "), raw_input("alamat = ")))
			con.commit()
			if(valt in self.data):
				self.tambah(valt)
				print "Data sudah ada"
				self.main()
			else:
				print "Berhasil"
				self.main()

		elif(inp == 'D'):
			prin = raw_input("masukan id data yang ingin di hapus : ")
			vald = cur.execute('delete from pegawai where id = %s', (prin))
			con.commit()
			if(prin in self.data):
				self.hapus(vald)
				print "Hapus"
				self.main()
			else:
				print "Berhasil! Data telah di hapus"
				self.main()

		elif(inp == 'E'):
			edt = raw_input("Masukan id data yang akan di edit : ")
			vale = cur.execute('select * from pegawai where id = %s', (edt)) 
			dt = cur.fetchall()
			print dt
#			satu = raw_input('id = ')
			dua = raw_input('nama = ')
			tiga = raw_input('alamat = ')
			edt  = cur.execute('update pegawai set nama = %s, alamat = %s where id = %s', (dua, tiga, edt))
			con.commit()
			if(edt in self.data):
				self.edit(vale, edt)
				print "BERHASIL"
				self.main()
			else:
				print "GAGAL" 


	def main(self):
		print "Data"
		print "============="
		for dat in self.data:
			print dat
		print "============="
		self.fungsi()

c = Crud()
c.main()