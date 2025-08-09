# Blender-Role

[![Alma9-CI](https://github.com/philnewm/ansible-blender/actions/workflows/alma9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/alma9-ci-caller.yml)  [![Rocky9-CI](https://github.com/philnewm/ansible-blender/actions/workflows/rocky9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/rocky9-ci-caller.yml)  [![CentOSStream9-CI](https://github.com/philnewm/ansible-blender/actions/workflows/centosstream9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/centosstream9-ci-caller.yml)  [![Debian12-CI](https://github.com/philnewm/ansible-blender/actions/workflows/debian12-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/debian12-ci-caller.yml)  [![Ubuntu2204-CI](https://github.com/philnewm/ansible-blender/actions/workflows/ubuntu2204-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/ubuntu2204-ci-caller.yml)

Role description

This role includes a vagrant based molecule testing setup as a submodule at `molecule/`

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
 ┃ ┣ 📜 main.yml
 ┃ ┣ 📜 present.yml
 ┃ ┣ 📜 pipeline_dev.yml
 ┃ ┣ 📜 absent.yml
 ┃ ┗ 📜 tests.yml
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

...
```

## License

Add license - if any.
