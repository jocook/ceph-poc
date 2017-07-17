from ucscsdk.ucschandle import UcscHandle
from ucscsdk.mometa.macpool.MacpoolPool import MacpoolPool
from ucscsdk.mometa.macpool.MacpoolBlock import MacpoolBlock
from ucscsdk.mometa.ippool.IppoolPool import IppoolPool
from ucscsdk.mometa.ippool.IppoolBlock import IppoolBlock
from ucscsdk.mometa.uuidpool.UuidpoolPool import UuidpoolPool
from ucscsdk.mometa.uuidpool.UuidpoolBlock import UuidpoolBlock
from ucscsdk.mometa.fabric.FabricVlan import FabricVlan
from ucscsdk.mometa.compute.ComputePool import ComputePool
from ucscsdk.mometa.compute.ComputePooledRackUnit import ComputePooledRackUnit
from ucscsdk.mometa.compute.ComputePooledSlot import ComputePooledSlot
from ucscsdk.mometa.nwctrl.NwctrlDefinition import NwctrlDefinition
from ucscsdk.mometa.dpsec.DpsecMac import DpsecMac
from ucscsdk.mometa.epqos.EpqosDefinition import EpqosDefinition
from ucscsdk.mometa.epqos.EpqosEgress import EpqosEgress
from ucscsdk.mometa.vnic.VnicLanConnTempl import VnicLanConnTempl
from ucscsdk.mometa.vnic.VnicEtherIf import VnicEtherIf
from ucscsdk.mometa.adaptor.AdaptorHostEthIfProfile import AdaptorHostEthIfProfile
from ucscsdk.mometa.adaptor.AdaptorEthAdvFilterProfile import AdaptorEthAdvFilterProfile
from ucscsdk.mometa.adaptor.AdaptorEthArfsProfile import AdaptorEthArfsProfile
from ucscsdk.mometa.adaptor.AdaptorEthCompQueueProfile import AdaptorEthCompQueueProfile
from ucscsdk.mometa.adaptor.AdaptorEthFailoverProfile import AdaptorEthFailoverProfile
from ucscsdk.mometa.adaptor.AdaptorEthInterruptProfile import AdaptorEthInterruptProfile
from ucscsdk.mometa.adaptor.AdaptorEthInterruptScalingProfile import AdaptorEthInterruptScalingProfile
from ucscsdk.mometa.adaptor.AdaptorEthNVGREProfile import AdaptorEthNVGREProfile
from ucscsdk.mometa.adaptor.AdaptorEthOffloadProfile import AdaptorEthOffloadProfile
from ucscsdk.mometa.adaptor.AdaptorEthRecvQueueProfile import AdaptorEthRecvQueueProfile
from ucscsdk.mometa.adaptor.AdaptorEthRoCEProfile import AdaptorEthRoCEProfile
from ucscsdk.mometa.adaptor.AdaptorEthVxLANProfile import AdaptorEthVxLANProfile
from ucscsdk.mometa.adaptor.AdaptorEthWorkQueueProfile import AdaptorEthWorkQueueProfile
from ucscsdk.mometa.adaptor.AdaptorExtIpV6RssHashProfile import AdaptorExtIpV6RssHashProfile
from ucscsdk.mometa.adaptor.AdaptorIpV4RssHashProfile import AdaptorIpV4RssHashProfile
from ucscsdk.mometa.adaptor.AdaptorIpV6RssHashProfile import AdaptorIpV6RssHashProfile
from ucscsdk.mometa.adaptor.AdaptorRssProfile import AdaptorRssProfile
from ucscsdk.mometa.bios.BiosVProfile import BiosVProfile
from ucscsdk.mometa.bios.BiosVfAltitude import BiosVfAltitude
from ucscsdk.mometa.bios.BiosVfCPUHardwarePowerManagement import BiosVfCPUHardwarePowerManagement
from ucscsdk.mometa.bios.BiosVfCPUPerformance import BiosVfCPUPerformance
from ucscsdk.mometa.bios.BiosVfConsistentDeviceNameControl import BiosVfConsistentDeviceNameControl
from ucscsdk.mometa.bios.BiosVfCoreMultiProcessing import BiosVfCoreMultiProcessing
from ucscsdk.mometa.bios.BiosVfDDR3VoltageSelection import BiosVfDDR3VoltageSelection
from ucscsdk.mometa.bios.BiosVfDRAMClockThrottling import BiosVfDRAMClockThrottling
from ucscsdk.mometa.bios.BiosVfDirectCacheAccess import BiosVfDirectCacheAccess
from ucscsdk.mometa.bios.BiosVfDramRefreshRate import BiosVfDramRefreshRate
# from ucscsdk.mometa.bios.BiosVfEnergyPerformanceTuning import BiosVfEnergyPerformanceTuning
from ucscsdk.mometa.bios.BiosVfEnhancedIntelSpeedStepTech import BiosVfEnhancedIntelSpeedStepTech
from ucscsdk.mometa.bios.BiosVfExecuteDisableBit import BiosVfExecuteDisableBit
from ucscsdk.mometa.bios.BiosVfFrequencyFloorOverride import BiosVfFrequencyFloorOverride
from ucscsdk.mometa.bios.BiosVfFrontPanelLockout import BiosVfFrontPanelLockout
from ucscsdk.mometa.bios.BiosVfIntelHyperThreadingTech import BiosVfIntelHyperThreadingTech
from ucscsdk.mometa.bios.BiosVfIntelTurboBoostTech import BiosVfIntelTurboBoostTech
from ucscsdk.mometa.bios.BiosVfIntelVTForDirectedIO import BiosVfIntelVTForDirectedIO
from ucscsdk.mometa.bios.BiosVfIntelVirtualizationTechnology import BiosVfIntelVirtualizationTechnology
from ucscsdk.mometa.bios.BiosVfInterleaveConfiguration import BiosVfInterleaveConfiguration
from ucscsdk.mometa.bios.BiosVfLocalX2Apic import BiosVfLocalX2Apic
from ucscsdk.mometa.bios.BiosVfLvDIMMSupport import BiosVfLvDIMMSupport
from ucscsdk.mometa.bios.BiosVfMaxVariableMTRRSetting import BiosVfMaxVariableMTRRSetting
from ucscsdk.mometa.bios.BiosVfMirroringMode import BiosVfMirroringMode
from ucscsdk.mometa.bios.BiosVfNUMAOptimized import BiosVfNUMAOptimized
from ucscsdk.mometa.bios.BiosVfPSTATECoordination import BiosVfPSTATECoordination
from ucscsdk.mometa.bios.BiosVfPOSTErrorPause import BiosVfPOSTErrorPause
from ucscsdk.mometa.bios.BiosVfPackageCStateLimit import BiosVfPackageCStateLimit
from ucscsdk.mometa.bios.BiosVfProcessorCState import BiosVfProcessorCState
from ucscsdk.mometa.bios.BiosVfProcessorC1E import BiosVfProcessorC1E
from ucscsdk.mometa.bios.BiosVfProcessorC3Report import BiosVfProcessorC3Report
from ucscsdk.mometa.bios.BiosVfProcessorC6Report import BiosVfProcessorC6Report
from ucscsdk.mometa.bios.BiosVfProcessorC7Report import BiosVfProcessorC7Report
# from ucscsdk.mometa.bios.BiosVfProcessorCMCI import BiosVfProcessorCMCI
from ucscsdk.mometa.bios.BiosVfProcessorEnergyConfiguration import BiosVfProcessorEnergyConfiguration
from ucscsdk.mometa.bios.BiosVfProcessorPrefetchConfig import BiosVfProcessorPrefetchConfig
from ucscsdk.mometa.bios.BiosVfQuietBoot import BiosVfQuietBoot
from ucscsdk.mometa.bios.BiosVfResumeOnACPowerLoss import BiosVfResumeOnACPowerLoss
from ucscsdk.mometa.bios.BiosVfScrubPolicies import BiosVfScrubPolicies
from ucscsdk.mometa.bios.BiosVfSelectMemoryRASConfiguration import BiosVfSelectMemoryRASConfiguration
# from ucscsdk.mometa.bios.BiosVfWorkloadConfiguration import BiosVfWorkloadConfiguration
from ucscsdk.mometa.lsboot.LsbootPolicy import LsbootPolicy
from ucscsdk.mometa.lsboot.LsbootVirtualMedia import LsbootVirtualMedia
from ucscsdk.mometa.lsboot.LsbootStorage import LsbootStorage
from ucscsdk.mometa.lsboot.LsbootLocalStorage import LsbootLocalStorage
from ucscsdk.mometa.lsboot.LsbootLocalHddImage import LsbootLocalHddImage
from ucscsdk.mometa.lsmaint.LsmaintMaintPolicy import LsmaintMaintPolicy
from ucscsdk.mometa.power.PowerPolicy import PowerPolicy
from ucscsdk.mometa.compute.ComputeScrubPolicy import ComputeScrubPolicy
from ucscsdk.mometa.firmware.FirmwareChassisPack import FirmwareChassisPack
from ucscsdk.mometa.firmware.FirmwareExcludeChassisComponent import FirmwareExcludeChassisComponent
from ucscsdk.mometa.cpmaint.CpmaintMaintPolicy import CpmaintMaintPolicy
from ucscsdk.mometa.lstorage.LstorageDiskZoningPolicy import LstorageDiskZoningPolicy
from ucscsdk.mometa.lstorage.LstorageDiskSlot import LstorageDiskSlot
from ucscsdk.mometa.lstorage.LstorageControllerRef import LstorageControllerRef
from ucscsdk.mometa.equipment.EquipmentChassisProfile import EquipmentChassisProfile
from ucscsdk.mometa.lstorage.LstorageDiskGroupConfigPolicy import LstorageDiskGroupConfigPolicy
from ucscsdk.mometa.lstorage.LstorageLocalDiskConfigRef import LstorageLocalDiskConfigRef
from ucscsdk.mometa.lstorage.LstorageVirtualDriveDef import LstorageVirtualDriveDef
from ucscsdk.mometa.lstorage.LstorageProfile import LstorageProfile
from ucscsdk.mometa.lstorage.LstorageDasScsiLun import LstorageDasScsiLun
from ucscsdk.mometa.ls.LsServer import LsServer
from ucscsdk.mometa.ls.LsVConAssign import LsVConAssign
from ucscsdk.mometa.vnic.VnicDefBeh import VnicDefBeh
from ucscsdk.mometa.vnic.VnicEther import VnicEther
from ucscsdk.mometa.vnic.VnicFcNode import VnicFcNode
from ucscsdk.mometa.ls.LsRequirement import LsRequirement
from ucscsdk.mometa.ls.LsPower import LsPower
from ucscsdk.mometa.lstorage.LstorageProfileBinding import LstorageProfileBinding
from ucscsdk.mometa.fabric.FabricVCon import FabricVCon
from ucscsdk.mometa.ls.LsServer import LsServer
from ucscsdk.mometa.equipment.EquipmentChassisProfile import EquipmentChassisProfile
from ucscsdk.mometa.equipment.EquipmentBinding import EquipmentBinding
from ucscsdk.mometa.fabric.FabricVlanReq import FabricVlanReq
from ucscsdk.utils.ucscdomain import get_domain
from ucscsdk.utils.ucscdomain import domain_assign_to_domaingroup
from ucscsdk.mometa.fcpool.FcpoolInitiators import FcpoolInitiators
from ucscsdk.mometa.fcpool.FcpoolBlock import FcpoolBlock
import re

