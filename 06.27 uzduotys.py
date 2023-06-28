import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales_data_sample.csv', encoding="ISO-8859-1")#encoding rašoma dėl failo klaidos

### 1.Suskirstykite klientus pagal šalį.
# pagal_saly=df.groupby('COUNTRY')['CUSTOMERNAME'].size()
# pagal_saly.plot(kind='bar')
# plt.title('Suveskite statistika pagal jų vardus ir atlyginimus')
# plt.xlabel('Klieabtuskaicius')
# plt.ylabel('Salis')
# plt.show()


### 5. su pribombasais. Sukurkite skritulinę diagramą,
# kurioje būtų pavaizduota klientų skaičiaus pasiskirstymas pagal šalis
# pagal_saly=df['COUNTRY'].value_counts().nlargest(10)
# plt.bar(pagal_saly.index, pagal_saly.values)
# plt.title('Suveskite statistika pagal jų vardus ir atlyginimus')
# plt.xlabel('Klientuskaicius')
# plt.ylabel('Salis')
# plt.xticks(rotation=90)
# plt.show()


### 2. Atrinkite užsakymus, kurių suma viršija 1000 eurų
# uzsakymai_virs_1000 = df[df['SALES'] > 1000]
# print(uzsakymai_virs_1000)

### 2. SPRENDIMAS SU PAPILDOMA UŽDUOTIM. Sukuriame naują stulpelį ir atvaizduojame daugybos rezultatą ir
### parodome du stulpelius, plius į faile pridedame stulpelį "TOTAL"
# df['TOTAL']= df['QUANTITYORDERED'] * df['PRICEEACH']
# uzsakymai_virs_1000 = df[df['TOTAL'] > 5000][['TOTAL', 'PRICEEACH']]
# df.to_csv('sales_data_sample.csv', index=False)
# print(uzsakymai_virs_1000)

###3. Išfiltruokite užsakymus, kurie buvo pristatyti nuo 2003/9/30 iki 2005/03/15 .
# df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'], format='%d/%m/%Y %H:%M', errors='coerce')
# datu_filtravimas = df[(df['ORDERDATE'] >='9/9/2003') & (df['ORDERDATE']<='3/3/2005')]
# print(datu_filtravimas)
###3. antras variantas
# df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
# start_date = '2003-09-30'
# end_date = '2005-03-15'
# order_date = df[df['ORDERDATE'].between(start_date, end_date)]
# print(order_date)

### 4. Išfiltruokite užsakymus, kurių statusas 'Disputed';
# disputed = df[df['STATUS']=='Disputed']
# print(disputed)




