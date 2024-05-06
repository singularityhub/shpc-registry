---
layout: container
name:  "quay.io/biocontainers/mutscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mutscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mutscan/container.yaml"
updated_at: "2024-05-06 04:22:05.175291"
latest: "1.14.0--h43eeafb_4"
container_url: "https://biocontainers.pro/tools/mutscan"
aliases:
 - "mutscan"
versions:
 - "1.14.0--h5b5514e_2"
 - "1.14.0--h43eeafb_4"
description: "shpc-registry automated BioContainers addition for mutscan"
config: {"url": "https://biocontainers.pro/tools/mutscan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mutscan", "latest": {"1.14.0--h43eeafb_4": "sha256:6dc463ec1888dd98172ee37d1af038ceea0fc59593b5967e84952a4a00376013"}, "tags": {"1.14.0--h5b5514e_2": "sha256:4f31f7f329fb45c19bcb101897234c5d79d509843fb4001ec6f90132c0c65602", "1.14.0--h43eeafb_4": "sha256:6dc463ec1888dd98172ee37d1af038ceea0fc59593b5967e84952a4a00376013"}, "docker": "quay.io/biocontainers/mutscan", "aliases": {"mutscan": "/usr/local/bin/mutscan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mutscan.
shpc-registry automated BioContainers addition for mutscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mutscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mutscan:1.14.0--h43eeafb_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mutscan/1.14.0--h43eeafb_4
$ module help quay.io/biocontainers/mutscan/1.14.0--h43eeafb_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mutscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mutscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mutscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mutscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mutscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mutscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mutscan

```bash
$ singularity exec <container> /usr/local/bin/mutscan
$ podman run --it --rm --entrypoint /usr/local/bin/mutscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutscan   -v ${PWD} -w ${PWD} <container> -c " $@"
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