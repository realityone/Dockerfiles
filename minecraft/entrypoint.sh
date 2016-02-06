#!/bin/bash

MCPATH="/spigotmc"

if [[ ! -f "$MCPATH/spigot-1.8.8.jar" && ! -f "$MCPATH/craftbukkit-1.8.8.jar" ]]; then
    echo "You have to volume spigot-1.8.8.jar and craftbukkit-1.8.8.jar to $MCPATH."
    exit
fi

cat << EOF > $MCPATH/eula.txt
eula=$EULA
EOF

java -Xmx1024M -Xms1024M -jar -XX:MaxPermSize=128M $MCPATH/spigot-1.8.8.jar
