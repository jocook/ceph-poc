from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.comm.CommNtpProvider import CommNtpProvider
from ucsmsdk.mometa.policy.PolicyControlEp import PolicyControlEp
from ucsmsdk.mometa.policy.PolicyConfigBackup import PolicyConfigBackup
from ucsmsdk.mometa.policy.PolicyCommunication import PolicyCommunication
from ucsmsdk.mometa.policy.PolicyDateTime import PolicyDateTime
from ucsmsdk.mometa.policy.PolicyDns import PolicyDns
from ucsmsdk.mometa.policy.PolicyEquipment import PolicyEquipment
from ucsmsdk.mometa.policy.PolicyInfraFirmware import PolicyInfraFirmware
from ucsmsdk.mometa.policy.PolicyFault import PolicyFault
from ucsmsdk.mometa.policy.PolicyMEp import PolicyMEp
from ucsmsdk.mometa.policy.PolicyMonitoring import PolicyMonitoring
from ucsmsdk.mometa.policy.PolicyPortConfig import PolicyPortConfig
from ucsmsdk.mometa.policy.PolicyPowerMgmt import PolicyPowerMgmt
from ucsmsdk.mometa.policy.PolicyPsu import PolicyPsu
from ucsmsdk.mometa.policy.PolicySecurity import PolicySecurity
from ucsmsdk.mometa.compute.ComputeChassisDiscPolicy import ComputeChassisDiscPolicy
from ucsmsdk.mometa.qosclass.QosclassEthBE import QosclassEthBE
from ucsmsdk.mometa.qosclass.QosclassFc import QosclassFc
from ucsmsdk.mometa.fabric.FabricDceSwSrvEp import FabricDceSwSrvEp
from ucsmsdk.mometa.fabric.FabricEthLanEp import FabricEthLanEp
from ucsmsdk.mometa.comm.CommDnsProvider import CommDnsProvider

