import pandas as pd
import numpy as np
# CREDIT TO: techsapphire's video at https://www.youtube.com/watch?v=X3KxjuVe-mk&t=74s
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
    # Returns when no more children are available
    if(len(df[df['parent_id'] == mgrid])==0):

        return
    else:
        # Get all direct children
        childs=df[df['parent_id'] == mgrid]

        # Get current row
        row=df[df['id'] == mgrid]

        # Get current row level
        rowlevel=(row.iloc[0,len(df['id'])-2])
        
        if rowlevel=='':

            # If root level, assign same id
            df.loc[df['id']==mgrid,'level'] = str(mgrid)
            rowlevel=str(mgrid)
            
        
        for ind in childs.index:
            empid=childs['id'][ind]
            # Build bread crumb of unit ids
            df.loc[df['id'] == empid, 'level'] = str(rowlevel) + '-' + str(childs['Name'][ind]) + '-' +  str(empid)
            getLevel(childs['id'][ind])

getLevel(1)
print(df)

RETURN_VALUE = """   id          Name  parent_id                                 level
0   1   grandfather          0                                   NaN
1   2        father          1                          nan-father-2
2   3        child1          2                 nan-father-2-child1-3
3   4        child2          2                 nan-father-2-child2-4
4   5  someone else          3  nan-father-2-child1-3-someone else-5"""


COMPLICATED_CASE = """data = {
        'id': [1,2,3,4,5],
        'UIC' : ['DJ8000', 'FF1WF0', 'DJ8294', 'FFCMF0', 'DJ8WMD'],
        'Name': ['HQSTRATOCOM','AFGSC','CTG 114','NRT 3', 'someone else'],
        'METTaskNumber' : ['SN 3.2.7', 'ST 4', 'SN 5.2.3.1', 'AFOP 1.2.3', 'ST 5'],
        'OPR': ['JQ/J35', 'JGSOC', 'NAOC', 'NAOC NRT', 'ELSE'],
        'parent_id': [0, 1,2,2,3],
        'SupportingMETOPR' : [None, 'JQ/J35','JGSOC','JGSOC','NAOC'],
        'SupportingMETUIC' : [None, 'DJ8000', 'FF1WF0', 'FF1WF0', 'DJ8294']
    }
df = pd.DataFrame.from_dict(data)
df = df.replace(np.nan,'',regex=True)
df['id'] = df['id'].astype(int)
df['parent_id'] = df['parent_id'].astype(int)

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
            df.loc[df['id'] == empid, 'level'] = str(rowlevel) + ':' + str(childs['UIC'][ind]) + ':' + str(childs['METTaskNumber'][ind]) + '-' +  str(empid)
            getLevel(childs['id'][ind])

getLevel(1)
print(df)
"""