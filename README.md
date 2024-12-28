# Scraper for https://cityexpert.rs/
With this application you can scrap https://cityexpert.rs/ and find an apartment in Belgrade, Novi Sad or Nish.

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

If you want to find an apartment in Novi Sad or Nish you should change "base_url" in "config.py" to

"https://cityexpert.rs/izdavanje-nekretnina/novi-sad" or "https://cityexpert.rs/izdavanje-nekretnina/nis" respectively.

And don't forget to change 'params["polygonsArray"]' in "config.py", because this parameter is responsible for the city's areas.

In "config.py" you can see a lot of filters. For example variables "max_price" and "min_size" or values in "params" dictionary such us "minPrice", "maxSize", "floor", "furnishingArray" etc.

'params["polygonsArray"]' is responsible for the city's areas. By default, in my app it's around the city center.
