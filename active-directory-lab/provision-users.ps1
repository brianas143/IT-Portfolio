# Run only in an isolated disposable lab as a domain administrator.
Import-Module ActiveDirectory
$base = (Get-ADDomain).DistinguishedName
$ou = "OU=Employees,$base"
if (-not (Get-ADOrganizationalUnit -LDAPFilter '(ou=Employees)' -SearchBase $base -ErrorAction SilentlyContinue)) {
    New-ADOrganizationalUnit -Name 'Employees' -Path $base -ProtectedFromAccidentalDeletion $true
}
$groupName = 'IT-Support-Lab'
if (-not (Get-ADGroup -Filter "Name -eq '$groupName'" -ErrorAction SilentlyContinue)) {
    New-ADGroup -Name $groupName -GroupScope Global -GroupCategory Security -Path $ou
}
# No hardcoded passwords. Example interactive user creation:
# $password = Read-Host 'Temporary password' -AsSecureString
# New-ADUser -Name 'Alex Example' -SamAccountName 'alex.example' -Path $ou -AccountPassword $password -Enabled $true -ChangePasswordAtLogon $true
Write-Host "Prepared OU and security group in $base"
