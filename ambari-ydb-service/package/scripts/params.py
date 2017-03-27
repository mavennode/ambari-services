#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from resource_management.libraries.functions.version import compare_versions
from resource_management import *
import commands

# server configurations
config = Script.get_config()

ydb_home = '/opt/ydbsoftware/ya100'
conf_dir = "/opt/ydbsoftware/ya100/conf"
ydb_user = 'root'
ydb_group = 'root'
log_dir = '/opt/ydbsoftware/ya100/logs'
pid_dir = '/opt/ydbsoftware/ya100/pid'
pid_file = '/opt/ydbsoftware/ya100/pid/spark-root-org.apache.spark.sql.hive.thriftserver.HiveThriftServer2-1.pid'
ydb_env_content = config['configurations']['1-ydb-env']['content']
spark_defaults_content = config['configurations']['3-spark-defaults']['content']
driver_log_content = config['configurations']['6-driver-log']['content']
worker_log_content = config['configurations']['5-worker-log']['content']

hostname = config['hostname']

# a,listen_address1=commands.getstatusoutput('hostname -i')
# listen_address=listen_address1.split()[0]
a,listen_address=commands.getstatusoutput("hostname -i | awk '{print $NF}'")

ydb_site_content = config['configurations']['2-ydb-site']['content']


a1_executor_count = config['configurations']['0-ydb-public']['a1_executor_count']
a2_executor_mem = config['configurations']['0-ydb-public']['a2_executor_mem']
a3_executor_cores = config['configurations']['0-ydb-public']['a3_executor_cores']
a4_driver_memory = config['configurations']['0-ydb-public']['a4_driver_memory']
a5_zookeeper_list = config['configurations']['0-ydb-public']['a5_zookeeper_list']
a6_zookeeper_port = config['configurations']['0-ydb-public']['a6_zookeeper_port']
a7_driver_port = config['configurations']['0-ydb-public']['a7_driver_port']
a8_ydbui_port = config['configurations']['0-ydb-public']['a8_ydbui_port']
a9_sparkui_port = config['configurations']['0-ydb-public']['a9_sparkui_port']

d1_reader_list = config['configurations']['0-ydb-public']['d1_reader_list']
d2_kafka_topic = config['configurations']['0-ydb-public']['d2_kafka_topic']
d3_kafka_group = config['configurations']['0-ydb-public']['d3_kafka_group']
d4_kafka_server = config['configurations']['0-ydb-public']['d4_kafka_server']
d5_kafka_reader = config['configurations']['0-ydb-public']['d5_kafka_reader']
d6_kafka_parser = config['configurations']['0-ydb-public']['d6_kafka_parser']

b1_spark_home = config['configurations']['0-ydb-public']['b1_spark_home']
b2_java_home = config['configurations']['0-ydb-public']['b2_java_home']
b3_hdfs_user = config['configurations']['0-ydb-public']['b3_hdfs_user']
b4_hadoop_conf = config['configurations']['0-ydb-public']['b4_hadoop_conf']
b5_hadoop_home = config['configurations']['0-ydb-public']['b5_hadoop_home']
c1_hive_warehouse = config['configurations']['0-ydb-public']['c1_hive_warehouse']
c2_ydb_path = config['configurations']['0-ydb-public']['c2_ydb_path']
c3_metastore = config['configurations']['0-ydb-public']['c3_metastore']



