#!/bin/bash

nohup python tileMapDownload.py > out-tianditu.log 2>&1 &
if [ $? -eq 0 ]
 then
   echo "启动成功！"
 else
   echo "启动失败，请查看日志:"${log_path}
fi

