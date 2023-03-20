## 🚌 Get started with Machine Learning for Beginners

[Today's article]({{ canonical }}) is about the Microsoft Machine Learning for Beginners curriculum, a free 12-week, 26-lesson curriculum all about Machine Learning.

In this curriculum, you will learn about what is sometimes called classic machine learning, using primarily Scikit-learn as a library and avoiding deep learning, which is covered in the [Artificial Intelligence for Beginners](https://microsoft.github.io/AI-For-Beginners/) curriculum. Pair these lessons with our [Data Science for Beginners](https://microsoft.github.io/ML-For-Beginners/) curriculum, as well!

What are you waiting for? Get started today!

## Machine Learning for Beginners Curriculum

The Machine Learning for Beginners Curriculum is a gentle introduction to the world of models taking you from predicting prices of North American pumpkins to discovering trends and patterns in Nigerian music consumption. The curriculum spans over 12 weeks (about 3 months) covering 26 topics including classic machine learning, time series analysis and an introduction to Natural Language Processing. The curriculum is extensively covered in Python but has a couple of lessons translated into R.

In addition to hands-on projects, the curriculum includes quizzes and a postscript on real world application of Machine Learning. In this blog, I will cover a brief overview of the different machine learning models linking them back to specific curriculum lessons for self-study.

## Classic Machine Learning

Machine Learning is often the foundation for an AI (artificial intelligence) system and is the way we "teach" a computer model to make predictions and draw conclusions from data. It automates the process of pattern-discovery by finding meaningful insights from real-world or generated data.

Classical Machine Learning includes supervised and unsupervised learning. Both require human effort to build the training set. In supervised learning involves training a model on a dataset that already has both input and output pairs, while in unsupervised learning, there is no known output.

Examples of supervised learning are regression analysis and classification, while unsupervised learning an example is clustering. The different models are explained below.

### Regression Models

The goal of regression is predicting a continuous value given several variables. For example, if you want to predict the probable height for a person of a given age, you will use linear regression, as you are seeking a numeric value. In the regression lessons, you will build a [model to determine pumpkin prices in North America](https://microsoft.github.io/ML-For-Beginners/#/2-Regression/README).

### Classification Models

Classification is a form of supervised learning that bears a lot in common with regression techniques. In classification, given various variables, you try and predict which category a value belongs in. For example, if you are interested in discovering whether a type of cuisine should be considered vegan or not, you are looking for a category assignment so you would use logistic regression. In the classification lessons, given a batch of ingredients you will determine which classes different Asian and Indian cusines fall into.

### Clustering Models

Clustering models help you make sense of chaos and is part of unsupervised learning. In a professional setting, clustering can be used to determine things like market segmentation, determining what age groups buy what items, for example. Another use would be anomaly detection, to detect fraud from a dataset of credit card transactions. In this lesson, you will [group Nigerian Music based on several factors including danceability, energy, speechiness and so much more](https://microsoft.github.io/ML-For-Beginners/#/5-Clustering/README). The algorithm used here is K-Means Clustering.

## Introduction Time Series analysis.

Time Series Forecasting: Time series forecasting is a sort of 'crystal ball': based on past performance of a variable such as price, you can predict its future potential value. Using time series, you can predict trends, understand seasons, detect outliers and many more. Time series data is a list of ordered observations, unlike data that can be analyzed by linear regression. The most common one is ARIMA (Auto Regressive Integrated Moving Average), an acronym that stands for "Autoregressive Integrated Moving Average". You can read [more on time series here](https://microsoft.github.io/ML-For-Beginners/#/7-TimeSeries/README).

## Introduction to Natural Language Processing

Natural Language Processing (NLP): Natural Language processing is the ability of machines to understand human-readable text. Using NLP, you can figure out sentiments, this is how people feel about a particular topic or subject and determine whether text is spam or not. In the Natural Language processing lessons, [you will build a simple bot and do sentiment analysis on hotel reviews](https://microsoft.github.io/ML-For-Beginners/#/6-NLP/README).

## Conclusion

For a deep dive into the different models, building projects using the scikit-learn library, head over to the [Machine Learning for Beginners curriculum]({{ canonical }}). At the end of the lessons, you will have a portfolio of various machine learning projects. Additionally, you will understand how you can implement your
