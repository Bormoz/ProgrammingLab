#===========================
# Classe per le eccezioni
#===========================
#Creo la classe ExamException che utilizzerò per poter
#alzare le eccezioni nel programma
class ExamException(Exception):
    pass

#==========================
# Classe per il file CSV
#==========================
#Creo la classe CSVTimeSeriesFile la quale mi servirà per creare
#una lista di liste contenente i dati del file data.csv
class CSVTimeSeriesFile():

    #si inizializza la classe stabilendo il nome
    def __init__(self, name):
        
        self.name = name

    #verifico di riuscire ad aprire e leggere il file
    #in caso contrario impostp can_read falsa e stampo l'errore  
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except ExamException as e:
            self.can_read = False
            print('Apertura file non riuscita. Errore: "{}"'.format(e))

    def get_data(self):
        
        #se can_read è falsa stampo a schermo che il file non è apribile
        #e non stampo nessun risultato
        if not self.can_read:
            print('Errore, file non aperto o illeggibile')
            return None
        
        #nel caso can_read sia vera continuo con la creazione della lista di 
        #liste. Tramite un ciclo for divido ogni riga del file alla comparsa
        #della virgola per poi aggiungere ogni lista formata alla lista data
        else:
            data = []  

            file = open(self.name, 'r')
            for line in file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                if elements[0] != 'date':            
                    data.append(elements)

            file.close()    
            return data

#================================================
# Funzione per calcolare la media di passeggeri
#================================================
#definisco la funzione che calcoli la media dei passeggeri
def compute_avg_monthly_difference(time_series, first_year, last_year):

    if type(first_year) is not str:
        raise ExamException('First_year non è un valore accettabile dato che il tipo di dato inserito è: {}'.format(type(first_year)))

    if type(last_year) is not str:
        raise ExamException('Last_year non è un valore computabile. Tipo di dato inserito: {}'.format(type(last_year)))

    if first_year.isdigit() is False:
        raise ExamException('First_year non è un valore trasformabile ad intero. Valore inserito: {}'.format(first_year))

    if last_year.isdigit() is False:
        raise ExamException('Last_year non è un valore trasformabile ad intero. Valore inserito: {}'.format(last_year))

    #dichiaro che la lista_dati sia una lista contente tutti i numeri
    #di passeggeri degli anni che prendo in considerazione
    #anni è il numero di anni che vado a considerare
    #n_p_a è una lista di liste contenenti i dati divisi per anno 
    #che verranno aggiunti in seguito.
    lista_dati = [int(i[1]) for i in time_series if int(i[0][:4]) >= int(first_year) and int(i[0][:4]) <= int(last_year)]
    anni = int(last_year)-int(first_year)+1
    n_p_a = [[]for i in range(0,anni)] 

    #dichiaro una variabile che mi permetta di inserire nella lista
    #n_p_a i numeri dei passeggeri divisi per anno
    num_el = 0
    for i in range(0,len(lista_dati)):
        if i != 0 and i % 12 == 0: 
                num_el = num_el + 1
        n_p_a[num_el].append(lista_dati[i])
        
    #dichiaro una lista in cui verrà inserito l'incremento medio
    #dei passeggeri per mese negli anni considerati
    #faccio anche in modo che se i passeggeri di un anno sono 0
    # e ci sono solo due anni per quel mese considererò la media 
    #nulla. Se invece sono più di due gli anni ignoro le riga senza 
    #dati e procedo al calcolo della media
    #Altrimenti se tutti i dati sono presenti procedo
    #con la media e agginugo l'elemento alla lista media
    conta = 0
    inc_m = 0
    
    media = []

    for i in range(0,12):
        for j in range(1,anni):
            if (n_p_a[j][i] == 0 or n_p_a[j-1][i] == 0) and anni == 2:
                inc_m = 0
            else: 
                if (n_p_a[j][i] == 0 or n_p_a[j-1][i] == 0) and anni > 2:
                    conta = conta + 1
                    if(conta - anni < 2):
                        inc_m = 0
                        j = anni
                    else:
                        inc_m = inc_m + 0
                else:
                    inc_m = inc_m + n_p_a[j][i] - n_p_a[j-1][i]
          
        media.append(inc_m/(anni-1))
        #dopo aver calcolato l'incremento medio per un mese
        #setto l'incremento a 0 e calcolo per il mese successivo
        inc_m = 0 
    return media  

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print('nome file: {}'.format(time_series_file.name))
print('contenuto file: {}'.format(time_series))
print('')
print("La media dell'incremento di passeggeri ogni mese è: {} ".format(compute_avg_monthly_difference(time_series,"1949","1951")))