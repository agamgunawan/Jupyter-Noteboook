#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import library
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#baca dataset
df = pd.read_csv(r'Supermart_Grocery_Sales_Retail_Analytics_Dataset.csv')

#dataset didapat di
#https://www.kaggle.com/datasets/mohamedharris/supermart-grocery-sales-retail-analytics-dataset


# In[3]:


#lihat bentuk dataset
df.shape


# In[4]:


#tampilkan nama kolom/atribut dataset
df.columns


# In[5]:


#tampilkan 10 dataset teratas
df.head(10)


# In[6]:


#lihat info dataset
df.info()


# In[7]:


#lihat rangkuman dataset
df.describe()


# In[8]:


#cari outlier
#cari terlebih dahulu nilai quntile
Q1 = df[['Sales']].quantile(0.25)
Q3 = df[['Sales']].quantile(0.75)
IQR = Q3-Q1
print(IQR)


# In[9]:


#cari outlier
print((df < (Q1 < 1.5*IQR)) | (df > (Q3 + 1.5*IQR)))

#False berarti nilai-nilai ini valid sedangkan True menunjukkan adanya outliers


# In[ ]:





# In[10]:


#rata-rata penjualan berdasarkan kategori
df.groupby(['Category']).mean('Sales')

# digunakan untuk mengetahui penjualan, diskon dan keuntungan (profit) dari setiap kategori


# In[11]:


#urutkan data sales dari yang terbesar
df.sort_values('Sales', ascending=False)

#digunakan untuk mengetahui urutan penjualan teratas/terbesar


# In[12]:


#ambil data sales terbesar
df.sort_values(['Sales'], ascending=False).head(10)


# In[13]:


#filter menampilkan data kolom tertentu
df[['Category','Sub Category','Sales']].head(10)


# In[14]:


#ambil data sales kurang dari 750
df[df['Sales'] < 750]


# In[15]:


#ambil data sales antara 1000-2000
df[(df['Sales'] >= 1000 ) & (df['Sales'] <=2000) ]


# In[16]:


#ambil data kategori snacks dengan penjualan lebih dari 2000
df[(df['Category'] == 'Snacks' ) & (df['Sales'] > 2000) ]


# In[17]:


#buat kolom tahun pada dataset
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df


# In[18]:


#rata-rata penjualan dari tahun ke tahun
df.groupby(['Year']).mean('Sales')


# In[19]:


#total penjualan berdasarkan kategory
df.groupby(['Category']).sum('Sales')


# In[ ]:





# In[20]:


#visualisai penjualan dari tahun ke tahun
plt.figure(figsize = (10, 5))
df.groupby(['Year'])['Sales'].sum().plot(color='green', marker='o',linewidth=2)
plt.title('Total Penjualan Tahun 2015-2018', loc='center', pad=20, fontsize=15, color='blue')
plt.xlabel('Tahun', fontsize=12)
plt.ylabel('Total Penjualan', fontsize=12)
plt.show()


# ### Insight
# Dari diagram diatas didapatkan beberapa insight yaitu :
# 1. Selalu terjadi kenaikan penjualan dari tahun ke tahun
# 2. Kenaikan tertinggi terjadi pada tahun 2017-2018

# In[ ]:





# In[22]:


#visualisasi perbandingan penjualan berdasarkan kategory
df.groupby('Category')['Sales'].sum().sort_values(ascending=False).plot(kind='bar', color='orange')
plt.title('Penjualan Berdsarkan Kategori',loc='center',pad=30,fontsize=15, color='blue')
plt.xlabel('Kategori', fontsize = 12)
plt.ylabel('Total',fontsize = 12)
plt.xticks(rotation=30)
plt.show()


# ### Insight
# Dari diagram diatas didapatkan beberapa insight yaitu :
# 1. Penjualan dari semua kategori relatif sama, tidak ada yang sangat tinggi ataupun sangat rendah
# 2. Pejualan tertinggi dimiliki oleh kategori Eggs, Meaat & Fish

# In[ ]:





# In[23]:


#visualisasi pernjualan berdasarkan wilayah (region)
df.groupby('Region')['Sales'].sum().sort_values(ascending=False).plot(kind='bar')
plt.title('Penjualan Berdasarkan Wilayah',loc='center', pad=30,fontsize=15, color='blue')
plt.xlabel('Wilayah', fontsize = 12)
plt.ylabel('Total',fontsize = 12)
plt.xticks(rotation=30)
plt.show()


# ### Insight
# Dari diagram diatas didapatkan beberapa insight yaitu :
# 1. Penjualan berdasarkan wilayah, penjualan tertinggi terdapat di wilayah west (barat) di ikuti east (timur), central (tengah) dan terendah yaitu north (utara)
# 

# In[25]:


#buat kolom tahun pada dataset
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
df


# In[26]:


#visualisasi penjualan berdasarkan bulan
df.groupby('Month')['Sales'].sum().plot(kind='bar')
plt.title('Penjualan Berdasarkan Bulan',loc='center',pad=30,fontsize=15, color='blue')
plt.xlabel('Bulan', fontsize = 12)
plt.ylabel('Total',fontsize = 12)
plt.show()


# ### Insight
# Dari diagram diatas didapatkan beberapa insight yaitu :
# 1. Penjualan berdasarkan bulan disemua tahun
# 2. penjualan terkecil terjadi pada bulan ke 2 dan terbesar terdapat di bulan 11
# 3. Di awal tahun penjualan relatif kecil
# 4. Di pertengahan tahun penjualan relatif sama / stabil
# 5. Di Kuartal tahun terakhir (4 bulan terakhir) penjualan relatif tinggi

