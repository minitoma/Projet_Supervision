#!/bin/bash

LSYNCFILE="/etc/lsyncd/lsyncd.conf.lua"
TARGET=`cat /etc/lsyncd/lsyncd.conf.lua | grep host | tail -1 | awk '{print $1}'| cut -d = -f 2 | cut -d \" -f 2`
FILECHECK="/data/workspace/lsync.txt"
EXIT=0
MESSAGE="Synchro opérationnelle"
#echo ${TARGET}
timestamp=`date +%s`
if [ -f ${FILECHECK} ]
then
        rm ${FILECHECK}
fi

#echo $timestamp
echo $timestamp > ${FILECHECK}
sleep 5

filesyncrho=`sudo /usr/bin/ssh -i /root/.ssh/id_rsa root@${TARGET} cat ${FILECHECK}`
#echo $filesyncrho

if [ -z $filesyncrho ]
then
        echo "Recuperation timestamp synchro impossible"
        exit 2
fi

if [ $timestamp -ne $filesyncrho ]
then
        MESSAGE="CRITICAL synchronisation erreur decalage $diff"
        EXIT=2
fi

echo ${MESSAGE}
exit ${EXIT}
