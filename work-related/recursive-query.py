import pandas as pd
import numpy as np

# Create example hierarchy dict
data = {
        'id': [1,2,3,4,5],
        'Name': ['grandfather','father','child1','child2', 'someone else'],
        'parent_id': [0, 1,2,2,3]
    }


df = pd.DataFrame.from_dict(data)

# Make sure ids are ints
df = df.replace(np.nan,'',regex=True)
df['id'] = df['id'].astype(int)
df['parent_id'] = df['parent_id'].astype(int)

# Will use recursive function to fill level column
df['level'] = pd.Series()