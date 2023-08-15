---
layout: container
name:  "quay.io/biocontainers/opencontactcli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/opencontactcli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/opencontactcli/container.yaml"
updated_at: "2023-08-15 03:04:40.135473"
latest: "1.1--py39hdd8045a_7"
container_url: "https://biocontainers.pro/tools/opencontactcli"
aliases:
 - "OpenContactCLI"
 - "contactgui.f"
 - "inputgui.f"
 - "ljresid"
 - "ljresidn"
 - "main_cli.py"
 - "f2py3.6"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "pyvenv"
versions:
 - "1.1--py36h5f405dc_6"
 - "1.1--py39hdd8045a_7"
description: "shpc-registry automated BioContainers addition for opencontactcli"
config: {"url": "https://biocontainers.pro/tools/opencontactcli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for opencontactcli", "latest": {"1.1--py39hdd8045a_7": "sha256:5e6cf597c03a565762d614f345c4a2bb63233d25ca48bd37495f6b3d1f791546"}, "tags": {"1.1--py36h5f405dc_6": "sha256:ac624ab162be8768da170c651c9093a02f9e8934d5aebe070025e040fce9923c", "1.1--py39hdd8045a_7": "sha256:5e6cf597c03a565762d614f345c4a2bb63233d25ca48bd37495f6b3d1f791546"}, "docker": "quay.io/biocontainers/opencontactcli", "aliases": {"OpenContactCLI": "/usr/local/bin/OpenContactCLI", "contactgui.f": "/usr/local/bin/contactgui.f", "inputgui.f": "/usr/local/bin/inputgui.f", "ljresid": "/usr/local/bin/ljresid", "ljresidn": "/usr/local/bin/ljresidn", "main_cli.py": "/usr/local/bin/main_cli.py", "f2py3.6": "/usr/local/bin/f2py3.6", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/opencontactcli.
shpc-registry automated BioContainers addition for opencontactcli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/opencontactcli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/opencontactcli:1.1--py39hdd8045a_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/opencontactcli/1.1--py39hdd8045a_7
$ module help quay.io/biocontainers/opencontactcli/1.1--py39hdd8045a_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### opencontactcli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### opencontactcli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### opencontactcli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### opencontactcli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### opencontactcli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### opencontactcli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### OpenContactCLI

```bash
$ singularity exec <container> /usr/local/bin/OpenContactCLI
$ podman run --it --rm --entrypoint /usr/local/bin/OpenContactCLI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/OpenContactCLI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contactgui.f

```bash
$ singularity exec <container> /usr/local/bin/contactgui.f
$ podman run --it --rm --entrypoint /usr/local/bin/contactgui.f   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contactgui.f   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inputgui.f

```bash
$ singularity exec <container> /usr/local/bin/inputgui.f
$ podman run --it --rm --entrypoint /usr/local/bin/inputgui.f   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inputgui.f   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ljresid

```bash
$ singularity exec <container> /usr/local/bin/ljresid
$ podman run --it --rm --entrypoint /usr/local/bin/ljresid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ljresid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ljresidn

```bash
$ singularity exec <container> /usr/local/bin/ljresidn
$ podman run --it --rm --entrypoint /usr/local/bin/ljresidn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ljresidn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### main_cli.py

```bash
$ singularity exec <container> /usr/local/bin/main_cli.py
$ podman run --it --rm --entrypoint /usr/local/bin/main_cli.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/main_cli.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)