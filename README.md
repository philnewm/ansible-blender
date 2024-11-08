# Blender-Role

[![Alma9-CI](https://github.com/philnewm/ansible-blender/actions/workflows/alma9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/alma9-ci-caller.yml)  [![Rocky9-CI](https://github.com/philnewm/ansible-blender/actions/workflows/rocky9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/rocky9-ci-caller.yml)  [![CentOSStream9-CI](https://github.com/philnewm/ansible-blender/actions/workflows/centosstream9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/centosstream9-ci-caller.yml)  [![Debian12-CI](https://github.com/philnewm/ansible-blender/actions/workflows/debian12-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/debian12-ci-caller.yml)  [![Ubuntu2204-CI](https://github.com/philnewm/ansible-blender/actions/workflows/ubuntu2204-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-blender/actions/workflows/ubuntu2204-ci-caller.yml)

Role description

* https://blender.stackexchange.com/questions/188043/python-autocompletion
* https://docs.blender.org/api/current/info_advanced_blender_as_bpy.html
* https://studio.blender.org/tools/td-guide/python
* https://projects.blender.org/blender/blender/issues/126686
* https://pypi.org/project/blender-stubs/
* https://github.com/ansible/ansible/issues/72220

This role includes a vagrant based molecule testing setup as a submodule at `molecule/default`

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
 ┃ ┣ 📜 dependencies.yml
 ┃ ┣ 📜 absent.yml
 ┃ ┗ 📜 init.yml
 ┣ 📂 vars
 ┃ ┗ 📜 main.yml
 ┗ 🗒️ README.md
 ┗ 📓 requirements.txt

```

Describe and explain role structure.

## Requirements

Elaborate external dependencies and how to use them.

## Role Variables

* defaults/main.yml
  * first_var
  * sec_var
  * third_var
* vars/main.yml
  * first_var
  * sec_var
  * third_var

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

## Notes

Includes special git configuration for submodule files that are most likely to get local overrides
`.git/info/attributes`

```code
molecule/default/cleanup.yml merge=ours
molecule/default/converge.yml merge=ours
molecule/default/verify.yml merge=ours
```

## Changes to role template

* Add github action that flags empty directories on release creation
