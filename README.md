journal2gelf
============

Get structured log records from the systemd journal and send them to a
Graylog2 server as GELF messages.

Tested on Python 2.7 and Fedora 17 (systemd-44-17).

Dependencies:
-------------

- graypy (pip-install graypy)

Install
-------

On Fedora 17+ (or other systems with a version of systemd that includes journal
support):

```
sudo yum install git python-pip
pip-python install git+http://github.com/systemd/journal2gelf.git#egg=journal2gelf
```

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
