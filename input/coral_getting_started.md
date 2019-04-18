# TITLE: Getting started with Google Coral's TPU USB Accelerator

IMAGE (`google_coral_getting_started_header.jpg`)

In this tutorial you will learn how to configure your Google Coral TPU USB Accelerator on Raspberry Pi and Ubuntu. You'll then learn how to perform classification and object detection using Google Coral's USB Accelerator.

A few weeks ago, Google released "Coral", a _super fast_, "no internet required" development board USB accelerator that enables deep learning practitioners to deploy their models "on the edge" and "closer to the data".

Using Coral, deep learning developers are _no longer required_ to have an internet connection, meaning that the Coral TPU is fast enough to perform inference _directly on the device_ rather than sending the image/frame to the cloud for inference and prediction.

**The Google Coral comes in two flavors:**

1. **A single-board computer** with an onboard Edge TPU. The dev board could be thought of an "advanced Raspberry Pi for AI" or a competitor to NVIDIA's Jetson Nano.
2. **A USB acclerator** that plugs into a device (such as a Raspberry Pi). The USB stick includes an Edge TPU built into it. Think of Google's Coral USB Accelerator as a competitor to Intel's Movidius NCS.

Today we'll be focusing on the Coral USB Accelerator as it's easier to get started with (and it fits nicely with our theme of Raspberry Pi-related posts the past few weeks).

**To learn how to configure your Google Coral USB Accelerator (and perform classification + object detection), _just keep reading!_**

JUMP TO CODE DOWNLOAD

## Getting started with Google Coral's TPU USB Accelerator

