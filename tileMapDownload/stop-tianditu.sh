#!/bin/bash

program_name=tileMapDownload.py

pid=`ps -ef|grep ${program_name} | grep -v grep | awk '{print $2}'`
   if [ -n $pid ];then
   	kill -9 $pid
   	echo "程序已停止。"
   fi

