class CSVFile:

  def __init__(self, name):
    self.name = name

  def get_data(self):
    all_data = []
    file_csv = open('shampoo_sales.csv', 'r')

    for line in file_csv:
      line = line.strip('\n')
      elemento = line.split(',')
      if(elemento[0] != 'Date'):
        all_data.append()

    file_csv.close()
    return all_data

myfile = CSVFile('shampoo_sales.csv')
print(myfile)
print(myfile.name)
print(myfile.get_data()) 