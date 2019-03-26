
from google.cloud import storage

"""
Copy a file from one google cloud bucket to another

{
 "source_bucket": /foo/etc,
 "source_file_name": file.x,
 "destination_bucket" bar/etc",
 "destination_file_name": file.x
}
"""
def main(request):


    # Sanity checks...
    try:
        args = request.get_json()
    except Exception as e1:
        print("There was an issue reading the request as json. Attempting to write original request to string.")
        try:
            print("Writing to string successful.")
            print(str(request))
            print("Printing root exception.")
            raise e1
        except Exception as e2:
            print("Unable to write failed request as string - printing root exception.")
            raise e2

    missingArgs = []
    for k in ["source_bucket", "destination_bucket", "source_file_name", "destination_file_name"]:
        if k not in args.keys():
            missingArgs.append(k)

    if len(missingArgs) > 0:
        print("Aborting operation. The request was missing the following arguments: " + ",".join(missingArgs))
        return

    # ---------------
    # Copy operation

    # 1.) Get the storage client
    try:
        storage_client = storage.Client()
    except Exception as e:
        print("Unable to get storage client. Aborting operation:")
        raise e


    # 2.) Get the buckets
    try:
        source_bucket = storage_client.get_bucket(args["source_bucket"])
        destination_bucket = storage_client.get_bucket(args["destination_bucket"])
    except Exception as e:
        print("Error. Failed to get buckets using the provided bucket names.")
        raise e

    # 3.) Copy the file
    try:
        source_blob = source_bucket.blob(args["source_file_name"])
        new_blob = source_bucket.copy_blob(
            source_blob, destination_bucket, args["source_file_name"])
    except Exception as e:
        print("Failure encountered while attempting the file copy.")
        raise e


    print("Successfully copied file between buckets.")
    print(args)
