class CSVFile:

  def __init__(self, name):

    self.name = name

  def get_data(self):

    data= []

    file = open(self.name, 'r')

    for line in file:
      element = line.split(',')
      element[-1] = element[-1].strip()

      if element[0] != 'Date':
        data.append(element)
      
    file.close()

    return data

file = CSVFile(name='shampoo_sales.csv')
print('Dati: "{}"'.format(file.get_data()))
