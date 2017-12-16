# Notes for module 2 week 6

Logistic Regression - The 5 Questions


For the most part logistic regression is very simliar to linear regression.  By answering the 5 questions about logistic regression we will cover how they're different.


1. What does it do?

  Logistic regression is used to predict membership of a class.  That class might be 'survived the sinking of the titanic,' 'a person that will buy our product,' 'someone who will graduate college,' or even 'a person that doesn't have cancer.'  Classifiers are extremely useful to make binary decisions.  
2. What are the inputs?

  The same inputs as linear regression,

3. What are the outputs?

  Logistic regression is a specialized case of linear regression where we've taken our linear hypothesis, h(x) and combined it with the sigmoid function g(x) so that we have gm(h(x).   When we do this, the output changes to some number between 0 and 1.  This allows us to use a threshold to come up with binary classifier.   Our dependent variable for logistic regression is a binary value.

4. How do we measure performance?

  Using AUC, precision, and recall, which are covered in the lecture.

5. How can it fail?

  The same ways linear regression fails (non i.i.d data, non linear problems, etc)
