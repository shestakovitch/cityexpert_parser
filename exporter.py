import gspread
import pandas as pd
from openpyxl import Workbook


def save_to_gs(generator):
    columns = ["Apartment ID", "Price", "Description", "Link"]
    df = pd.DataFrame(generator, columns=columns)

    gc = gspread.service_account(filename="creds.json")

    # Open a sheet from a spreadsheet in one go
    file_name = "cityexpert_parsing_report"
    wks = gc.open(file_name).sheet1

    wks.update([df.columns.values.tolist()] + df.values.tolist())
    wks.format('A1:D1', {'textFormat': {'bold': True}})
    print(f"Data saved to the file {file_name} on Google Drive")


def save_to_xlsx(apartments_generator, output_file="cityexpert_data.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Apartments Data"

    # Adding headers
    ws.append(["ID", "Cost in Euro", "Description", "Link"])

    # Writing data from generator
    for apartment in apartments_generator:
        ws.append(apartment)

    wb.save(output_file)
    print(f"Data saved to the file {output_file} on your computer")

