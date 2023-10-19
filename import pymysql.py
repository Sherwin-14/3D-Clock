import pymysql
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

# Connect to the MySQL database
conn = pymysql.connect(
    host='localhost',   
    user='root',
    password='',
    db='codingthunder'
)

c = conn.cursor()

os.environ['PYTHONIOENCODING'] = 'utf-8'

# Generate a key pair
random_generator = Random.new().read
key = RSA.generate(2048, random_generator)

# Export the public key
public_key = key.publickey()

# Retrieve data from the 'PhoneNumber' column
c.execute("SELECT PhoneNumber FROM contact")
data = c.fetchone()

# Encrypt the data using the public key
cipher = PKCS1_OAEP.new(public_key)
encrypted_data = cipher.encrypt(data[0].encode('utf-8'))

c.execute("UPDATE contact SET PhoneNumber = %s", (encrypted_data,))

conn.commit()

# Decrypt the data using the private key
cipher = PKCS1_OAEP.new(key)
decrypted_data = cipher.decrypt(encrypted_data).decode(errors='ignore')
print(decrypted_data)

conn.commit()

conn.close()
































"""import pymysql
from cryptography.fernet import Fernet

# Connect to the MySQL database
conn = pymysql.connect(
    host='localhost',   
    user='root',
    password='',
    db='codingthunder'
)

c = conn.cursor()

# Generate a key for encryption/decryption
key = Fernet.generate_key()
f = Fernet(key)

# Retrieve data from the 'PhoneNumber' column
c.execute("SELECT PhoneNumber FROM contact")
data = c.fetchone()

# Encrypt the data
string1 = f.encrypt(data[0].encode())


c.execute("UPDATE contact SET PhoneNumber = %s", (string1,))

conn.commit()



decrypted = f.decrypt(string1).decode()
print(decrypted)

conn.close()

"""
