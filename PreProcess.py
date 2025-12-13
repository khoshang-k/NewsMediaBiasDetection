import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import numpy as np


df=pd.read_csv('raw_dataset.csv')
print(df.head())

def TotalWordCount(text):
    if not isinstance(text, str) or not text.strip():
        return 0
    tokens=word_tokenize(text)
    return len(tokens)

df['word_count']=df['text'].apply(TotalWordCount)

print(f"Total rows: {len(df)}")
print("\nCounts per Bias Ratings: ")
print(df['bias_rating'].value_counts())

stats=df.groupby('bias_rating')['word_count'].agg(['mean','std'])

print("\nAverage word count and standard deviation by Bias kind: ")
print(stats)

# Till now we have found stats for unprocessed data

# PreProcessing main code:
def cleaning(text):
    if not isinstance(text,str) or not text.strip():
        return ""
    
    text=text.lower()

    if len(text)>1 and text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    if text.endswith('...'):
        content=text[:-3]
        
        last_fullstop=content.rfind('.')
        if last_fullstop!=-1:
            text=content[:last_fullstop+1]
        else:
            text = ""
    return text
def cleaning_heading(text):
    if len(text)>1 and text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    return text

df['cleaned_text']=df['text'].apply(cleaning)
df['heading']=df['heading'].apply(cleaning_heading)
df['cleaned_text']=df['cleaned_text'].replace('',pd.NA)
df=df.dropna(subset=['cleaned_text'])

print("\nCleanup done")
print(f"Total rows: {len(df)}")
print("\nCounts per Bias Ratings: ")
print(df['bias_rating'].value_counts())

stats=df.groupby('bias_rating')['word_count'].agg(['mean','std'])

print("\nAverage word count and standard deviation by Bias kind: ")
print(stats)

# Now we keep only those columns who have all three biased side left, right, centre

def filterEqualBiased(x):
    is_three_rows= (len(x)==3)
    has_all_biases=(x['bias_rating'].nunique()==3)
    return is_three_rows and has_all_biases

df_triplets=df.groupby('title').filter(filterEqualBiased)
df_triplets = df_triplets.reset_index(drop=True)

print("\nFiltering done")
print(f"Total rows: {len(df_triplets)}")
print("\nCounts per Bias Ratings: ")
print(df_triplets['bias_rating'].value_counts())

stats=df_triplets.groupby('bias_rating')['word_count'].agg(['mean','std'])

print("\nAverage word count and standard deviation by Bias kind: ")
print(stats)

# Now we save these cleaned rows in new csv file

final_df=df_triplets[['title','tags','heading','source','cleaned_text','bias_rating']].copy()
final_df.columns=['title','tags','heading','source','text','bias']

final_df.to_csv('data.csv', index=False, encoding='utf-8')