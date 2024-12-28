base_url = 'https://cityexpert.rs/izdavanje-nekretnina/beograd'

# Filters
max_price = "800"
min_size = "40"

cookies = {
    '_gcl_au': '1.1.834019488.1735073377',
    'cw_conversation': 'eyJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfaWQiOiJlNzJiZTY0NC1jOWIwLTQyYzUtOGFkZi1jZGNhNzJkMjM0Y2QiLCJpbmJveF9pZCI6MX0.Po5r-0oxT2Rf-e_0vwod_WB7V8R4j7dzWZ7c5Z4jCWw',
    '_gid': 'GA1.2.67698151.1735073379',
    '_ga': 'GA1.2.460061828.1735073379',
    '_ga_7EWXF6Y9ER': 'GS1.1.1735075704.2.1.1735076595.59.0.0',
    '_dc_gtm_UA-61103808-1': '1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': '_gcl_au=1.1.834019488.1735073377; cw_conversation=eyJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfaWQiOiJlNzJiZTY0NC1jOWIwLTQyYzUtOGFkZi1jZGNhNzJkMjM0Y2QiLCJpbmJveF9pZCI6MX0.Po5r-0oxT2Rf-e_0vwod_WB7V8R4j7dzWZ7c5Z4jCWw; _gid=GA1.2.67698151.1735073379; _ga=GA1.2.460061828.1735073379; _ga_7EWXF6Y9ER=GS1.1.1735075704.2.1.1735076595.59.0.0; _dc_gtm_UA-61103808-1=1',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

params = {
    "ptId": "1",
    "currentPage": "1",
    # "minPrice": "500",
    "maxPrice": max_price,
    "minSize": min_size,
    # "maxSize": "100",
    # "floor": "1,2_4,5_10,11+,SU,VPR,PR,NPR,PTK", # floors
    "furnished": "1,2", # 1 - furnished, 2 - partially furnished, 3 - empty
    "furnishingArray": "furAircon,furInternet", # furBed,furCable,furTV,furWasher,furDishWasher,furStove,furShower,furFridge,furTub
    # "heatingArray": "1", # central heating, uncomment this string if it doesn't matter
    # "petsArray": "1,2,3,4,5", # 1 - dog, 2 - cat, 3 - in aquarium, 4 - in cage, 5 - in terrarium
    "polygonsArray": "Stara Palilula,Stari grad,Trg Republike,Botanička bašta,Hram Svetog Save,Savamala,Dorćol,Cvetni trg / park Manjež,Slavija,Vukov spomenik,Profesorska kolonija,Centar,Kopitareva Gradina,K-District,Palilula - uži deo,Novi Dorćol,Beograd na vodi,Savski amfiteatar,Tašmajdan,Kalenić pijaca,Gundulićev venac,Terazije,Kosančićev venac,Vračar"
}
