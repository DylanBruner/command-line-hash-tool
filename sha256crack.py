import click
import itertools
import hashlib
nl = []
fhash = 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'
notfound = True
stleng = 0
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for x in letters:
	nl.append(x)
	nl.append(x.upper())
letters = nl
@click.command()
@click.option('--hash', help='Ip to connect to')
#@click.option('--type', help='')


def crack(hash):
	global notfound
	while notfound:
		print('[+] Cracking')
		for x in getstring():
			x = str(x)
			x = x.replace('(','')
			x = x.replace("'",'')
			x = x.replace(')','')
			x = x.replace(',','')
			x = x.replace(' ','')
			if str(hashtext(x)) == hash:
				print('[+] Text: ' + x)
				notfound = False
				break


#Hashes the text
def hashtext(word):
	return hashlib.sha256(bytes(str(word),'utf-8')).hexdigest()
#returns the options
def getstring():
	global stleng
	stleng += 1
	return itertools.product(letters, repeat = stleng)
#checks if true

		
if __name__ == '__main__':
    crack()

