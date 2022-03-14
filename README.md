# python-gpio-fan

´´´bash
mv pwm.py /opt/
chown root:root /opt/pwm.py
systemctl --force --full edit python-fan-pwm.service
systemctl daemon-reload
systemctl enable python-fan-pwm.service
systemctl start python-fan-pwm.service
´´´

## Sources

- https://stackoverflow.com/questions/2440511/getting-cpu-temperature-using-python
- https://www.raspberrypi.com/documentation/computers/os.html#gpio-and-the-40-pin-header
- https://ubuntu.com/tutorials/gpio-on-raspberry-pi#5-pwm-example
- https://wiki.52pi.com/index.php/5V_Adjustable_speed_fan_for_RPi_SKU:_F-0011#SETTING_THE_PWM_SETTINGS
- https://blog.merzlabs.com/posts/python-autostart-systemd/
- https://unix.stackexchange.com/questions/68059/daemontools-multilog-loses-log-line-time-information-how-to-fix-it