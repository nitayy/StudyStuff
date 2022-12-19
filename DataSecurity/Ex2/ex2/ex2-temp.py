from Crypto.Cipher import AES

f = open("text.abc",'wb')
f.write("Hadar Fargun!!!!Hadar Fargun!!!!")
f.close()
f = open("text.abc",'rb')
text = f.read()
f.close()
print(len(text),text)
obj = AES.new('This is a key123', AES.MODE_CBC, text[:16])
ciphertext = obj.encrypt(text)
print (ciphertext, text)
#'\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
obj2 = AES.new('This is a key123', AES.MODE_CBC, text[:16])
print (obj2.decrypt(ciphertext))

