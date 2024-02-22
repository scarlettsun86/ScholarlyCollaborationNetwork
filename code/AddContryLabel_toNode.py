#!/usr/bin/env python
# coding: utf-8

# In[132]:


import pandas as pd
import numpy as np
import itertools 
import igraph
from igraph import *
import xlwt


# In[134]:


# Read papers data for each year

# df = pd.read_excel('2016（130）.xlsx')
# df = pd.read_excel('2017（76）.xlsx')
# df = pd.read_excel('2018（138）.xls')
# df = pd.read_excel('2019（159）.xlsx')
# df = pd.read_excel('2020（135）.xlsx')
df = pd.read_excel('2021（217）.xls')

print(df)


# In[135]:


dict={
    'Afghanistan':'阿富汗',
    'Singapore':'新加坡',
    'Angola':'安哥拉',
    'Albania':'阿尔巴尼亚',
    'United Arab Emirates':'阿联酋',
    'Argentina':'阿根廷',
    'Armenia':'亚美尼亚',
    'French Southern and Antarctic Lands':'法属南半球和南极领地',
    'Australia':'澳大利亚',
    'Austria':'奥地利',
    'Azerbaijan':'阿塞拜疆',
    'Burundi':'布隆迪',
    'Belgium':'比利时',
    'Benin':'贝宁',
    'Burkina Faso':'布基纳法索',
    'Bangladesh':'孟加拉国',
    'Bulgaria':'保加利亚',
    'The Bahamas':'巴哈马',
    'Bosnia and Herzegovina':'波斯尼亚和黑塞哥维那',
    'Belarus':'白俄罗斯',
    'Belize':'伯利兹',
    'Bermuda':'百慕大',
    'Bolivia':'玻利维亚',
    'Brazil':'巴西',
    'Brunei':'文莱',
    'Bhutan':'不丹',
    'Botswana':'博茨瓦纳',
    'Central African Republic':'中非共和国',
    'Canada':'加拿大',
    'Switzerland':'瑞士',
    'Chile':'智利',
    'China':'中国',
    'Ivory Coast':'象牙海岸',
    'Cameroon':'喀麦隆',
    'Democratic Republic of the Congo':'刚果民主共和国',
    'Republic of the Congo':'刚果共和国',
    'Colombia':'哥伦比亚',
    'Costa Rica':'哥斯达黎加',
    'Cuba':'古巴',
    'Northern Cyprus':'北塞浦路斯',
    'Cyprus':'塞浦路斯',
    'Czech Republic':'捷克共和国',
    'Germany':'德国',
    'Djibouti':'吉布提',
    'Denmark':'丹麦',
    'Dominican Republic':'多明尼加共和国',
    'Algeria':'阿尔及利亚',
    'Ecuador':'厄瓜多尔',
    'Egypt':'埃及',
    'Eritrea':'厄立特里亚',
    'Spain':'西班牙',
    'Estonia':'爱沙尼亚',
    'Ethiopia':'埃塞俄比亚',
    'Finland':'芬兰',
    'Fiji':'斐',
    'Falkland Islands':'福克兰群岛',
    'France':'法国',
    'Gabon':'加蓬',
    'England':'英国',
    'Ghana':'加纳',
    'Guinea':'几内亚',
    'Gambia':'冈比亚',
    'Guinea Bissau':'几内亚比绍',
    'Equatorial Guinea':'赤道几内亚',
    'Greece':'希腊',
    'Greenland':'格陵兰',
    'Guatemala':'危地马拉',
    'French Guiana':'法属圭亚那',
    'Guyana':'圭亚那',
    'Honduras':'洪都拉斯',
    'Croatia':'克罗地亚',
    'Haiti':'海地',
    'Hungary':'匈牙利',
    'Indonesia':'印尼',
    'India':'印度',
    'Ireland':'爱尔兰',
    'Iran':'伊朗',
    'Iraq':'伊拉克',
    'Iceland':'冰岛',
    'Israel':'以色列',
    'Italy':'意大利',
    'Jamaica':'牙买加',
    'Jordan':'约旦',
    'Japan':'日本',
    'Kazakhstan':'哈萨克斯坦',
    'Kenya':'肯尼亚',
    'Kyrgyzstan':'吉尔吉斯斯坦',
    'Cambodia':'柬埔寨',
    'South Korea':'韩国',
    'Kosovo':'科索沃',
    'Kuwait':'科威特',
    'Laos':'老挝',
    'Lebanon':'黎巴嫩',
    'Liberia':'利比里亚',
    'Libya':'利比亚',
    'Sri Lanka':'斯里兰卡',
    'Lesotho':'莱索托',
    'Lithuania':'立陶宛',
    'Luxembourg':'卢森堡',
    'Latvia':'拉脱维亚',
    'Morocco':'摩洛哥',
    'Moldova':'摩尔多瓦',
    'Madagascar':'马达加斯加',
    'Mexico':'墨西哥',
    'Macedonia':'马其顿',
    'Mali':'马里',
    'Myanmar':'缅甸',
    'Montenegro':'黑山',
    'Mongolia':'蒙古',
    'Mozambique':'莫桑比克',
    'Mauritania':'毛里塔尼亚',
    'Malawi':'马拉维',
    'Malaysia':'马来西亚',
    'Namibia':'纳米比亚',
    'New Caledonia':'新喀里多尼亚',
    'Niger':'尼日尔',
    'Nigeria':'尼日利亚',
    'Nicaragua':'尼加拉瓜',
    'Netherlands':'荷兰',
    'Norway':'挪威',
    'Nepal':'尼泊尔',
    'New Zealand':'新西兰',
    'Oman':'阿曼',
    'Pakistan':'巴基斯坦',
    'Panama':'巴拿马',
    'Peru':'秘鲁',
    'Philippines':'菲律宾',
    'Papua New Guinea':'巴布亚新几内亚',
    'Poland':'波兰',
    'Puerto Rico':'波多黎各',
    'North Korea':'北朝鲜',
    'Portugal':'葡萄牙',
    'Paraguay':'巴拉圭',
    'Qatar':'卡塔尔',
    'Romania':'罗马尼亚',
    'Russia':'俄罗斯',
    'Rwanda':'卢旺达',
    'Western Sahara':'西撒哈拉',
    'Saudi Arabia':'沙特阿拉伯',
    'Sudan':'苏丹',
    'South Sudan':'南苏丹',
    'Senegal':'塞内加尔',
    'Solomon Islands':'所罗门群岛',
    'Sierra Leone':'塞拉利昂',
    'El Salvador':'萨尔瓦多',
    'Somaliland':'索马里兰',
    'Somalia':'索马里',
    'Serbia':'塞尔维亚',
    'Suriname':'苏里南',
    'Slovakia':'斯洛伐克',
    'Slovenia':'斯洛文尼亚',
    'Sweden':'瑞典',
    'Swaziland':'斯威士兰',
    'Syria':'叙利亚',
    'Chad':'乍得',
    'Togo':'多哥',
    'Thailand':'泰国',
    'Tajikistan':'塔吉克斯坦',
    'Turkmenistan':'土库曼斯坦',
    'East Timor':'东帝汶',
    'Trinidad and Tobago':'特里尼达和多巴哥',
    'Tunisia':'突尼斯',
    'Turkey':'土耳其',
    'United Republic of Tanzania':'坦桑尼亚',
    'Uganda':'乌干达',
    'Ukraine':'乌克兰',
    'Uruguay':'乌拉圭',
    'USA':'美国',
    'Uzbekistan':'乌兹别克斯坦',
    'Venezuela':'委内瑞拉',
    'Vietnam':'越南',
    'Vanuatu':'瓦努阿图',
    'West Bank':'西岸',
    'Yemen':'也门',
    'South Africa':'南非',
    'Zambia':'赞比亚',
    'Zimbabwe':'津巴布韦',
    'Taiwan':'中国台湾',
    'Wales':'威尔士',
    'Scotland':'苏格兰'
}


