from google.cloud import storage

# Replace with your project ID and bucket name
project_id = "lunar-goal-413922"
bucket_name = "billsstore"

# Path to the local text file
file_path = "path/to/your/text.txt"

# Create a storage client
client = storage.Client(project=project_id)

# Get the bucket
bucket = client.get_bucket(bucket_name)

# Create a blob with the file name
blob = bucket.blob("my-text-file.txt")

# Upload the text content from the file
blob.upload_from_filename(file_path)

print(f"Text uploaded to: {blob.public_url}")
