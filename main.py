# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 20:11:44 2025

@author: harivonyratefiarison
"""


import pandas as pd
from tqdm import tqdm
from script.piloterr import email_status_checker



if __name__ == "__main__" :

    # Specify csv path & email column
    file_path = "https://raw.githubusercontent.com/harivonyR/Bulk_Email_Validator/main/input/random_email.csv"
    email_column_name = "Email"
    
    # Load email list with pandas
    emails_df = pd.read_csv(file_path, sep=";")
    emails_df.head()
    
    # Loop email checking
    emails_df["status"] = None

    for idx, email in tqdm(enumerate(emails_df[email_column_name]), total=len(emails_df)):
        result = email_status_checker(email)
        emails_df.loc[idx, "status"] = result["status"]

    # Print summary        
    summary = emails_df["status"].value_counts()
    print(summary)
 
