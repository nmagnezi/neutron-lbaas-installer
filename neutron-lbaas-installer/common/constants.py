# DB Migrations
DB_MIGRATION_STARTING_NEWTON = 'neutron-db-manage --subproject neutron-lbaas --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head'
DB_MIGRATION_UP_TO_NEWTON = 'neutron-db-manage --service lbaas --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head'


# Packages
OPENSTACK_PACKAGES = 'openstack-neutron-lbaas'
ADDITIONAL_PACKAGES = 'haproxy'
PIP_PACKAGES = 'neutron-lbaas'

# Files
NEUTRON_DIR = '/etc/neutron'

NEUTRON_CONF = 'neutron.conf'
NEUTRON_LBAAS_CONF = 'neutron_lbaas.conf'
LBAAS_AGENT_INI = 'lbaas_agent.ini'
SERVICES_LBAAS = 'services_lbaas.conf'


# Supported Interface Drivers
INTERFACE_DRIVER = 'neutron.agent.linux.interface.OVSInterfaceDriver'


# Supported Service Providers
HAPROXY_SERVICE_PROVIDER = 'LOADBALANCERV2:Haproxy:neutron_lbaas.drivers.haproxy.plugin_driver.HaproxyOnHostPluginDriver:default'
HAPROXY_USER_GROUP = 'haproxy'


# Systemctl Service Names
NEUTRON_SERVER = 'neutron-server.service'
LBAAS2_AGENT = 'neutron-lbaasv2-agent.service'
