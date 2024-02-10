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


def getLevel(mgrid):
    if(len(df[df['parent_id'] == mgrid])==0):

        return
    else:
        childs=df[df['parent_id'] == mgrid]

        row=df[df['id'] == mgrid]

        rowlevel=(row.iloc[0,len(df['id'])-2])
        if rowlevel=='':

            df.loc[df['id']==mgrid,'level'] = str(mgrid)
            rowlevel=str(mgrid)
            
        
        for ind in childs.index:
            empid=childs['id'][ind]
            df.loc[df['id'] == empid, 'level'] = str(rowlevel) + '-' + str(childs['Name'][ind]) + '-' + str(childs['Name'][ind]) + '-' +  str(empid)
            getLevel(childs['id'][ind])