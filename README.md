# Role MariaDB

This role installs and configures MariaDB from upstream repositories.

# Example play

```yaml
- hosts: all
  become: yes
  vars:
    mariadb_enabled: yes
    mariadb_root_password: secretpassword
  roles:
    - blunix.role-mariadb
```

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```