#coding: UTF-8

#########################################
## Author   : ExtremeBoy               ##
## Facebook : fb.com/ExtremeBoy.GGUser ##
## Github   : github.com/ExtremeBoyGG  ##
#########################################

from collections import OrderedDict
from pprint import pformat
import base64,os,sys,marshal,zlib,time,random
try:
	from uncompyle6 import main
except ImportError:
	os.system('pip2 install uncompyle6')
	exit('[#] Run The Script With Command > python2 '+sys.argv[0])
from datetime import datetime
purple,gray,hijau, putih, merah, cyan, kuning, biru = '\x1b[1;35m','\x1b[1;30m','\x1b[1;92m', '\x1b[1;97m', '\x1b[1;91m', '\x1b[1;96m', '\x1b[1;93m', '\x1b[1;94m'
import py_compile
data={}
data1={}
waduu= ['ExtremeBoy']

EMOTICONS =[':)',':D',':P',':S',':(','=)','=/',':/',':{',';)']
MAX_STR_LEN =70
def chunk_string (striing ,stringg):
	return '\n'.join ('{}\\'.format (striing [mlz :mlz +stringg ])for mlz in range (0 ,len (striing ),stringg )).rstrip ('\\')
def encode_string (isifilee ,emojii ):
	gtw =OrderedDict (enumerate (emojii ))
	mhank =OrderedDict ((btul ,gbtul )for gbtul ,btul in gtw.items ())
	return ('# coding: utf-8\n' '# Obfuscate By ExtremeBoy\n' '# Github : github.com/ExtremeBoyGG\n' 'from collections import OrderedDict\n\n' 'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n' '"{}"\n.split("  ")])))\n'.format (pformat (mhank ),chunk_string ('  '.join (' '.join (gtw [int (angka )]for angka in str (ord (silahkan )))for silahkan in isifilee ),MAX_STR_LEN )))


def berjalan(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random() * 0.0009)

def banner():
	berjalan ("""
              {}____ _  _ ____ ____ _   _ ___  ___
{}__________    {}|___ |\ | |    |__/  \_/  |__]  | {}     __________
{}\_________\   {}|___ | \| |___ |  \   |   |     | {}    /_________/
{}  \________\  {}___  _   _ ___ _  _ ____ _  _  ___{}   /________/
{}    \_______\ {}|__]  \_/   |  |__| |  | |\ |  ___|{} /_______/
              |      |    |  |  | |__| | \| |___

         {}=============================================
            {}[+] {}Github   : {}github.com/ExtremeBoyGG
            {}[+] {}Facebook : {}fb.com/ExtremeBoy.GGUser
         {}=============================================
""".format(merah,cyan,merah,cyan,cyan,merah,cyan,cyan,putih,cyan,cyan,putih,cyan,kuning,cyan,merah,putih,cyan,merah,putih,kuning))
	time.sleep(0.8)

def mengetik():
	for o in ['-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','✔']:
		time.sleep(0.25)
		sys.stdout.write(
			'\r{}[ {}⬤ {}] {}Loading... {}[{}{}{}]  '.format(cyan,kuning,cyan,putih,cyan,hijau,o,cyan)
		); sys.stdout.flush()


def size(namafile):
	ple=os.stat(namafile)
	if ple.st_size >= 1000000:
		print('\r'+cyan+'[ '+kuning+'# '+cyan+'] '+putih+'File size : '+hijau+str(ple.st_size / (1024 * 1024))+' MB')
	elif ple.st_size >= 1000:
		print('\r'+cyan+'[ '+kuning+'# '+cyan+'] '+putih+'File size : '+hijau+str(ple.st_size / 1000)+' KB')
	elif ple.st_size <= 999:
		print('\r'+cyan+'[ '+kuning+'# '+cyan+'] '+putih+'File size : '+hijau+str(ple.st_size)+' B')
