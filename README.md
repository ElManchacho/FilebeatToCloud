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


### Disclaimer

I don't to modify any file / folder content or name or the app could stop working
