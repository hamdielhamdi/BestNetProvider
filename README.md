
# BestNetProvider
BestNetProvider is a small API that calculate network coverage based on the address.


----

### Assumption: 
* Web dev framework  : flask 
* Data processing and manipulation  : pandas + numpy 
* The initial data process is an offline process (local)

### Installation and requirements
1 - The first of all clone the project.
```
git clone https://github.com/hamdielhamdi/BestNetProvider.git
```
2 - Access the project.
```
cd BestNetProvider
```
3 - Before starting, a set of requirement shloud be installed.
```
pip install -r requirements.txt
```
---
### Offline processing: 
The offline process use pandas and numpy to read, write, manipulate and process the data as a pandas dataframe.Steps : 
* 1- Download the data 
* 2- Save the data while downloading 
* 3- convert the data to a pandas dataframe
* 4- map the provider name and identifier 
* 5- save the final dataframe
To run the offline process, use the following steps : 
```python
# access the local process folder under the utils folder
cd utils/local_process
# offline process can be started in two ways : 
#  1- downloads and process data, using the keyword update 
python offline_process.py  update
# 2 - use the existing file from the local folder 
python offline_process.py
```
Note, the offline process must be lunched atleast one time, before running the web server.

---
### Data processing and web server
To illustrate the logic behind the webserver, those are the mean steps : 
* 1- the server get a requests with a query like adress
* 2- the workflow process, will requests the **[https://adresse.data.gouv.fr/api](https://adresse.data.gouv.fr/api)** to get the geo location as a tupe (x,y).
* 3- the workflow will calculate the nearest 3 point with 3 diffrente provider as following : 
![https://github.com/hamdielhamdi/BestNetProvider/blob/979febeeafdefe8992175b436f6464663e597398/IMAGE.png](ok)

The distance is calculated base on the **[https://en.wikipedia.org/wiki/Euclidean_distance](https://en.wikipedia.org/wiki/Euclidean_distance)** 

### usage 
To run the server in debug mode : 
```python 
python run.py  
```

access the server thu **[http://localhost/bestprovider/?q=2 rue paul..](http://localhost/bestprovider/?q=2 rue paul..)**.

---
