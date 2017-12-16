# Notes for module 2 week 9

Support Vector Machines - The 5 Questions

1. What does it do?

  The Support Vector Machine is a mathematically elegant, but complicated classifier.   It's goal is to find a hyperplane that is as far apart from the datapoints as possible.   It's fast, efficient, and it does a good job with datasets that have many dense variables.

  Contrast this preference for highly dimensional dense datasets with Naive Bayes, that is best for highly dimensional sparse datasets (where most variables are often 0).  Datasets that are highly dimensional and dense tend to be images, sound data, or biological data (think genomics).

2. What are the inputs?

  SVM needs numerical inputs.   You probably should scale your features.

3. What are the outputs?

  For classification, the ouputs are either A) the predicted class membership for the observation or B) the probability of class membership (using .predict_proba)

4. How do we measure performance?

  Binary Classification - Using AUC, precision, and recall, as with logistic.

  Multiclass Classification - Using confusion matricies and average precision.   There are some novel, but not well accepted multiclass AUC implmentations (volume under the hyperplane) not covered here.

5. How can it fail?

  SVM is usually not as good as Random Forest.  Start with Random Forest and go to SVM as an alternative or member of an ensemble.   



  Neural Networks - The 5 Questions

1. What does it do?

  Neural Networks are artificial classifiers and regression models  that stand at the cutting edge of machine learning.   They also have applications in unsupervised machine learning(Auto Encoders) and in time series modeling (RNNs).

  The focus in my career over the last year has been on a special type of neural network called a Convolutional Neural Network (CNN), which is used for computer vision tasks.   In case you've heard the term before, CNNs are a type of 'deep learning.'   Deep Learning is a term used for Neural Networks with many hidden layers, a concept you'll read more about later.

  Often Neural Networks don't perform as well as Random Forest (noticing a trend there yet?).   Sometimes, they're much better.   Those sometimes include computer vision, text, sound, and other places where features need to be 'learned' because they can't be engineered.   

2. What are the inputs?

  In most cases the inputs are numerical variables, as with most models.  

  Special Case:  In the case of a Convolusional Network applied to a picture, the input becomes a 4 dimensional 'tensor'  where dimensions 1,2,3 are the MxN image matrix separated into red, blue, and green channels.   The 4th dimension is the 'list' of images in your training set.    If that makes absolutely no sense, that's ok.   Convolutional Neural Networks are an entire semester, so we're just going to mention the idea here.

3. What are the outputs?

  For most classification tasks the output layer will be N neurons, where N is the number of classes you are classifying.   Each neuron will output the probability of the example's membership to their assigned class.   

4. How do we measure performance?

  For classification tasks accuracy and AUC apply as before.   Note that because of how Neural Nets are trained, you will often see RMSE used as a performance metric, even for classification tasks.   All you have to know about RMSE in this application is that lower is better.

5. How can it fail?

  Neural Networks are VERY prone to overfitting, although this can be adjusted for by using 'drop out.'

  Neural Networks have many, many hyperparameters and using one is a time consuming, tedious process.   It's often not worth the time.

  Neural Networks are hard.   There isn't a great 'scikit' style implementation of neural networks.   Most of the time when using one, I have to 'wire it' from the ground up using a package called Theano
