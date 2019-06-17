from google.cloud import storage
storage_client = storage.Client.from_service_account_json("C:/Users/Aditi Gangrade/Downloads/aditi-key-custom-account.json")

print("name of bucket")
bucket_name=input("")
print("Enter name of the file to be downloaded ")
source_file=input("")
print("Enter the name by which file is to be downloaded")
destination_file =input("")
bucket = storage_client.get_bucket(bucket_name)

blob = bucket.blob(source_file)
blob.download_to_filename("C:/xyz/" + destination_file )
print('Blob {} downloaded to {}.'.format(source_file,destination_file))