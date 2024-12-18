# -*- coding: utf-8 -*-
"""Pandas_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v3m6HIhhCA9nGPhHErlMgnXcJCSRs2sj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/drive/MyDrive/Dataset_ML/gym and diet recommendation1.csv')

df

df.isna().sum()

df.duplicated().sum()

df.drop_duplicates(inplace=True)

df.head()
df.tail()

df.describe()

df.info()

df.shape

df

df.dtypes

df['Diet']=df['Diet'].replace('and',',')

df=df[df['Diet']!='Diet']

df['Diet'].value_counts().head(1)

df['Vegetables'] = df['Diet'].str.extract(r'Vegetables:\s*\((.*?)\)')
df['Protein_Intake'] = df['Diet'].str.extract(r'Protein Intake:\s*\((.*?)\)')
df['Juice'] = df['Diet'].str.extract(r'Juice:\s*\((.*?)\)')

df['Juice'].ffill(inplace=True)

df

df['Juice'].value_counts()

df ['Vegetables'].value_counts()

df['Protein_Intake'].value_counts()

df['Vegetables']=df['Vegetables'].replace('Carrots, Sweet Potato, and Lettuce','Carrots, Sweet Potato, Lettuce')

df['Juice']=df['Juice'].replace('Apple juice, beetroot juice, and mango juice','Apple juice, beetroot juice and mango juice')

df

df['Exercises'].value_counts()

df.drop(columns='ID',inplace=True)

df.dtypes

df.drop(columns='Diet',inplace=True)

df

plt.boxplot(df['Height'])
plt.title("Boxplot of Height")
plt.show()

q1=df['Height'].quantile(0.25)
q3=df['Height'].quantile(0.75)
iqr=q3-q1
min_range=q1-1.5*iqr
max_range=q3+1.5*iqr
max_range
df=df[(df['Height']<max_range)&(df['Height']>=min_range)]

df.reset_index(inplace=True,drop=True)

df

gender_distribution=df['Sex'].value_counts()
gender_distribution

age_distribution=df['Age'].describe()
age_distribution

age_groups=pd.cut(df['Age'],bins=[10,20,30,40,50,60,70],labels=["10-20","20-30","30-40","40-50","50-60","60-70"])
df['Age Group']=age_groups
bmi_by_age_group=df.groupby('Age Group')['BMI'].describe()
bmi_by_age_group

normal_bmi=df[(df['BMI']>18)&(df['BMI']<24)]
normal_bmi

hypertension_counts=df['Hypertension'].value_counts()
diabetes_counts=df['Diabetes'].value_counts()
print("\nHypertension Counts:\n", hypertension_counts)
print("\nDiabetes Counts:\n", diabetes_counts)

df['Hypertension_Binary']=df['Hypertension'].apply(lambda x:1 if x=="Yes" else 0)
df['Diabetes_Binary']=df['Diabetes'].apply(lambda x:1 if x=="Yes" else 0)

correlation_matrix=df[['BMI','Hypertension_Binary','Diabetes_Binary']].corr()
correlation_matrix

fitness_goals_by_gender=df.groupby(['Sex','Fitness Goal']).size().reset_index(name='Count')
fitness_goals_by_gender

fitness_type_by_age=df.groupby(['Age Group','Fitness Type']).size().reset_index(name='Count')
fitness_type_by_age

average_bmi_table=df.groupby(['Age Group','Sex'])['BMI'].mean().reset_index(name='Count')
average_bmi_table

weight_height_correlation=df[['Height','Weight']].corr()
weight_height_correlation

from collections import Counter
exercise_recommendations=Counter(", ".join(df['Exercises']).split(", "))
exercise_freq_table=pd.DataFrame.from_dict(exercise_recommendations, orient="index").reset_index()
exercise_freq_table.columns=["Exercise","Frequency"]
exercise_freq_table.sort_values(by="Frequency",inplace=True)
exercise_freq_table.reset_index(inplace=True,drop=True)
exercise_freq_table

vegetable_recommendations=Counter(", ".join(df['Vegetables']).split(", "))
vegetable_freq_table=pd.DataFrame.from_dict(vegetable_recommendations, orient="index").reset_index()
vegetable_freq_table.columns=["Vegetable","Frequency"]
vegetable_freq_table.sort_values(by="Frequency",ascending=False,inplace=True)
vegetable_freq_table.reset_index(inplace=True,drop=True)
vegetable_freq_table

protein_recommendations=Counter(", ".join(df['Protein_Intake']).split(", "))
protein_freq_table=pd.DataFrame.from_dict(protein_recommendations, orient="index").reset_index()
protein_freq_table.columns=["Protein", "Frequency"]
protein_freq_table.sort_values(by="Frequency", ascending=False, inplace=True)
protein_freq_table.reset_index(inplace=True,drop=True)
protein_freq_table

plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

gender_distribution=df['Sex'].value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=gender_distribution.index, y=gender_distribution.values,color='Teal')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['Age'],bins=6,color="Teal")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.xticks(range(10,70,10))
plt.show()

age_groups=pd.cut(df['Age'],bins=[10,20,30,40,50,60,70],labels=["10-20","20-30","30-40","40-50","50-60","60-70"])
df['Age Group']=age_groups
plt.figure(figsize=(10,6))
sns.boxplot(x="Age Group",y="BMI",data=df,palette="dark")
plt.title("BMI Distribution Across Age Groups")
plt.xlabel("Age Group")
plt.ylabel("BMI")
plt.show()

health_conditions=df[['Hypertension','Diabetes']].melt(var_name="Condition",value_name="Presence")
health_proportions=health_conditions.groupby(['Condition','Presence']).size().reset_index(name='Count')
plt.figure(figsize=(8,5))
sns.barplot(x="Condition",y="Count",hue="Presence",data=health_proportions,palette="deep")
plt.title("Proportion of Individuals with Health Conditions")
plt.ylabel("Count")
plt.xlabel("Condition")
plt.show()

fitness_goals_gender=df.groupby(['Sex','Fitness Goal']).size().reset_index(name="Count")
plt.figure(figsize=(10,6))
sns.barplot(x="Fitness Goal",y="Count",hue="Sex",data=fitness_goals_gender,palette="muted")
plt.title("Fitness Goals by Gender")
plt.ylabel("Count")
plt.xlabel("Fitness Goal")
plt.show()

fitness_type_age=df.groupby(['Age Group','Fitness Type']).size()
fitness_type_age.plot(kind='line',figsize=(12,6))
plt.title("Fitness Type Variation with Age")
plt.ylabel("Count")
plt.xlabel("Age Group")
plt.xticks(rotation=45)
plt.show()

exercise_recommendations=Counter(", ".join(df['Exercises']).split(", "))
exercise_freq=pd.DataFrame.from_dict(exercise_recommendations, orient="index").reset_index()
exercise_freq.columns=["Exercise", "Frequency"]
exercise_freq.sort_values(by="Frequency", ascending=False, inplace=True)
plt.figure(figsize=(12,6))
sns.barplot(x="Frequency",y="Exercise",data=exercise_freq.head(10),palette="viridis")
plt.title("Top 10 Exercise Recommendations")
plt.xlabel("Frequency")
plt.ylabel("Exercise")
plt.show()

vegetables=Counter(", ".join(df['Vegetables']).split(", "))
vegetable_freq=pd.DataFrame.from_dict(vegetables, orient="index").reset_index()
vegetable_freq.columns=["Vegetable","Frequency"]
vegetable_freq.sort_values(by="Frequency",ascending=False,inplace=True)
plt.figure(figsize=(12,6))
sns.barplot(x="Frequency",y="Vegetable",data=vegetable_freq.head(10),palette="coolwarm")
plt.title("Top 10 Recommended Vegetables")
plt.xlabel("Frequency")
plt.ylabel("Vegetable")
plt.show()

proteins=Counter(", ".join(df['Protein_Intake']).split(", "))
protein_freq=pd.DataFrame.from_dict(proteins,orient="index").reset_index()
protein_freq.columns=["Protein","Frequency"]
protein_freq.sort_values(by="Frequency",ascending=False,inplace=True)
plt.figure(figsize=(12,6))
sns.barplot(x="Frequency",y="Protein",data=protein_freq.head(10),palette="coolwarm")
plt.title("Top 10 Recommended Protein Sources")
plt.xlabel("Frequency")
plt.ylabel("Protein")
plt.show()

average_bmi=df.groupby(['Age Group','Sex'])['BMI'].mean().unstack()
average_bmi_reset=average_bmi.reset_index().melt(id_vars='Age Group',var_name='Gender',value_name='Average BMI')
plt.figure(figsize=(10,6))
sns.barplot(data=average_bmi_reset,x='Age Group',y='Average BMI',hue='Gender',palette='viridis')
plt.title("Average BMI by Age Group and Gender")
plt.xlabel("Age Group")
plt.ylabel("Average BMI")
plt.legend(title='Gender')
plt.show()

average_bmi = df.groupby(['Age Group','Sex'])['BMI'].mean().unstack()
plt.figure(figsize=(12,6))
sns.heatmap(average_bmi,annot=True)
plt.title("Average BMI by Age Group and Gender")
plt.ylabel("Age Group")
plt.xlabel("Gender")
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x="Height",y="Weight",hue="Sex",data=df,palette="cool")
plt.title("Relationship Between Height and Weight")
plt.xlabel("Height (m)")
plt.ylabel("Weight (kg)")
plt.show()

df

df['Level'].value_counts()

plt.pie(x=df['Level'].value_counts(),labels=df['Level'].value_counts().index,autopct='%1.1f%%')
plt.title('Classified by BMI')
plt.show()