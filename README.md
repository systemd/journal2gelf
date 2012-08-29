journal2gelf
============

Get structured log records from the systemd journal and send them to a
Graylog2 server as GELF messages.

Tested on Python 2.7, may work on other versions.

Dependencies:
-------------

- graypy (pip-install graypy)

Usage:
------

- Send all logs in the journal to graylog then exit:
  `systemd-journalctl -o json | journal2gelf.py`

- Continuously tail the journal and send logs to graylog:
  `systemd-journalctl -o json -f | journal2gelf.py`

License
-------
Copyright 2012 Joe Miller <https://github.com/joemiller>

Released under the MIT license, see LICENSE for details.
