#!/bin/sh

if [ "$(id -u)" != 0 ]; then
    echo "$(basename "$0"): only root can do that" >&2
    exit 1
fi

apt-get install i2c-tools python-smbus

cat <<EOF >>/etc/boot.txt
dtparam=i2c_arm=on
dtoverlay=i2c-rtc,ds1307
EOF

cat <<EOF >>/etc/modules

# RTC DS1307
i2c-bcm2708
i2c-dev
rtc-ds1307
EOF

sed 's/^[# \t]*HWCLOCKACCESS=.*$/HWCLOCKACCESS=no/g' -i /etc/default/hwclock

update-rc.d fake-hwclock remove
update-rc.d rtc-hwclock defaults 
