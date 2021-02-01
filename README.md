### Word counting using Map Reduce Hadoop framework in Python

This practical example is for creating map reduce implementation in AWS EMR cluster

### Commands

#### Step 1

Log to the AWS EMR cluster name node terminal.

#### Step 2

create folder to download sample files.

`mkdir books-input`

#### Step 3

`cd books-input` and run `download.py` to get the test files.

#### Step 4

create a folder in hadoop file system to copy testing files.

`hdfs dfs -mkdir books-input`

#### Step 5

copy files to hdfs

`hdfs dfs -put books-input/*.txt books-input`

#### Step 6

check whether required `jar` is available.

`find /usr/lib/ -name *hadoop*streaming*.jar`

#### Step 7

start the job attaching mapper and reducer files.

`hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input books-input -output books-output
`

#### Step 8

check `/books-output` folder to results.

#### Step 9

delete testing files if needed.

`find . -name '*.txt' -delete`