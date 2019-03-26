
# Simple move file

A simple file copy function, designed for use as a google cloud function.

The functions takes the a request with the following json body.

```json
{

 "source_bucket": "mytest123_1",
 "source_file_name": "test.txt",
 "destination_bucket": "mytest123_2",
 "destination_file_name": "test.txt"
}
```

And moves the file between the provided buckets.

## NOTE

You'll need to create a service user with the appropriate permissions for the buckets in
question - dd this via the google terminal (or command line, or terraform etc).
