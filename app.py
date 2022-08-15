#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "post":
        return(render_template("index.html",result1="temp",result2="temp"))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[4]:


if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=False)


# In[ ]:




