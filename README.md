# Scraper for https://cityexpert.rs/
This application allows you to get information about apartments from https://cityexpert.rs/ and find an apartment in Belgrade, Novi Sad, or Nish.

## Installation

Cloning a repository:

```git clone https://github.com/shestakovitch/cityexpert_parser.git```

Creating a virtual environment:

```python3 -m venv venv```


Activating the virtual environment:

```source venv/bin/activate```

Installing the required packages from requirements.txt﻿:

```pip3 install -r requirements.txt```

## Description

1. If you want to find an apartment in Novi Sad or Nish you should change "base_url" in "config.py" to

"https://cityexpert.rs/izdavanje-nekretnina/novi-sad" or "https://cityexpert.rs/izdavanje-nekretnina/nis" respectively.

  And don't forget to change 'params["polygonsArray"]' in "config.py", because this parameter is responsible for the city's areas.

2. In "config.py" you can see a lot of filters. For example variables "max_price" and "min_size" or values in "params" dictionary such us "minPrice", "maxSize", "floor", "furnishingArray" etc.

3. 'params["polygonsArray"]' is responsible for the city's areas. By default, in my app it's around the city center.
By default, this app saves data to output_file="cityexpert_data.xlsx" on your computer. If you want to save it on your Google Drive:

You should install gspread. Here is a link to the documentation: https://docs.gspread.org/

Also, you should enable API Access for a Project: https://docs.gspread.org/en/v6.1.3/oauth2.html#enable-api-access

You will automatically download a JSON file with credentials. It may look like this:

{

    "type": "service_account",
    
    "project_id": "api-project-XXX",
    
    "private_key_id": "2cd … ba4",
    
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    
    "client_id": "473 … hd.apps.googleusercontent.com",
    
    ...
}

Save it as "creds.json" in the root folder of the project.

Than you should create a new sheet on your Google Drive and shared it with "client_email" from "creds.json".
