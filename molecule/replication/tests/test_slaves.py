import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('slaves')

SHOW_SLAVE_STATUS = "sudo mysql -Bse 'show slave status\G'"


def test_master_id(host):
    assert host.file('/etc/mysql/mariadb.conf.d/50-server.cnf').contains("server_id = 20")


def test_slave_io(host):
    for line in str(host.run(SHOW_SLAVE_STATUS).stdout).split('\n'):
        if line.strip() == 'Slave_IO_Running: Yes':
            return True
    raise AssertionError("Slave IO not running!")


def test_slave_sql(host):
    for line in str(host.run(SHOW_SLAVE_STATUS).stdout).split('\n'):
        if line.strip() == 'Slave_SQL_Running: Yes':
            return True
    raise AssertionError("Slave SQL not running!")


def test_seconds_behind_master(host):
    for line in str(host.run(SHOW_SLAVE_STATUS).stdout).split('\n'):
        if line.strip() == 'Seconds_Behind_Master: NULL':
            raise AssertionError("Slave not catching up to master!")
