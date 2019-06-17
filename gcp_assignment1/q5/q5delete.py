from google.cloud import storage
storage_client = storage.Client.from_service_account_json("C:/Users/Aditi Gangrade/Downloads/aditi-key-custom-account.json")

print("name of bucket")
bucket_name=input("")
print("Enter name of the file to be deleted ")
source_file=input("")
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(source_file)
blob.delete()

print('Blob {} deleted.'.format(source_file))