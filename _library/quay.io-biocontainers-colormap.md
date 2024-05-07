---
layout: container
name:  "quay.io/biocontainers/colormap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/colormap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/colormap/container.yaml"
updated_at: "2024-05-07 02:58:34.837301"
latest: "0.9.8--py36_0"
container_url: "https://biocontainers.pro/tools/colormap"
aliases:
 - "easydev_buildPackage"
 - "ibrowse"
 - "multigit"
 - "browse"
 - "easy_install-3.6"
 - "qhelpconverter"
 - "pylupdate5"
 - "pyrcc5"
 - "pyuic5"
 - "sip"
versions:
 - "0.9.8--py36_0"
description: "shpc-registry automated BioContainers addition for colormap"
config: {"url": "https://biocontainers.pro/tools/colormap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for colormap", "latest": {"0.9.8--py36_0": "sha256:7e87f07f959c206b6c3572aa992e833aab21e39e26c33ffcc4f4edf127c173c7"}, "tags": {"0.9.8--py36_0": "sha256:7e87f07f959c206b6c3572aa992e833aab21e39e26c33ffcc4f4edf127c173c7"}, "docker": "quay.io/biocontainers/colormap", "aliases": {"easydev_buildPackage": "/usr/local/bin/easydev_buildPackage", "ibrowse": "/usr/local/bin/ibrowse", "multigit": "/usr/local/bin/multigit", "browse": "/usr/local/bin/browse", "easy_install-3.6": "/usr/local/bin/easy_install-3.6", "qhelpconverter": "/usr/local/bin/qhelpconverter", "pylupdate5": "/usr/local/bin/pylupdate5", "pyrcc5": "/usr/local/bin/pyrcc5", "pyuic5": "/usr/local/bin/pyuic5", "sip": "/usr/local/bin/sip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/colormap.
shpc-registry automated BioContainers addition for colormap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/colormap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/colormap:0.9.8--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/colormap/0.9.8--py36_0
$ module help quay.io/biocontainers/colormap/0.9.8--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### colormap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### colormap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### colormap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### colormap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### colormap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### colormap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### easydev_buildPackage

```bash
$ singularity exec <container> /usr/local/bin/easydev_buildPackage
$ podman run --it --rm --entrypoint /usr/local/bin/easydev_buildPackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easydev_buildPackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibrowse

```bash
$ singularity exec <container> /usr/local/bin/ibrowse
$ podman run --it --rm --entrypoint /usr/local/bin/ibrowse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibrowse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multigit

```bash
$ singularity exec <container> /usr/local/bin/multigit
$ podman run --it --rm --entrypoint /usr/local/bin/multigit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multigit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### browse

```bash
$ singularity exec <container> /usr/local/bin/browse
$ podman run --it --rm --entrypoint /usr/local/bin/browse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/browse   -v ${PWD} -w ${PWD} <container> -c " $@"
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