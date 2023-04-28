<p align="center">
  <img src="https://i.imgur.com/4TfRxmI.png" alt="ctrldf"></img>
  <br/>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54"></img></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/-Streamlit-61DAFB?style=plastic&logo=streamlit"></img></a>
  <a href="https://matplotlib.org/"><img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=plastic&logo=matplotlib&logoColor=black"></img></a>
  <a href="https://numpy.org/doc/stable/index.html"><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=plastic&logo=numpy&logoColor=white"></img></a>
  <a href="https://pandas.pydata.org/docs/index.html"><img src="https://img.shields.io/badge/pandas-%23150458.svg?style=plastic&logo=pandas&logoColor=white"></img></a>
  <a href="http://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic"></img></a>
  </a>

  
  <br/>
  <a href="#Documentation">Documentation</a> ·
  <a href="https://github.com/joshjetson/SCDF/issues">Report a Bug</a> ·
  <a href="#Demo">Demo</a> .
  <a href="https://github.com/joshjetson/SCDF/issues">Request Feature</a> ·
  <a href="https://github.com/joshjetson/SCDF/pulls">Send a Pull Request</a>

</p>

## Controller DF

[]()

<i>A python library which creates a simple and easy to use data frame controller.
Using this library, along with streamlit and minimal (*included*) code, anyone can spin up a web app which allows you to control, manipulate and display a data set quickly and easily.
</i>

## Demo

<table>
<tr>
<td>
<center>

<img src="/pics/exgif.gif"></img>

- Quick column metrics

  <img src="/pics/ex1.gif"></img>

- Rapid column filter

  <img src="/pics/ex3.png"></img>

- Instant type based column widgets

  <img src="/pics/ex2.png"></img>
</center>

</table>
</tr>
</td>

## Installation

```
$ pip install controllerDF
```

## Getting started

<i>After you pip install the module</i>

<ins>

**Batteries included method:**

</ins>

<details><summary>Quick start</summary>

>
> - `Copy the included test_code.py`
> - `Rename the file to your projects name`
> ~~~
> $ streamlit run your_project.py 
> ~~~
> - `Drag and drop csv file`
> - `Enjoy!`

</details>

<ins>

**Batteries excluded method:**

</ins>

<details><summary>Module only</summary>

> ~~~
> import streamlit_controllerDF as sc
> ~~~
> - `see documentation for usage`


</details>

## Documentation

<table>
<tr>
<td>

**class streamlit_controllerDF.Widgets(dataframe, omit_columns=list())**


> Parameters:
>> - dataframe: A pandas data frame
>>> - *Two-dimensional, size-mutable, potentially heterogeneous tabular data.*
>> - omit_columns: A list of column names to be excluded
>>> - *The column names must be exact*

#### Example
```
import streamlit_controllerDF as sc
import pandas as pd

mydf = pd.read_csv('mycsv.csv')

ctrldf = sc.Widgets(mydf,omit_columns=['Engine_Size', 'Year'])
```

**method streamlit_controllerDF.Widgets.metrics()**

> Parameters:
>> - *None*

#### Example
```
import streamlit_controllerDF as sc
import pandas as pd

mydf = pd.read_csv('mycsv.csv')

ctrldf = sc.Widgets(mydf,omit_columns=['Engine_Size', 'Year'])

ctrldf.metrics()
```

</table>
</tr>
</td>

## Limitations
- *This library is currently limited to support only files under 20MB*
- *Due to browser limitations only 12000 rows of data can be viewed at a time*

## To Do
*This library is the base of a much larger project.*
- [ ] Create a chart method which will populate various charts automatically
- [ ] Create a model method which will populate various ML models automatically
- [ ] Add support for automated api data import
- [ ] Add support for relational and non relational data bases
- [ ] Add support for automated queries
- [ ] Add support for big data
- [ ] Create large file size detection and implement chunking automatically
- [ ] Migrate from Pandas to Dask
- [ ] After Dask migration remove file size limitation

Thank you for viewing my project
sincerely
