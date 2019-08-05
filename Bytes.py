"""
Bytes not characters: Learn about Bytes
Bytes are similar to str type, but they are a sequence of bytes instead of Unicode code points.
Use for raw binary data, fixed-width, single-byte encoding: Ascii
will be using the byte constructor
"""
d = b'data' #must prefix with b for byte
print(d, type(d))

info = b'some bytes here'
#can split the bytes using the split() method for bytes (separates at spaces)
print(info.split())

#Encoding
message = "Vamos al zoológico" #alt +162 will print the ó - we are going to the zoo
print(message)

#lets try to encode this string message
data = message.encode("utf-8") #python default for encoding is utf-8
print(data)

#lets try to decode string message , take the data and call the data
new_message = data.decode("utf-8")
print(new_message)
#bytes are tranmutted encoded. we have to decode them, exercise from web: decode