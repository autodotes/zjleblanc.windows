# zjleblanc.windows.mssql

Install MS SQL Server on Windows using Desired State Configuration

## Requirements

- Ansible `>=2.15.0`
- A domain-joined Windows target
- Inventory host named by `mssql_domain_controller`
- Network access to the SQL Server media URL and the PowerShell Gallery

## Entry points

### main

Installs PowerShell modules and Windows features, creates the SQL service accounts, downloads setup media, installs the instance with Desired State Configuration, then sets the TCP port, memory, and parallelism.

#### Options

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| mssql_sqlsvc_account_pass | str | yes |  | Password for the SQL Server service account. |
| mssql_agentsvc_account_pass | str | yes |  | Password for the SQL Agent service account. |
| mssql_assvc_account_pass | str | yes |  | Password for the Analysis Services service account. |
| mssql_ps_sqlserver_dsc_version | str | no | `16.5.0` | Version of the SqlServerDsc PowerShell module to install. |
| mssql_version | str | no | `2022` | SQL Server version used in downloader filenames and as the key into mssql_version_media. |
| mssql_version_media | dict | no | `{"2022": "https://go.microsoft.com/fwlink/p/?linkid=2215158", "2019": "https://go.microsoft.com/fwlink/?linkid=866664"}` | Map of SQL Server version to the media downloader URL. |
| mssql_installation_source | str | no | `{{ mssql_version_media[mssql_version] }}` | URL of the SQL Server media downloader. |
| mssql_installation_path | str | no | `C:\SQLInstall` | Directory that receives the extracted SQL Server installation media. |
| mssql_temp_download_path | str | no | `C:\tmp` | Directory that receives the media downloader executable. |
| mssql_instance_name | str | no | `MSSQLSERVER` | SQL Server instance name. |
| mssql_drive | str | no | `C` | Drive letter used to build mssql_userdbvol_path. |
| mssql_userdbvol_name | str | no | `Userdbvol01` | Directory name used to build mssql_userdbvol_path. |
| mssql_port | int | no | `1433` | TCP port configured on the instance. |
| mssql_max_server_memory | int | no | `1024` | Value applied to max server memory (MB). Must be divisible by 512. |
| mssql_suppress_reboot | bool | no | `false` | Skip the reboot handler and pass SuppressReboot to SQL setup when true. |
| mssql_base_ldap_path | str | no | `ou=Users,dc=contoso,dc=com` | LDAP path where the role creates the service accounts. |
| mssql_domain_controller | str | no | `dc01` | Inventory hostname of the domain controller where service accounts are created. |
| mssql_netbios | str | no | `CONTOSO` | NetBIOS domain name used to build the default service account names. |
| mssql_sqlsvc_account | str | no | `{{ mssql_netbios }}\sql_svc` | SQL Server service account in DOMAIN\user form. |
| mssql_agentsvc_account | str | no | `{{ mssql_netbios }}\sql_agt` | SQL Agent service account in DOMAIN\user form. |
| mssql_assvc_account | str | no | `{{ mssql_sqlsvc_account }}` | Analysis Services service account in DOMAIN\user form. |
| mssql_userdbvol_path | str | no | `{{ mssql_drive }}:\{{ mssql_userdbvol_name }}` | Volume path that contains database files and logs. |
| mssql_db_accesspath | str | no | `{{ mssql_userdbvol_path }}\DatabaseFiles` | Directory for database files. |
| mssql_logs_accesspath | str | no | `{{ mssql_userdbvol_path }}\DatabaseLogs` | Directory for database logs. |
| mssql_installshared_path | str | no | `C:\Program Files\Microsoft SQL Server` | SQLSetup InstallSharedDir path. |
| mssql_installsharedwow_path | str | no | `C:\Program Files (x86)\Microsoft SQL Server` | SQLSetup InstallSharedwowDir path. |
| mssql_instance_path | str | no | `C:\Program Files\Microsoft SQL Server\{{ mssql_instance_name }}` | SQLSetup InstanceDir path. |
| mssql_sqlinstalldata_path | str | no | `{{ mssql_db_accesspath }}\{{ mssql_instance_name }}` | SQLSetup InstallSQLDataDir path. |
| mssql_sqluserdata_path | str | no | `{{ mssql_db_accesspath }}\{{ mssql_instance_name }}` | SQLSetup SQLUserDBDir path. |
| mssql_sqluserlog_path | str | no | `{{ mssql_logs_accesspath }}\{{ mssql_instance_name }}` | SQLSetup SQLUserDBLogDir path. |
| mssql_sqltempDB_path | str | no | `C:\TempDBFiles\Data\{{ mssql_instance_name }}` | SQLSetup SQLTempDBDir path. |
| mssql_sqltempDBlog_path | str | no | `C:\TempDBFiles\Log\{{ mssql_instance_name }}` | SQLSetup SQLTempDBLogDir path. |
| mssql_features | str | no | `SQLENGINE,AS` | Comma-separated SQL Server features to install. |
| mssql_collation | str | no | `SQL_Latin1_General_CP1_CI_AS` | SQL Server collation. |
| mssql_browsersvc_mode | str | no | `Automatic` | Startup mode for the SQL Server Browser service. Choices: `Automatic`, `Disabled`, `Manual`. |
| mssql_sysadmin_accounts | list of str | no | `["{{ mssql_netbios }}\\Domain Admins", "{{ mssql_netbios }}\\Administrator"]` | Windows accounts granted the sysadmin role. |
| mssql_asadmin_accounts | list of str | no | `{{ mssql_sysadmin_accounts }}` | Windows accounts granted Analysis Services administrator rights. |
| mssql_max_degree_of_parallelism | int | no | `0` | max degree of parallelism. 0 lets SQL Server choose. |
| mssql_min_server_memory | int | no | `0` | Value applied to min server memory (MB). |

### test_connection

Installs the SqlServer PowerShell module on the target, runs `SELECT GETDATE()` against the target `ansible_host`, and prints the result.

#### Options

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| mssql_domain_controller | str | no | `dc01` | Domain controller name included in the task names for this entry point. |

## Dependencies

- ansible.windows
- community.windows
- microsoft.ad

## Example Playbook

```yaml
- hosts: sql_servers
  tasks:
    - name: Install SQL Server
      ansible.builtin.include_role:
        name: zjleblanc.windows.mssql
      vars:
        mssql_netbios: ANSIBLE
        mssql_base_ldap_path: OU=Users,DC=ansible,DC=local
        mssql_sqlsvc_account_pass: "{{ sql_svc_pass }}"
        mssql_agentsvc_account_pass: "{{ sql_agent_pass }}"
        mssql_assvc_account_pass: "{{ sql_as_pass }}"

    - name: Test SQL connectivity
      ansible.builtin.include_role:
        name: zjleblanc.windows.mssql
        tasks_from: test_connection
```

## License

GPL-3.0-only. See the collection `LICENSE`.

## Author

Zach LeBlanc (@zjleblanc)
