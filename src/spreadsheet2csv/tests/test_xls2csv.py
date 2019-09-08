from spreadsheet2csv.xls2csv import xls2csv


def test_xls2csv_naive():
    xls_filename = 'sample.xlsx'
    xls2csv(xls_filename, 'output.csv')
    with open('output.csv') as csv_file:
        assert csv_file.readline().strip() == 'indice,nome,valor'
        assert csv_file.readline().strip() == '1.0,marta,4.0'
        assert csv_file.readline().strip() == '2.0,zuca,5.3'


def test_xls2csv_tmpdir(tmpdir):
    xls_filename = 'sample.xlsx'
    csv_filename = tmpdir.join('output.csv')
    xls2csv(xls_filename, csv_filename)
    with open(csv_filename) as csv_file:
        assert csv_file.readline().strip() == 'indice,nome,valor'
        assert csv_file.readline().strip() == '1.0,marta,4.0'
        assert csv_file.readline().strip() == '2.0,zuca,5.3'


def test_xls2csv_datadir(datadir):
    xls_filename = str(datadir/'sample.xlsx')
    csv_filename = str(datadir/'output.csv')
    xls2csv(xls_filename, csv_filename)
    with open(csv_filename) as csv_file:
        assert csv_file.readline().strip() == 'indice,nome,valor'
        assert csv_file.readline().strip() == '1.0,marta,4.0'
        assert csv_file.readline().strip() == '2.0,zuca,5.3'


def test_xls2csv_ninja(datadir, file_regression):
    output_csv_path = datadir / 'output.csv'
    xls2csv(str(datadir / 'sample.xlsx'), str(output_csv_path))
    file_regression.check(output_csv_path.read_text(), extension=".csv")







# GitPitch
