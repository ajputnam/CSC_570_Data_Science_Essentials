# Notes for module 0 week 2


## A Taxonomy of Data Science
[A Taxonomy of Data Science](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/)
#### Highlights
* Part of the skillset of a data scientist is knowing how to obtain a sufficient corpus of usable data, possibly from multiple sources, and possibly from sites which require specific query syntax.
* The most basic form of scrubbing data is just making sure that it’s read cleanly, stripped of extraneous characters, and parsed into a usable format.
* Visualizing, clustering, performing dimensionality reduction: these are all part of 'looking at data.'


## Statistical Modeling: The Two Cultures
[Statistical Modeling: The Two Cultures](https://projecteuclid.org/euclid.ss/1009213726)
#### Highlights
* There are two goals in analyzing the data
  * **Prediction**: To be able to predict what the responses
are going to be to future input variables
  * **Information**: To extract some information about
how nature is associating the response variables
to the input variables.


## Data Science Lifecycle
[Data Science Lifecycle](https://www.youtube.com/watch?v=ZvQn2nWyOqc) (video)

#### Highlights
* Data Science = apply(science).to(data)
* **Lifecycle phases**
  1. Hypotheses
  2. Data
  3. Model
  4. Data Product: what we build out of our data.
    * Information - Visualization
    * Experiment - (correlation does not equal causation)
    * Predictive model - (predicts future values)

## Machine Learning Overview
[Machine Learning Overview](https://www.youtube.com/watch?v=66KsK5gBQYg) (20min video)

#### Highlights

* Model
  * Statistical Inference
  * Machine Learning
* Types of Machine Learning
  * Supervised (labeled data)
    * Regression
      * Predict a value based on historical data
    * Classification
      * Predict a class based on historical data
  * Unsupervised (unlabeled data)
    * Clustering
      * Find/organize data into groups or outliers
    * Recommender

## Measuring ML Model Performance
[Measuring ML Model Performance](https://www.youtube.com/watch?v=T0pFC4qs_4I) (7min video)
#### Highlights
x -> [nature]-> y

x -> [model]->  ŷ

compare ŷ to y

(holdout) Train the model with some of the data and then test with remaining data.
