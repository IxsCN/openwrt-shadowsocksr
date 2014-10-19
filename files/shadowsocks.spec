#!/bin/sh /etc/rc.common

START=95

SERVICE_USE_PID=1
SERVICE_WRITE_PID=1
SERVICE_DAEMONIZE=1

CONFIG=/etc/shadowsocks/config.json
IGNORE=/etc/shadowsocks/ignore.list

start() {
	/usr/bin/ss-rules -c $CONFIG -i $IGNORE && \
	service_start /usr/bin/ss-redir -c $CONFIG
	service_start /usr/bin/ss-tunnel -c $CONFIG -t 5 -l 5353 -L 8.8.4.4:53 -u
}

stop() {
	/usr/bin/ss-rules -c $CONFIG -f && \
	service_stop /usr/bin/ss-redir
	service_stop /usr/bin/ss-tunnel
}

reload() {
	/usr/bin/ss-rules -c $CONFIG -i $IGNORE
}