import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apt_repository(host):
    sources = host.file("/etc/apt/sources.list.d/mariadb.list")
    assert sources.exists
    assert sources.user == "root"
    assert sources.group == "root"


def test_package_install(host):
    assert host.package("mariadb-server-10.3").is_installed


def test_socket(host):
    assert host.socket("tcp://0.0.0.0:3306").is_listening
