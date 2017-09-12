# Data Science Lifecycle

## Required videos and reading
* [A taxonomy of Data Science](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/) (Reading)
* [Statistical Modeling: The Two Cultures](https://projecteuclid.org/euclid.ss/1009213726) (Reading)
* [Data Science Lifecycle](https://www.youtube.com/watch?v=ZvQn2nWyOqc) (13 min video)
* [Machine Learning Overview](https://www.youtube.com/watch?v=66KsK5gBQYg) (20 min video)
* [Measuring ML Model Performance](https://www.youtube.com/watch?v=T0pFC4qs_4I) (7 min video)

## Assignments
* Lab 1: iPython Notebook and the Titanic Dataset. (see labs folder)
* Lab 2: Set up Git (see labs folder)


## Terminology

When I was making the videos this week, I quickly found myself using some terminology that may be unfamiliar to you.  Here are some of the terms I want you to be familiar with:

#### Observations/Variables

First, lets talk about observations and variables.  Observations are just individual data elements (datum) in data.   They could be individual experiments (imagine coin flips), which is how they got their name.  They are an instance of something happening.  Variables are bits of information we have for each observation.  Variables can also be called features.


   | Variable 1 | Variable 2
  --- | --- | ---
  Observation 1	 |  |
  Observation 2	 |  |
  Observation 3	 |  |  

#### Continuous/Categorical

Some variables are continuous, and some are categorical.   Imagine a variable that contains the result of a coin flip.   Lets call that variable flip.   Flip could equal 1 for a head, or 0 for a tail.   It's important to note though, that for categorical variables, heads isn't 'greater than' tails, just because 1 > 0.   It's also important to note that the distance between a head and a tail isn't |1-0| = 1.   Categorical variables don't have any ordinal properties.   They're just labels.

#### Independent/Dependent variables

When we're building models, we typically care to try to predict some dependent variable, based on the independent variables in the dataset.  

Independence is pretty rigorously defined.   Simply though, if A and B are independent then P(A,B) = P(A) * P(B) and P(B|A) = P(B).   In real life, it's really hard to know if A and B are truly independent, and we have to make assumptions about those variables.  Careful though, A and B are dependent, and both find our way into our model, that's called collinearity.   If you have too much collinearity in your dataset, you're going to have a bad time.   We will talk about that more later.  


Lets put this all together in an example:

num | bedrooms | basement | price
--- | --- | --- | ---
house1 | 3 | 1 | 200k
house2 | 2 | 1 | 150k
house3 | 3 | 0 | 180k

In this dataset, there are two independent variables (bedrooms and basement) and three observations.  Basement is categorical.   The dependent variable would be price.  
