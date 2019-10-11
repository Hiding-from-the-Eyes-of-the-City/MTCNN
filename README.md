# MTCNN

## Usage
### Still Images
Use ```mtcnn_image.py``` to find a bounding box and dots on a still image. To do this, edit the file and replace the input and output file names with you appropriate files.

### Live Video MT
Use ```mtcnn_video.py``` to find a bounding box and dots on a live video. If you are using a Nvidia TX2 the video capture input should be ```cv2.VideoCapture(1)```. If you are using your own computer your video capture input should be ```cv2.VideoCapture(0)```. 
