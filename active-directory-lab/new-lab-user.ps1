# Run in an isolated Active Directory lab with delegated privileges.
param([Parameter(Mandatory=$true)][string]$Username,
      [Parameter(Mandatory=$true)][string]$DisplayName)
Import-Module ActiveDirectory -ErrorAction Stop
$base = (Get-ADDomain).DistinguishedName
$ou = "OU=Employees,$base"
if (Get-ADUser -Filter "SamAccountName -eq '$Username'" -ErrorAction SilentlyContinue) {
    throw "User already exists: $Username"
}
$password = Read-Host 'Enter temporary password' -AsSecureString
New-ADUser -Name $DisplayName -SamAccountName $Username -Path $ou -AccountPassword $password -Enabled $true -ChangePasswordAtLogon $true
Get-ADUser -Identity $Username -Properties Enabled | Select-Object Name,SamAccountName,Enabled
