Role MariaDB
============

This role installs and configures MariaDB from upstream repositories.

Example play
------------

```yaml
- hosts: all
  become: yes
  vars:
    mariadb_enabled: yes
    mariadb_root_password: s3cr3t
  roles:
    - blunix.role-mariadb
```

Testing
-------

This role uses [Molecule](https://molecule.readthedocs.io/en/latest/) and
[Vagrant](https://www.vagrantup.com/) for automated testing. Simply use the
included `Makefile` to prepare and run all tests.

```bash
make install
make molecule
# or simply
make all
```

License
-------

Apache2

Author Information
------------------

Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux and open-source technology stacks are available from:

```
Blunix GmbH - Professional Linux Service
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: mailto:service@blunix.org
```