def waktu(mengangka):
	sys.stdout.write(
		'\r{}[{}{}{}]{} Compiling : {}  '.format(cyan,putih,datetime.now().strftime('%H:%M:%S'),cyan,putih,mengangka)
	); sys.stdout.flush()

def enckeras(namafile):
	mauen=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Encrypt to bytes code (y/n) : '+hijau)
	mengopen=open(namafile).read()
	if mauen.lower()=='y':
		if 'marshal' or 'zlib' or 'd=[' in mengopen:
			mengetik()
			py_compile.compile(namafile)
			time.sleep(1)
			print('')
			os.remove(namafile)
			nama=namafile.replace('.py','.pyc')
			new=open(nama,'a')
			new.write('\n\n\n     EXTREMEBOY COMPILER\n   =======================\n   github.com/ExtremeBoyGG\n   fb.com/ExtremeBoy.GGUser')
			new.close()
			size(nama)
			print(cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'Done')
			exit(os.system('mv '+nama+' '+namafile))
		mengetik()
		py_compile.compile(namafile)
		time.sleep(1)
		print('')
		os.remove(namafile)
		time.sleep(1)
		nama=namafile.replace('.py','.pyc')
		size(nama)
		print(cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'Done')
		exit(os.system('mv '+nama+' '+namafile))
	else:
		size(namafile)
	sys.exit(cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'Done')

