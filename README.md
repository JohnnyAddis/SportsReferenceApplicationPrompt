
For the engineering prompt, I used Python because of its ease of use and available packages.

First off, this code will work for any JSON file containing head-to-head records. I printed the output to the terminal, saved it as a CSV, and also saved it in an HTML format which when previewed displays the table.
I split my program up into three functions. The most complicated is the create_matrix function which takes in a parsed JSON file as a parameter. To make the matrix, I created a Pandas data frame called df where each key in the JSON is a column in the data frame. Next, I initialized a new data frame called matrix with the same column names as df, for both rows and columns.
From here I used a nested for loop to iterate over each team and each of their opponents. I retrieved wins and losses and placed them into the returned matrix as a data frame.

The input for my program is the complete or relative path to the JSON file you would like to see in a table format. Also, I would only need to add one line of code if I would like to save my output to a SQL database, or Excel. 
