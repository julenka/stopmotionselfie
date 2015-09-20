## Make Stop Motion Selfies With Python
Scripts to help you take photos of yourself with your webcam every minute or so. 

### Installation (OSX)
Make sure you install [homebrew](http://brew.sh/) first.

```
# this will take a while...
brew install opencv
brew install imagemagick
brew install ffmpeg
```

### Capture from webcam
Capture photos every 90 seconds, output to `output_dir`

```
python camcapture.py -o output_dir -r 90
```

### Make a video from the pictures

```
python make_video.py --out test.avi --framerate 10 jpegs/20150919 
```
