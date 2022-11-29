#Menggunakan python versi terakhir
FROM python:latest

#Memberikan label owner atau maintainer
LABEL Maintainer="FahmiHamzah"

#Menambahkan file yang diperlukan ke dalam container
ADD upload_gcs.py iykra-370008-00022ed80ef9.json ./

#Command untuk docker agar menginstall library requests dan GCS
RUN pip install google-cloud-storage requests

#Command yang akan dilakukan oleh image untuk menjalankan script
CMD ["python", "./upload_gcs.py"]