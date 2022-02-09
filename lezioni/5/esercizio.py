class CSVFile:

  def __init__(self, nome_file):
    self.name = nome_file

  def get_data(self):
    
    try:
      file_csv = open(self.name, 'r')
      all_data = []

    except('l errore è qua' )
    for line in file_csv:
      elemento = line.split(',')
      if(elemento[0] != 'Date'):
        all_data.append(elemento)

    file_csv.close()
    return all_data

myfile = CSVFile('shampoo_sales.csv')
print(myfile)
print(myfile.name)
print(myfile.get_data())