# FilebeatToCloud

An easy way to add a Filebeat configuration to your system


## Used Filebeat version

This app currently runs with the 8.3.1 version of Filebeat --> https://www.elastic.co/downloads/past-releases/filebeat-8-3-1


## Ideas

Make a upper level menu to choose to add a new Filebeat configuration or to use an existing/ancient one

Being able to export / import a gonfiguration --> generated/parserscript.js + generated/headersConfigs/config_..js + filebeat.yml

Being able to have multiple Filebeat instances/services + create a management panel



## Menu preview :

![image](https://user-images.githubusercontent.com/74706889/183057279-5c144461-7b74-4121-9946-fce537736f4c.png)

:warning: For now, you can only use the 1st Menu option, as the other ones are ready for deployment yet


## New Filebeat configuration :

### General display

![image](https://user-images.githubusercontent.com/74706889/183057765-19967f47-5dd9-49e4-9e04-45bb50819240.png)

:information_source: This page makes you prepare the filebeat.yml file. There are some base field values that you can modify at your ease.

(more info here : https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-reference-yml.html)

### General usage

![image](https://user-images.githubusercontent.com/74706889/183058818-2db9e42e-cc8b-4926-90c6-56d7ceac6415.png)

:information_source: There is a local '.env' file in the 'FilebeatToCloud\py-scripts\' folder in which you can adress your personal information.

  For now, you need to create it youself and write the following properties :
  
  ````
  HOSTS=<kiban url>
  USRNAME=<username(usually 'elastic')>
  PASSWORD=<password>
  ````
  
  With it, you won't have to rewrite the same infos everytime.
  
:information_source: You can add multiple logs input folders paths.

:information_source: If the index doesn't exist in you Cloud instance, it will be automatically created.

:information_source: You can edit the file extension and the attribute separator accrding tou your logs format.

:information_source: Copy/Paste a sample of your logs to identify it's headers and/or how many attributes you need to distinguish in your logs.

Then, press the validation button.

![image](https://user-images.githubusercontent.com/74706889/183060158-232e2a14-1ddc-4c70-8067-4bc8a99703a9.png)

:information_source: Now you can see and modify the attribute names that have been generated by your sample (will be empty if no sample provided)

#### Let's set test our Filebeat instance with the following log column format
```
header1;header2;header3
value1.1;value2.1;value3.1
```

Now let's that our logs doesn't respect that exact format and that some columns content could be missing, like the following :

```
header1;header2;header3
value1.1;value2.1;value3.1
value3.2
value1.3;value2.3;value3.3
value1.4;value3.4
value3.5
value3.6
value3.7
value1.8;value3.8
value1.9;value3.9
value1.10;value2.10;value3.10

```

We can see 3 différent logs formats here : not every field is filled


```value1.3;value2.3;value3.3``` --> OK

```value1.4;value3.4``` --> 1 field missing (2nd column)

```value3.5``` --> 2 fields missing (2nd and 3rd columns)


So let's set up 3 logs fields configuration :

![image](https://user-images.githubusercontent.com/74706889/183070162-6c6d685f-2ced-4f8b-8a43-c05fc5db1020.png)

- Set up the first configuration :

![image](https://user-images.githubusercontent.com/74706889/183070446-53f4c547-fbca-4266-9c70-d0c5f64a8dba.png)

- Set up the second configuration :

![image](https://user-images.githubusercontent.com/74706889/183070612-d9c592ca-4b93-4abd-8cd2-3a07772ac55c.png)

- Set up the third configuration :

![image](https://user-images.githubusercontent.com/74706889/183070686-8fa57da1-e707-49d2-b46e-de756a5efd56.png)

And then, set up is done !

Go into the 'FilebeatToCloud\filebeat-8.3.1-windows-x86_64\' folder and start your Filebeat instance in a powershell terminal with the ```.\filebeat.exe -e``` command :

```...\FilebeatToCloud\filebeat-8.3.1-windows-x86_64> .\filebeat.exe -e```
 
Before sending any log, let's check our Elastic Cloud indexes (```host:port/app/management/data/index_management/indices```) :

![image](https://user-images.githubusercontent.com/74706889/183071659-59de8a6c-65b7-4c86-852a-1c90307aa960.png)

We can see that our index hasn't been created yet.

Now let's send the log we used as a sample in our 2 input folders :

![image](https://user-images.githubusercontent.com/74706889/183072213-2393e79f-ba24-4c20-a890-983b5d8da46d.png)

In folder 1 (as a '.txt' file) :

```
value1.1;value2.1;value3.1
value3.2
value1.3;value2.3;value3.3
value1.4;value3.4
value3.5

```

In folder 2 (as a '.txt' file) :
```
value3.6
value3.7
value1.8;value3.8
value1.9;value3.9
value1.10;value2.10;value3.10

```

Now check if our index has been crated :

![image](https://user-images.githubusercontent.com/74706889/183072849-f0ef727c-8a6d-4e87-9c9e-f47889ee1a5e.png)

Yes !

Let's now create a Data View to explore our log's data (```host:port/app/management/kibana/dataViews```) :

![image](https://user-images.githubusercontent.com/74706889/183073258-b3027fac-907f-4fc8-9da3-c898be7ae735.png)

Now, we can visualize our data in the Kibana Discover section :

![image](https://user-images.githubusercontent.com/74706889/183074649-992fe4bb-ae07-485c-80bf-9ec6b24f90a7.png)

We received our 10 rows splitted in the 2 '.txt' files in the 2 precedently setp up folders !

Let's now observe our data fields to check if our formats were properly set up :

We can now select our headers in the field search input :

![image](https://user-images.githubusercontent.com/74706889/183074731-016f56ce-6c6f-45e4-be0e-b8c7bde5a6db.png)

:information_source: All the received data are prefixed by 'parsed.'

Now let's properly display our data :

![image](https://user-images.githubusercontent.com/74706889/183075372-e485c1a7-4fc7-4d60-8d7d-457862fff5f1.png)

Wonderful ! Our data fields are perfectly classified !

You can now use the FilebeatToCloud application to send your logs with your very own formats on your cloud !


### Disclaimer

I don't to modify any file / folder content or name or the app could stop working


##### Regards,

##### LEROY DUCARDONNOY Paul
