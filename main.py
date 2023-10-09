from datasets import load_dataset
from datasets import Dataset

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd


en_ko = load_dataset("bongsoo/news_talk_en_ko")
print(en_ko)

en_ko.set_format(type="pandas")

df = en_ko["train"][:]
k = df.head()
print(k)

example_0 = list(df.columns)
print(example_0)

example_0_df = pd.DataFrame({col: [value] for col, value in zip(('en', 'ko'), example_0)})
df.columns = ('en', 'ko')

en_ko_df = pd.concat([example_0_df, df],).reset_index(drop=True)
ko_k = en_ko_df.head()
print(ko_k)

dataset = Dataset.from_pandas(en_ko_df)
print(dataset)

num_train = 1200000
num_valid = 90000
num_test = 10000

en_ko_df_train = en_ko_df.iloc[:num_train]
en_ko_df_valid = en_ko_df.iloc[num_train:num_train+num_valid]
en_ko_df_test = en_ko_df.iloc[-num_test:]

en_ko_df_train.to_csv("train.tsv", sep="\t", index=False)
en_ko_df_valid.to_csv("valid.tsv", sep="\t", index=False)
en_ko_df_test.to_csv("test.tsv", sep="\t", index=False)

data_files = {"train": "train.tsv", "valid": "valid.tsv", "test": "test.tsv"}
dataset = load_dataset("csv", data_files=data_files, delimiter="\t")
print(dataset)

print(dataset['train']['en'][:3], dataset['train']['ko'][:3])
print(dataset['train'][:3]['en'], dataset['train'][:3]['ko'])
