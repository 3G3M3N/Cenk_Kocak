import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("openpowerlifting-2024-01-06-4c732975.csv", low_memory=False)
df1
df1 = df1.loc[(df1["Country"]=="Turkey") & (df1["Federation"]=="IPF")]
df1
cenk = df1.loc[(df1["Name"]=="Cenk Koçak")]
cenk
Turkish = df.loc[(df["MeetCountry"]=="Turkey")]

#grafikler
#kilo
data = {
    "Name": ["Cenk Koçak","Cenk Koçak", "Cenk Koçak", "Cenk Koçak", "Cenk Koçak"],
    "BodyweightKg": [145.37,143.20, 135.45, 119.46, 119.50],
    "Date": ["2023-12-12","2023-06-11", "2022-06-06", "2021-09-23", "2019-06-04"]
}
df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

plt.plot(df["Date"], df["BodyweightKg"], marker='o')
plt.title("Cenk Koçak'ın Kilosunun Zaman İçinde Değişimi")
plt.xlabel("Tarih")
plt.ylabel("Kilo (kg)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#deadlift
data = {
    "Name": ["Cenk Koçak", "Cenk Koçak", "Cenk Koçak", "Cenk Koçak", "Cenk Koçak"],
    "3. Deadlift Hakkı": [400.5, 370.0, 370.0, 370.0, 352.5],  # Deadlift hakkını burada varsayılan olarak ekleyin
    "Date": ["2023-12-11", "2023-06-11", "2022-06-06", "2021-09-23", "2019-06-04"]
}
df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

plt.plot(df["Date"], df["3. Deadlift Hakkı"], marker='o')
plt.title("Cenk Koçak'ın 3. Deadlift Hakkının Zaman İçinde Değişimi")
plt.xlabel("Tarih")
plt.ylabel("Deadlift Hakkı (kg)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

pd.set_option('display.max_columns', None)
#tüm columnları görmek için 
cenk

#total
data = {
    "Name": ["Cenk Koçak","Cenk Koçak", "Cenk Koçak", "Cenk Koçak", "Cenk Koçak"],
    "TotalKg": [1018,980.0, 930.0, 900.0, 892.5],  # TotalKg sütununu burada varsayılan olarak ekleyin
    "Date": ["2023-12-12","2023-06-11", "2022-06-06", "2021-09-23", "2019-06-04"]
}
df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

plt.plot(df["Date"], df["TotalKg"], marker='o')
plt.title("Cenk Koçak'ın Total Kilogramının Zaman İçinde Değişimi")
plt.xlabel("Tarih")
plt.ylabel("Toplam Kilogram")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
