from datasets import load_dataset
en_ko = load_dataset("bongsoo/news_talk_en_ko")

print(en_ko)

import pandas as pd
en_ko.set_format(type="pandas")

df = en_ko["train"][:]
k = df.head()
print(k)

example_0 = list(df.columns)
print(example_0)

