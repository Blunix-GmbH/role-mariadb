import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_root_password(host):
    assert host.run("sudo mysql -uroot -pmolecule").rc == 0


def test_configuration_template(host):
    assert host.file("/etc/mysql/conf.d/99-custom.cnf").contains('bind-address = 0.0.0.0')


def test_service_running(host):
    assert host.service('mysqld').is_running
