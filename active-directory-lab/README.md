# Active Directory Administration Lab

Windows Server and Windows client virtual-machine lab. Keep the virtual network isolated from production networks.

## Lab plan
Domain: `corp.example.test`; domain controller `192.168.56.10/24`; client `192.168.56.20/24`, DNS pointing to the controller.

1. Create Windows Server and Windows client VMs on an isolated virtual switch.
2. Install Active Directory Domain Services and DNS on the server.
3. Promote to a new forest `corp.example.test`; reboot.
4. Join a compatible Windows client to the domain.
5. Review and execute `provision-users.ps1` on the domain controller.
6. Create a screen-lock Group Policy for Employees OU.
7. Run `gpupdate /force` and `gpresult /r`; test account sign-in, groups and disable/enable.

## Troubleshooting
Domain join failure: check DNS, network reachability, clock synchronization and credentials. Login failures: account state and event logs. GPO failures: OU links, filtering and `gpresult /h report.html`.

**Status:** lab plan and provisioning script only; domain has not been deployed.
