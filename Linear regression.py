#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
print(tf.version)


# In[2]:


import tensorflow as tf


# In[3]:


tensorflow --version


# In[ ]:


tf.version


# In[ ]:


import tensorflow as tf
print(tf.version)


# In[ ]:


tensorflow_version 2.x


# In[4]:


string= tf.Variable("This is a string",tf.string)


# In[7]:


rank1_tensor = tf.Variable(["Test","Ok","tim"],tf.string)


# In[9]:


rank2_tensor = tf.Variable([["test", "ok"], ["test", "Yes"]], tf.string)


# In[10]:


tf.rank(rank1_tensor)


# In[11]:


rank2_tensor.shape


# In[12]:


rank1_tensor.shape


# In[17]:


#%tensorflow_versioon 2.x
import tensorflow as tf
print(tf.version)

t=tf.zeros([5,5,5,5])
t=tf.reshape(t,[125,-1])
print(t)


# In[18]:


get_ipython().system('pip install -q sklearn')


# In[19]:


from __future__ import absolute_import, dvision, print_function, unicode_literals


# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Ipython.display import clear_output


# In[21]:


get_ipython().system('pip install pandas')


# In[22]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Ipython.display import clear_output


# In[23]:


get_ipython().system('pip install matplotlib')


# In[24]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Ipython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_colum as fc

import tensorfow as tf


# In[25]:


get_ipython().system('pip install Ipython')


# In[26]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Ipython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_colum as fc

import tensorfow as tf


# In[30]:


from Ipython.display  import clear_output
  


# In[31]:


get_ipython().system('pip install Ipython')


# In[32]:


get_ipython().system('pip install clear_output')


# In[33]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Ipython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_colum as fc

import tensorfow as tf


# In[34]:


get_ipython().system('pip install matplotlib.pyplot')


# In[35]:


get_ipython().system('pip install pyplot')


# In[36]:


get_ipython().system('pip Ipython.display')


# In[37]:


get_ipython().system('pip install ipython')


# In[38]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.feature_column as fc

import tensorfow as tf


# In[39]:


get_ipython().system('pip freeze | grep tensorflow')


# In[40]:


get_ipython().system('pip freeze | findstr tensorflow')


# In[42]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.feature_column as fc

import tensorflow as tf


# In[43]:


# Load dataset.
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')


# In[44]:


print(dftrain.head())


# In[45]:


dftrain.describe()


# In[46]:


dftrain.shape


# In[47]:


y_train.head()


# In[48]:


dftrain.age.hist(bins=20)


# In[49]:


dftrain.sex.value_counts().plot(kind='barh')


# In[50]:


dftrain['class'].value_counts().plot(kind='barh')


# In[51]:


pd.concat([dftrain, y_train], axis=1).groupby('sex').survived.mean().plot(kind='barh').set_xlabel('% survive')


# In[52]:


CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = dftrain[feature_name].unique()  # gets a list of all unique values from given feature column######  important hehe
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(feature_columns)


# In[53]:


def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():  # inner function, this will be returned
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))  # create tf.data.Dataset object with data and its label
    if shuffle:
      ds = ds.shuffle(1000)  # randomize order of data
    ds = ds.batch(batch_size).repeat(num_epochs)  # split dataset into batches of 32 and repeat process for number of epochs
    return ds  # return a batch of the dataset
  return input_function  # return a function object for use

train_input_fn = make_input_fn(dftrain, y_train)  # here we will call the input_function that was returned to us to get a dataset object we can feed to the model
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)


# In[54]:


linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)
# We create a linear estimtor by passing the feature columns we created earlier


# In[55]:


linear_est.train(train_input_fn)  # train
result = linear_est.evaluate(eval_input_fn)  # get model metrics/stats by testing on tetsing data

clear_output()  # clears consoke output
print(result['accuracy'])  # the result variable is simply a dict of stats about our model


# In[ ]:




