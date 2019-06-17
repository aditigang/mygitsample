# Imports the Google Cloud client library

from google.cloud import storage

# Instantiates a client
storage_client = storage.Client.from_service_account_json("C:/Users/Aditi Gangrade/Downloads/aditi-key-custom-account.json")

print("want to create bucket or not?")
response=input("")

print("name the bucket")
bucket_name = input("")                                          # The name for the new bucket
bucket = storage_client.create_bucket(bucket_name)               # Creates the new bucket
print('Bucket {} created.'.format(bucket.name))



bucket = storage_client.get_bucket(bucket_name)
destination_file_name=input("")
blob= bucket.blob(destination_file_name)
blob.upload_from_filename(source_file_name)
print('File {} uploaded to {}.'.format(source_file_name,destination_file_name))


