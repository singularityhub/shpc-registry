---
layout: container
name:  "quay.io/biocontainers/tmb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tmb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tmb/container.yaml"
updated_at: "2022-10-27 00:52:05.295984"
latest: "1.3.0--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/tmb"
aliases:
 - "pyEffGenomeSize.py"
 - "pyTMB.py"
versions:
 - "1.3.0--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for tmb"
config: {"url": "https://biocontainers.pro/tools/tmb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tmb", "latest": {"1.3.0--pyh5e36f6f_0": "sha256:74b5ab0c643003bafedf3d08ee465e1c8287aefbb274b284e8108fe4d0394cb3"}, "tags": {"1.3.0--pyh5e36f6f_0": "sha256:74b5ab0c643003bafedf3d08ee465e1c8287aefbb274b284e8108fe4d0394cb3"}, "docker": "quay.io/biocontainers/tmb", "aliases": {"pyEffGenomeSize.py": "/usr/local/bin/pyEffGenomeSize.py", "pyTMB.py": "/usr/local/bin/pyTMB.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tmb.
shpc-registry automated BioContainers addition for tmb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tmb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tmb:1.3.0--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tmb/1.3.0--pyh5e36f6f_0
$ module help quay.io/biocontainers/tmb/1.3.0--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tmb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tmb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tmb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tmb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tmb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tmb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyEffGenomeSize.py

```bash
$ singularity exec <container> /usr/local/bin/pyEffGenomeSize.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyEffGenomeSize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyEffGenomeSize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyTMB.py

```bash
$ singularity exec <container> /usr/local/bin/pyTMB.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyTMB.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyTMB.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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