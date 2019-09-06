import xlrd


def xls2csv(spreadsheet_filename, output_csv_filename, sep=","):
    """
    Converte um arquvi XLS para CSV
    """
    endl = "\n"
    wb = xlrd.open_workbook(spreadsheet_filename)
    sheet = wb.sheet_by_index(0)
    with open(output_csv_filename, 'w') as output_csv:
        for sheet_row in sheet.get_rows():
            row = [str(cel.value) for cel in sheet_row]
            output_csv.write(sep.join(row))
            output_csv.write(endl)
