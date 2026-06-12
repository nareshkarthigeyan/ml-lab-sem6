#!/usr/bin/env bash
set -euo pipefail

export JAVA_HOME=${JAVA_HOME:-/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.212.b04-0.el7_6.x86_64}
export HADOOP_HOME=${HADOOP_HOME:-/opt/hadoop}
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-$HADOOP_HOME/etc/hadoop}
export HADOOP_LOG_DIR=${HADOOP_LOG_DIR:-$HADOOP_HOME/logs}
export HDFS_NAMENODE_USER=hadoop
export HDFS_DATANODE_USER=hadoop
export HDFS_SECONDARYNAMENODE_USER=hadoop
export YARN_RESOURCEMANAGER_USER=hadoop
export YARN_NODEMANAGER_USER=hadoop

mkdir -p /opt/hadoop/data/namenode /opt/hadoop/data/datanode "$HADOOP_LOG_DIR"
chown -R hadoop:users /opt/hadoop/data "$HADOOP_LOG_DIR"

if [ ! -d /opt/hadoop/data/namenode/current ]; then
  su hadoop -c "$HADOOP_HOME/bin/hdfs namenode -format -force -nonInteractive"
fi

su hadoop -c "$HADOOP_HOME/bin/hdfs --daemon start namenode"
su hadoop -c "$HADOOP_HOME/bin/hdfs --daemon start datanode"
su hadoop -c "$HADOOP_HOME/bin/yarn --daemon start resourcemanager"
su hadoop -c "$HADOOP_HOME/bin/yarn --daemon start nodemanager"
su hadoop -c "$HADOOP_HOME/bin/mapred --daemon start historyserver"

tail -F "$HADOOP_HOME"/logs/*.log
