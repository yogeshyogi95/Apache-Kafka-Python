# Apache Kafka Implementation in Python
Inorder to install Kafka and Zookeeper Run the below docker-compose file
Note: Make sure docker and docker-compose is installed on the host machine

docker-compose -f docker-compose.yml up -d

This pulls the kafka and zookeeper images from docker hub and runs the containers in background.

Then Inorder to install the UI manager for Kafka

clone the git repository https://github.com/yahoo/CMAK

then cd into that repo and run the below command
Note: Make sure Java is installed on your host machine

./sbt clean dist

Then unzip a zip file present under /CMAK/target/universal using the below command

unzip /CMAK/target/universal/cmak-3.0.0.5.zip

cd cmak-3.0.0.5/

open application.conf under cmak-3.0.0.5/conf/

enter the ip where zookeeper is installed in the following line in application.conf

cmak.zkhosts="<zookeeper-host>:2181"

Then to run the cmac kafka manager

bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080

Then inorder to access kafka manager in browser go to this URL

localhost:8080

if any issues arise while creating a cluster in kafka manager

Refer the below link

https://github.com/yahoo/CMAK/issues/731#issuecomment-643880544









