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

### offline processing: 
1- Download the data 
2- Save the data while downloading 
3- convert the data to a pandas dataframe
4- map the provider name and identifier 
5- save the final dataframe

### 