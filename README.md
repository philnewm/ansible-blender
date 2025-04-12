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
 ┃ ┣ 📜 config.yml
 ┃ ┣ 📜 gpu_query.yml
 ┃ ┣ 📜 favorite.yml
 ┃ ┣ 📜 pipeline_dev.yml
 ┃ ┣ 📜 absent.yml
 ┃ ┗ 📜 tests.yml
 ┣ 📂 vars
 ┃ ┗ 📜 main.yml
 ┗ 🗒️ README.md
 ┗ 📓 requirements.txt

```

Describe and explain role structure.

## Requirements

Elaborate external dependencies and how to use them.

## Role Variables

* `defaults/main.yml`
  * state (str): Desired setup state
  * default_version (bool): Set version in launcher
  * gnome_favorite (bool): Add to Gnome favorites
  * pipeline_dev (bool): Add pipeline development setup
  * launcher: Launcher name per Linux OS family
  * version: Split into major, minor and patch

* `vars/main.yml`
  * dependencies - to enable favorite setting on gnome desktop

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

## Blender launcher local build

* dependency: python3-devel, xcb-util-image, xcb-util-keysyms, xcb-util-wm, xcb-util-renderutil, python3-xlib  # TODO test if epel repo is actually required
* python dependencies: sip
* git clone -b v2.2.0 https://github.com/Victor-IX/Blender-Launcher-V2
* change to repo root
* python -m ensurepip
* python -m pip install virtualenv
* python -m virtualenv --clear --download .venv
* source .venv/bin/activate
* pip install -e .
* python build_style.py
* cd scripts && sh build_linux.sh
* sudo cp ../../extras/blenderlauncher.desktop /usr/share/applications/
* sudo cp Blender\ Launcher /usr/bin/blenderlauncher
* find icon
