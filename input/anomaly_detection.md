IMAGE (intro_anomaly_detection_header.jpg)

In this tutorial you will learn how to perform anomaly/novelty detection in image datasets using OpenCV, Computer Vision, and the scikit-learn machine learning library.

Imagine this — you're fresh out of college with a degree in Computer Science. You focused your studies specifically on computer vision and machine learning.

Your first job out of school is with the United States National Parks department.

Your task?

**Build a computer vision system that can *automatically recognize flower species* in the park.** Such a system can be used to **detect invasive plant species** that may be harmful to the overall ecosystem of the park.

You recognize immediately that computer vision can be used to recognize flower species.  **But first you need to:**

1. Gather example images of *each flower species* in the park (i.e., **build a dataset**).
2. Quantify the image dataset and **train a machine learning model** to recognize the species.
3. **Spot when outlier/anomaly plant species are detected,** that way a trained botanist can inspect the plant and determine if it's harmful to the park's environment.

Steps #1 and #2 and fairly straightforward — **but Step #3 is *substantially* harder to perform.**

How are you supposed to train a machine learning model to automatically detect if a given input image is outside the "normal distribution" of what plants look like in the park?

The answer lies in a special class of machine learning algorithms, including **outlier detection** and **novelty/anomaly detection.**

In the remainder of this tutorial you'll learn the difference between these algorithms and how you can use them to spot outliers and anomalies in your own image datasets.

**To learn how to perform anomaly/novelty detection in image datasets, *just keep reading!***

JUMP TO CODE DOWNLOAD

# Intro to anomaly detection with OpenCV, Computer Vision, and scikit-learn

- In the first part of this tutorial we'll discuss the difference between standard events that occur and outliers/anomalies.
    - We'll also discuss why these types of events can be especially hard for machine learning algorithms to detect.
- From there we'll review our example dataset for this tutorial.
- I'll then show you how to:
    - 1. Load our input images from disk.
    - 2. Quantify them.
    - 3. Train a machine learning model used for anomaly detection on our quantify images.
    - 4. From there we'll be able to detect outliers/anomalies in new input images.
- Let's get started!

## What are outliers and anomalies? And why are they hard to detect?

