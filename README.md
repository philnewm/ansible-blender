# Blender-Role

[![AlmaLinux9-CI](https://github.com/philnewm/ansible-blender/actions/workflows/almalinux9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/almalinux9-ci-caller.yml) [![Rocky9-CI](https://github.com/philnewm/ansible-blender/actions/workflows/rocky9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/rocky9-ci-caller.yml) [![CentOSStream9-CI](https://github.com/philnewm/ansible-blender/actions/workflows/centosstream9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/centosstream9-ci-caller.yml) [![Fedora43-CI](https://github.com/philnewm/ansible-blender/actions/workflows/fedora43-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/fedora43-ci-caller.yml)<br>
[![Ubuntu2404-CI](https://github.com/philnewm/ansible-blender/actions/workflows/ubuntu2404-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/ubuntu2404-ci-caller.yml) [![Debian13-CI](https://github.com/philnewm/ansible-blender/actions/workflows/debian13-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/debian13-ci-caller.yml)

Role description

This role includes a molecule testing setup as a submodule at `molecule/`

## Structure

```code
📦 ansible-blender
 ┣ 📂 defaults
 ┃ ┗ 📜 main.yml
 ┣ 📂 meta
 ┃ ┗ 📜 main.yml
 ┣ 📂 molecule
 ┃ ┗ 📂 default
 ┃   ┗ 📜, 📜, 📜, scenario_files
 ┣ 📂 tasks
 ┃ ┣ 📜 absent.yml
 ┃ ┣ 📜 install.yml
 ┃ ┣ 📜 main.yml
 ┃ ┣ 📜 present.yml
 ┃ ┗ 📜 tests.yml
 ┣ 📂 vars
 ┃ ┗ 📜 main.yml
 ┗ 🗒️ README.md

```

Describe and explain role structure.

## Requirements

Elaborate external dependencies and how to use them.

## Role Variables

* `defaults/main.yml`
  * state (str): Desired setup state
  * default_version (bool): Set version in launcher
  * version: Split into major, minor and patch

## Dependencies

List role ansible-galaxy dependencies - if any.

## Example Playbook

Add an example playbook

```yaml
---

tasks:
  - name: Include ansible-blender present
    ansible.builtin.include_role:
      name: ansible-blender
    vars:
      state: present
      set_default_version: true
      blender_major_version: 5
      blender_minor_version: 0
      blender_patch_version: 1
      blender_architecture: "x64"
      blender_source_url: "https://download.blender.org/release/Blender{{ blender_version_short }}/blender-{{ blender_version_long }}-linux-{{ blender_architecture }}.tar.xz"
      blender_install_path: "/opt/blender/{{ blender_version_long }}_{{ blender_architecture }}"

...
```

## License

Add license - if any.
