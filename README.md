# News Bias Detection 

News presented to us is usually biased. This is natural since Humans are inherently biased. But hidden bias presented in the news can mislead people. This project is related to detection of these kinds of biases.

# Data
Dataset: [Qbias Repo](https://github.com/irgroup/Qbias/blob/main/allsides_balanced_news_headlines-texts.csv)

The datset was scraped from [Allsides](https://www.allsides.com/unbiased-balanced-news)

# File Information
raw_dataset.csv: It contains raw data scraped from Allsides.com  
PreProcess.py: It contains preprocessing code used to preprocess raw_dataset.  
- Removed unfinished scentences by truncating it to last completed sentence. (eg: Github is good. It is... -> Github is good.)
- Removed uppercase lettering to avoid different identification of same words.
- Left, Right and Center bias news articles were unequal, which were equaled to avoid bias in processing. Each news heading has 3 news article in processed dataset (data.csv)  
data.csv: It contains pre-processed dataset.   