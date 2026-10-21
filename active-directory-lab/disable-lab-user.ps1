# Demo: disable a lab account; requires appropriate AD permissions.
param([Parameter(Mandatory=$true)][string]$Username)
Import-Module ActiveDirectory -ErrorAction Stop
$user = Get-ADUser -Identity $Username -ErrorAction Stop
$answer = Read-Host "Disable account $($user.SamAccountName)? Type YES"
if ($answer -ne 'YES') { Write-Host 'Cancelled'; exit }
Disable-ADAccount -Identity $user
Get-ADUser -Identity $user -Properties Enabled | Select-Object Name,Enabled