# In[136]:


# Get keywords in dictionary format, that is, country names in english.

cons=list(dict.keys())
cons


# In[137]:


# Find out which country the scholar is from based on the address column.
nodes=[]

for i in df['Addresses']:
    nodes1=[]
    con = str(i).split("; [")

    for afn in df['Author Full Names']:
        auths = afn.split("; ")
        for c in con:
            for auth in auths:
                for ii in cons:
                    if auth in c and ii in c.split(",")[-1]:
                        if ii=='Taiwan':
                            nodes1.append('China')
                            break
                        elif ii=='Wales':
                            nodes1.append('England')
                            break
                        elif ii=='Scotland':
                            nodes1.append('England')
                            break
                        else:
                            nodes1.append(ii)
                            break
    nodes.append(nodes1)
nodes


# In[138]:


# Add country attributes for scholars and store them as a excel file.

book = xlwt.Workbook() 

sheet = book.add_sheet(u'sheet1',cell_overwrite_ok=True)
 
sheet.write(0,0,'author')
sheet.write(0,1,'country')

w =1


for i in df['Addresses']:
    nodes1=[]
    con = str(i).split("; [")

    for afn in df['Author Full Names']:
        auths = afn.split("; ")
        for auth in auths:
    #         print(auth)
            for c in con:
                for ii in cons:
                    if auth in c and ii in c.split(",")[-1]:
                        if ii=='Taiwan':
                            sheet.write(w,0,auth)
                            sheet.write(w,1,'China')
                            w=w+1
