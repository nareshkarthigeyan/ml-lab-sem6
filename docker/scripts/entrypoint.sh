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
export HADOOP_LOG_APPEARANCE_TIMEOUT_SECONDS=${HADOOP_LOG_APPEARANCE_TIMEOUT_SECONDS:-30}
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

daemons_ready=false
for _ in $(seq 1 10); do
  if pgrep -f "NameNode|DataNode|ResourceManager|NodeManager|JobHistoryServer" > /dev/null; then
    daemons_ready=true
    break
  fi
  sleep 1
done

if [ "$daemons_ready" != true ]; then
  echo "ERROR: Hadoop daemons failed to start after 10 seconds" >&2
  exit 1
fi

logs_appeared=false
for _ in $(seq 1 "$HADOOP_LOG_APPEARANCE_TIMEOUT_SECONDS"); do
  if compgen -G "$HADOOP_LOG_DIR/*.log" > /dev/null; then
    logs_appeared=true
    break
  fi
  sleep 1
done

log_files=()
if [ "$logs_appeared" = true ]; then
  shopt -s nullglob
  log_files=("$HADOOP_LOG_DIR"/*.log)
  shopt -u nullglob
fi

if [ "${#log_files[@]}" -gt 0 ]; then
  tail -F "${log_files[@]}"
else
  tail -f /dev/null
fi