def menu():
	os.system('clear')
	banner()
	print ("             {}╔════╦══════════════════════════════╗".format(biru))
	print ("             {}║{} NO {}║ {}       ENCRYPT MENU          {}║".format(biru,merah,biru,merah,biru))
	print ("             ╠════╬══════════════════════════════╣")
	print ("             {}║{} 01 {}║ {}Encrypt {}Base64               {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 02 {}║ {}Encrypt {}Base32               {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 03 {}║ {}Encrypt {}Base16               {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 04 {}║ {}Encrypt {}Marshal              {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 05 {}║ {}Encrypt {}Zlib                 {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 06 {}║ {}Encrypt {}Hex                  {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 07 {}║ {}Encrypt {}Base64 Super         {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 08 {}║ {}Encrypt {}Base64,Base32        {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 09 {}║ {}Encrypt {}Zlib,Base64          {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 10 {}║ {}Encrypt {}Marshal,Zlib,Base32 {} ║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 11 {}║ {}Encrypt {}Base64,Base32,Base16 {}║".format(biru,putih,biru,gray,putih,biru))
	print ("             {}║{} 12 {}║ {}Encrypt {}ExtremeBoy Enc       {}║").format(biru,putih,biru,gray,putih,biru)
	print ("             {}║{} 13 {}║ {}Encrypt {}Bytes Code           {}║").format(biru,putih,biru,gray,putih,biru)
	print ("             {}║{} 14 {}║ {}Encrypt {}Emoticon             {}║").format(biru,putih,biru,gray,putih,biru)
	print ("             {}║{} 15 {}║ {}Encrypt {}Simple Enc           {}║").format(biru,putih,biru,gray,putih,biru)
	print ("             {}║{} 16 {}║ {}Encrypt {}Obfuscate Hard       {}║").format(biru,putih,biru,gray,putih,biru)
	print ("             {}╚════╩══════════════════════════════╝\n".format(biru))

	jenis=int(raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+merah+'Compile Type : '+hijau))
	if jenis == 3:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
		enk=base64.b16encode(str(file))
		wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b16decode('"+enk+"'))"
		try:
			os.remove(rep)
		except IOError:
			pass
		new=open(rep,'w')
		new.write(wm)
		new.close()
		angka= q - 1
		for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=base64.b16encode(lur)
			waktu(i+1)
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b16decode('"+ens+"'))"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih+'          ')
		enckeras(rep)

	elif jenis == 2:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
        	rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
		        file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
        	q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
	        enk=base64.b32encode(str(file))
        	wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b32decode('"+enk+"'))"
		try:
			os.remove(rep)
		except IOError:
			pass
	        new=open(rep,'w')
        	new.write(wm)
	        new.close()
		angka=q - 1
        	for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=base64.b32encode(lur)
			waktu(i+1)
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b32decode('"+ens+"'))"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
	        print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih+'          ')
		enckeras(rep)

	elif jenis == 5:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
		enk=zlib.compress(file)
		enk2=repr(enk)
		wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport zlib\nexec(zlib.decompress("+enk2+"))"
		try:
			os.remove(rep)
		except:	pass
		new=open(rep,'w')
		new.write(wm)
		new.close()
		angka=q - 1
		for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=zlib.compress(lur)
			ens2=repr(ens)
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport zlib\nexec(zlib.decompress("+ens2+"))"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as : '+hijau+rep+putih)
		enckeras(rep)

	elif jenis == 1:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
        	rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
		        file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
	        q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
        	enk=base64.b64encode(str(file))
	        wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b64decode('"+enk+"'))"
		try:
			os.remove(rep)
		except:	pass
	        new=open(rep,'w')
        	new.write(wm)
	        new.close()
		angka=q - 1
        	for i in range(int(angka)):
			waktu(i+1)
                	lur=open(rep).read()
                	ens=base64.b64encode(lur)
			waktu(i+1)
                	newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b64decode('"+ens+"'))"
		        os.remove(rep)
	                req=open(rep,'w')
              	        req.write(newm)
	                req.close()
	        print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih+'          ')
		enckeras(rep)

	elif jenis == 6:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How many : '+hijau)
		enk=file.encode('hex')
		wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nexec('"+enk+"').decode('hex')"
		try:	os.remove(rep)
		except:	pass
		new=open(rep,'w')
		new.write(wm)
		new.close()
		angka=q - 1
		for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=lur.encode('hex')
			waktu(i+1)
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nexec('"+ens+"').decode('hex')"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih)
		enckeras(rep)
	elif jenis == 4:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
		cek=marshal.dumps(compile(file,'<ExtremeBoy>','exec'))
		cekk=repr(cek)
		wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport marshal\nexec(marshal.loads("+cekk+"))"
		try:	os.remove(rep)
		except:	pass
		new=open(rep,'w')
		new.write(wm)
		new.close()
		angka=q - 1
		for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=marshal.dumps(compile(lur,'<ExtremeBoy>','exec'))
			enss=repr(ens)
			waktu(i+1)
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport marshal\nexec(marshal.loads("+enss+"))"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih+'          ')
		enckeras(rep)

	elif jenis == 7:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		enk=base64.b64encode(file)
		qwe=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
		q = enk.replace("q","@^@^^@q@^@^@")
		w = q.replace("w","@^@^^@w@^@^@")
		e = w.replace("e","@^@^^@e@^@^@")
		r = e.replace("r","@^@^^@r@^@^@")
		t = r.replace("t","@^@^^@t@^@^@")
		y = t.replace("y","@^@^^@y@^@^@")
		u = y.replace("u","@^@^^@u@^@^@")
		i = u.replace("i","@^@^^@i@^@^@")
		o = i.replace("o","@^@^^@o@^@^@")
		p = o.replace("p","@^@^^@p@^@^@")
		a = p.replace("a","@^@^^@a@^@^@")
		s = a.replace("s","@^@^^@s@^@^@")
		d = s.replace("d","@^@^^@d@^@^@")
		f = d.replace("f","@^@^^@f@^@^@")
		g = f.replace("g","@^@^^@g@^@^@")
		h = g.replace("h","@^@^^@h@^@^@")
		j = h.replace("j","@^@^^@j@^@^@")
		k = j.replace("k","@^@^^@k@^@^@")
		l = k.replace("l","@^@^^@l@^@^@")
		z = l.replace("z","@^@^^@z@^@^@")
		x = z.replace("x","@^@^^@x@^@^@")
		c = x.replace("c","@^@^^@c@^@^@")
		v = c.replace("v","@^@^^@v@^@^@")
		b = v.replace("b","@^@^^@b@^@^@")
		n = b.replace("n","@^@^^@n@^@^@")
		m = n.replace("m","@^@^^@m@^@^@")
		Q = m.replace("Q","@^@^^@Q@^@^@")
		W = Q.replace("W","@^@^^@W@^@^@")
		E = W.replace("E","@^@^^@E@^@^@")
		R = E.replace("R","@^@^^@R@^@^@")
		T = R.replace("T","@^@^^@T@^@^@")
		Y = T.replace("Y","@^@^^@Y@^@^@")
		U = Y.replace("U","@^@^^@U@^@^@")
		I = U.replace("I","@^@^^@I@^@^@")
		O = I.replace("O","@^@^^@O@^@^@")
		P = O.replace("P","@^@^^@P@^@^@")
		A = P.replace("A","@^@^^@A@^@^@")
		S = A.replace("S","@^@^^@S@^@^@")
		D = S.replace("D","@^@^^@D@^@^@")
		F = D.replace("F","@^@^^@F@^@^@")
		G = F.replace("G","@^@^^@G@^@^@")
		H = G.replace("H","@^@^^@H@^@^@")
		J = H.replace("J","@^@^^@J@^@^@")
		K = J.replace("K","@^@^^@K@^@^@")
		L = K.replace("L","@^@^^@L@^@^@")
		Z = L.replace("Z","@^@^^@Z@^@^@")
		X = Z.replace("X","@^@^^@X@^@^@")
		C = X.replace("C","@^@^^@C@^@^@")
		V = C.replace("V","@^@^^@V@^@^@")
		B = V.replace("B","@^@^^@B@^@^@")
		N = B.replace("N","@^@^^@N@^@^@")
		M = N.replace("M","@^@^^@M@^@^@")
		s0 = M.replace("0","@^@^^@0@^@^@")
		s1 = s0.replace("1","@^@^^@1@^@^@")
		s2 = s1.replace("2","@^@^^@2@^@^@")
		s3 = s2.replace("3","@^@^^@3@^@^@")
		s4 = s3.replace("4","@^@^^@4@^@^@")
		s5 = s4.replace("5","@^@^^@5@^@^@")
		s6 = s5.replace("6","@^@^^@6@^@^@")
		s7 = s6.replace("7","@^@^^@7@^@^@")
		s8 = s7.replace("8","@^@^^@8@^@^@")
		s9 = s8.replace("9","@^@^^@9@^@^@")
		ba = s9.replace("=","@^@^^@=@^@^@")
		result = ba.replace("@","#*!*!*!*#")
		wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b64decode('"+result+"'))"
		try:	os.remove(rep)
		except:	pass
		new=open(rep,'w')
		new.write(wm)
		new.close()
		angka=qwe-1
		for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=base64.b64encode(lur)
			q = ens.replace("q","@^@^^@q@^@^@")
			w = q.replace("w","@^@^^@w@^@^@")
			e = w.replace("e","@^@^^@e@^@^@")
			r = e.replace("r","@^@^^@r@^@^@")
			t = r.replace("t","@^@^^@t@^@^@")
			y = t.replace("y","@^@^^@y@^@^@")
			u = y.replace("u","@^@^^@u@^@^@")
			i = u.replace("i","@^@^^@i@^@^@")
			o = i.replace("o","@^@^^@o@^@^@")
			p = o.replace("p","@^@^^@p@^@^@")
			a = p.replace("a","@^@^^@a@^@^@")
			s = a.replace("s","@^@^^@s@^@^@")
			d = s.replace("d","@^@^^@d@^@^@")
			f = d.replace("f","@^@^^@f@^@^@")
			g = f.replace("g","@^@^^@g@^@^@")
			h = g.replace("h","@^@^^@h@^@^@")
			j = h.replace("j","@^@^^@j@^@^@")
			k = j.replace("k","@^@^^@k@^@^@")
			l = k.replace("l","@^@^^@l@^@^@")
			z = l.replace("z","@^@^^@z@^@^@")
			x = z.replace("x","@^@^^@x@^@^@")
			c = x.replace("c","@^@^^@c@^@^@")
			v = c.replace("v","@^@^^@v@^@^@")
			b = v.replace("b","@^@^^@b@^@^@")
			n = b.replace("n","@^@^^@n@^@^@")
			m = n.replace("m","@^@^^@m@^@^@")
			Q = m.replace("Q","@^@^^@Q@^@^@")
			W = Q.replace("W","@^@^^@W@^@^@")
			E = W.replace("E","@^@^^@E@^@^@")
			R = E.replace("R","@^@^^@R@^@^@")
			T = R.replace("T","@^@^^@T@^@^@")
			Y = T.replace("Y","@^@^^@Y@^@^@")
			U = Y.replace("U","@^@^^@U@^@^@")
			I = U.replace("I","@^@^^@I@^@^@")
			O = I.replace("O","@^@^^@O@^@^@")
			P = O.replace("P","@^@^^@P@^@^@")
			A = P.replace("A","@^@^^@A@^@^@")
			S = A.replace("S","@^@^^@S@^@^@")
			D = S.replace("D","@^@^^@D@^@^@")
			F = D.replace("F","@^@^^@F@^@^@")
			G = F.replace("G","@^@^^@G@^@^@")
			H = G.replace("H","@^@^^@H@^@^@")
			J = H.replace("J","@^@^^@J@^@^@")
			K = J.replace("K","@^@^^@K@^@^@")
			L = K.replace("L","@^@^^@L@^@^@")
			Z = L.replace("Z","@^@^^@Z@^@^@")
			X = Z.replace("X","@^@^^@X@^@^@")
			C = X.replace("C","@^@^^@C@^@^@")
			V = C.replace("V","@^@^^@V@^@^@")
			B = V.replace("B","@^@^^@B@^@^@")
			N = B.replace("N","@^@^^@N@^@^@")
			M = N.replace("M","@^@^^@M@^@^@")
			s0 = M.replace("0","@^@^^@0@^@^@")
			s1 = s0.replace("1","@^@^^@1@^@^@")
			s2 = s1.replace("2","@^@^^@2@^@^@")
			s3 = s2.replace("3","@^@^^@3@^@^@")
			s4 = s3.replace("4","@^@^^@4@^@^@")
			s5 = s4.replace("5","@^@^^@5@^@^@")
			s6 = s5.replace("6","@^@^^@6@^@^@")
			s7 = s6.replace("7","@^@^^@7@^@^@")
			s8 = s7.replace("8","@^@^^@8@^@^@")
			s9 = s8.replace("9","@^@^^@9@^@^@")
			ba = s9.replace("=","@^@^^@=@^@^@")
			result = ba.replace("@","#*!*!*!*#")
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b64decode('"+result+"'))"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih+'          ')
		enckeras(rep)

	elif jenis == 8:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
		enk=base64.b64encode(file)
		enk2=base64.b32encode(enk)
		wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b64decode(base64.b32decode('"+enk2+"')))"
		try:	os.remove(rep)
		except:	pass
		new=open(rep,'w')
		new.write(wm)
		new.close()
		angka=q - 1
		for i in range (int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=base64.b64encode(lur)
			ens2=base64.b32encode(ens)
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b64decode(base64.b32decode('"+ens2+"')))"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih+'          ')
		enckeras(rep)

	elif jenis == 9:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
            	rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
	        try:
        	        file=open(w).read()
		except IOError:
        		sys.exit(merah+'[ ! ] '+putih+'File Not Found')
	       	q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
		enk=zlib.compress(file)
		enk2=base64.b64encode(enk)
		wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport marshal,zlib,base64\nexec(zlib.decompress(base64.b64decode('"+enk2+"')))"
		try:	os.remove(rep)
		except:	pass
		new=open(rep,'w')
		new.write(wm)
		new.close()
		angka=q - 1
		for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=zlib.compress(lur)
			ens2=base64.b64encode(ens)
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport marshal,base64,zlib\nexec(zlib.decompress(base64.b64decode('"+ens2+"')))"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih+'          ')
		enckeras(rep)

	elif jenis == 10:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
		enk=compile(file,'<ExtremeBoy>','exec')
		ew=marshal.dumps(enk)
		enk2=zlib.compress(ew)
		enk3=base64.b32encode(enk2)
		wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode('"+enk3+"'))))"
		try:	os.remove(rep)
		except:	pass
		new=open(rep,'w')
		new.write(wm)
		new.close()
		angka=q - 1
		for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=compile(lur,'<ExtremeBoy>','exec')
			es=marshal.dumps(ens)
			ens2=zlib.compress(es)
			ens3=base64.b32encode(ens2)
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode('"+ens3+"'))))"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih+'          ')
		enckeras(rep)

	elif jenis == 11:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
		enk=base64.b64encode(file)
		enk2=base64.b32encode(enk)
		enk3=base64.b16encode(enk2)
		wm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b64decode(base64.b32decode(base64.b16decode('"+enk3+"'))))"
		try:	os.remove(rep)
		except:	pass
		new=open(rep,'w')
		new.write(wm)
		new.close()
		angka=q - 1
		for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=base64.b64encode(lur)
			ens2=base64.b32encode(ens)
			ens3=base64.b16encode(ens2)
			newm="#########################################\n##              COMPILE BY             ##\n#########################################\n## Author   : ExtremeBoy               ##\n## Facebook : fb.com/ExtremeBoy.GGUser ##\n## Github   : github.com/ExtremeBoyGG  ##\n#########################################\nimport base64\nexec(base64.b64decode(base64.b32decode(base64.b16decode('"+ens3+"'))))"
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih+'          ')
		enckeras(rep)

	elif jenis == 12:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How many : '+hijau)
		zic=[]
		zac=[]
		for ww in file:
			zic.append(ord(ww))
		for www in zic:
			#wado=random.choice([' ','?','!','+','.','=','*','#','^','~','@','|'])
			zac.append(' ExtremeBoy '*www)
		for i in range(int(200)):
			waduu.append('ExtremeBoy')
		wm='d={};exec("".join([chr(len(i) / 12) for i in d]))#epep={}\n"""\nexec(d)\n"""'.format(zac,waduu)
		outt=open(rep,'w')
		outt.write(wm)
		outt.close()
		angka=q-1
		for i in range(int(angka)):
			#wado=random.choice([' ','?','!','+','.','*','#','@','^','~','='])
			wado=' ExtremeBoy '
			waktu(i+1)
			lur=open(rep).read()
			data[i]=[]
			data1[i]=[]
			for wat in lur:
				data[i].append(ord(wat))
			for wut in data[i]:
				data1[i].append(wado*wut)
			waktu(i+1)
			newm='d={};exec("".join([chr(len(i) / 12) for i in d]))#epep={}\n"""\nexec(d)\n"""'.format(data1[i],waduu)
			os.remove(rep)
			req=open(rep,'w')
			req.write(newm)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as : '+hijau+rep+putih)
		enckeras(rep)
	elif jenis == 13:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		py_compile.compile(w)
		namafile=w+'c'
		size(w)
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as '+hijau+rep+putih)
		exit(os.system('mv '+namafile+' '+rep))

	elif jenis == 14:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How many : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		enk=encode_string(file,EMOTICONS)
		outt=open(rep,'w')
		outt.write(enk)
		outt.close()
		angka=q-1
		for i in range(int(angka)):
			waktu(i+1)
			lur=open(rep).read()
			ens=encode_string(lur,EMOTICONS)
			os.remove(rep)
			req=open(rep,'w')
			req.write(ens)
			req.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as : '+hijau+rep+putih)
		enckeras(rep)

	elif jenis == 15:
		w=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'File : '+hijau)
		rep=raw_input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'Output : '+hijau)
		q=input(cyan+'[ '+kuning+'+ '+cyan+'] '+putih+'How Many : '+hijau)
		try:
			file=open(w).read()
		except IOError:
			sys.exit(merah+'[ ! ] '+putih+'File Not Found')
		enc=base64.b64encode(file)
		enck="""def ExtremeBoy(code):
	global i
	aww=code.split('%')
	l=''
	for xxx in aww:
		try:
			l+=xxx[0]
		except:pass
	i = base64.b64decode(l)"""

		enc_y=base64.b64encode(enck)
		www=''
		for i in str(enc):
			www+=i+'%'
		tamnel=['ExtremeBoy']
		for i in range(300):
			ple=random.choice(['$','!','*','@','#','?','&','%','+','='])
			ple1=random.choice(['$','!','*','@','#','?','&','%','+','='])
			ow=random.randrange(0,10000)
			ow2=random.randrange(0,999)
			if i==120:
				tamnel.append(enc_y)
			else:
				tamnel.append(str(ow)+ple+'ExtremeBoy'+ple1+str(ow2))
		slur='ExtremeBoy'
		for i in range(30):
			am=base64.b64encode(slur)
			slur=am
		gg='ExtremeBoy'
		for i in range(17):
			am=base64.b32encode(gg)
			gg=am
		text='''#coding: utf-8
import zlib,marshal,base64
ExtremeBoy='{}'
i='{}'
agent_={};exec(base64.b64decode(agent_[ord('y')]))#sayanx={}
exec("""ExtremeBoy('{}')""")
exec('{}'.replace('{}','').join(i))'''.format(slur,gg,tamnel,tamnel,www,www,www)
		out=open(rep,'w')
		out.write(text)
		out.close()
		angka=q-1
		tol=[]
		toll=0
		if q>1:
			line1='exec(base64.b64decode('+tamnel[121]+'))'
			line2='exec("""ExtremeBoy("'+www+'")"""'
			os.remove(rep)
			file=open(rep,'w')
			file.write(line1)
		for i in range(angka):
			waktu(i+1)
			eww=''
			enk=base64.b64encode(open(rep).readlines()[5])
			for i in enk:
				eww+=i+"%"
