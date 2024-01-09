# Group_Project_4-NFL_Game_Outcome_Predictor
Group project 4 using machine learning.

////////////////////////////////////////////
NFL Machine Learning Model
////////////////////////////////////////////

Summary:
--------------------------------------------------

Findings:
--------------------------------------------------


////////////////////////////////////////////
Sources for Code
////////////////////////////////////////////

The folowing data sources were used:

Wikipeia Pages:



--------------------------------------------------
Grabbing_Data.ipynb
--------------------------------------------------

The following source was used for the method of pulling the data
from Wikipedia tables:

    https://pbpython.com/pandas-html-table.html


--------------------------------------------------
Wrangling_Data.ipynb
--------------------------------------------------

From:
    
    https://www.geeksforgeeks.org/how-to-drop-rows-that-contain-a-specific-string-in-pandas/

The following method was used:

    df = df[df["team"].str.contains("Team 1") == False]

To write:

    cur_df = cur_df[cur_df["Result"].str.contains("Bye") == False]

and:
    cur_df_cleaned_home = cur_df_cleaned[cur_df_cleaned["Opponent"].str.contains("at ") == False]

and:
    cur_df_cleaned_away = cur_df_cleaned[cur_df_cleaned["Opponent"].str.contains("at ") == True]



From:

    Professor Benjamin Alford

The method for the concatination of dataframes was used to write:

    master_home_df = pd.concat([master_home_df, cur_df_cleaned_home], ignore_index= True)

and:

    master_away_df = pd.concat([master_away_df, cur_df_cleaned_away], ignore_index= True)



--------------------------------------------------
Building_Model.ipynb
--------------------------------------------------




--------------------------------------------------
Creating_Application.ipynb
-------------------------------------------------



--------------------------------------------------
App.py
-------------------------------------------------