#                             nodes1.append('China')
                        elif ii=='Wales':
                            sheet.write(w,0,auth)
                            sheet.write(w,1,'England')
                            w=w+1
#                             nodes1.append('England')
                        elif ii=='Scotland':
                            sheet.write(w,0,auth)
                            sheet.write(w,1,'England')
                            w=w+1

                        else:
                            sheet.write(w,0,auth)
                            sheet.write(w,1,ii)
                            w=w+1

book.save('2021country.xls')
           
# nodes


# In[139]:


coun= pd.read_excel('2021country.xls')

coun


# In[140]:


# Delete duplicate rows

ccoun1=coun.drop_duplicates(subset=['author'],keep='first')
author=ccoun1['author'].values.tolist()
country=ccoun1['country'].values.tolist()
ccoun1


# In[141]:


country_node=ccoun1['country'].values.tolist()
country_node=list(set(country_node))
country_node


# In[142]:


# Putting two authors who have a collaborative relationship into a tuple makes it easier to build the network later 

edges=[]
for i in df['Author Full Names']:
    auths = i.split("; ")
    a=list(itertools.combinations(auths, 2))
    edges=a+edges
print(edges)
len(edges)


# In[143]:


# Replace the name of the scholar with the country to which they belong, based on the country label previously added.

edges1=[]
for t in edges:
    edges2=[]
    for tt in t:
        if tt in author:
            num=author.index(tt)
            con=country[num]
            edges2.append(con)
        else:
            edges2.append('nan') #Some scholars do not provide address information, 
#                                 and the country label of such scholars is filled with nan value
    edges1.append(tuple(edges2))
            
print(edges1)
len(edges1)        
        


# In[155]:


# Delete edges containing nan values.

for i in edges1:
    if 'nan' in i:
        edges1.remove(i)

print(edges1)
len(edges1)        


# In[156]:


# Calculate the number of edges composed of authors from different countries.

w=0
for n in edges1:
    if len(n)==len(set(n)):
        w=w+1
print(w)


# In[157]:


# Use the total number of collaborative edges as the denominator and the edges composed of authors from different countries as the numerator in order to calculate its cross-country collaboration degree.

rate=w/len(edges1)
rate=round(rate*100,2)
print(str(rate)+'%')


# In[158]:


# Modify the data format to one accepted by Gephi.

Source1=[]
Target1=[]

for e in edges1:
    Source1.append(e[0])
    Target1.append(e[1])

con_edges=pd.DataFrame({'Source':Source1,'Target':Target1})

con_edges


# In[159]:


# Build network.

g2= Graph()
g2.add_vertices(country_node)
g2.add_edges(edges1)


# In[ ]:


communities = g2.community_multilevel()   
plot(communities,vertex_label=country_node,vertex_size=15,
     bbox=(600,600),vertex_label_size=8,autocurve=True,margin=10,vertex_label_dist=-2)


# In[160]:


con_=pd.DataFrame({'country':country_node})
con_


# In[162]:


# Calculate network centrality indicators.

con_['Degree']=np.round(g2.degree(),2)
con_['Closeness']=np.round(g2.closeness(),2)
con_['Betweeness']=np.round(g2.betweenness(),2)
con_


# In[163]:


# Take the top 10 nodes based on degree.

degree=con_.sort_values(by=['Degree'],axis=0,ascending=False).head(10)

degree.to_csv('2021degree.xls')
degree


# In[164]:


# Take the top 10 nodes based on the Closeness Centrality.

clo=con_.sort_values(by=['Closeness'],axis=0,ascending=False).head(10)

clo.to_csv('2021Closeness.xls')
clo


# In[165]:


# Take the top 10 nodes based on the Betweenness Centrality.
bet=con_.sort_values(by=['Betweeness'],axis=0,ascending=False).head(10)
bet.to_csv('2021Betweeness.xls')
bet


# In[166]:


# Store nodes and edges as csv files.

con_edges.to_csv("2021con-edges.csv",index=False,sep=',')

n=pd.DataFrame({'ID':country_node,'Label':country_node})
n.to_csv("2021con-nodes.csv",index=False,sep=',')


# In[ ]:





# In[ ]:




