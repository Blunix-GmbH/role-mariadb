import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('masters')


def test_master_listening(host):
    assert host.socket("tcp://0.0.0.0:3306").is_listening


def test_master_id(host):
    assert host.file('/etc/mysql/mariadb.conf.d/50-server.cnf').contains("server_id = 10")