class UcsmCeph:
    """UcsmCeph Class"""

    def __init__(self):
        pass

    def create_policies(self,s_policies):
        """Policies"""

        policies = {}

        """
        NTP
        """

        ntp_servers = {}

        for key in s_policies['ntp']:
            n_dn = str(s_policies['ntp'][key]['dn'])
            n_name = str(s_policies['ntp'][key]['name'])
            n_descr = str(s_policies['ntp'][key]['descr'])

            mo = CommNtpProvider(parent_mo_or_dn=n_dn,
                                 name=n_name, descr=n_descr)


            ntp_servers.update({key: {'mo':mo}})

        policies.update({'ntp': ntp_servers})

        print "> NTP.............................................[OK]"

        """
        DNS
        """

        dns_servers = {}

        for key in s_policies['dns']:
            d_dn = str(s_policies['dns'][key]['dn'])
            d_name = str(s_policies['dns'][key]['name'])
            d_descr = str(s_policies['dns'][key]['descr'])

            mo = CommDnsProvider(parent_mo_or_dn=d_dn,
                                 name=d_name, descr=d_descr)


            dns_servers.update({key: {'mo':mo}})

        policies.update({'dns': dns_servers})

        print "> DNS.............................................[OK]"

        """
        General
        """

        general = {}

        g_dn = str(s_policies['general']['global']['dn'])
        g_backplane = str(s_policies['general']['global']['backplane'])
        g_discovery = str(s_policies['general']['global']['discovery'])

        mo = ComputeChassisDiscPolicy(parent_mo_or_dn=g_dn, name="", descr="", multicast_hw_hash="disabled",
                                        backplane_speed_pref=g_backplane, action=g_discovery,
                                        rebalance="user-acknowledged", link_aggregation_pref="none")


        general.update({'global': {'mo':mo}})

        print "> Global Policies.................................[OK]"

        policies.update({'general': general})

        return policies

    def enable_fi_ports(selfs,s_fi_ports):
        """Fabric Interconnect Ports"""

        fi_ports = {}

        """
        Server        
        """

        server_ports = {}

        for key in s_fi_ports['server']:
            f_dn = str(s_fi_ports['server'][key]['dn'])
            f_slot_id = str(s_fi_ports['server'][key]['slot_id'])

            for port in s_fi_ports['server'][key]['port_id']:
                f_port = str(port)
                f_key_port = "%s-%s" % (key, f_port)
                mo = FabricDceSwSrvEp(parent_mo_or_dn=f_dn, name="", auto_negotiate="yes", usr_lbl="",
                                  slot_id=f_slot_id, admin_state="enabled", port_id="1")

                server_ports.update({f_key_port: {'mo': mo}})

        fi_ports.update({'server': server_ports})

        print "> Server Ports....................................[OK]"


        """
        Uplinks
        """

        uplink_ports = {}

        for key in s_fi_ports['uplinks']:
            f_dn = str(s_fi_ports['uplinks'][key]['dn'])
            f_slot_id = str(s_fi_ports['uplinks'][key]['slot_id'])

            for port in s_fi_ports['uplinks'][key]['port_id']:
                f_port = str(port)
                f_key_port = "%s-%s" % (key, f_port)
                mo = FabricEthLanEp(parent_mo_or_dn=f_dn, eth_link_profile_name="default", name="",
                                    flow_ctrl_policy="default", admin_speed="10gbps", auto_negotiate="yes", usr_lbl="",
                                    slot_id=f_slot_id, admin_state="enabled", port_id=f_port)

                uplink_ports.update({f_key_port: {'mo': mo}})

        fi_ports.update({'uplinks': uplink_ports})

        print "> Uplink Ports....................................[OK]"

        return fi_ports

    def register_to_ucsc(self,s_register):
        """Register"""



        r_ucsc_address = str(s_register['ucsc_address'])
        r_shared_secret = str(s_register['shared_secret'])

        mo = PolicyControlEp(parent_mo_or_dn="sys", svc_reg_name=r_ucsc_address, svc_reg_ip="0.0.0.0",
                             cleanup_mode="localize-global", secret=r_shared_secret, suspend_state="off", type="policy",
                             ack_state="no-ack")
        mo_1 = PolicyConfigBackup(parent_mo_or_dn=mo, source="local")
        mo_2 = PolicyCommunication(parent_mo_or_dn=mo, source="local")
        mo_3 = PolicyDateTime(parent_mo_or_dn=mo, source="local")
        mo_4 = PolicyDns(parent_mo_or_dn=mo, source="local")
        mo_5 = PolicyEquipment(parent_mo_or_dn=mo, source="local")
        mo_6 = PolicyInfraFirmware(parent_mo_or_dn=mo, source="local")
        mo_7 = PolicyFault(parent_mo_or_dn=mo, source="local")
        mo_8 = PolicyMEp(parent_mo_or_dn=mo, source="local")
        mo_9 = PolicyMonitoring(parent_mo_or_dn=mo, source="local")
        mo_10 = PolicyPortConfig(parent_mo_or_dn=mo, source="local")
        mo_11 = PolicyPowerMgmt(parent_mo_or_dn=mo, source="local")
        mo_12 = PolicyPsu(parent_mo_or_dn=mo, source="local")
        mo_13 = PolicySecurity(parent_mo_or_dn=mo, source="local")

        return mo

    def deploy(self,settings):
        """Deploy"""

        ucsm_ip = settings['ucsm']['credentials']['ip']
        ucsm_user = settings['ucsm']['credentials']['user']
        ucsm_pw = settings['ucsm']['credentials']['pw']
        handle = UcsHandle(ucsm_ip, ucsm_user, ucsm_pw)
        print ucsm_ip
        print ucsm_user
        print ucsm_pw

        handle.login()

        print "\n>>>>>>>>>>>>> UCSM Login <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"

        print "############# Creating Policies #######################"

        s_policies = settings['ucsm']['policies']
        policies = self.create_policies(s_policies)

        """
        Timezone
        """
        mo = handle.query_dn("sys/svc-ext/datetime-svc")
        mo.timezone = str(settings['ucsm']['policies']['timezone'])
        mo.policy_owner = "local"
        mo.admin_state = "enabled"
        mo.port = "0"
        mo.descr = ""

        handle.set_mo(mo)
        handle.commit()

        """
        Policies
        """

        for key in policies:
            #print 'Type: ' + key
            for sub_key in policies[key]:
                #print key + ': ' + sub_key
                handle.add_mo(policies[key][sub_key]['mo'], True)  # Overwrite
                handle.commit()

        """
        Qos System Class
        """

        mo = handle.query_dn("fabric/lan/classes")
        mo.policy_owner = "local"
        mo.descr = ""
        mo_1 = QosclassEthBE(parent_mo_or_dn=mo, multicast_optimize="no", name="", weight="10", mtu="9216")
        mo_2 = QosclassFc(parent_mo_or_dn=mo, cos="3", name="", weight="none")
        handle.set_mo(mo)
        handle.commit()

        print "> QoS System Class................................[OK]"



        print "############# Enabling FI Ports #######################"

        s_fi_ports = settings['ucsm']['fi_ports']
        fi_ports = self.enable_fi_ports(s_fi_ports)

        for key in fi_ports:
            #print 'Type: ' + key
            for sub_key in fi_ports[key]:
                #print key + ': ' + sub_key
                handle.add_mo(fi_ports[key][sub_key]['mo'], True)  # Overwrite
                handle.commit()

        print "############# Labeling Equipment ######################"

        labels = settings['ucsm']['labels']

        for key in labels['chassis']:
            #print key
            l_dn = labels['chassis'][key]['dn']
            l_label = labels['chassis'][key]['label']
            mo = handle.query_dn(l_dn)
            mo.usr_lbl = l_label
            mo.admin_state = "acknowledged"
            handle.set_mo(mo)
            handle.commit()


        print "> Chassis.........................................[OK]"

        for key in labels['servers']:
            print key
            l_dn = labels['servers'][key]['dn']
            l_label = labels['servers'][key]['label']
            l_lc = labels['servers'][key]['lc']
            mo = handle.query_dn(l_dn)
            #mo.lc = l_lc
            mo.descr = ""
            mo.usr_lbl = l_label
            mo.admin_power = "policy"
            mo.policy_owner = "local"
            mo.name = ""
            handle.set_mo(mo)
            handle.commit()

        print "> Servers.........................................[OK]"

        print "############# Register to UCSC ########################"

        s_register = settings['ucsm']['register']
        mo = self.register_to_ucsc(s_register)

        handle.add_mo(mo, True)
        handle.commit()

        print "> Register........................................[OK]"
        print "\n>>>>>>>>>>>>> UCSM Logout <<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"

        handle.logout()


