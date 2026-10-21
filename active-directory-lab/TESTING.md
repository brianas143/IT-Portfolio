# Active Directory lab verification

- [ ] Domain controller installed and DNS resolving `corp.example.test`
- [ ] Windows client joined domain and logged in with a lab user
- [ ] Employees OU and IT-Support-Lab group visible in ADUC
- [ ] Run `new-lab-user.ps1` with a dummy user; verify sign-in and password-change prompt
- [ ] Disable the dummy account; verify login is blocked
- [ ] Link a screen-lock policy and verify using `gpresult /r`
- [ ] Save real screenshots from ADUC, PowerShell, and Group Policy console (hide credentials)

These steps require a Windows Server virtual machine; files alone do not establish completion.