class UcscCeph:
    """UcscCeph Class"""

    def __init__(self):
        pass

    def check_settings(self, settings):
        pass

    def get_system_id(self,handle,ucsm_ip):
        """
        Get system_id
        """


        object = get_domain(handle, domain_ip=ucsm_ip, domain_name="") #ucsm_ip should be IP and not hostname

        re.findall(r'\W*id[^:]*:\D*(\d+)', str(object))

        system_id = ''.join(re.findall(r'\W*id[^:]*:\D*(\d+)', str(object)))

        return system_id



    def create_pools(self, s_pools, system_id):
        """ Pools """

        pools = {}

        pools_dn = str(s_pools['dn'])


        """
        KVM IP Pool
        """

        kvm_ip_pools = {}

        for key in s_pools['kvm_ip']:
            k_dn = str(s_pools['kvm_ip'][key]['dn'])
            k_name = str(s_pools['kvm_ip'][key]['name'])
            k_descr = str(s_pools['kvm_ip'][key]['descr'])
            k_from = str(s_pools['kvm_ip'][key]['from'])
            k_to = str(s_pools['kvm_ip'][key]['to'])
            k_def_gw = str(s_pools['kvm_ip'][key]['def_gw'])

            mo = IppoolPool(parent_mo_or_dn=k_dn,
                            name=k_name,
                            descr=k_descr)
            mo_1 = IppoolBlock(parent_mo_or_dn=mo,
                             to=k_to,
                             r_from=k_from,
                             def_gw=k_def_gw)


            kvm_ip_pools.update({key: {'mo':mo,'mo_1':mo_1}})

        pools.update({'kvm_ip': kvm_ip_pools})

        print "> KVM IP..........................................[OK]"

        """
        MAC Pools
        """

        mac_pools = {}

        for key in s_pools['mac']:
            m_name = str(s_pools['mac'][key]['name'])
            m_dn = str(s_pools['mac'][key]['dn'])
            m_descr = str(s_pools['mac'][key]['descr'])
            m_from = str(s_pools['mac'][key]['from'])
            m_to = str(s_pools['mac'][key]['to'])

            mo = MacpoolPool(parent_mo_or_dn=m_dn,
                             descr=m_descr,
                             name=m_name)
            mo_1 = MacpoolBlock(parent_mo_or_dn=mo,
                                to=m_to,
                                r_from=m_from)

            mac_pools.update({key: {'mo': mo, 'mo_1': mo_1}})

        pools.update({'mac': mac_pools})

        print "> MAC.............................................[OK]"

        """
        UUID Pools
        """

        uuid_pools = {}

        for key in s_pools['uuid']:
            u_name = str(s_pools['uuid'][key]['name'])
            u_dn = str(s_pools['uuid'][key]['dn'])
            u_descr = str(s_pools['uuid'][key]['descr'])
            u_from = str(s_pools['uuid'][key]['from'])
            u_to = str(s_pools['uuid'][key]['to'])
            u_prefix = str(s_pools['uuid'][key]['prefix'])
            mo = UuidpoolPool(parent_mo_or_dn=u_dn,
                              prefix=u_prefix,
                              descr=u_descr,
                              name=u_name
                              )
            mo_1 = UuidpoolBlock(parent_mo_or_dn=mo,
                                 to=u_to,
                                 r_from=u_from)

            uuid_pools.update({key: {'mo': mo, 'mo_1': mo_1}})

        pools.update({'uuid': uuid_pools})

        print "> UUID............................................[OK]"

        """
        Server Pools
        """


        
        server_pools = {}

        for key in s_pools['server']:
            s_name = str(s_pools['server'][key]['name'])
            s_dn = str(s_pools['server'][key]['dn'])
            s_descr = str(s_pools['server'][key]['descr'])
            s_type = str(s_pools['server'][key]['type'])
            s_count = int(s_pools['server'][key]['count'])

            mo = ComputePool(parent_mo_or_dn=s_dn, name=s_name,
                         descr=s_descr)

            server_pools.update({key: {'mo':mo}})

            if s_type == "S3260":
                s_slot = str(s_pools['server'][key]['slot'])
                for count in range(1,s_count+1):
                    server_pools[key]['mo_' + str(count)] = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id,
                                                                               slot_id=s_slot, chassis_id=str(count))
            elif s_type == "C220":
                for count in range(1,s_count+1):
                    server_pools[key]['mo_' + str(count)] = ComputePooledRackUnit(parent_mo_or_dn=mo, system_id=system_id, id=str(count))


        pools.update({'server': server_pools})
        print "> Servers.........................................[OK]"



        """


        server_pools = {}

        s_name = str(s_pools['server']['S3260-Node1']['name'])
        s_dn = str(s_pools['server']['S3260-Node1']['dn'])
        s_descr = str(s_pools['server']['S3260-Node1']['descr'])




        mo = ComputePool(parent_mo_or_dn=s_dn, name=s_name,
                         descr=s_descr)
        mo_1 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="1", chassis_id="1")
        mo_2 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="1", chassis_id="2")
        mo_3 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="1", chassis_id="3")
        mo_4 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="1", chassis_id="4")
        mo_5 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="1", chassis_id="5")

        server_pools.update({'S3260-Node1': {'mo':mo,
                                             'mo_1':mo_1,
                                             'mo_2':mo_2,
                                             'mo_3':mo_3,
                                             'mo_4':mo_4,
                                             'mo_5':mo_5
                                             }})

        s_name = str(s_pools['server']['S3260-Node2']['name'])
        s_dn = str(s_pools['server']['S3260-Node2']['dn'])
        s_descr = str(s_pools['server']['S3260-Node2']['descr'])

        mo = ComputePool(parent_mo_or_dn=s_dn, name=s_name,
                         descr=s_descr)
        mo_1 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="2", chassis_id="1")
        mo_2 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="2", chassis_id="2")
        mo_3 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="2", chassis_id="3")
        mo_4 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="2", chassis_id="4")
        mo_5 = ComputePooledSlot(parent_mo_or_dn=mo, system_id=system_id, slot_id="2", chassis_id="5")

        server_pools.update({'S3260-Node2': {'mo':mo,
                                             'mo_1':mo_1,
                                             'mo_2':mo_2,
                                             'mo_3':mo_3,
                                             'mo_4':mo_4,
                                             'mo_5':mo_5
                                             }})

        s_name = str(s_pools['server']['C220-M4S']['name'])
        s_dn = str(s_pools['server']['C220-M4S']['dn'])
        s_descr = str(s_pools['server']['C220-M4S']['descr'])

        mo = ComputePool(parent_mo_or_dn=s_dn, name=s_name,
                         descr=s_descr)
        mo_1 = ComputePooledRackUnit(parent_mo_or_dn=mo, system_id=system_id, id="1")
        mo_2 = ComputePooledRackUnit(parent_mo_or_dn=mo, system_id=system_id, id="2")
        mo_3 = ComputePooledRackUnit(parent_mo_or_dn=mo, system_id=system_id, id="3")
        mo_4 = ComputePooledRackUnit(parent_mo_or_dn=mo, system_id=system_id, id="4")

        server_pools.update({'C220-M4S': {'mo':mo,
                                          'mo_1':mo_1,
                                          'mo_2':mo_2,
                                          'mo_3':mo_3,
                                          "mo_4":mo_4
                                          }})

        pools.update({'server': server_pools})

        print "> Servers.........................................[OK]"

        """

        """
        VLANs
        """

        vlans = {}

        for key in s_pools['vlan']:
            v_name = str(s_pools['vlan'][key]['name'])
            v_dn = str(s_pools['vlan'][key]['dn'])
            v_id = str(s_pools['vlan'][key]['id'])
            mo = FabricVlan(parent_mo_or_dn=v_dn,
                            sharing="none",
                            name=v_name,
                            id=v_id,
                            mcast_policy_name="",
                            policy_owner="local",
                            default_net="no",
                            pub_nw_name="",
                            compression_type="included")

            vlans.update({key: {'mo': mo}})

            mo = FabricVlanReq(parent_mo_or_dn=pools_dn,
                               name=v_name)

            vlans.update({key + "_permit": {'mo': mo}})

        pools.update({'vlan': vlans})

        print "> VLANs...........................................[OK]"

        return pools


    def create_policies(self, s_policies):
        """ Policies """

        policies = {}

        """
        Network Control
        """

        network_control_policies = {}

        for key in s_policies['network_control']:
            n_dn = str(s_policies['network_control'][key]['dn'])
            n_name = str(s_policies['network_control'][key]['name'])
            n_descr = str(s_policies['network_control'][key]['descr'])
            mo = NwctrlDefinition(parent_mo_or_dn=n_dn, lldp_transmit="disabled", name=n_name,
                                  lldp_receive="disabled", mac_register_mode="all-host-vlans",
                                  cdp="enabled", uplink_fail_action="link-down",
                                  descr=n_descr)
            mo_1 = DpsecMac(parent_mo_or_dn=mo, forge="allow", name="", descr="")
            network_control_policies.update({key: {'mo': mo, 'mo_1': mo_1}})

        policies.update({'network_control': network_control_policies})

        print "> Network Control.................................[OK]"

        """
        Qos
        """

        qos_policies = {}

        for key in s_policies['qos']:
            q_dn = str(s_policies['qos'][key]['dn'])
            q_name = str(s_policies['qos'][key]['name'])
            mo = EpqosDefinition(parent_mo_or_dn=q_dn, name=q_name, descr="")
            mo_1 = EpqosEgress(parent_mo_or_dn=mo, rate="line-rate", host_control="none", name="", prio="best-effort",
                               burst="10240")
            qos_policies.update({key: {'mo': mo, 'mo_1': mo_1}})

        policies.update({'qos': qos_policies})

        print "> QoS.............................................[OK]"

        """
        vNIC Template
        """

        vnic_templates = {}

        for key in s_policies['vnic_template']:
            v_dn = str(s_policies['vnic_template'][key]['dn'])
            v_name = str(s_policies['vnic_template'][key]['name'])
            v_descr = str(s_policies['vnic_template'][key]['descr'])
            v_switch_id = str(s_policies['vnic_template'][key]['switch_id'])
            v_mtu = str(s_policies['vnic_template'][key]['mtu'])
            v_qos = str(s_policies['vnic_template'][key]['qos'])
            v_mac = str(s_policies['vnic_template'][key]['mac'])
            v_net = str(s_policies['vnic_template'][key]['net'])
            v_vlan = str(s_policies['vnic_template'][key]['vlan'])
            v_native = str(s_policies['vnic_template'][key]['native'])
            mo = VnicLanConnTempl(parent_mo_or_dn=v_dn, redundancy_pair_type="none", name=v_name,
                                  descr=v_descr, stats_policy_name="", admin_cdn_name="",
                                  switch_id=v_switch_id, pin_to_group_name="", mtu=v_mtu,
                                  peer_redundancy_templ_name="", templ_type="initial-template",
                                  qos_policy_name=v_qos, ident_pool_name=v_mac, cdn_source="vnic-name",
                                  nw_ctrl_policy_name=v_net)
            mo_1 = VnicEtherIf(parent_mo_or_dn=mo, default_net=v_native, name=v_vlan)
            vnic_templates.update({key: {'mo': mo, 'mo_1': mo_1}})

        policies.update({'vnic_template': vnic_templates})

        print "> vNIC Templates..................................[OK]"


        """
        Adapter
        """

        adapter_policies = {}

        for key in s_policies['adapter']:
            a_dn = str(s_policies['adapter'][key]['dn'])
            a_name = str(s_policies['adapter'][key]['name'])
            a_descr = str(s_policies['adapter'][key]['descr'])
            mo = AdaptorHostEthIfProfile(parent_mo_or_dn=a_dn, name=a_name,
                                         descr=a_descr)
            mo_1 = AdaptorEthAdvFilterProfile(parent_mo_or_dn=mo, admin_state="disabled")
            mo_2 = AdaptorEthArfsProfile(parent_mo_or_dn=mo, accelarated_rfs="disabled")
            mo_3 = AdaptorEthCompQueueProfile(parent_mo_or_dn=mo, count="16")
            mo_4 = AdaptorEthFailoverProfile(parent_mo_or_dn=mo, timeout="5")
            mo_5 = AdaptorEthInterruptProfile(parent_mo_or_dn=mo, count="32", coalescing_type="min", mode="msi-x",
                                              coalescing_time="125")
            mo_6 = AdaptorEthInterruptScalingProfile(parent_mo_or_dn=mo, admin_state="disabled")
            mo_7 = AdaptorEthNVGREProfile(parent_mo_or_dn=mo, admin_state="disabled")
            mo_8 = AdaptorEthOffloadProfile(parent_mo_or_dn=mo, tcp_segment="enabled", large_receive="enabled",
                                            tcp_rx_checksum="enabled", tcp_tx_checksum="enabled")
            mo_9 = AdaptorEthRecvQueueProfile(parent_mo_or_dn=mo, count="8", ring_size="4096")
            mo_10 = AdaptorEthRoCEProfile(parent_mo_or_dn=mo, resource_groups="32", queue_pairs="256",
                                          memory_regions="131072", admin_state="disabled")
            mo_11 = AdaptorEthVxLANProfile(parent_mo_or_dn=mo, admin_state="disabled")
            mo_12 = AdaptorEthWorkQueueProfile(parent_mo_or_dn=mo, count="8", ring_size="4096")
            mo_13 = AdaptorExtIpV6RssHashProfile(parent_mo_or_dn=mo, )
            mo_14 = AdaptorIpV4RssHashProfile(parent_mo_or_dn=mo, )
            mo_15 = AdaptorIpV6RssHashProfile(parent_mo_or_dn=mo, )
            mo_16 = AdaptorRssProfile(parent_mo_or_dn=mo, receive_side_scaling="enabled")
            adapter_policies.update({key: {'mo': mo,
                                           'mo_1': mo_1,
                                           'mo_2': mo_2,
                                           'mo_3': mo_3,
                                           'mo_4': mo_4,
                                           'mo_5': mo_5,
                                           'mo_6': mo_6,
                                           'mo_7': mo_7,
                                           'mo_8': mo_8,
                                           'mo_9': mo_9,
                                           'mo_10': mo_10,
                                           'mo_11': mo_11,
                                           'mo_12': mo_12,
                                           'mo_13': mo_13,
                                           'mo_14': mo_14,
                                           'mo_15': mo_15,
                                           'mo_16': mo_16
                                           }})

        policies.update({'adapter': adapter_policies})

        print "> Adapter.........................................[OK]"



        """
        BIOS
            *missing options
        """

        bios_policies = {}

        for key in s_policies['bios']:
            b_dn = str(s_policies['bios'][key]['dn'])
            b_name = str(s_policies['bios'][key]['name'])
            b_descr = str(s_policies['bios'][key]['descr'])
            mo = BiosVProfile(parent_mo_or_dn=b_dn, name=b_name,
                              descr=b_descr, reboot_on_update="no")
            mo_1 = BiosVfAltitude(parent_mo_or_dn=mo, vp_altitude="auto")
            mo_2 = BiosVfCPUHardwarePowerManagement(parent_mo_or_dn=mo,
                                                    vp_cpu_hardware_power_management="platform-default")
            mo_3 = BiosVfCPUPerformance(parent_mo_or_dn=mo, vp_cpu_performance="enterprise")
            mo_4 = BiosVfConsistentDeviceNameControl(parent_mo_or_dn=mo, vp_cdn_control="platform-default")
            mo_5 = BiosVfCoreMultiProcessing(parent_mo_or_dn=mo, vp_core_multi_processing="all")
            mo_6 = BiosVfDDR3VoltageSelection(parent_mo_or_dn=mo, vp_dd_r3_voltage_selection="platform-default")
            mo_7 = BiosVfDRAMClockThrottling(parent_mo_or_dn=mo, vp_dram_clock_throttling="performance")
            mo_8 = BiosVfDirectCacheAccess(parent_mo_or_dn=mo, vp_direct_cache_access="enabled")
            mo_9 = BiosVfDramRefreshRate(parent_mo_or_dn=mo, vp_dram_refresh_rate="1x")
            # mo_10 = BiosVfEnergyPerformanceTuning(parent_mo_or_dn=mo, vp_pwr_perf_tuning="os")
            mo_11 = BiosVfEnhancedIntelSpeedStepTech(parent_mo_or_dn=mo, vp_enhanced_intel_speed_step_tech="enabled")
            mo_12 = BiosVfExecuteDisableBit(parent_mo_or_dn=mo, vp_execute_disable_bit="platform-default")
            mo_13 = BiosVfFrequencyFloorOverride(parent_mo_or_dn=mo, vp_frequency_floor_override="enabled")
            mo_14 = BiosVfFrontPanelLockout(parent_mo_or_dn=mo, vp_front_panel_lockout="platform-default")
            mo_15 = BiosVfIntelHyperThreadingTech(parent_mo_or_dn=mo, vp_intel_hyper_threading_tech="enabled")
            mo_16 = BiosVfIntelTurboBoostTech(parent_mo_or_dn=mo, vp_intel_turbo_boost_tech="enabled")
            mo_17 = BiosVfIntelVTForDirectedIO(parent_mo_or_dn=mo,
                                               vp_intel_vtd_pass_through_dma_support="platform-default",
                                               vp_intel_vtdats_support="platform-default",
                                               vp_intel_vtd_interrupt_remapping="platform-default",
                                               vp_intel_vtd_coherency_support="platform-default",
                                               vp_intel_vt_for_directed_io="platform-default")
            mo_18 = BiosVfIntelVirtualizationTechnology(parent_mo_or_dn=mo,
                                                        vp_intel_virtualization_technology="disabled")
            mo_19 = BiosVfInterleaveConfiguration(parent_mo_or_dn=mo, vp_channel_interleaving="platform-default",
                                                  vp_rank_interleaving="platform-default",
                                                  vp_memory_interleaving="platform-default")
            mo_20 = BiosVfLocalX2Apic(parent_mo_or_dn=mo, vp_local_x2_apic="platform-default")
            mo_21 = BiosVfLvDIMMSupport(parent_mo_or_dn=mo, vp_lv_ddr_mode="performance-mode")
            mo_22 = BiosVfMaxVariableMTRRSetting(parent_mo_or_dn=mo, vp_processor_mtrr="platform-default")
            mo_23 = BiosVfMirroringMode(parent_mo_or_dn=mo, vp_mirroring_mode="platform-default")
            mo_24 = BiosVfNUMAOptimized(parent_mo_or_dn=mo, vp_numa_optimized="enabled")
            mo_25 = BiosVfPSTATECoordination(parent_mo_or_dn=mo, vp_pstate_coordination="hw-all")
            mo_26 = BiosVfPOSTErrorPause(parent_mo_or_dn=mo, vp_post_error_pause="platform-default")
            mo_27 = BiosVfPackageCStateLimit(parent_mo_or_dn=mo, vp_package_c_state_limit="auto")
            mo_28 = BiosVfProcessorCState(parent_mo_or_dn=mo, vp_processor_c_state="disabled")
            mo_29 = BiosVfProcessorC1E(parent_mo_or_dn=mo, vp_processor_c1_e="disabled")
            mo_30 = BiosVfProcessorC3Report(parent_mo_or_dn=mo, vp_processor_c3_report="disabled")
            mo_31 = BiosVfProcessorC6Report(parent_mo_or_dn=mo, vp_processor_c6_report="disabled")
            mo_32 = BiosVfProcessorC7Report(parent_mo_or_dn=mo, vp_processor_c7_report="disabled")
            # mo_33 = BiosVfProcessorCMCI(parent_mo_or_dn=mo, vp_processor_cmci="platform-default")
            mo_34 = BiosVfProcessorEnergyConfiguration(parent_mo_or_dn=mo, vp_power_technology="performance",
                                                       vp_energy_performance="performance")
            mo_35 = BiosVfProcessorPrefetchConfig(parent_mo_or_dn=mo, vp_dcuip_prefetcher="enabled",
                                                  vp_adjacent_cache_line_prefetcher="enabled",
                                                  vp_hardware_prefetcher="enabled", vp_dcu_streamer_prefetch="enabled")
            mo_36 = BiosVfQuietBoot(parent_mo_or_dn=mo, vp_quiet_boot="platform-default")
            mo_37 = BiosVfResumeOnACPowerLoss(parent_mo_or_dn=mo, vp_resume_on_ac_power_loss="platform-default")
            mo_38 = BiosVfScrubPolicies(parent_mo_or_dn=mo, vp_patrol_scrub="disabled", vp_demand_scrub="disabled")
            mo_39 = BiosVfSelectMemoryRASConfiguration(parent_mo_or_dn=mo,
                                                       vp_select_memory_ras_configuration="maximum-performance")
            # mo_40 = BiosVfWorkloadConfiguration(parent_mo_or_dn=mo, vp_workload_configuration="io-sensitive")
            bios_policies.update({key: {'mo': mo,
                                        'mo_1': mo_1,
                                        'mo_2': mo_2,
                                        'mo_3': mo_3,
                                        'mo_4': mo_4,
                                        'mo_5': mo_5,
                                        'mo_6': mo_6,
                                        'mo_7': mo_7,
                                        'mo_8': mo_8,
                                        'mo_9': mo_9,
                                        # 'mo_10': mo_10,
                                        'mo_11': mo_11,
                                        'mo_12': mo_12,
                                        'mo_13': mo_13,
                                        'mo_14': mo_14,
                                        'mo_15': mo_15,
                                        'mo_16': mo_16,
                                        'mo_17': mo_17,
                                        'mo_18': mo_18,
                                        'mo_19': mo_19,
                                        'mo_20': mo_20,
                                        'mo_21': mo_21,
                                        'mo_22': mo_22,
                                        'mo_23': mo_23,
                                        'mo_24': mo_24,
                                        'mo_25': mo_25,
                                        'mo_26': mo_26,
                                        'mo_27': mo_27,
                                        'mo_28': mo_28,
                                        'mo_29': mo_29,
                                        'mo_30': mo_30,
                                        'mo_31': mo_31,
                                        'mo_32': mo_32,
                                        # 'mo_33': mo_33,
                                        'mo_34': mo_34,
                                        'mo_35': mo_35,
                                        'mo_36': mo_36,
                                        'mo_37': mo_37,
                                        'mo_38': mo_38,
                                        'mo_39': mo_39
                                        # 'mo_40': mo_40
                                        }})

        policies.update({'bios': bios_policies})


        print "> BIOS............................................[OK]"

        """
        Boot
        """

        boot_policies = {}

        for key in s_policies['boot']:
            bo_dn = str(s_policies['boot'][key]['dn'])
            bo_name = str(s_policies['boot'][key]['name'])
            bo_descr = str(s_policies['boot'][key]['descr'])
            mo = LsbootPolicy(parent_mo_or_dn=bo_dn, name=bo_name, descr=bo_descr,
                              reboot_on_update="no", enforce_vnic_name="yes", boot_mode="legacy")
            mo_1 = LsbootVirtualMedia(parent_mo_or_dn=mo, access="read-only-local", lun_id="0", mapping_name="",
                                      order="2")
            mo_2 = LsbootStorage(parent_mo_or_dn=mo, order="1")
            mo_2_1 = LsbootLocalStorage(parent_mo_or_dn=mo_2, )
            mo_2_1_1 = LsbootLocalHddImage(parent_mo_or_dn=mo_2_1, order="1")
            boot_policies.update({key: {'mo': mo,
                                        'mo_1': mo_1,
                                        'mo_2': mo_2,
                                        'mo_2_1': mo_2_1,
                                        'mo_2_1_1': mo_2_1_1
                                        }})

        policies.update({'boot': boot_policies})

        print "> Boot............................................[OK]"

        """
        Maintenance
        """

        maintenance_policies = {}

        for key in s_policies['maintenance']:
            m_dn = str(s_policies['maintenance'][key]['dn'])
            m_name = str(s_policies['maintenance'][key]['name'])
            m_descr = str(s_policies['maintenance'][key]['descr'])
            mo = LsmaintMaintPolicy(parent_mo_or_dn=m_dn, uptime_disr="user-ack", name=m_name,
                                    descr=m_descr, trigger_config="", sched_name="")
            maintenance_policies.update({key: {'mo': mo}})

        policies.update({'maintenance': maintenance_policies})

        print "> Maintenance.....................................[OK]"

        """
        Power Control
        """

        power_control_policies = {}

        for key in s_policies['power_control']:
            p_dn = str(s_policies['power_control'][key]['dn'])
            p_name = str(s_policies['power_control'][key]['name'])
            p_descr = str(s_policies['power_control'][key]['descr'])
            mo = PowerPolicy(parent_mo_or_dn=p_dn, fan_speed="any", name=p_name,
                             prio="no-cap", descr=p_descr)
            power_control_policies.update({key: {'mo': mo}})

        policies.update({'power_control': power_control_policies})

        print "> Power Control...................................[OK]"

        """
        Disk Scrub
        """

        disk_scrub_policies = {}

        for key in s_policies['disk_scrub']:
            d_dn = str(s_policies['disk_scrub'][key]['dn'])
            d_name = str(s_policies['disk_scrub'][key]['name'])
            d_descr = str(s_policies['disk_scrub'][key]['descr'])
            d_scrub = str(s_policies['disk_scrub'][key]['scrub'])
            mo = ComputeScrubPolicy(parent_mo_or_dn=d_dn, flex_flash_scrub="no", name=d_name,
                                    descr=d_descr, bios_settings_scrub="no", disk_scrub=d_scrub)
            disk_scrub_policies.update({key: {'mo': mo}})

        policies.update({'disk_scrub': disk_scrub_policies})


        print "> Disk Scrub......................................[OK]"

        return policies

    def create_chassis_profiles(self, s_chassis_profiles, system_id):
        """ Chassis Profile"""

        chassis_profiles = {}

        """
        Firmware Package
        """

        chassis_firmware_packages = {}

        for key in s_chassis_profiles['firmware_packages']:
            c_name = str(s_chassis_profiles['firmware_packages'][key]['name'])
            c_dn = str(s_chassis_profiles['firmware_packages'][key]['dn'])
            c_descr = str(s_chassis_profiles['firmware_packages'][key]['descr'])
            c_bundle = str(s_chassis_profiles['firmware_packages'][key]['bundle'])

            mo = FirmwareChassisPack(parent_mo_or_dn=c_dn, chassis_bundle_version=c_bundle, name=c_name,
                                     descr=c_descr, stage_size="0", update_trigger="immediate",
                                     force_deploy="no", mode="staged", override_default_exclusion="yes")
            mo_1 = FirmwareExcludeChassisComponent(parent_mo_or_dn=mo, chassis_component="local-disk")

            chassis_firmware_packages.update({key: {'mo': mo, 'mo_1': mo_1}})

        chassis_profiles.update({'firmware_packages': chassis_firmware_packages})

        print "> Firmware Packages...............................[OK]"

        """
        Maintenance
        """

        chassis_maintenance = {}

        for key in s_chassis_profiles['maintenance']:
            m_name = str(s_chassis_profiles['maintenance'][key]['name'])
            m_dn = str(s_chassis_profiles['maintenance'][key]['dn'])
            m_descr = str(s_chassis_profiles['maintenance'][key]['descr'])

            mo = CpmaintMaintPolicy(parent_mo_or_dn=m_dn, uptime_disr="user-ack", name=m_name,
                                    descr=m_descr, trigger_config="", sched_name="")

            chassis_maintenance.update({key: {'mo': mo}})

        chassis_profiles.update({'maintenance': chassis_maintenance})

        print "> Maintenance Policies............................[OK]"

        """
        Disk Zoning

        """

        chassis_disk_zoning = {}

        for key in s_chassis_profiles['disk_zoning']:
            d_name = str(s_chassis_profiles['disk_zoning'][key]['name'])
            d_dn = str(s_chassis_profiles['disk_zoning'][key]['dn'])
            d_descr = str(s_chassis_profiles['disk_zoning'][key]['descr'])

            mo = LstorageDiskZoningPolicy(parent_mo_or_dn=d_dn, preserve_config="no",
                                          name=d_name, descr=d_descr)
            mo_1 = LstorageDiskSlot(parent_mo_or_dn=mo, id="1", ownership="dedicated")
            mo_1_1 = LstorageControllerRef(parent_mo_or_dn=mo_1, controller_type="SAS", server_id="1",
                                           controller_id="1")
            mo_2 = LstorageDiskSlot(parent_mo_or_dn=mo, id="10", ownership="dedicated")
            mo_2_1 = LstorageControllerRef(parent_mo_or_dn=mo_2, controller_type="SAS", server_id="1",
                                           controller_id="1")
            mo_3 = LstorageDiskSlot(parent_mo_or_dn=mo, id="11", ownership="dedicated")
            mo_3_1 = LstorageControllerRef(parent_mo_or_dn=mo_3, controller_type="SAS", server_id="1",
                                           controller_id="1")
            mo_4 = LstorageDiskSlot(parent_mo_or_dn=mo, id="12", ownership="dedicated")
            mo_4_1 = LstorageControllerRef(parent_mo_or_dn=mo_4, controller_type="SAS", server_id="1",
                                           controller_id="1")
            mo_5 = LstorageDiskSlot(parent_mo_or_dn=mo, id="13", ownership="dedicated")
            mo_5_1 = LstorageControllerRef(parent_mo_or_dn=mo_5, controller_type="SAS", server_id="1",
                                           controller_id="1")
            mo_6 = LstorageDiskSlot(parent_mo_or_dn=mo, id="14", ownership="dedicated")
            mo_6_1 = LstorageControllerRef(parent_mo_or_dn=mo_6, controller_type="SAS", server_id="1",
                                           controller_id="1")
            mo_7 = LstorageDiskSlot(parent_mo_or_dn=mo, id="15", ownership="dedicated")
            mo_7_1 = LstorageControllerRef(parent_mo_or_dn=mo_7, controller_type="SAS", server_id="1",
                                           controller_id="1")
            mo_8 = LstorageDiskSlot(parent_mo_or_dn=mo, id="16", ownership="dedicated")
            mo_8_1 = LstorageControllerRef(parent_mo_or_dn=mo_8, controller_type="SAS", server_id="1",
                                           controller_id="1")
            mo_9 = LstorageDiskSlot(parent_mo_or_dn=mo, id="17", ownership="dedicated")
            mo_9_1 = LstorageControllerRef(parent_mo_or_dn=mo_9, controller_type="SAS", server_id="1",
                                           controller_id="1")
            mo_10 = LstorageDiskSlot(parent_mo_or_dn=mo, id="18", ownership="dedicated")
            mo_10_1 = LstorageControllerRef(parent_mo_or_dn=mo_10, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_11 = LstorageDiskSlot(parent_mo_or_dn=mo, id="19", ownership="dedicated")
            mo_11_1 = LstorageControllerRef(parent_mo_or_dn=mo_11, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_12 = LstorageDiskSlot(parent_mo_or_dn=mo, id="2", ownership="dedicated")
            mo_12_1 = LstorageControllerRef(parent_mo_or_dn=mo_12, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_13 = LstorageDiskSlot(parent_mo_or_dn=mo, id="20", ownership="dedicated")
            mo_13_1 = LstorageControllerRef(parent_mo_or_dn=mo_13, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_14 = LstorageDiskSlot(parent_mo_or_dn=mo, id="21", ownership="dedicated")
            mo_14_1 = LstorageControllerRef(parent_mo_or_dn=mo_14, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_15 = LstorageDiskSlot(parent_mo_or_dn=mo, id="22", ownership="dedicated")
            mo_15_1 = LstorageControllerRef(parent_mo_or_dn=mo_15, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_16 = LstorageDiskSlot(parent_mo_or_dn=mo, id="23", ownership="dedicated")
            mo_16_1 = LstorageControllerRef(parent_mo_or_dn=mo_16, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_17 = LstorageDiskSlot(parent_mo_or_dn=mo, id="24", ownership="dedicated")
            mo_17_1 = LstorageControllerRef(parent_mo_or_dn=mo_17, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_18 = LstorageDiskSlot(parent_mo_or_dn=mo, id="25", ownership="dedicated")
            mo_18_1 = LstorageControllerRef(parent_mo_or_dn=mo_18, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_19 = LstorageDiskSlot(parent_mo_or_dn=mo, id="26", ownership="dedicated")
            mo_19_1 = LstorageControllerRef(parent_mo_or_dn=mo_19, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_20 = LstorageDiskSlot(parent_mo_or_dn=mo, id="27", ownership="dedicated")
            mo_20_1 = LstorageControllerRef(parent_mo_or_dn=mo_20, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_21 = LstorageDiskSlot(parent_mo_or_dn=mo, id="28", ownership="dedicated")
            mo_21_1 = LstorageControllerRef(parent_mo_or_dn=mo_21, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_22 = LstorageDiskSlot(parent_mo_or_dn=mo, id="29", ownership="dedicated")
            mo_22_1 = LstorageControllerRef(parent_mo_or_dn=mo_22, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_23 = LstorageDiskSlot(parent_mo_or_dn=mo, id="3", ownership="dedicated")
            mo_23_1 = LstorageControllerRef(parent_mo_or_dn=mo_23, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_24 = LstorageDiskSlot(parent_mo_or_dn=mo, id="30", ownership="dedicated")
            mo_24_1 = LstorageControllerRef(parent_mo_or_dn=mo_24, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_25 = LstorageDiskSlot(parent_mo_or_dn=mo, id="31", ownership="dedicated")
            mo_25_1 = LstorageControllerRef(parent_mo_or_dn=mo_25, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_26 = LstorageDiskSlot(parent_mo_or_dn=mo, id="32", ownership="dedicated")
            mo_26_1 = LstorageControllerRef(parent_mo_or_dn=mo_26, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_27 = LstorageDiskSlot(parent_mo_or_dn=mo, id="33", ownership="dedicated")
            mo_27_1 = LstorageControllerRef(parent_mo_or_dn=mo_27, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_28 = LstorageDiskSlot(parent_mo_or_dn=mo, id="34", ownership="dedicated")
            mo_28_1 = LstorageControllerRef(parent_mo_or_dn=mo_28, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_29 = LstorageDiskSlot(parent_mo_or_dn=mo, id="35", ownership="dedicated")
            mo_29_1 = LstorageControllerRef(parent_mo_or_dn=mo_29, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_30 = LstorageDiskSlot(parent_mo_or_dn=mo, id="36", ownership="dedicated")
            mo_30_1 = LstorageControllerRef(parent_mo_or_dn=mo_30, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_31 = LstorageDiskSlot(parent_mo_or_dn=mo, id="37", ownership="dedicated")
            mo_31_1 = LstorageControllerRef(parent_mo_or_dn=mo_31, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_32 = LstorageDiskSlot(parent_mo_or_dn=mo, id="38", ownership="dedicated")
            mo_32_1 = LstorageControllerRef(parent_mo_or_dn=mo_32, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_33 = LstorageDiskSlot(parent_mo_or_dn=mo, id="39", ownership="dedicated")
            mo_33_1 = LstorageControllerRef(parent_mo_or_dn=mo_33, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_34 = LstorageDiskSlot(parent_mo_or_dn=mo, id="4", ownership="dedicated")
            mo_34_1 = LstorageControllerRef(parent_mo_or_dn=mo_34, controller_type="SAS", server_id="1",
                                            controller_id="1")
            mo_35 = LstorageDiskSlot(parent_mo_or_dn=mo, id="40", ownership="dedicated")
            mo_35_1 = LstorageControllerRef(parent_mo_or_dn=mo_35, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_36 = LstorageDiskSlot(parent_mo_or_dn=mo, id="41", ownership="dedicated")
            mo_36_1 = LstorageControllerRef(parent_mo_or_dn=mo_36, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_37 = LstorageDiskSlot(parent_mo_or_dn=mo, id="42", ownership="dedicated")
            mo_37_1 = LstorageControllerRef(parent_mo_or_dn=mo_37, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_38 = LstorageDiskSlot(parent_mo_or_dn=mo, id="43", ownership="dedicated")
            mo_38_1 = LstorageControllerRef(parent_mo_or_dn=mo_38, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_39 = LstorageDiskSlot(parent_mo_or_dn=mo, id="44", ownership="dedicated")
            mo_39_1 = LstorageControllerRef(parent_mo_or_dn=mo_39, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_40 = LstorageDiskSlot(parent_mo_or_dn=mo, id="45", ownership="dedicated")
            mo_40_1 = LstorageControllerRef(parent_mo_or_dn=mo_40, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_41 = LstorageDiskSlot(parent_mo_or_dn=mo, id="46", ownership="dedicated")
            mo_41_1 = LstorageControllerRef(parent_mo_or_dn=mo_41, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_42 = LstorageDiskSlot(parent_mo_or_dn=mo, id="47", ownership="dedicated")
            mo_42_1 = LstorageControllerRef(parent_mo_or_dn=mo_42, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_43 = LstorageDiskSlot(parent_mo_or_dn=mo, id="48", ownership="dedicated")
            mo_43_1 = LstorageControllerRef(parent_mo_or_dn=mo_43, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_44 = LstorageDiskSlot(parent_mo_or_dn=mo, id="49", ownership="dedicated")
            mo_44_1 = LstorageControllerRef(parent_mo_or_dn=mo_44, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_45 = LstorageDiskSlot(parent_mo_or_dn=mo, id="5", ownership="dedicated")
            mo_45_1 = LstorageControllerRef(parent_mo_or_dn=mo_45, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_46 = LstorageDiskSlot(parent_mo_or_dn=mo, id="50", ownership="dedicated")
            mo_46_1 = LstorageControllerRef(parent_mo_or_dn=mo_46, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_47 = LstorageDiskSlot(parent_mo_or_dn=mo, id="51", ownership="dedicated")
            mo_47_1 = LstorageControllerRef(parent_mo_or_dn=mo_47, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_48 = LstorageDiskSlot(parent_mo_or_dn=mo, id="52", ownership="dedicated")
            mo_48_1 = LstorageControllerRef(parent_mo_or_dn=mo_48, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_49 = LstorageDiskSlot(parent_mo_or_dn=mo, id="53", ownership="dedicated")
            mo_49_1 = LstorageControllerRef(parent_mo_or_dn=mo_49, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_50 = LstorageDiskSlot(parent_mo_or_dn=mo, id="54", ownership="dedicated")
            mo_50_1 = LstorageControllerRef(parent_mo_or_dn=mo_50, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_51 = LstorageDiskSlot(parent_mo_or_dn=mo, id="55", ownership="dedicated")
            mo_51_1 = LstorageControllerRef(parent_mo_or_dn=mo_51, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_52 = LstorageDiskSlot(parent_mo_or_dn=mo, id="56", ownership="dedicated")
            mo_52_1 = LstorageControllerRef(parent_mo_or_dn=mo_52, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_53 = LstorageDiskSlot(parent_mo_or_dn=mo, id="6", ownership="dedicated")
            mo_53_1 = LstorageControllerRef(parent_mo_or_dn=mo_53, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_54 = LstorageDiskSlot(parent_mo_or_dn=mo, id="7", ownership="dedicated")
            mo_54_1 = LstorageControllerRef(parent_mo_or_dn=mo_54, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_55 = LstorageDiskSlot(parent_mo_or_dn=mo, id="8", ownership="dedicated")
            mo_55_1 = LstorageControllerRef(parent_mo_or_dn=mo_55, controller_type="SAS", server_id="2",
                                            controller_id="1")
            mo_56 = LstorageDiskSlot(parent_mo_or_dn=mo, id="9", ownership="dedicated")
            mo_56_1 = LstorageControllerRef(parent_mo_or_dn=mo_56, controller_type="SAS", server_id="1",
                                            controller_id="1")

            chassis_disk_zoning.update({key: {'mo': mo,
                                              'mo_1': mo_1,
                                              'mo_1_1': mo_1_1,
                                              'mo_2': mo_2,
                                              'mo_2_1': mo_2_1,
                                              'mo_3': mo_3,
                                              'mo_3_1': mo_3_1,
                                              'mo_4': mo_4,
                                              'mo_4_1': mo_4_1,
                                              'mo_5': mo_5,
                                              'mo_5_1': mo_5_1,
                                              'mo_6': mo_6,
                                              'mo_6_1': mo_6_1,
                                              'mo_7': mo_7,
                                              'mo_7_1': mo_7_1,
                                              'mo_8': mo_8,
                                              'mo_8_1': mo_8_1,
                                              'mo_9': mo_9,
                                              'mo_9_1': mo_9_1,
                                              'mo_10': mo_10,
                                              'mo_10_1': mo_10_1,
                                              'mo_11': mo_11,
                                              'mo_11_1': mo_11_1,
                                              'mo_12': mo_12,
                                              'mo_12_1': mo_12_1,
                                              'mo_13': mo_13,
                                              'mo_13_1': mo_13_1,
                                              'mo_14': mo_14,
                                              'mo_14_1': mo_14_1,
                                              'mo_15': mo_15,
                                              'mo_15_1': mo_15_1,
                                              'mo_16': mo_16,
                                              'mo_16_1': mo_16_1,
                                              'mo_17': mo_17,
                                              'mo_17_1': mo_17_1,
                                              'mo_18': mo_18,
                                              'mo_18_1': mo_18_1,
                                              'mo_19': mo_19,
                                              'mo_19_1': mo_19_1,
                                              'mo_20': mo_20,
                                              'mo_20_1': mo_20_1,
                                              'mo_21': mo_21,
                                              'mo_21_1': mo_21_1,
                                              'mo_22': mo_22,
                                              'mo_22_1': mo_22_1,
                                              'mo_23': mo_23,
                                              'mo_23_1': mo_23_1,
                                              'mo_24': mo_24,
                                              'mo_24_1': mo_24_1,
                                              'mo_25': mo_25,
                                              'mo_25_1': mo_25_1,
                                              'mo_26': mo_26,
                                              'mo_26_1': mo_26_1,
                                              'mo_27': mo_27,
                                              'mo_27_1': mo_27_1,
                                              'mo_28': mo_28,
                                              'mo_28_1': mo_28_1,
                                              'mo_29': mo_29,
                                              'mo_29_1': mo_29_1,
                                              'mo_30': mo_30,
                                              'mo_30_1': mo_30_1,
                                              'mo_31': mo_31,
                                              'mo_31_1': mo_31_1,
                                              'mo_32': mo_32,
                                              'mo_32_1': mo_32_1,
                                              'mo_33': mo_33,
                                              'mo_33_1': mo_33_1,
                                              'mo_34': mo_34,
                                              'mo_34_1': mo_34_1,
                                              'mo_35': mo_35,
                                              'mo_35_1': mo_35_1,
                                              'mo_36': mo_36,
                                              'mo_36_1': mo_36_1,
                                              'mo_37': mo_37,
                                              'mo_37_1': mo_37_1,
                                              'mo_38': mo_38,
                                              'mo_38_1': mo_38_1,
                                              'mo_39': mo_39,
                                              'mo_39_1': mo_39_1,
                                              'mo_40': mo_40,
                                              'mo_40_1': mo_40_1,
                                              'mo_41': mo_41,
                                              'mo_41_1': mo_41_1,
                                              'mo_42': mo_42,
                                              'mo_42_1': mo_42_1,
                                              'mo_43': mo_43,
                                              'mo_43_1': mo_43_1,
                                              'mo_44': mo_44,
                                              'mo_44_1': mo_44_1,
                                              'mo_45': mo_45,
                                              'mo_45_1': mo_45_1,
                                              'mo_46': mo_46,
                                              'mo_46_1': mo_46_1,
                                              'mo_47': mo_47,
                                              'mo_47_1': mo_47_1,
                                              'mo_48': mo_48,
                                              'mo_48_1': mo_48_1,
                                              'mo_49': mo_49,
                                              'mo_49_1': mo_49_1,
                                              'mo_50': mo_50,
                                              'mo_50_1': mo_50_1,
                                              'mo_51': mo_51,
                                              'mo_51_1': mo_51_1,
                                              'mo_52': mo_52,
                                              'mo_52_1': mo_52_1,
                                              'mo_53': mo_53,
                                              'mo_53_1': mo_53_1,
                                              'mo_54': mo_54,
                                              'mo_54_1': mo_54_1,
                                              'mo_55': mo_55,
                                              'mo_55_1': mo_55_1,
                                              'mo_56': mo_56,
                                              'mo_56_1': mo_56_1
                                              }})

        chassis_profiles.update({'disk_zoning': chassis_disk_zoning})

        print "> Disk Zoning.....................................[OK]"

        """
        Profile Templates
        """

        chassis_profile_template = {}

        for key in s_chassis_profiles['profile_templates']:
            p_name = str(s_chassis_profiles['profile_templates'][key]['name'])
            p_dn = str(s_chassis_profiles['profile_templates'][key]['dn'])
            p_descr = str(s_chassis_profiles['profile_templates'][key]['descr'])
            p_maintenance = str(s_chassis_profiles['profile_templates'][key]['maintenance'])
            p_firmware_package = str(s_chassis_profiles['profile_templates'][key]['firmware_package'])
            p_disk_zoning = str(s_chassis_profiles['profile_templates'][key]['disk_zoning'])

            mo = EquipmentChassisProfile(parent_mo_or_dn=p_dn, src_templ_name="", name=p_name,
                                         descr=p_descr, usr_lbl="", maint_policy_name=p_maintenance,
                                         chassis_fw_policy_name=p_firmware_package, resolve_remote="yes",
                                         type="updating-template", disk_zoning_policy_name=p_disk_zoning)

            chassis_profile_template.update({key: {'mo': mo}})

        chassis_profiles.update({'profiles_templates': chassis_profile_template})

        print "> Profiles Templates..............................[OK]"

        """
        Profile & Association
        """

        profiles = {}


        for key in s_chassis_profiles['profiles']:
            cp_name = str(s_chassis_profiles['profiles'][key]['name'])
            cp_dn = str(s_chassis_profiles['profiles'][key]['dn'])
            cp_template = str(s_chassis_profiles['profiles'][key]['template'])
            cp_suffix = int(s_chassis_profiles['profiles'][key]['suffix'])
            cp_instances = int(s_chassis_profiles['profiles'][key]['instances'])

            for instance in range(cp_suffix, cp_instances + 1):
                cp_name_ins = "%s-%s" % (cp_name,instance)
                cp_chassis_dn = "compute/sys-" + system_id + "/chassis-%s" % (instance)
                print cp_chassis_dn
                mo = EquipmentChassisProfile(parent_mo_or_dn=cp_dn,
                            src_templ_name=cp_template,
                            name=cp_name_ins,
                            type="instance")
                mo_1 = EquipmentBinding(parent_mo_or_dn=mo,
                                        chassis_dn=cp_chassis_dn,
                                        restrict_migration="no")
                profiles.update({cp_name_ins: {'mo':mo,'mo_1':mo_1}})

        chassis_profiles.update({'profiles': profiles})

        print "> Profiles from Templates.........................[OK]"


        return chassis_profiles

    def create_storage_profiles(self, s_storage_profiles):
        """Storage Profiles"""

        storage_profiles = {}

        storage_dn = str(s_storage_profiles['dn'])


        """


mo = LstorageProfile(parent_mo_or_dn="org-root", policy_owner="local", name="test", descr="")
mo_1 = LstorageDasScsiLun(parent_mo_or_dn=mo, local_disk_policy_name="", auto_deploy="auto-deploy", expand_to_avail="no", lun_map_type="non-shared", size="1", fractional_size="0", admin_state="online", deferred_naming="no", order="not-applicable", name="testlun")
handle.add_mo(mo)

handle.commit()
        """

        """
        Storage Profiles for S3260
        """

        s3260 = {}

        mo = LstorageDiskGroupConfigPolicy(parent_mo_or_dn=storage_dn, name="S3260-Boot", descr="S3260-Boot",
                                           raid_level="mirror")
        mo_1 = LstorageLocalDiskConfigRef(parent_mo_or_dn=mo, role="normal", slot_num="201", span_id="unspecified")
        mo_2 = LstorageLocalDiskConfigRef(parent_mo_or_dn=mo, role="normal", slot_num="202", span_id="unspecified")
        mo_3 = LstorageVirtualDriveDef(parent_mo_or_dn=mo, read_policy="platform-default",
                                       drive_cache="platform-default", strip_size="platform-default",
                                       io_policy="platform-default", write_cache_policy="platform-default",
                                       access_policy="platform-default")

        s3260.update({'disk_group_config': {'mo': mo, 'mo_1': mo_1, 'mo_2': mo_2, 'mo_3': mo_3}})

        # top

        s1_name = str(s_storage_profiles['S3260']['S3260-Node1']['name'])
        s1_dn = str(s_storage_profiles['S3260']['S3260-Node1']['dn'])
        s1_descr = str(s_storage_profiles['S3260']['S3260-Node1']['descr'])

        mo = LstorageProfile(parent_mo_or_dn=s1_dn, name=s1_name, descr=s1_descr)
        mo_1 = LstorageDasScsiLun(parent_mo_or_dn=mo, local_disk_policy_name="S3260-Boot", auto_deploy="auto-deploy",
                                  expand_to_avail="yes", lun_map_type="non-shared", size="1",
                                  admin_state="online", deferred_naming="no", order="not-applicable", name="Boot")

        s3260.update({'S3260-Node1': {'mo': mo, 'mo_1': mo_1}})

        # bottom

        s2_name = str(s_storage_profiles['S3260']['S3260-Node2']['name'])
        s2_dn = str(s_storage_profiles['S3260']['S3260-Node2']['dn'])
        s2_descr = str(s_storage_profiles['S3260']['S3260-Node2']['descr'])

        mo = LstorageProfile(parent_mo_or_dn=s2_dn, name=s2_name, descr=s2_descr)
        mo_1 = LstorageDasScsiLun(parent_mo_or_dn=mo, local_disk_policy_name="S3260-Boot", auto_deploy="auto-deploy",
                                  expand_to_avail="yes", lun_map_type="non-shared", size="1",
                                  admin_state="online", deferred_naming="no", order="not-applicable", name="Boot")

        s3260.update({'S3260-Node2': {'mo': mo, 'mo_1': mo_1}})

        storage_profiles.update({'S3260': s3260})

        print "> S3260 Profiles..................................[OK]"


        """
        Storage Profile for Cisco UCS C220 M4S
        """

        c220 = {}

        mo = LstorageDiskGroupConfigPolicy(parent_mo_or_dn=storage_dn, name="Boot-Ceph", descr="Boot-Ceph",
                                           raid_level="mirror")
        mo_1 = LstorageLocalDiskConfigRef(parent_mo_or_dn=mo, role="normal", slot_num="1", span_id="unspecified")
        mo_2 = LstorageLocalDiskConfigRef(parent_mo_or_dn=mo, role="normal", slot_num="2", span_id="unspecified")
        mo_3 = LstorageVirtualDriveDef(parent_mo_or_dn=mo, read_policy="platform-default",
                                       drive_cache="platform-default", strip_size="platform-default",
                                       io_policy="platform-default", write_cache_policy="platform-default",
                                       access_policy="platform-default")

        c220.update({'disk_group_config': {'mo': mo, 'mo_1': mo_1, 'mo_2': mo_2, 'mo_3': mo_3}})

        c_name = str(s_storage_profiles['C220']['C220-Boot']['name'])
        c_dn = str(s_storage_profiles['C220']['C220-Boot']['dn'])
        c_descr = str(s_storage_profiles['C220']['C220-Boot']['descr'])

        mo = LstorageProfile(parent_mo_or_dn=c_dn, name=c_name, descr=c_descr)
        mo_1 = LstorageDasScsiLun(parent_mo_or_dn=mo, local_disk_policy_name="Boot-Ceph", auto_deploy="auto-deploy",
                                  expand_to_avail="yes", lun_map_type="non-shared", size="100",
                                  admin_state="online", deferred_naming="no", order="not-applicable", name="Boot")

        c220.update({'C220-Boot': {'mo': mo, 'mo_1': mo_1}})

        storage_profiles.update({'C220': c220})

        print "> C220 Profile....................................[OK]"

        return storage_profiles

    def create_service_profiles(self, s_service_profiles):
        """Templates & From Template"""

        service_profiles = {}

        service_dn = str(s_service_profiles['dn'])

        """
        Service Profile Templates for S3260
            *ext_ip_pool_name="ceph-ext-mgmt" (fixed, should be var)
        """

        s3260_templates = {}

        for key in s_service_profiles['S3260_templates']:
            t_name = str(s_service_profiles['S3260_templates'][key]['name'])
            t_descr = str(s_service_profiles['S3260_templates'][key]['descr'])
            t_uuid = str(s_service_profiles['S3260_templates'][key]['uuid'])
            t_storage = str(s_service_profiles['S3260_templates'][key]['storage'])
            t_vnic1_name = str(s_service_profiles['S3260_templates'][key]['vnic1_name'])
            t_vnic2_name = str(s_service_profiles['S3260_templates'][key]['vnic2_name'])
            t_vnic3_name = str(s_service_profiles['S3260_templates'][key]['vnic3_name'])
            t_vnic1_template = str(s_service_profiles['S3260_templates'][key]['vnic1_template'])
            t_vnic2_template = str(s_service_profiles['S3260_templates'][key]['vnic2_template'])
            t_vnic3_template = str(s_service_profiles['S3260_templates'][key]['vnic3_template'])
            t_vnic_adapter = str(s_service_profiles['S3260_templates'][key]['vnic_adapter'])
            t_boot = str(s_service_profiles['S3260_templates'][key]['boot'])
            t_maint = str(s_service_profiles['S3260_templates'][key]['maint'])
            t_pool = str(s_service_profiles['S3260_templates'][key]['pool'])
            t_bios = str(s_service_profiles['S3260_templates'][key]['bios'])
            t_power = str(s_service_profiles['S3260_templates'][key]['power'])
            t_scrub = str(s_service_profiles['S3260_templates'][key]['scrub'])


            mo = LsServer(parent_mo_or_dn=service_dn, vmedia_policy_name="", ext_ip_state="pooled",
                          bios_profile_name=t_bios, mgmt_fw_policy_name="", agent_policy_name="",
                          mgmt_access_policy_name="", dynamic_con_policy_name="",
                          sol_policy_name="", uuid="0", descr=t_descr, stats_policy_name="",
                          ext_ip_pool_name="ceph-ext-mgmt", boot_policy_name=t_boot, usr_lbl="",
                          host_fw_policy_name="", vcon_profile_name="", ident_pool_name=t_uuid, src_templ_name="",
                          type="initial-template", local_disk_policy_name="", scrub_policy_name=t_scrub,
                          power_policy_name=t_power, maint_policy_name=t_maint,
                          name=t_name) #resolve_remote = yes, stats_policy_name="default", power_sync_policy_name=""
            mo_1 = LsVConAssign(parent_mo_or_dn=mo, admin_vcon="1", admin_host_port="ANY", order="1",
                                transport="ethernet", vnic_name=t_vnic1_name)
            mo_2 = LsVConAssign(parent_mo_or_dn=mo, admin_vcon="1", admin_host_port="ANY", order="3",
                                transport="ethernet", vnic_name=t_vnic3_name)
            mo_3 = LsVConAssign(parent_mo_or_dn=mo, admin_vcon="1", admin_host_port="ANY", order="2",
                                transport="ethernet", vnic_name=t_vnic2_name)
            mo_4 = VnicDefBeh(parent_mo_or_dn=mo, name="", descr="", action="none", type="vhba",
                              nw_templ_name="")
            mo_5 = VnicEther(parent_mo_or_dn=mo, nw_ctrl_policy_name="", admin_host_port="ANY",
                             admin_vcon="1", stats_policy_name="", admin_cdn_name="", switch_id="A-B",
                             pin_to_group_name="", name=t_vnic1_name, order="1", qos_policy_name="",
                             adaptor_profile_name=t_vnic_adapter, ident_pool_name="", cdn_source="vnic-name",
                             mtu="1500",
                             nw_templ_name=t_vnic1_template, addr="derived")
            mo_6 = VnicEther(parent_mo_or_dn=mo, nw_ctrl_policy_name="", admin_host_port="ANY",
                             admin_vcon="1", stats_policy_name="", admin_cdn_name="", switch_id="B-A",
                             pin_to_group_name="", name=t_vnic3_name, order="3", qos_policy_name="",
                             adaptor_profile_name=t_vnic_adapter, ident_pool_name="", cdn_source="vnic-name",
                             mtu="1500",
                             nw_templ_name=t_vnic3_template, addr="derived")
            mo_7 = VnicEther(parent_mo_or_dn=mo, nw_ctrl_policy_name="", admin_host_port="ANY",
                             admin_vcon="1", stats_policy_name="", admin_cdn_name="", switch_id="A-B",
                             pin_to_group_name="", name=t_vnic2_name, order="2", qos_policy_name="",
                             adaptor_profile_name=t_vnic_adapter, ident_pool_name="", cdn_source="vnic-name",
                             mtu="1500",
                             nw_templ_name=t_vnic2_template, addr="derived")
            mo_8 = VnicFcNode(parent_mo_or_dn=mo, ident_pool_name="global-node-default", addr="pool-derived")
            mo_9 = LsRequirement(parent_mo_or_dn=mo, restrict_migration="no", name=t_pool, qualifier="")
            mo_10 = LsPower(parent_mo_or_dn=mo, state="admin-up")
            mo_11 = LstorageProfileBinding(parent_mo_or_dn=mo, storage_profile_name=t_storage)
            mo_12 = FabricVCon(parent_mo_or_dn=mo, placement="physical", fabric="NONE", share="shared", select="all",
                               transport="ethernet,fc", id="1", inst_type="manual")
            mo_13 = FabricVCon(parent_mo_or_dn=mo, placement="physical", fabric="NONE", share="shared", select="all",
                               transport="ethernet,fc", id="2", inst_type="manual")
            mo_14 = FabricVCon(parent_mo_or_dn=mo, placement="physical", fabric="NONE", share="shared", select="all",
                               transport="ethernet,fc", id="3", inst_type="manual")
            mo_15 = FabricVCon(parent_mo_or_dn=mo, placement="physical", fabric="NONE", share="shared", select="all",
                               transport="ethernet,fc", id="4", inst_type="manual")

            s3260_templates.update({key: {'mo': mo,
                                          'mo_1': mo_1,
                                          'mo_2': mo_2,
                                          'mo_3': mo_3,
                                          'mo_4': mo_4,
                                          'mo_5': mo_5,
                                          'mo_6': mo_6,
                                          'mo_7': mo_7,
                                          'mo_8': mo_8,
                                          'mo_9': mo_9,
                                          'mo_10': mo_10,
                                          'mo_11': mo_11,
                                          'mo_12': mo_12,
                                          'mo_13': mo_13,
                                          'mo_14': mo_14,
                                          'mo_15': mo_15
                                          }})

        service_profiles.update({'S3260_templates': s3260_templates})
        print "> S3260 Templates.................................[OK]"

        """
        Service Profile Template for C220M4S
        """


        c220_templates = {}

        for key in s_service_profiles['C220_templates']:
            t_name = str(s_service_profiles['C220_templates'][key]['name'])
            t_descr = str(s_service_profiles['C220_templates'][key]['descr'])
            t_uuid = str(s_service_profiles['C220_templates'][key]['uuid'])
            t_storage = str(s_service_profiles['C220_templates'][key]['storage'])
            t_vnic1_name = str(s_service_profiles['C220_templates'][key]['vnic1_name'])
            t_vnic2_name = str(s_service_profiles['C220_templates'][key]['vnic2_name'])
            t_vnic1_template = str(s_service_profiles['C220_templates'][key]['vnic1_template'])
            t_vnic2_template = str(s_service_profiles['C220_templates'][key]['vnic2_template'])
            t_vnic_adapter = str(s_service_profiles['C220_templates'][key]['vnic_adapter'])
            t_boot = str(s_service_profiles['C220_templates'][key]['boot'])
            t_maint = str(s_service_profiles['C220_templates'][key]['maint'])
            t_pool = str(s_service_profiles['C220_templates'][key]['pool'])
            t_bios = str(s_service_profiles['C220_templates'][key]['bios'])
            t_power = str(s_service_profiles['C220_templates'][key]['power'])
            t_scrub = str(s_service_profiles['C220_templates'][key]['scrub'])

            mo = LsServer(parent_mo_or_dn=service_dn, vmedia_policy_name="", ext_ip_state="pooled",
                          bios_profile_name=t_bios, mgmt_fw_policy_name="", agent_policy_name="",
                          mgmt_access_policy_name="", dynamic_con_policy_name="",
                          sol_policy_name="", uuid="0", descr=t_descr, stats_policy_name="",
                          ext_ip_pool_name="ceph-ext-mgmt", boot_policy_name=t_boot, usr_lbl="",
                          host_fw_policy_name="", vcon_profile_name="", ident_pool_name=t_uuid, src_templ_name="",
                          type="initial-template", local_disk_policy_name="", scrub_policy_name=t_scrub,
                          power_policy_name=t_power, maint_policy_name=t_maint,
                          name=t_name)
            mo_1 = LsVConAssign(parent_mo_or_dn=mo, admin_vcon="1", admin_host_port="ANY", order="1",
                                transport="ethernet", vnic_name=t_vnic1_name)
            mo_2 = LsVConAssign(parent_mo_or_dn=mo, admin_vcon="1", admin_host_port="ANY", order="2",
                                transport="ethernet", vnic_name=t_vnic2_name)
            mo_3 = VnicDefBeh(parent_mo_or_dn=mo, name="", descr="", action="none", type="vhba",
                              nw_templ_name="")
            mo_4 = VnicEther(parent_mo_or_dn=mo, nw_ctrl_policy_name="", admin_host_port="ANY",
                             admin_vcon="1", stats_policy_name="", admin_cdn_name="", switch_id="A-B",
                             pin_to_group_name="", name=t_vnic1_name, order="1", qos_policy_name="",
                             adaptor_profile_name=t_vnic_adapter, ident_pool_name="", cdn_source="vnic-name",
                             mtu="1500",
                             nw_templ_name=t_vnic1_template, addr="derived")
            mo_5 = VnicEther(parent_mo_or_dn=mo, nw_ctrl_policy_name="", admin_host_port="ANY",
                             admin_vcon="1", stats_policy_name="", admin_cdn_name="", switch_id="A-B",
                             pin_to_group_name="", name=t_vnic2_name, order="2", qos_policy_name="",
                             adaptor_profile_name=t_vnic_adapter, ident_pool_name="", cdn_source="vnic-name",
                             mtu="9000",
                             nw_templ_name=t_vnic2_template, addr="derived")
            mo_6 = VnicFcNode(parent_mo_or_dn=mo, ident_pool_name="global-node-default", addr="pool-derived")
            mo_7 = LsRequirement(parent_mo_or_dn=mo, restrict_migration="no", name=t_pool, qualifier="")
            mo_8 = LsPower(parent_mo_or_dn=mo, state="admin-up")
            mo_9 = LstorageProfileBinding(parent_mo_or_dn=mo, storage_profile_name=t_storage)
            mo_10 = FabricVCon(parent_mo_or_dn=mo, placement="physical", fabric="NONE", share="shared", select="all",
                               transport="ethernet,fc", id="1", inst_type="manual")
            mo_11 = FabricVCon(parent_mo_or_dn=mo, placement="physical", fabric="NONE", share="shared", select="all",
                               transport="ethernet,fc", id="2", inst_type="manual")
            mo_12 = FabricVCon(parent_mo_or_dn=mo, placement="physical", fabric="NONE", share="shared", select="all",
                               transport="ethernet,fc", id="3", inst_type="manual")
            mo_13 = FabricVCon(parent_mo_or_dn=mo, placement="physical", fabric="NONE", share="shared", select="all",
                               transport="ethernet,fc", id="4", inst_type="manual")

            c220_templates.update({key: {'mo': mo,
                                          'mo_1': mo_1,
                                          'mo_2': mo_2,
                                          'mo_3': mo_3,
                                          'mo_4': mo_4,
                                          'mo_5': mo_5,
                                          'mo_6': mo_6,
                                          'mo_7': mo_7,
                                          'mo_8': mo_8,
                                          'mo_9': mo_9,
                                          'mo_10': mo_10,
                                          'mo_11': mo_11,
                                          'mo_12': mo_12,
                                          'mo_13': mo_13
                                          }})

        service_profiles.update({'C220_templates': c220_templates})
        print "> C220 Templates..................................[OK]"

        """
        Services Profiles S3260, C220
        """

        profiles = {}

        for key in s_service_profiles['profiles']:
            sp_name = str(s_service_profiles['profiles'][key]['name'])
            sp_dn = str(s_service_profiles['profiles'][key]['dn'])
            sp_template = str(s_service_profiles['profiles'][key]['template'])
            sp_suffix = int(s_service_profiles['profiles'][key]['suffix'])
            sp_instances = int(s_service_profiles['profiles'][key]['instances'])

            for instance in range(sp_suffix, sp_instances + 1):
                sp_name_ins = "%s-%s" % (sp_name, instance)
                mo = LsServer(parent_mo_or_dn=sp_dn,
                            src_templ_name=sp_template,
                            name=sp_name_ins,
                            type="instance",
                            uuid="derived")
                profiles.update({sp_name_ins: {'mo':mo}})

        service_profiles.update({'profiles': profiles})

        print "> Profiles from Templates.........................[OK]"


        return service_profiles

    def deploy(self, settings):
        """ UCS Central Ceph Deployment """

        ucsc_ip = settings['ucsc']['credentials']['ip']
        ucsc_user = settings['ucsc']['credentials']['user']
        ucsc_pw = settings['ucsc']['credentials']['pw']
        handle = UcscHandle(ucsc_ip, ucsc_user, ucsc_pw)
        handle.login()

        print "\n>>>>>>>>>>>>> UCSC Login <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"


        print "############# Assigning UCS to Domain #################"

        ucsm_ip = settings['ucsm']['credentials']['ip']
        ucsm_domain_group = settings['ucsm']['credentials']['domain_group']

        system_id = self.get_system_id(handle,ucsm_ip)
        print "> Getting system_id...............................[OK]"

        domain_assign_to_domaingroup(handle, domain_ip=ucsm_ip, domain_group=ucsm_domain_group)
        print "> Assigned........................................[OK]"

        print "############# Creating Pools ##########################"

        s_pools = settings['ucsc']['pools']
        pools = self.create_pools(s_pools,system_id)

        for key in pools:
            #print 'Type: ' + key
            for sub_key in pools[key]:
                #print key + ': ' + sub_key
                handle.add_mo(pools[key][sub_key]['mo'], True)
                handle.commit()

        # wwnn global-node-default

        mo = FcpoolInitiators(parent_mo_or_dn="org-root", name="global-node-default",
                              descr="global-node-default", purpose="node-wwn-assignment")
        mo_1 = FcpoolBlock(parent_mo_or_dn=mo, to="20:00:00:25:B5:00:00:63", r_from="20:00:00:25:B5:00:00:00")
        handle.add_mo(mo,True)
        handle.commit()

        print "############# Creating Policies #######################"

        s_policies = settings['ucsc']['policies']
        policies = self.create_policies(s_policies)



        for key in policies:
            #print 'Type: ' + key
            for sub_key in policies[key]:
                #print key + ': ' + sub_key
                handle.add_mo(policies[key][sub_key]['mo'], True)  # Overwrite
                handle.commit()


        print "############# Creating Chassis Profiles ###############"

        s_chassis_profiles = settings['ucsc']['chassis_profiles']
        chassis_profiles = self.create_chassis_profiles(s_chassis_profiles,system_id)

        for key in chassis_profiles:
            #print 'Type: ' + key
            for sub_key in chassis_profiles[key]:
                #print key + ': ' + sub_key
                handle.add_mo(chassis_profiles[key][sub_key]['mo'], True)  # Overwrite
                handle.commit()


        print "############# Creating Storage Profiles ###############"

        s_storage_profiles = settings['ucsc']['storage_profiles']
        storage_profiles = self.create_storage_profiles(s_storage_profiles)

        for key in storage_profiles:
            print 'Type: ' + key
            for sub_key in storage_profiles[key]:
                print key + ': ' + sub_key
                handle.add_mo(storage_profiles[key][sub_key]['mo'],True)  # Overwrite
                handle.commit()


        print "############# Creating Service Profiles ###############"

        s_service_profiles = settings['ucsc']['service_profiles']
        service_profiles = self.create_service_profiles(s_service_profiles)

        for key in service_profiles:
            #print 'Type: ' + key
            for sub_key in service_profiles[key]:
                #print key + ': ' + sub_key
                handle.add_mo(service_profiles[key][sub_key]['mo'], True)  # Overwrite
                handle.commit()



        handle.logout()

        print "\n>>>>>>>>>>>>> UCSC Logout <<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"







