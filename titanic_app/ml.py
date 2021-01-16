__author__ = 'PRIYANSH KHANDELWAL'


import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
import pickle
import os
import  numpy as np
from sklearn.ensemble import RandomForestClassifier

def preprocessing(df):
    def get_title(name):
        if '.' in name:
            return name.split(',')[1].split('.')[0].strip()
        else:
            return 'Unknown'
    def title_map(title):
        if title in['Mr']:
            return 1
        elif title in['Master']:
            return 2
        elif title in['Ms','Mlle','Miss']:
            return 3
        elif title in['Mme','Mrs']:
            return 4
        else :
            return 0
    df['Sex']=df['Sex'].replace(["male","female"],[0,1])
    ns=df['Fare'].mean()
    df['title']=df['Name'].apply(get_title).apply(title_map)

    #df['Cabin']=df['Cabin'].isna()



    df['Fare']=df['Fare']>ns
    df.drop(['PassengerId','Ticket','Name','Cabin'],axis="columns",inplace=True)

    df['Age'][df['title']==1].fillna(32,inplace=True)
    df['Age'][df['title']==2].fillna(45,inplace=True)
    df['Age'][df['title']==3].fillna(4,inplace=True)
    df['Age'][df['title']==4].fillna(21,inplace=True)
    df['Age'][df['title']==5].fillna(35,inplace=True)
    #df['Age'][df['Age'].isna()]=df['Age'].mean()
    df['Age'].fillna(df['Age'].mean(),inplace=True)
    #s['Age'][s['Age'].isna()]=s['Age'].mean()
    print(df['Age'])

    df['fam']=df['SibSp']+df['Parch']+1
    df.drop(['Parch','SibSp'],axis='columns',inplace=True)
    df['fam']=pd.cut(df['fam'],bins=[0,2,5,7,100],labels=[0,10,3,2])
    df['Age']=df['Age'].astype(int)
    df['fam']=df['fam'].astype(int)
    df['Pclass']=df['Pclass'].astype(int)
    df['Fare']=df['Fare'].astype(int)


    df=pd.get_dummies(df)

    return df



def training(df):
    df=preprocessing(df)
    y=df['Survived']
    x=df.drop(['Survived'],axis='columns')
    dummyRow=pd.DataFrame(np.zeros(len(x.columns)).reshape(1,len(x.columns)),columns=x.columns)
    dummyRow.to_csv("dummy.csv",index=False)



    training_x,testing_x,training_y,testing_y=train_test_split(x,y,test_size=0.4,random_state=101)


    model=RandomForestClassifier()

    c=model.fit(training_x,training_y)
    print('p')
    print(model.score(testing_x,testing_y))
    file_name='titanic_pickle.pkl'
    with open(file_name,'wb') as file:
        pickle.dump(model,file)

def pred(ob):
    d1=ob.to_dict()


    df=pd.DataFrame(d1,index=[0])
    df=preprocessing(df)
    print(df,'lllllllllllllllllllllllllllllllllllll')
    df.drop('Survived',axis='columns',inplace=True)
    dummy="./dummy.csv"
    dummy=os.path.join(os.path.abspath(os.path.dirname(__file__)),dummy)
    dummyRow=pd.read_csv(dummy)
    print(dummyRow,'pppppppppppppppppppppppppppppppppppp')
    for i in df.columns:
        dummyRow[i]=df[i]
        print(dummyRow[i],'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
    print(dummyRow,'llllllllllllllllllllllllllllllllllllllllllllllllnnn')
    pickle_f='./titanic_pickle.pkl'
    pickle_f=os.path.join(os.path.abspath(os.path.dirname(__file__)),pickle_f)
    with open(pickle_f,'rb') as file:
        model=pickle.load(file)
        preds=model.predict(dummyRow)

        return preds

if __name__=="__main__":
    print('kkkkkkkkkkkkkk')
    df=pd.read_csv('titanic_train.csv')

    training(df)
















