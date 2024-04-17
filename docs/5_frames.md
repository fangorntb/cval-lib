# Frames

## General parameters
* dataset_id: id of the dataset
* part_of_dataset: frames are raw images that can be divided into RGB vectors (optional)

## Frame
* frame_id: the unique identifier of the image within the dataset part

### read (get-method)
Returns a raw image

### create (post-method)
accepts a raw image for uploading

### update (put-method)
accepts a raw image for uploading

### delete
deletes frame by id

## Frames

### create_fb (post-method)
uploading raw images wrapped in Iterable[FrameModel]:
* img_external_id: the unique identifier of the image within the dataset part
* img_raw: raw image data

### create_fl (post-method)

uploading raw images wrapped in Iterable[FrameModel] in train, test, val:
* img_external_id: the unique identifier of the image within the dataset part
* img_link: img link with data

This method is executed asynchronously. 
Therefore, there is a need to check the completion 
of the download. However, it can be estimated that 
in order to download 14 GB of data from cocodataset, you need to wait 30 minutes.

### read_meta (get-method)

* limit: The number of linked frames that need to be returned

### Returns:

* frames_quantity: num of frames in part of dataset
* frames: ids of frames