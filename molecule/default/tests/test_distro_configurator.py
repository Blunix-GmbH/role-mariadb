import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_root_password(host):
    assert host.run("sudo mysql -uroot -pmolecule").rc == 0


def test_configuration_template(host):
    assert host.file("/etc/mysql/mariadb.conf.d/50-server.cnf").contains('bind-address = 0.0.0.0')


def test_service_running(host):
    distro = host.system_info.distribution

    if distro == "debian":
        assert host.service('mysqld').is_running
    elif distro == "ubuntu":
        assert host.service('mysql').is_running
