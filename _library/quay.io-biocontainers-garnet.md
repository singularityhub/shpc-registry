---
layout: container
name:  "quay.io/biocontainers/garnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/garnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/garnet/container.yaml"
updated_at: "2024-08-26 03:20:10.110709"
latest: "0.4.5--py36_0"
container_url: "https://biocontainers.pro/tools/garnet"
aliases:
 - "easy_install-3.6"
 - "qhelpconverter"
 - "pylupdate5"
 - "pyrcc5"
 - "pyuic5"
 - "sip"
 - "qdoc"
 - "gst-device-monitor-1.0"
 - "gst-discoverer-1.0"
 - "gst-play-1.0"
versions:
 - "0.4.5--py36_0"
 - "0.4.5--py35_0"
description: "shpc-registry automated BioContainers addition for garnet"
config: {"url": "https://biocontainers.pro/tools/garnet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for garnet", "latest": {"0.4.5--py36_0": "sha256:bac3aaa0bd007c56bb9ab5c8ca93d9d13ee8122aec55091ce8c08c4f989f838a"}, "tags": {"0.4.5--py36_0": "sha256:bac3aaa0bd007c56bb9ab5c8ca93d9d13ee8122aec55091ce8c08c4f989f838a", "0.4.5--py35_0": "sha256:727030c2342310195b3abf52d5b4278a44e5a1cab68d10fc09e4e04eda38b259"}, "docker": "quay.io/biocontainers/garnet", "aliases": {"easy_install-3.6": "/usr/local/bin/easy_install-3.6", "qhelpconverter": "/usr/local/bin/qhelpconverter", "pylupdate5": "/usr/local/bin/pylupdate5", "pyrcc5": "/usr/local/bin/pyrcc5", "pyuic5": "/usr/local/bin/pyuic5", "sip": "/usr/local/bin/sip", "qdoc": "/usr/local/bin/qdoc", "gst-device-monitor-1.0": "/usr/local/bin/gst-device-monitor-1.0", "gst-discoverer-1.0": "/usr/local/bin/gst-discoverer-1.0", "gst-play-1.0": "/usr/local/bin/gst-play-1.0"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/garnet.
shpc-registry automated BioContainers addition for garnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/garnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/garnet:0.4.5--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/garnet/0.4.5--py36_0
$ module help quay.io/biocontainers/garnet/0.4.5--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### garnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### garnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### garnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### garnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### garnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### garnet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### easy_install-3.6

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylupdate5

```bash
$ singularity exec <container> /usr/local/bin/pylupdate5
$ podman run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrcc5

```bash
$ singularity exec <container> /usr/local/bin/pyrcc5
$ podman run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyuic5

```bash
$ singularity exec <container> /usr/local/bin/pyuic5
$ podman run --it --rm --entrypoint /usr/local/bin/pyuic5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyuic5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip

```bash
$ singularity exec <container> /usr/local/bin/sip
$ podman run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdoc

```bash
$ singularity exec <container> /usr/local/bin/qdoc
$ podman run --it --rm --entrypoint /usr/local/bin/qdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-device-monitor-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-device-monitor-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-device-monitor-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-device-monitor-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-discoverer-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-discoverer-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-discoverer-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-discoverer-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gst-play-1.0

```bash
$ singularity exec <container> /usr/local/bin/gst-play-1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gst-play-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gst-play-1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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