# In[ ]:





# In[27]:


#vizualisasi berdasarkan totol penjualan perkategori
#belum fix
plt.figure(figsize = (9, 6))
plt.bar(x = df["Category"],
       height = df["Sales"])
plt.title("Daftar Penjualan Berdasarkan Kategori", pad=20, fontsize=15)
plt.xticks(rotation=45, fontsize=13)
plt.yticks(fontsize=13)
plt.ylabel("Jumlah Unit Terjual", fontsize=13)
plt.show


# In[ ]:





# In[29]:


#coba fitur baru python
#sweetviz
#digunakan untuk melakukan EDA secara otomatis
import sweetviz as sv
analyze_report = sv.analyze(df)
analyze_report.show_html('hasil.html', open_browser=True)


# In[30]:


#coba fitur baru python
#autoviz
#digunakan untuk melakukan visualisasi otomatis
from autoviz.AutoViz_Class import AutoViz_Class


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')

AV = AutoViz_Class()

viz = AV.AutoViz('Supermart_Grocery_Sales_Retail_Analytics_Dataset.csv' ,sep=",")


# In[ ]:





# ## Revisi / Tambahan

# In[39]:


#visualisasi perbandingan penjualan dari tahun 2015-2018 berdasarkan bulan
df.groupby(['Month','Year'])['Sales'].sum().unstack().plot(cmap='plasma')
plt.title('Perbandingan Tren Penjualan Berdasarkan Tahun',loc='center', pad=25, fontsize=20, color='blue')
plt.xlabel('Bulan', fontsize = 12)
plt.ylabel('Penjualan',fontsize = 12)
plt.grid(color='darkgray')
plt.gcf().set_size_inches(10, 5)
plt.show()


# ### Insight
# Dari diagram diatas didapatkan beberapa insight yaitu :
# 1. Penjualan dari tahun ke tahun relatif terjadi peningkatan
# 2. Tahun 2018 menjadi tahun dengan penjualan tertingg
# 3. Di awal tahun penjualan relatif rendah
# 4. Di pertengahan tahun penjualan relatif stabil / sama
# 5. Di bulan ke 3, 9 dan 11 terjadi penigkatan penjualan di semua tahun
# 6. Bulan ke 10 selalu terjadi penurunan penjualan pada setiap masing-masing tahun

# In[ ]:





# In[48]:


#visualisasi perbandingan rata-rata penjualan dari tahun 2015-2018 berdasarkan bulan
df.groupby(['Month','Category'])['Sales'].mean().unstack().plot(cmap='viridis')
plt.title('Perbandingan Tren Penjualan Berdasarkan Kategori-Bulan',loc='center', pad=25, fontsize=20, color='blue')
plt.xlabel('Bulan', fontsize = 12)
plt.ylabel('Penjualan',fontsize = 12)
plt.grid(color='darkgray')
plt.gcf().set_size_inches(15, 8)
plt.show()


# ### Insight
# Dari diagram diatas didapatkan beberapa insight yaitu :
# 1. Penjualan tertinggi per bulan dimiliki oleh kategori Fruits & vegigies yaitu pada bulan ke 3
# 2. penjualan terendah per bulan dimiliki oleh kategori Snacks yaitu pada bulan ke 4
# 3. Bulan ke 4, 7, dan 10 sebagian besar terjadi peningkatan penjualan dari setiap kategori

# In[ ]:





# In[45]:


#visualisasi berdasarkan wilayah / Region
#Perbaikan/penambahan warna
#Insight sudah ada pada grafik yang sebelumnya
import seaborn as sns
plt.figure(figsize=(10,5))
sns.countplot(x = df['Region'])
plt.title('Perbandingan Penjualan Berdasarkan Wilayah', pad=25, fontsize=20, color='blue')
plt.ylabel('Jumlah', size=14)
plt.xlabel('Wilayah', size=14)
plt.show()


# ### Insight
# Dari diagram diatas didapatkan beberapa insight yaitu :
# 
# Penjualan berdasarkan wilayah, penjualan tertinggi terdapat di wilayah west (barat) di ikuti east (timur), central (tengah) dan terendah yaitu north (utara)

# In[ ]:





# In[46]:


#Visualisasi penjualan berdasarkan Kategori
#Perbaikan/penambahan warna
plt.figure(figsize=(10,5))
sns.countplot(x = df['Category'])
plt.title('Perbandingan Penjualan Berdasarkan Kategori', pad=25, fontsize=20, color='blue')
plt.ylabel('Jumlah', size=14)
plt.xlabel('Kategori', size=14)
plt.xticks(rotation=15)
plt.show()


# ### Insight
# Dari diagram diatas didapatkan beberapa insight yaitu :
# 1. Penjualan relatif sama, tidak ada yang signifikan pada masing-masing kategori
# 2. Penjualan terendah dimiliki oleh kategori Oil & Masala dan terbesar oleh Snacks

# In[ ]:





# In[47]:


#visualisasi korelasi Penjualan dan bulan
#belum fix
plt.figure(figsize=(10,10))
plt.scatter(df['Month'],df['Sales'], marker='.', color='blue')
plt.title('Korelasi antara Penjualan dengan Bulan', pad=25, fontsize=20, color='blue')
plt.xlabel('Bulan', fontsize = 12)
plt.ylabel('Penjualan',fontsize = 12)
plt.show()


# In[ ]:




