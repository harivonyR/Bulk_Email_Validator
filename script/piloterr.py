# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 11:13:00 2025

@author: harivonyratefiarison
"""

import requests
from credential import x_api_key

def email_status_checker(email:str):
    """
    this function will verify the email address status using the Piloterr API
    """
    url = "https://piloterr.com/api/v2/email/verify"

    headers = {
        "Content-Type": "application/json",
        "x-api-key": x_api_key
    }

    params = {"query": email}

    response = requests.get(url, headers=headers, params=params)
    print(response.json())

    # Handle error if request status isn't OK
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return {"email": email, "status": f"Error: {response.status_code}"} # Return an error status

    return response.json()