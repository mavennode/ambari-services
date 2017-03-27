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

from resource_management import *
import signal
import sys
import os
from os.path import isfile


class Ydb_Master(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print 'Install'
        Execute('wget -P /opt/ydbsoftware http://archive.redoop.com/crh4/redhat/6/x86_64/crh/package/redoop-ydb/1.1.3/ya100-1.1.3.0930.18.380.95.stable.tar.gz',user=params.ydb_user)
        Execute('tar -xzvf /opt/ydbsoftware/ya100-1.1.3.0930.18.380.95.stable.tar.gz -C /opt/ydbsoftware ' + ' > /var/log/ydb ' + ' 2>&1')
        Execute('rm -rf /opt/ydbsoftware/ya100-1.1.3.0930.18.380.95.stable.tar.gz')
        self.install_packages(env)

    def configure(self, env):
        import params
        env.set_params(params)
        print 'Install plugins'

        configurations = params.config['configurations']['ydb-site']

        ydb_site_content=InlineTemplate(params.ydb_site_content)
        File(format("{params.ydb_home}/conf/ydb_site.yaml"), content=ydb_site_content, owner=params.ydb_user, group=params.ydb_group)

        ydb_env_content=InlineTemplate(params.ydb_env_content)
        File(format("{params.ydb_home}/conf/ya100_env.sh"), content=ydb_env_content, owner=params.ydb_user, group=params.ydb_group)

        spark_defaults_content=InlineTemplate(params.spark_defaults_content)
        File(format("{params.ydb_home}/conf/spark-defaults.conf"), content=spark_defaults_content, owner=params.ydb_user, group=params.ydb_group)

        driver_log_content=InlineTemplate(params.driver_log_content)
        File(format("{params.ydb_home}/conf/driver.log.properties"), content=driver_log_content, owner=params.ydb_user, group=params.ydb_group)

        worker_log_content=InlineTemplate(params.worker_log_content)
        File(format("{params.ydb_home}/conf/worker.log.properties"), content=worker_log_content, owner=params.ydb_user, group=params.ydb_group)

        XmlConfig('hive-site.xml',conf_dir=params.conf_dir,configurations=params.config['configurations']['4-hive-site'],owner=params.ydb_user,group=params.ydb_group) 

    def stop(self, env):
        import params
        env.set_params(params)
        Execute('sh /opt/ydbsoftware/ya100/bin/stop-all.sh')
        cmd_pid = 'rm -f /var/run/ya100.pid'
        Execute(cmd_pid)
        cmd_pid = 'rm -f /opt/ydbsoftware/ya100/pid/*.pid'
        Execute(cmd_pid)
        print 'Stop the YDB'

    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        Execute('sh /opt/ydbsoftware/ya100/bin/restart-all.sh > /var/log/ydb-restart.log')
        cmd_pid = format("cat /opt/ydbsoftware/ya100/pid/*.pid > /var/run/ya100.pid")
        Execute(cmd_pid)
        print 'Start the YDB'

    def status(self, env):
        import params
        env.set_params(params)
        pid_file = format("/var/run/ya100.pid")
        check_process_status(pid_file)
        print 'Status of the YDB'
    
if __name__ == "__main__":
    Ydb_Master().execute()
