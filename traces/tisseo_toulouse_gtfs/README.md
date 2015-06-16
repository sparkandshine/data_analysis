Import **Tisseo Toulouse** into MySQL
-------------------------------------

#Description 
Author: SparkandShine
Homepage: [sparkandshine.net](http://sparkandshine.net/).
Date: June 16th, 2015


#The trace
This trace is from [Tisseo Toulouse Open Data](https://data.toulouse-metropole.fr/explore/dataset/tisseo-gtfs/?tab=table).


#The code
This SQL code is based on [py-gtfs-mysql](https://github.com/sbma44/py-gtfs-mysql). I change a little bit.

#How to import
```bash
cd tisseo_toulouse_gtfs 
./import_gtfs_mysql.sh  
```
By the way, my platform is AWS EC2 Ubuntu.

#Troubleshooting
##The used command is not allowed with this MySQL version
The reason is that the operation `LOAD DATA LOCAL INFILE` is disable in default, as shown in the mysql offical website:

> LOCAL works only if your server and your client both have been configured to permit it. For example, if mysqld was started with --local-infile=0, LOCAL does not work. See Section 6.1.6, “Security Issues with LOAD DATA LOCAL”.

The solution is add `local-infile=1` to `/etc/mysql/my.cnf` (under `[mysql]`):

```
[mysql]
local-infile=1
```
