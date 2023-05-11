#დავალება1
class Disease:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

    def __str__(self):
        return f"Disease ID: {self.ID}, Name: {self.name}"
class Doctor:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.patients = []
    def __str__(self):
        return f"Doctor: {self.name}, Department: {self.department}"
class Patient:
    def __init__(self, personal_number, name, disease, attending_doctor):
        self.personal_number = personal_number
        self.name = name
        self.disease = [disease]
        self.attending_doctor = attending_doctor
    def __str__(self):
        return f"Patient: {self.name}, Personal Number: {self.personal_number}, Disease: {self.disease[0]}, Attending Doctor: {self.attending_doctor.name}"

    def diagnose(self, disease, doctor=None):
        self.disease.append(disease)
        if doctor:
            self.attending_doctor = doctor
        print(f"{self.name} has been diagnosed with {disease.name} by {self.attending_doctor.name}")
disease1 = Disease("D001", "Flu")
disease2 = Disease("D002", "Pneumonia")

doctor1 = Doctor("John Smith", "Cardiology")

patient1 = Patient("P001", "Alice Brown", disease1, doctor1)
patient1.diagnose(disease2, doctor1)

print(patient1)
print(doctor1)
print(disease1)
print(disease2)
#დავალება2
import requests
from bs4 import BeautifulSoup
import sqlite3
url = 'https://finance.yahoo.com/crypto/'
response = requests.get(url)

if response.status_code == 200:
    print('Request successful!')
else:
    print('Request failed with status code: ', response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')
crypto_list = []
for row in rows[1:]:
    name = row.find('td', class_='data-col1').text.strip()
    price = row.find('td', class_='data-col2').text.strip()
    crypto_list.append((name, price))
conn = sqlite3.connect('Crypto.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS cryptoMarket
             (name TEXT, price TEXT)''')
c.executemany('INSERT INTO cryptoMarket VALUES (?,?)', crypto_list)
conn.commit()
conn.close()
conn = sqlite3.connect('Crypto.sqlite')
c = conn.cursor()
c.execute('SELECT * FROM cryptoMarket')
rows = c.fetchall()
for row in rows:
    print(row[0].ljust(10), row[1].rjust(10))
conn.close()



