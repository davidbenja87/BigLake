import pandas as pd
import json
from pandas.io.json import json_normalize
df = pd.DataFrame({'ID': [1, 2], 'phone_numbers': [[{'a': '2017', 'b': '2017', 'sms': 1}, 
                                                    {'a': '2018', 'b': '2017', 'sms': 2}], 
                                                  [{'a': '2017', 'b': '2017', 'sms': 3}]]})

df = json_normalize(df,max_level=3)

print(df)