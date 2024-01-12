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

    https://saturncloud.io/blog/how-to-delete-rows-with-null-values-in-a-specific-column-in-pandas-dataframe/#:~:text=Deleting%20rows%20with%20null%20values%20in%20a%20specific%20column%20can,values%20in%20the%20specified%20column.&text=df%20is%20the%20Pandas%20DataFrame%20that%20you%20want%20to%20modify.

The following method was used:

    # Drop Games With Null Values for Time
    cur_df = cur_df.dropna(subset=["time"], how="any")

From:

    Professor Benjamin Alford

The method for the concatination of dataframes was used to write:

    master_home_df = pd.concat([master_home_df, cur_df_cleaned_home], ignore_index= True)

and:

    master_away_df = pd.concat([master_away_df, cur_df_cleaned_away], ignore_index= True)



--------------------------------------------------
Building_Model.ipynb
--------------------------------------------------

The Following Section:

    # Create a StandardScaler Instance
    scaler = StandardScaler()

    # Fit the StandardScaler
    features_scaler = scaler.fit(features_array)

    # Scale the Features
    scaled_features = features_scaler.transform(features_array)

Was taken from Caleb Wolf's "AlphabetSoupCharity_Optimization.ipynb" file from the week 21 homework.


The Following Section:

    rf_model = RandomForestClassifier(random_state=1, n_estimators=1000).fit(X_train, y_train)

    print(f'Training Score: {rf_model.score(X_train, y_train)}')
    print(f'Testing Score: {rf_model.score(X_test, y_test)}')

Was mirroring code from Week 20, Class 3, Activity 4, 04-Ins_Forest-Features", "RandomForest-Feature-Selection.ipynb" provided by Professor Benajamin Alfrord :

    clf = RandomForestClassifier(random_state=1, n_estimators=500).fit(X_train_scaled, y_train)
    print(f'Training Score: {clf.score(X_train_scaled, y_train)}')
    print(f'Testing Score: {clf.score(X_test_scaled, y_test)}')


--------------------------------------------------
Creating_Application.ipynb
-------------------------------------------------



--------------------------------------------------
App.py
-------------------------------------------------




