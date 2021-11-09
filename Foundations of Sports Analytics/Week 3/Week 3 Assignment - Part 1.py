#!/usr/bin/env python
# coding: utf-8

# ## Part 1 - NBA Player Comparision

# In[1]:


# As usual, we begin by importing the packages we will need

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# The data consists of the shot log for the NBA season 2016/17

shot = pd.read_csv("Assignment Data/Week 3/NBA shotlog_16_17.csv")
pd.set_option('display.max_columns', 100)
print(shot.columns.tolist())
shot.describe()


# ## Westbrook - Durant Comparision

# In[8]:


shot['halfcourt_x'] =np.where(shot['location_x'] < 933/2, 933 - shot['location_x'],shot['location_x'])
shot['halfcourt_y'] =np.where(shot['location_x'] < 933/2, 500 - shot['location_y'],shot['location_y'])
shot.describe()


# In[12]:


Westbrook = shot[shot['shoot_player'] == 'Russell Westbrook']
hxW = Westbrook['halfcourt_x']
hyW = Westbrook['halfcourt_y']
colors = np.where(Westbrook['current_shot_outcome']=='SCORED','r',np.where(Westbrook['current_shot_outcome']=='MISSED','b','g'))
plt.figure(figsize=(94/12,50/6))
plt.scatter(hxW,hyW, s=10, c= colors, marker= '.')
plt.grid(True)
plt.title("Russell Westbrook", fontsize = 15)


# In[13]:


Durant = shot[shot['shoot_player'] == 'Kevin Durant']
hxD = Durant['halfcourt_x']
hyD = Durant['halfcourt_y']
colors = np.where(Durant['current_shot_outcome']=='SCORED','r',np.where(Durant['current_shot_outcome']=='MISSED','b','g'))
plt.figure(figsize=(94/12,50/6))
plt.scatter(hxD,hyD, s=10, c= colors, marker= '.')
plt.grid(True)
plt.title("Kevin Durant", fontsize = 15)


# In[14]:


# Russell Westbrook and Kevin Durant side by side

f = plt.figure(figsize=(94/6,50/6))
ax = f.add_subplot(121)
colors = np.where(Westbrook['current_shot_outcome']=='SCORED','r',np.where(Westbrook['current_shot_outcome']=='MISSED','b','g'))
ax = plt.scatter(hxW,hyW, s=10, c= colors, marker= '.')
plt.grid(True)
plt.title("Russell Westbrook", fontsize = 15)
ax = f.add_subplot(122)
colors = np.where(Durant['current_shot_outcome']=='SCORED','r',np.where(Durant['current_shot_outcome']=='MISSED','b','g'))
ax = plt.scatter(hxD,hyD, s=10, c= colors, marker= '.')
plt.grid(True)
plt.title("Kevin Durant", fontsize = 15)


# ## Jordan - Howard Comparision

# In[15]:


shot['shoot_player'].value_counts()


# In[23]:


# DeAndre Jordan and Dwight Howard
# shot[shot['shoot_player'].str.contains('Jordan')].shoot_player.value_counts()

Jordan = shot[shot['shoot_player'] == 'DeAndre Jordan']
hxJ = Jordan['halfcourt_x']
hyJ = Jordan['halfcourt_y']

Howard = shot[shot['shoot_player'] == 'Dwight Howard']
hxH = Howard['halfcourt_x']
hyH = Howard['halfcourt_y']

f = plt.figure(figsize=(94/6,50/6))
ax = f.add_subplot(121)
colors = np.where(Jordan['current_shot_outcome']=='SCORED','r',np.where(Jordan['current_shot_outcome']=='MISSED','b','g'))
ax = plt.scatter(hxJ,hyJ, s=10, c= colors, marker= '.')
plt.grid(True)
plt.title("DeAndre Jordan", fontsize = 15)
ax = f.add_subplot(122)
colors = np.where(Howard['current_shot_outcome']=='SCORED','r',np.where(Howard['current_shot_outcome']=='MISSED','b','g'))
ax = plt.scatter(hxH,hyH, s=10, c= colors, marker= '.')
plt.grid(True)
plt.title("Dwight Howard", fontsize = 15)


# ## Lopez - Lopez Comparision

# In[21]:


# Brook Lopez and Robin Lopez

Brook = shot[shot['shoot_player'] == 'Brook Lopez']
hxB = Brook['halfcourt_x']
hyB = Brook['halfcourt_y']

Robin = shot[shot['shoot_player'] == 'Robin Lopez']
hxR = Robin['halfcourt_x']
hyR = Robin['halfcourt_y']

f = plt.figure(figsize=(94/6,50/6))
ax = f.add_subplot(121)
colors = np.where(Brook['current_shot_outcome']=='SCORED','r',np.where(Brook['current_shot_outcome']=='MISSED','b','g'))
ax = plt.scatter(hxB,hyB, s=10, c= colors, marker= '.')
plt.grid(True)
plt.title("Brook Lopez", fontsize = 15)
ax = f.add_subplot(122)
colors = np.where(Robin['current_shot_outcome']=='SCORED','r',np.where(Robin['current_shot_outcome']=='MISSED','b','g'))
ax = plt.scatter(hxR,hyR, s=10, c= colors, marker= '.')
plt.grid(True)
plt.title("Robin Lopez", fontsize = 15)


# In[22]:


shot


# In[ ]:




