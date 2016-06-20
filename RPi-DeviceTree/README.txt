/etc/boot.txt settings:

[pi1]
...
# device_tree=
dtparam=i2c_arm=on,spi=on
# for linux 3.18
dtoverlay=spi-bcm2708
# for linux 4.1+
# dtoverlay=spi-bcm2835
dtoverlay=i2c-rtc,ds1307

/etc/modules:
# RTC DS1307
i2c-bcm2708
i2c-dev
rtc-ds1307

# SPI
spi-bcm2708
spidev