IMAGE (`google_coral_getting_started_device.jpg` source: https://coral.withgoogle.com/docs/accelerator/get-started/)

In this post I'll be assuming that you have:

- Your **Google Coral USB Accelerator stick**
- A fresh install of a Debian-based Linux distribution (i.e., **Raspbian, Ubuntu,** etc.)
- Understand **basic Linux commands and file paths**

If you don't already own a Google Coral Accelerator, you can purchase one via [Google's official website](https://coral.withgoogle.com/).

I'll be configuring the Coral USB Accelerator on Raspbian, but again, provided that you have a Debian-based OS, these commands will still work.

Let's get started!

### Downloading and installing Edge TPU runtime library

If you are using a Raspberry Pi, you first need to install `feh`, used by the Edge TPU runtime example scripts to display output images:

```
$ sudo apt-get install feh
```

The next step is to download the Edge TPU runtime and Python library. The easiest way to download the package is to simply use the command line + `wget`:

```
$ wget http://storage.googleapis.com/cloud-iot-edge-pretrained-models/edgetpu_api.tar.gz
```

**Note to Hoffman:** Make sure you include the full URL (probably via a wraparound in the code block)

Now that the TPU runtime has been downloaded we can extract it, change directory into `python-tflite-source`, and then install it (notice that `sudo` permissions are _not_ required):

```
$ tar xzf edgetpu_api.tar.gz
$ cd python-tflite-source
$ bash ./install.sh
...
Creating /home/pi/.local/lib/python3.5/site-packages/edgetpu.egg-link (link to .)
Adding edgetpu 1.2.0 to easy-install.pth file

Installed /home/pi/python-tflite-source
Processing dependencies for edgetpu==1.2.0
Searching for Pillow==4.0.0
Best match: Pillow 4.0.0
Adding Pillow 4.0.0 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Searching for numpy==1.12.1
Best match: numpy 1.12.1
Adding numpy 1.12.1 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Finished processing dependencies for edgetpu==1.2.0
```

During the install you'll be prompted ***"Would you like to enable the maximum operating frequency?""*** &mdash; _be careful with this setting!_

According to Google's [official getting started guide](https://coral.withgoogle.com/docs/accelerator/get-started/), enabling this option will:

1. *Improve* your inference speed...
2. ...but cause the USB Accelerator to become _very hot._

If you were to touch it/brush up against the USB stick, **it may burn you,** so be careful with it!

**My personal recommend is to to select `N` (for "No, I don't want maximum operating frequency"), at least for your first install.** You can always increase the operating frequency later.

Secondly, it's important to note that **you need _at least_ Python 3.5 for the Edge TPU runtime library.**

You *cannot* use Python 2.7 or any Python 3 version below Python 3.5.

The `install.sh` scripts **assumes you're using Python 3.5**, so if you're not, you'll want to open up the `install.sh` script, scroll down to the final line of the file (i.e., the `setup.py`) where you'll see this line:

```
python3.5 setup.py develop --user
```

If you're using Python 3.6 you'll simply want to change the Python version number:

```
python3.6 setup.py develop --user
```

After that you'll be able to successfully run the `install.sh` script.

Overall, the entire install process on a Raspberry Pi took just over one minute. If you're using a more powerful system than the RPi then the install should be even faster.

### Classification, object detection, and face detection using the Google Coral USB Accelerator

Now that we've installed the TPU runtime library, let's put the Coral USB Accelerator to the test!

First, make sure you are in the `python-tflite-source/edgetpu` directory. If you followed my instructions and put `python-tflite-source` in your home directory then the following command will work for you:

```
$ cd ~/python-tflite-source/edgetpu
```

The next step is to download the pre-trained classification and object detection models. [**The full list of pre-trained models Google provides can be found here**](https://coral.withgoogle.com/models/), including:

- **MobileNet V1 and V2** trained on ImageNet, iNat Insects, iNat Plants, and iNat Birds
- **Inception V1, V2, and V4**, all trained on ImageNet
- **MobileNet + SSD V1 and V2** trained on COCO
- **MobileNet + SSD V2** for face detection

Again, refer to [this link](https://coral.withgoogle.com/models/) for the pre-trained models Google Coral provides.

For the sake of this tutorial, we'll be using the following models:

1. **MobileNet V2** trained on **ImageNet**
2. **MobileNet + SSD V2** for **face detection**
2. **MobileNet + SSD V2** trained on **COCO**

You can use the following commands to download the models and follow along with this tutorial:

```
$ mkdir ~/edgetpu_models
$ wget https://storage.googleapis.com/cloud-iot-edge-pretrained-models/canned_models/mobilenet_v2_1.0_224_quant_edgetpu.tflite -P ~/edgetpu_models
$ wget http://storage.googleapis.com/cloud-iot-edge-pretrained-models/canned_models/imagenet_labels.txt -P ~/edgetpu_models
$ wget http://storage.googleapis.com/cloud-iot-edge-pretrained-models/canned_models/mobilenet_ssd_v2_face_quant_postprocess_edgetpu.tflite -P ~/edgetpu_models
$ wget http://storage.googleapis.com/cloud-iot-edge-pretrained-models/canned_models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite -P ~/edgetpu_models
$ wget http://storage.googleapis.com/cloud-iot-edge-pretrained-models/canned_models/coco_labels.txt -P ~/edgetpu_models
```

**Note to Hoffman:** Make sure those commands are formatted correctly.

**For conveience, I've included all models + example images used in this tutorial in the _"Downloads"_ section** &mdash; I would recommend using the downloads to ensure you can follow along with the guide.

Again, **notice how the models are downloaded to the `~/edgetpu_models` directory** &mdash; that is _important_ as it ensures the paths used in the examples below will work out of the box for you.

Let's start by performing a simple image classification example:

```
$ cd python-tflite-source/edgetpu
$ python3 demo/classify_image.py \
	--model ~/edgetpu_models/ mobilenet_v2_1.0_224_quant_edgetpu.tflite \
	--label ~/edgetpu_models/imagenet_labels.txt \
	--image test_data/parrot.jpg 
---------------------------
macaw
Score :  0.99609375
```

IMAGE (`google_coral_getting_started_classification.jpg`)

As you can see, MobileNet (trained on ImageNet) has correctly labeled the image as "Macaw", a type of parrot.

_**Note:** If you are using a Python virtual environment (covered below) you would want to use `python` rather than `python3` as the Python binary._

Now let's try performing face detection using the Google Coral USB Accelerator:

```
$ cd python-tflite-source/edgetpu
$ python3 demo/object_detection.py \
	--model ~/edgetpu_models/mobilenet_ssd_v2_face_quant_postprocess_edgetpu.tflite \
	--input test_data/face.jpg
-----------------------------------------
score =  0.99609375
box =  [474.22854804992676, 38.03488787482766, 738.8013491630554, 353.5309683683231]
-----------------------------------------
score =  0.9921875
box =  [205.4297697544098, 110.28378465056959, 487.75309658050537, 439.73802454331343]
-----------------------------------------
score =  0.83203125
box =  [6.2277887016534805, 182.35811898071842, 127.13575917482376, 326.5376813379348]
-----------------------------------------
score =  0.5
box =  [859.8422718048096, 213.5472493581642, 1008.978108882904, 383.9367261515483]
```

IMAGE (`google_coral_getting_started_face_detection.jpg`)

Here the MobileNet + SSD face detector was able to detect all four faces in the image. This is _especially impressive_ given the poor lighting conditions and the partially obscured face on the far right.

The next example shows how to perform object detection using a MobileNet + SSD trained on the COCO dataset:

```
$ cd python-tflite-source/edgetpu
$ python3 demo/object_detection.py \
	--model ~/edgetpu_models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite \
	--label ~/edgetpu_models/coco_labels.txt \
	--input test_data/owl.jpg
-----------------------------------------
bird
score =  0.9921875
box =  [474.58224296569824, 40.04487991333008, 1063.5828018188477, 1135.0372314453125]
-----------------------------------------
bird
score =  0.06640625
box =  [208.7918758392334, 288.1847858428955, 1408.0253601074219, 1200.0]
-----------------------------------------
bird
score =  0.06640625
box =  [159.07530784606934, 0.0, 1473.2084274291992, 934.4905853271484]
```

IMAGE (`google_coral_getting_started_object_detection.jpg`)

Notice there are _three_ detections but only _one_ bird in the image &mdash; **why is that?**

The reason is because the `object_detection.py` script is not filtering on a _minimum probability_. You could easily modify the script to ignore detections with _< 50%_ probability (I'll leave that as an exercise to you, the reader, to implement).

For fun, I decided to try an image that was _not_ included in the example TPU runtime library demos.

Here's an example of applying the face detector to a custom image:

```
$ python3 demo/object_detection.py \
	--model ~/edgetpu_models/mobilenet_ssd_v2_face_quant_postprocess_edgetpu.tflite \
	--input ~/IMG_7687.jpg
-----------------------------------------
score =  0.98046875
box =  [190.66683948040009, 0.0, 307.4474334716797, 125.00646710395813]
```

IMAGE (`google_coral_getting_started_ccustom_face_detection.jpg`)

Sure enough, my face is detected!

Finally, here's an example of running the MobileNet + SSD on the same image:

```
$ python3 demo/object_detection.py \
	--model ~/edgetpu_models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite \
	--label ~/edgetpu_models/coco_labels.txt \
	--input ~/IMG_7687.jpg
-----------------------------------------
person
score =  0.87890625
box =  [58.70787799358368, 10.639026761054993, 371.2196350097656, 494.61638927459717]
-----------------------------------------
dog
score =  0.58203125
box =  [50.500258803367615, 358.102411031723, 162.57299482822418, 500.0]
-----------------------------------------
dog
score =  0.33984375
box =  [13.502731919288635, 287.04309463500977, 152.83603966236115, 497.8201985359192]
-----------------------------------------
couch
score =  0.26953125
box =  [0.0, 88.88640999794006, 375.0, 423.55993390083313]
-----------------------------------------
couch
score =  0.16015625
box =  [3.753773868083954, 64.79595601558685, 201.68977975845337, 490.678071975708]
-----------------------------------------
dog
score =  0.12109375
box =  [65.94736874103546, 335.2701663970947, 155.95845878124237, 462.4992609024048]
-----------------------------------------
dog
score =  0.12109375
box =  [3.5936199128627777, 335.3758156299591, 118.05401742458344, 497.33099341392517]
-----------------------------------------
couch
score =  0.12109375
box =  [49.873560667037964, 97.65596687793732, 375.0, 247.15487658977509]
-----------------------------------------
dog
score =  0.12109375
box =  [92.47469902038574, 338.89272809028625, 350.16247630119324, 497.23270535469055]
-----------------------------------------
couch
score =  0.12109375
box =  [20.54794132709503, 99.93192553520203, 375.0, 369.604617357254]
```

IMAGE (`google_coral_getting_started_custom_object_detection.jpg`)

Again, we can improve results by filtering on a minimum probability to remove the extraneous detections.

### Installing the `edgetpu` runtime into Python virtual enviromments

IMAGE (`google_coral_getting_started_imports.jpg`)

It's a best practice to use Python virtual environments for development, and as you know, we make heavy use of Python virtual environments on the PyImageSearch blog.

Installing the `edgetpu` library into a Python virtual environment definitely requires a few more steps, but is _well worth it_ to ensure you libraries are kept in sequestered, independent environments.

The first step is to install both `virtualenv` and `virtualenvwrapper`:

```
$ sudo pip3 install virtualenv virtualenvwrapper
```

You'll notice that I'm using `sudo` here &mdash; this is **super important** as when installing the TPU runtime, the `install.sh` script created `~/.local` directory.  If we try to install `virtualenv` and `virtualenvwrapper` via `pip` they would actually go into the `~/.local/bin` directory (which is what we _don't_ want).

The solution is to use `sudo` with `pip3` (like we did above) so `virtualenv` and `virtualenvwrapper` end up in `/usr/local/bin`.

The next step is to open our `~/.profile` file:

```
$ nano ~/.profile
```

Then, scroll down to the button and insert the following lines to `~/.profile`:

```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

You can then re-load the `.profile` using `source`:

```
$ source ~/.profile`
```

We can now create our Python 3 virtual environment:

```
$ mkvirtualenv coral -p python3
```

I'm naming my virtual environment `coral` but you can call it whatever you like:

Finally, sym-link in the `edgetpu` library to your Python virtual environment:

```
$ cd ~/.virtualenvs/coral/lib/python3.5/site-packages/
$ ln -s ~/python-tflite-source/edgetpu edgetpu
$ cd ~
```

Assuming you followed my _exact_ instructions then your path to the `edgetpu` directory should match mine. If you didn't follow my exact instructions then you'll want to double-check and triple-check your paths.

As a sanity test, let's try to import the `edgetpu` library into our Python virtual environment:

```
$ workon coral
$ python
>>> import edgetpu
>>> 
```

As you can see, everything is working and we can now execute the demo scripts above using our Python virtual environment!

### What about custom models on Google's Coral?

You'll notice that I'm only using _pre-trained_ deep learning models on the Google Coral in this post &mdash; **what about custom models that you train yourself?**

Google [does provide some documentation on that](https://coral.withgoogle.com/docs/edgetpu/retrain-detection/) but it's _much_ more advanced, far too much for me to include in this blog post.

If you're interested in learning how to train your own custom models for Google's Coral I would recommend you take a look at my upcoming book, [*Raspberry Pi for Computer Vision*](#) where I'll be covering the Google Coral in detail.

### How do I use Google Coral's Python runtime library in my own custom scripts?

Use the `edgetpu` library in conjunction with OpenCV and your own custom Python scripts is outside the scope of this post.

I'll be covering how to use Google Coral in your own Python scripts in a future blog post as well as in my [_Raspberry Pi for Computer Vision_ book](#).

### Thoughts, tips, and suggestions when using Google's TPU USB Accelerator

Overall, I _really liked_ the Coral USB Accelerator. I thought it was super easy to install, and while not all the demos ran out of the box, with some basic knowledge of file paths, I was able to get them running in a few minutes.

In the future I would like to see the Python TPU runtime library _more compatible_ with Python virtual environments.

Technically, I could create a Python virtual environment and then edit the `install.sh` script to install _into_ that virtual environment, but editing the `install.sh` script shouldn't be a strict requirement &mdash; **instead, I'd like to see that script _detect_ my Python binary/environment and then install for that specific Python binary.**

I'll also add that inference on the Raspberry Pi is a bit slower than what's advertised by the Google Coral TPU Accelerator &mdash; that's actually _not_ a problem with the TPU Accelerator, **but rather the Raspberry Pi.**

What do I mean by that?

Keep in mind that the Raspberry Pi 3B+ uses **USB 2.0** but more optimal inference speeds the Google Coral USB Accelerator **recommends USB 3.**

Since the RPi 3B+ doesn't have USB 3, that's not much we can do about that until the RPi 4 comes out &mdash; once it does, we'll have even _faster_ inference on the Pi.

Finally, I'll wrote that once or twice during the object detection examples it appeared that the Coral USB Accelerator "locked up" and wouldn't perform inference, forcing me to `ctrl + c` out of the script.

Killing the script must have prevented a critical "shut down" script to run o nthe Coral &mdash; any subsequent executions of the demo Python scripts would result in an error.

**To fix the problem I had to unplug the Coral USB accelerator and then plug it back in.** Again, I'm not sure why that happened and I couldn't find any documentation on the Google Coral site that referenced the issue.

## Interested in using the Google Coral in your own projects?

IMAGE

Insert pitch

## Summary

In this tutorial you learned how to get started with the Google Coral USB Accelerator.

We started by installing the Edge TPU runtime library on your Debian-based operating system (we specifically used Raspbian for the Raspberry Pi).

After that we learned how to run the example demo scripts included in the Edge TPU library download.

We also learned how to install the `edgetpu` library into a Python virtual environment (that way we can keep our packages/projects nice and tidy).

We wrapped up the tutorial by discussing some of my thoughts, feedback, and suggestions when using the Coral USB Accelerator (be sure to refer them first if you have any questions).

I hope you enjoyed this tutorial!

**To download the source code to this post, and be notified when future tutorials are published here on PyImageSearch, _just enter your email address in the form below!_**