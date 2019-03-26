
# Google CloudFunc: 
# Python: 
## Copies A File Between Buckets

A simple google cloud function that copies a file from one bucket to another.

The function takes the a request with the following json body.

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
question - add this via the google terminal (or command line, or terraform etc).
