# zjleblanc.windows.patch

Patch a Windows server and publish reports to a designated host

## Requirements

- Ansible `>=2.15.0`
- pywinrm on the controller
- Inventory host `raspi` to receive reports

## Entry points

### main

Searches for Windows updates. When `skip_install` is false, installs them and can reboot. Search reports and failed-update reports are written on the `raspi` host.

#### Options

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| skip_install | bool | yes |  | Search and publish a report without installing when true. Install updates when false. |
| patch_categories | list of str | no | `[SecurityUpdates, CriticalUpdates, UpdateRollups]` | Windows update categories passed to ansible.windows.win_updates. |
| patch_kbs | list of str | no |  | Knowledge base ids passed as accept_list. Omitted when unset, so category matching is unchanged. |
| patch_allow_reboot | bool | no | `true` | Allow the install task to reboot the host. |
| patch_failed_report | bool | no | `true` | Write a failed-update report when an install reports failures. |
| patch_report_dest_dir | str | no | `%Temp%` | Directory on the raspi host where reports are written. |
| template_run_date | str | no |  | Timestamp rendered into the failed-update report. The report task fails when this is unset. |

## Dependencies

- ansible.windows

## Example Playbook

```yaml
- hosts: windows
  tasks:
    - name: Install updates
      ansible.builtin.include_role:
        name: zjleblanc.windows.patch
      vars:
        skip_install: false

    - name: Search for updates and publish a report
      ansible.builtin.include_role:
        name: zjleblanc.windows.patch
      vars:
        skip_install: true

    - name: Install specific updates without a failed-update report
      ansible.builtin.include_role:
        name: zjleblanc.windows.patch
      vars:
        skip_install: false
        patch_failed_report: false
        patch_categories:
          - SecurityUpdates
        patch_kbs:
          - KB4056892
          - KB4073117
```

## License

GPL-3.0-only. See the collection `LICENSE`.

## Author

Zach LeBlanc (@zjleblanc)
