import requests
import os
from google.cloud import storage


#-------------------Download File--------------------#
#Menginputkan URL yang akan diupload
URL = input('Please paste the URL: ')

#Memberikan nama file
nama = input('What is your file name? ')
#Memberikan nama tipe file
tipe = input('What is your file extension? ')

#Mengambil / mendownload file yang ada diinternet
response = requests.get(URL)
#Menyimpan file yang telah didownload ke dalam directory
open("{}.{}".format(nama, tipe), "wb").write(response.content)

#-------------------Upload to GCS--------------------#

#Assign nama project yang telah dibuat
project = 'iykra-370008' 
#Memasukkan nama bucket dari project GCS
bucket_name = 'data-fellowship-8' 
#Memasukkan nama file yang akan diupload ke suatu variabel
your_filename = "{}.{}".format(nama, tipe)
file_to_upload = "{}.{}".format(nama, tipe)

#Untuk autentikasi dari service account dengan permission yang
#telah dibuat sesuai dengan ROLE nya
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'iykra-370008-00022ed80ef9.json'

#Menginisiasi client
client = storage.Client(project)
#Mengambil nama bucket yang telah kita assign
bucket = client.get_bucket(bucket_name)
#Membuat suatu objek blob dari file kita
blob = bucket.blob(your_filename)
#Mengpload blob ke bucket kita sesuai dengan nama file nya
blob.upload_from_filename(file_to_upload)

#Menghapus file yang ada pada directory local
os.remove(file_to_upload)