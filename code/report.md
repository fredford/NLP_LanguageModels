# Assignment 3 - Report

- Scott Kavalinas - skavalin
- Fraser Redford - fredford

## Question 1

> How did you select the final sets of parameters (N)? What are the values?

### Unsmoothed

For our unsmoothed model, we selected an `N` of `2` by testing running the program with a variety of `N` values between `1` and `10` and determined that the best results occurred at `2`. This is the result of an unsmoothed model performing best while testing two words at a time to determine if they are a part of the training data or not. This helped to eliminate instances where a word might be in one vocabulary by coincidence.

### Laplace

For our laplace model, we selected an `N` of `3` by testing and running the program with a variety of `N` values between `1` and `10` and determined that the best results occurred between `1` and `4`. This is the result of needing more impactful smoothing to deal with unknown values. On the same vein, there is not nearly enough training data to properly deal with unknown values and whether or not a potentially unknown value should be a valid word in the language or not. Having more training data would substantially improve the ability for smoothing to be more impactful in finding the best results. Given the data sets are only 600-1000 words long and most languages are in the 200,000+ words.

### Interpolation

For our interpolation model, we were unable to select an `N` value. One of the reasons for this is that running through the interpolation algorithm would require a hold-out set of data. And while we could segment our dataset to manage this, given the already small dataset we're working with this would cause the interpolation method to have inaccurate results as a smaller dataset would not result in a more accurate interpretation of the test data. A reason for this is due to the interpolation method requiring additional data to perform lambda testing, without impacting the comparison to the other two modeling methods.

## Question 2

> Which model performed the best? Discuss the relative performance of the smoothing variants and n-gram settings.

Without testing interpolation as we were unable to get it properly running, by comparing the results of Unsmoothed and Laplace only. We found that our unsmoothed model performed significantly better than the Laplace model. From the test data set provided our Unsmoothed model found `52` of the `55` labels accurately. Meanwhile, using the Laplace model given an `N` of `3` we were unable to get more than `41` results accurately labelled.

The method for laplace of simply adding an additional plus 1 to the token count does not provide a robust enough solution to the language detection problem. As noted in the textbook that the add one method does not perform well when compared to modern n-gram models. However it does provide a sufficient introduction comparison.

With the interpolation method, given a training, heldout, and test datasets a proper testing procedure on the data could be performed. The performance would more accurately represent the improvements that should exist in using the interpolation method. A heldout corpus is an additional corpus designed to set the hyperparameters. With the hyperparamters accurately set the interpolation should yield the best results as it scans over the data to provide the most effective `N` value for the dataset while adjusting the ngrams in process.

Part of why the unsmoothed model performed so well given the data provided is because there are relatively few instances where a word in the testing set is not found in the training data. Therefore it the unsmoothed method is more likely to find the best matching test file to its training file as the vocabulary is closely matching with few instances of unknown words which is the best case scenario for an unsmoothed model.

While laplace's add one method increases the probability of the model recognizing a token that it is not trained on, it also effectively would decrease the probabiltity of the others by dulling the overall set impact.