#			enk2=base64.b64encode(tamnel[121])
#			tamnel=['ExtremeBoy']
#			for i in range(300):
#				ple=random.choice(['$','!','*','@','#','?','&','%','+','='])
#				ple1=random.choice(['$','!','*','@','#','?','&','%','+','='])
#				ow=random.randrange(0,10000)
#				ow2=random.randrange(0,999)
#				if i==120:
#					tamnel.append(enk2)
#				else:
#					tamnel.append(str(ow)+ple+'ExtremeBoy'+ple1+str(ow2))
			text='''#coding: utf-8
import zlib,marshal,base64
ExtremeBoy='{}'
i='{}'
agent_={};exec(base64.b64decode(agent_[ord('y')]))#sayanx={}
exec("""ExtremeBoy('{}')""")
exec('{}'.replace('{}','').join(i))'''.format(slur,gg,tamnel,slur,eww,eww,eww)
			outt=open(rep,'w')
			outt.write(text)
			outt.close()
		print('\r'+cyan+'[ '+kuning+'✔ '+cyan+'] '+putih+'File saved as : '+hijau+rep+putih)
		enckeras(rep)
        else:
            sys.exit(merah+'[ ! ]'+putih+' Wrong Input')


if __name__=="__main__":
	try:
		menu()
	except KeyboardInterrupt:
		sys.exit('\r'+merah+'[ ! ] '+putih+'Keyboard Interrupt          ')
	except NameError:
		sys.exit('\r'+merah+'[ ! ] '+putih+'Wrong Input          ')
	except ValueError:
		sys.exit('\r'+merah+'[ ! ] '+putih+'Wrong Input          ')
#	except Exception as err:
#		sys.exit('\r'+merah+'[ ! ] '+putih+str(err))