- IMAGE
    - intro_anomaly_detection_definition.png
    - Image source:
        - [https://www.slideshare.net/agramfort/anomalynovelty-detection-with-scikitlearn](https://www.slideshare.net/agramfort/anomalynovelty-detection-with-scikitlearn)
- Anomalies are defined as **events that deviate from the standard, rarely happen, and don't follow the rest of the "pattern".**
- Examples of anomalies include:
    - Large dips and spikes in the stock market due to world events
    - Detective items in a factory/conveyor belt
    - Contaminated samples in a lab
- If you were to think of a bell curve, anomalies exist on the far, *far* ends of the tails.
    - IMAGE
        - intro_anomaly_detection_bell_curve.png
        - Image source:
            - [https://www.slideshare.net/agramfort/anomalynovelty-detection-with-scikitlearn](https://www.slideshare.net/agramfort/anomalynovelty-detection-with-scikitlearn)
    - They will occur, but will happen with an *incredibly small probability.*
- From a machine learning perspective this makes detecting anomalies *hard* — by definition we have many examples of "standard" events and few examples of "anomaly" events.
- **We therefore have a *massive skew* in our dataset.**
- How are machine learning algorithms, which tend to work optimally with balanced datasets, supposed to work when the anomalies we want to detect may only happen 1%, 0.1%, or 0.0001% of the time?
- Luckily, machine learning researchers have investigated this type of problem and have devised algorithms to handle the task.

## Anomaly detection algorithms

- IMAGE
    - intro_anomaly_detection_plot.png
    - Image source:
        - [https://www.engineering.com/AdvancedManufacturing/ArticleID/19058/Anomaly-Detection-Industrial-Asset-Insights-Without-Historical-Data.aspx](https://www.engineering.com/AdvancedManufacturing/ArticleID/19058/Anomaly-Detection-Industrial-Asset-Insights-Without-Historical-Data.aspx)
- Anomaly detection algorithms can be broken down into two subclasses:
    - **Outlier detection:** Our input dataset contains examples of ***both*** standard events and anomaly events. These algorithms seek to fit regions of the training data where the standard events are most concentrated, disregarding, and therefore isolating, the anomaly events. Such algorithms are often trained in an **unsupervised fashion** (i.e., without labels). We sometimes used to help clean and pre-process datasets before applying additional machine learning techniques.
    - **Novelty detection:** Unlikely outlier detection, which includes examples of both standard and anomaly events, **novelty detection algorithms have *only* the standard event data points (i.e., *no anomaly events*) during training time.** During training, we provide these algorithms with labeled examples of standard events (**supervised learning**). At testing/prediction time novelty detection algorithms must detect when an input data point is an outlier.
- Outlier detection is a form of **unsupervised learning**.
    - Here we provide our entire dataset of example data points and ask the algorithm to group them into **inliers** (standard data points) and **outliers** (anomalies).
- Novelty detection is a form of **supervised learning**, but we only have labels for the standard data points — it's up to the novelty detection algorithm to predict if a given data point is an inlier or outlier at test time.
- In the rest of this blog post we'll be focusing on novelty detection as a form of anomaly detection.

## Isolation Forests for anomaly detection

- IMAGE
    - intro_anomaly_detection_isolation_forest.png
    - Image source:
        - [https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html)
- We'll be using **Isolation Forests** to perform anomaly detection, based on Liu et al.'s 2012 paper, *[Isolation-Based Anomaly Detection.](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/tkdd11.pdf)*
- Isolation forests are a type of ensemble algorithm and consists of multiple decision trees used to partition the input dataset into distinct groups of inliers.
- As **Figure X** shows above, Isolation Forests accept an input dataset (*white points*) and then builds a manifold surrounding them.
- At test time, the Isolation Forest can then determine if the input points fall inside the manifold (standard events; *green points*) or outside the high-density area (anomaly events; *red points*).
- Reviewing how the Isolation Forests constructs an ensemble of partitioning trees is outside the scope of this post, so be sure to refer to [Liu et al.'s paper for more details.](https://www.notion.so/adrianrosebrock/2020-01-20-Intro-to-anomaly-detection-with-OpenCV-Computer-Vision-and-scikit-learn-589e5f89d14b4d12ad166937aadc42ec)

## Project structure

- Review project structure

## Our example image dataset

- IMAGE
    - intro_anomaly_detection_dataset.jpg
- Our example dataset for this tutorial includes **16 images of forests** (each of which is shown in **Figure X** above).
- These example images are a subset of the 8 Scenes Dataset from Oliva and Torralba's paper, *[Modeling the shape of the scene: a holistic representation of the spatial envelope](https://people.csail.mit.edu/torralba/code/spatialenvelope/)*.
- We'll take this dataset and train an anomaly detection algorithm on top of it.
- When presented with a new input image, our anomaly detection algorithm will return one of two values:
    - `1`: *"Yep, that's a forest."*
    - `-1`: *"No, doesn't look like a forest. It must be an outlier."*
- **You can thus think of this model as a "forest" vs "not forest" detector.**
    - This model was trained on forest images and now must decide if a new input image fits inside the "forest manifold" or if is truly an anomaly/outlier.
- To evaluate our anomaly detection algorithm we have **3 testing images:**
    - intro_anomaly_detection_test_images.jpg
- As you can see, only one of these images is a forest — the other two are examples of highways and beach coasts, respectively.
- If our anomaly detection pipeline is working properly, our model should return `1` (inlier) for the *forest* image and `-1` for the two *non-forest* images.

## Implementing our feature extraction and dataset loader helper functions

- IMAGE
    - intro_anomaly_detection_histogram.jpg
- Before we can train a machine learning model to detect anomalies and outliers, we must first define a process to quantify and characterize the contents of our input images.
- To accomplish this task, we'll be using **color histograms.**
- Color histograms are simple yet effective methods to characterize the color distribution of an image.
- Since our task here is to characterize forest vs. non-forest images, we may assume that forest images will contain more shades of green versus their non-forest counterparts.
- Let's take a look at how we can implement color histogram extraction using OpenCV.
- Open up the `[features.py](http://features.py)` file in the `pyimagesearch` module and insert the following code:
    - Review `features.py`
    - Codeblock #1: Lines 1-13
        - Imports
        - Define `quantify_image` function
        - Explain function parameters
        - Compute color histogram and normalize it
        - Return it to the calling function
    - Our next function handles:
        - 1. Accepting the path to a directory containing our dataset of images
        - 2. Looping over the image paths
        - 3. Quantifying them using our `quantify_image` method
    - Let's take a look at this method now:
    - Codeblock #2: Lines 15-32
        - Grab image paths in dataset directory
        - Loop over image paths
        - Load image
        - Quantify image
        - Return data to calling function

## Implementing our anomaly detection training script with scikit-learn

- With our helper functions implemented we can now move on to training an anomaly detection model.
- As mentioned earlier in this tutorial, we'll be using an Isolation Forest to help determine anomaly/novelty data points.
    - Our implementation of [Isolation Forests comes from the scikit-learn library](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html).
- Open up the `train_anomaly_detector.py` file and let's get to work:
    - Review `train_anomaly_detector.py`
    - Codeblock #1: Lines 1-13
        - Imports
        - Command line arguments
    - Codeblock #2: Lines 15-23
        - Load and quantify image dataset
        - Train the Isolation Forest
    - Codeblock #3: Lines 25-28
        - Serialize the anomaly detection model to disk

## Training our anomaly detector

- Now that we have implemented our anomaly detection training script, let's put it to work.
- Start by making sure you have used the ***"Downloads"*** section of this tutorial to download the source code and example images.
- From there, open up a terminal and execute the following command:
    - COMMAND OUTPUT
- To verify that the anomaly detector has been serialized to disk, check the contents of your working project directory:
    - COMMAND OUTPUT

## Creating the anomaly detector testing script

- At this point we have trained our anomaly detection model — **but how do we use to actually *detect anomalies* in new data points?**
- To answer that question, let's look at the `test_anomaly_detector.py` script:
    - Review `test_anomaly_detector.py`
    - Codeblock #1: Lines 1-13
        - Imports
        - Command line arguments
    - Codeblock #2: Lines 15-23
        - Load pre-trained anomaly detector
        - Quantify the image in the *same manner* as we did in our training script
    - Codeblock #3: Lines 25-37
        - Make predictions on the input image
        - Anomaly detection model will return `1` for a "normal" data point and `-1` for an "outlier".
        - Draw prediction and show the output image

## Detecting anomalies in image datasets using computer vision and scikit-learn

- To see our anomaly detection model in action make sure you have used the ***"Downloads"*** section of this tutorial to download the source code, example image dataset, and pre-trained model.
- From there, you can use the following command to test the anomaly detector:
    - COMMAND OUTPUT
    - IMAGE
        - intro_anomaly_detection_forest_result.jpg
- Here you can see that our anomaly detector has correctly labeled the forest as an **inlier.**
- Let's now see how the model handles an image of a highway, which is certainly *not* a forest:
    - COMMAND OUTPUT
    - IMAGE
        - intro_anomaly_detection_highway_result.jpg
- Our anomaly detector correctly labels this image as an **outlier/anomaly.**
- As a final test, let's supply an image of a beach/coast to the anomaly detector:
    - COMMAND OUTPUT
    - IMAGE
        - intro_anomaly_detection_coast_result.jpg
- Once again, our anomaly detector correctly correctly identifies the image as an **outlier/anomaly.**

## Where can I learn more about machine learning applied to computer vision problems?

- Insert Gurus pitch

# Summary

- In this tutorial you learned how to perform anomaly and outlier detection in image datasets using computer vision and the scikit-learn machine learning library.
- To perform anomaly detection, we:
    - 1. Gathered an example image dataset of forest images.
    - 2. Quantified the image dataset using color histograms and the OpenCV library.
    - 3. Trained an Isolation Forest on our quantified images.
    - 4. Used the Isolation Forest to detect image outliers and anomalies.
- You should use outlier/anomaly detection algorithms such as Isolation Forests, One-class SVMs, Elliptic Envelopes, and Local Outlier Factor algorithms when you can quantify your input images using image/feature extraction algorithms.
- **But what about deep learning?**
- Can deep learning be used to perform anomaly detection as well?
- I'll answer that question in a future tutorial.
- **To download the source code to this post (and be notified when future tutorials are published here on PyImageSearch), *just enter your email address in the form below!***

DOWNLOAD FORM