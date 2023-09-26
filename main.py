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

example_0_df = pd.DataFrame({col: [value] for col, value in zip(('en', 'ko'), example_0)})
df.columns = ('en', 'ko')

en_ko_df = pd.concat([example_0_df, df],).reset_index(drop=True)
ko_k = en_ko_df.head()
print(ko_k)
