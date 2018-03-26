
# coding: utf-8

# This is markdown
# ============
# 
# Paragraphs are separated by a blank line.
# 
# 2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
# look like:
# 
#   * this one
#   * that one
#   * the other one
# 
# Note that --- not considering the asterisk --- the actual text
# content starts at 4-columns in.
# 
# > Block quotes are
# > written like so.
# >
# > They can span multiple paragraphs,
# > if you like.
# 
# Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
# in chapters 12--14"). Three dots ... will be converted to an ellipsis.
# Unicode is supported. ☺

# In[1]:


# this i my first jupyter note-book

print('hello world')


# In[2]:


'hello world'


# In[3]:


var = 'raghav'


# In[15]:


var


# In[14]:


var = 'gupta'


# In[6]:


get_ipython().system('ls -l')
get_ipython().system("echo '\\nthis is a bash command'")
#!pip list


# In[7]:


get_ipython().run_line_magic('lsmagic', '')


# In[8]:


get_ipython().system('ls')
get_ipython().run_line_magic('ls', '')


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()


# In[11]:


get_ipython().run_cell_magic('HTML', '', '<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/458791/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"></iframe>')


# In[12]:


get_ipython().run_cell_magic('timeit', '', 'for i in range(10**1):\n    pass')


# In[13]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 10))
df.head()

