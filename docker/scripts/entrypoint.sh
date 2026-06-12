#!/usr/bin/env bash
set -euo pipefail

if [ -z "${JAVA_HOME:-}" ]; then
  JAVA_BIN=$(command -v java || true)
  if [ -n "$JAVA_BIN" ]; then
    JAVA_HOME=$(dirname "$(dirname "$(readlink -f "$JAVA_BIN")")")
  else
    JAVA_HOME=/usr/lib/jvm/jre
  fi
fi
export JAVA_HOME
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

for _ in $(seq 1 30); do
  if compgen -G "$HADOOP_LOG_DIR/*.log" > /dev/null; then
    break
  fi
  sleep 1
done

if compgen -G "$HADOOP_LOG_DIR/*.log" > /dev/null; then
  tail -F "$HADOOP_LOG_DIR"/*.log
else
  tail -f /dev/null
fi
