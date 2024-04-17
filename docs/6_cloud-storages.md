# Cloud Storage
## General

To work with cloud storage, the service needs: 
* s3-like cloud storage (Minio, Scality, Yandex Cloud, Google Cloud);
* user access with read permissions,
* the /cval directory in the bucket;
* datasets in the format:


    images
        train
        test
        val

    annotations
        train
        test
        val

* The presence of content in train, test, val in the format that is set in the openapi specification.


## Connection

### Create connection

`POST`
`/api/cloud`

This POST method is used to create a connection to a storage service. It requires specific parameters for authentication and specifying the location of the storage.

    body:
        {
            "access_key": "your_access_key",
            "secret_key": "your_secret_key",
            "endpoint": "https://your-storage-endpoint.com",
            "bucket": "your_bucket_name",
            "synchronize": true
        }

* access_key - The access key for authentication in the service.
* secret_key - The secret key for authentication in the service.
* endpoint - The URL or address of the repository.
* bucket - The name of the bucket in the storage.
* synchronize - a flag indicating the need to synchronize data.

In the cval-lib POST method corresponds to cval_lib.CVALConnection.storage.create.

response:

    body: 
        {
            "id": '<uuid>'
        }

### Get connection for storage

`GET`
`/api/cloud/{storage_id}`

This method allows you to get the cloud storage parameters.

response:

    body: 
        {
            "id": '<uuid>',
            "access_key": "your_access_key",
            "secret_key": "your_secret_key",
            "endpoint": "https://your-storage-endpoint.com",
            "bucket": "your_bucket_name",
            "synchronize": true
        }

In the cval-lib POST method corresponds to cval_lib.CVALConnection.storage.get.

### Get connections

`GET`
`/api/clouds/all`

This method allows you to get the cloud storages parameters.

response:

    body: 
        [
            {
            "id": '<uuid>',
            "access_key": "your_access_key",
            "secret_key": "your_secret_key",
            "endpoint": "https://your-storage-endpoint.com",
            "bucket": "your_bucket_name",
            "synchronize": true
            }
        ]

In the cval-lib POST method corresponds to cval_lib.CVALConnection.storage.get_all.

### Delete connection

`DELETE`
`/api/cloud/{storage_id}`

This method allows you to delete cloud storage connection.

response:

    body: 
        {
            "id": '<uuid>'
        }

In the cval-lib POST method corresponds to cval_lib.CVALConnection.storage.delete.

### Change synchronization

`PUT`
`/api/cloud/{storage_id}`

This method allows you to enable or disable auto-synchronization with CVAL and storage.  

params:

    syncronization: boolean


response:

    body: 
        {
            "id": '<uuid>'
        }

In the cval-lib POST method corresponds to cval_lib.CVALConnection.storage.put.
