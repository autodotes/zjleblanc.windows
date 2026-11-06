# zjleblanc.windows

Windows automation content.

[Galaxy](https://galaxy.ansible.com/ui/repo/published/zjleblanc/windows/) | [Changelog](CHANGELOG.md)

## Contents

### Roles

| Name | Description |
| --- | --- |
| [mssql](roles/mssql/tasks/main.yml) | Install MS SQL Server on Windows using Desired State Configuration |
| [patch](roles/patch/tasks/main.yml) | Patch a Windows server and publish reports to a designated host |

Working examples are in the [mssql](roles/mssql/README.md) and [patch](roles/patch/README.md) role READMEs.

### Modules

| Name | Description |
| --- | --- |
| [smb_info](plugins/modules/smb_info.py) | Gather information regarding server message block shares |

```yaml
- name: Get info for all server message block shares
  zjleblanc.windows.smb_info:

- name: Get info for shares starting with Net
  zjleblanc.windows.smb_info:
    name: Net*
```
