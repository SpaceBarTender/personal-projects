import pandas as pd
import numpy as np

data = {
        'id': [1,2,3,4,5],
        'Name': ['grandfather','father','child1','child2', 'someone else'],
        'parent_id': [0, 1,2,2,3]
    }
df = pd.DataFrame.from_dict(data)
df = df.replace(np.nan,'',regex=True)
df['id'] = df['id'].astype(int)
df['parent_id'] = df['parent_id'].astype(int)
