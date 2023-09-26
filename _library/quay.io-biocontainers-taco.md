---
layout: container
name:  "quay.io/biocontainers/taco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/taco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/taco/container.yaml"
updated_at: "2023-09-26 02:30:01.092112"
latest: "0.7.3--py27_0"
container_url: "https://biocontainers.pro/tools/taco"
aliases:
 - "pyi-archive_viewer"
 - "pyi-bindepend"
 - "pyi-grab_version"
 - "pyi-makespec"
 - "pyi-set_version"
 - "pyinstaller"
 - "taco_refcomp"
 - "taco_run"
 - "easy_install-2.7"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "tclsh8.5"
 - "wish8.5"
versions:
 - "v0.7.0--py27_0"
 - "0.7.3--py27_0"
description: "shpc-registry automated BioContainers addition for taco"
config: {"url": "https://biocontainers.pro/tools/taco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for taco", "latest": {"0.7.3--py27_0": "sha256:6f83695531aa2b6fbb07d56e53b139ab41883631892426c3efdbd6ab5ba3ee7f"}, "tags": {"v0.7.0--py27_0": "sha256:413c880fd6d29f84293cca1d4f3e0f7ecb883d700445ee31d319da078df09820", "0.7.3--py27_0": "sha256:6f83695531aa2b6fbb07d56e53b139ab41883631892426c3efdbd6ab5ba3ee7f"}, "docker": "quay.io/biocontainers/taco", "aliases": {"pyi-archive_viewer": "/usr/local/bin/pyi-archive_viewer", "pyi-bindepend": "/usr/local/bin/pyi-bindepend", "pyi-grab_version": "/usr/local/bin/pyi-grab_version", "pyi-makespec": "/usr/local/bin/pyi-makespec", "pyi-set_version": "/usr/local/bin/pyi-set_version", "pyinstaller": "/usr/local/bin/pyinstaller", "taco_refcomp": "/usr/local/bin/taco_refcomp", "taco_run": "/usr/local/bin/taco_run", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/taco.
shpc-registry automated BioContainers addition for taco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/taco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/taco:0.7.3--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/taco/0.7.3--py27_0
$ module help quay.io/biocontainers/taco/0.7.3--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### taco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### taco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### taco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### taco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### taco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### taco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyi-archive_viewer

```bash
$ singularity exec <container> /usr/local/bin/pyi-archive_viewer
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-archive_viewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-archive_viewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyi-bindepend

```bash
$ singularity exec <container> /usr/local/bin/pyi-bindepend
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-bindepend   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-bindepend   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyi-grab_version

```bash
$ singularity exec <container> /usr/local/bin/pyi-grab_version
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-grab_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-grab_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyi-makespec

```bash
$ singularity exec <container> /usr/local/bin/pyi-makespec
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-makespec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-makespec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyi-set_version

```bash
$ singularity exec <container> /usr/local/bin/pyi-set_version
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-set_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-set_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyinstaller

```bash
$ singularity exec <container> /usr/local/bin/pyinstaller
$ podman run --it --rm --entrypoint /usr/local/bin/pyinstaller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyinstaller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taco_refcomp

```bash
$ singularity exec <container> /usr/local/bin/taco_refcomp
$ podman run --it --rm --entrypoint /usr/local/bin/taco_refcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taco_refcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taco_run

```bash
$ singularity exec <container> /usr/local/bin/taco_run
$ podman run --it --rm --entrypoint /usr/local/bin/taco_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taco_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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