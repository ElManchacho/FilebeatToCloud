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


```value1.3;value2.3;value3.3 ```--> OK

```value1.4;value3.4          ```--> 1 field missing (2nd column)

```value3.5                   ```--> 2 fields missing (2nd and 3rd columns)


So let's set up 3 logs fields configuration.


![image](https://user-images.githubusercontent.com/74706889/183070162-6c6d685f-2ced-4f8b-8a43-c05fc5db1020.png)

 
### Disclaimer

I don't to modify any file / folder content or name or the app could stop working
