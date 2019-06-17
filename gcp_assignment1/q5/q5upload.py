from google.cloud import storage
storage_client = storage.Client.from_service_account_json("C:/Users/Aditi Gangrade/Downloads/aditi-key-custom-account.json")

print("Enter path of the file to be uploaded ")
source_file_name=input("")
print("Enter the name of the bucket")
bucket_name=input("")
print("enter the name of destination file")
destination_file_name=input("")

bucket = storage_client.get_bucket(bucket_name)
blob= bucket.blob(destination_file_name)
blob.upload_from_filename(source_file_name)

print('File {} uploaded to {}.'.format(source_file_name,destination_file_name))

