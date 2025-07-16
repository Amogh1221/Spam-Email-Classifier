# Spam-Email-Classifier
This project is a machine learning-based spam email classifier trained on the spam_ham_dataset.csv containing 5,171 email samples.
# Data Preprocessing
Duplicates: 178 duplicate entries were removed.

Class Imbalance: The dataset was imbalanced, so precision was prioritized over accuracy to reduce false positives.

Feature Engineering: Two new features were added — the number of words and the number of sentences in each email — though they showed no significant difference between spam and non-spam classes.

Text Cleaning Pipeline: A preprocessing function was created to:
    Convert text to lowercase
    Tokenize into words
    Filter out non-alphanumeric tokens
    Remove stopwords
    Apply stemming
This function was applied to the email content and stored as a new column for modeling.

# Model Building
Multiple models were evaluated using both Bag of Words (BoW) and TF-IDF vectorization techniques.
Ridge Classifier provided the best results in terms of both accuracy and precision.
Hyperparameter Tuning did not yield any significant improvements.

# Final Metrics:
Accuracy: 98.88%

Precision: 98.00%
