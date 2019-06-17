'''
:Author: Madhusudhan Ramachandra
:Contact: madhusur@cisco.com
:Updated: May 18th 2016
'''

import asgard_app.lib.constants as const
from asgard_app.pre_migrate.tenant import Tenant

class Apic():
    def __init__(self, apic_host, tenant_name, target_anp):
        self.type = const.TYPE_APIC
#         super(Apic, self).__init__(apic_host, tenant_name, target_anp)
        self.tenant = Tenant(apic_host, tenant_name, target_anp)

    def retrieve(self):
        return self.tenant.info()

    def retrieve_detailed(self):
        return self.tenant.detailed_info()
