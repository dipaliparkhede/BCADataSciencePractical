# Creating dataframe from a dictionary,list or reading csv file
import pandas as pd

data_dict = {'Name': ['Dipali', 'Payal', 'Renu', 'Swati'],
             'Age': [20, 21, 18, 19],
             'city': ['Mumbai', 'surat', 'Rewa', 'Dilhi']
             }
df_from_dict = pd.DataFrame(data_dict)
print("Data frame:\n",df_from_dict)

col_list=['Name','Age','City']
data_list=[['Ram',20,'Ayodhya'],['Krishna',22,'Mathura'],['Balaji',25,'Tirupati']]

df_from_list=pd.DataFrame(data_list,columns=col_list)
print("\nData frame:\n",df_from_list)

col_list=['Name','Age','City']
name_list=['Dipali','Renu','Payal']
Age_list=[20,25,13]
city_list=['Khamgaon','Pune','Atali']

df_from_last2=pd.DataFrame(list(zip(name_list,Age_list,city_list)),columns=col_list)
print("\nData frame:\n",df_from_last2)

df_from_csv=pd.read_csv('sample.csv')
print("\nDataFrame from csv")
print(df_from_csv)


