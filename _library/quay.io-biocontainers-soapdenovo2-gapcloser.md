---
layout: container
name:  "quay.io/biocontainers/soapdenovo2-gapcloser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/soapdenovo2-gapcloser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/soapdenovo2-gapcloser/container.yaml"
updated_at: "2024-06-11 05:12:52.466701"
latest: "1.12--he941832_2"
container_url: "https://biocontainers.pro/tools/soapdenovo2-gapcloser"
aliases:
 - "GapCloser"
versions:
 - "1.12--he941832_2"
description: "shpc-registry automated BioContainers addition for soapdenovo2-gapcloser"
config: {"url": "https://biocontainers.pro/tools/soapdenovo2-gapcloser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for soapdenovo2-gapcloser", "latest": {"1.12--he941832_2": "sha256:5da1369181a0ae7f0a2f40ed22f8ca5278eeda0e00565927f932bf3a7bf1604b"}, "tags": {"1.12--he941832_2": "sha256:5da1369181a0ae7f0a2f40ed22f8ca5278eeda0e00565927f932bf3a7bf1604b"}, "docker": "quay.io/biocontainers/soapdenovo2-gapcloser", "aliases": {"GapCloser": "/usr/local/bin/GapCloser"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/soapdenovo2-gapcloser.
shpc-registry automated BioContainers addition for soapdenovo2-gapcloser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/soapdenovo2-gapcloser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/soapdenovo2-gapcloser:1.12--he941832_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/soapdenovo2-gapcloser/1.12--he941832_2
$ module help quay.io/biocontainers/soapdenovo2-gapcloser/1.12--he941832_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### soapdenovo2-gapcloser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo2-gapcloser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo2-gapcloser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### soapdenovo2-gapcloser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### soapdenovo2-gapcloser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### soapdenovo2-gapcloser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GapCloser

```bash
$ singularity exec <container> /usr/local/bin/GapCloser
$ podman run --it --rm --entrypoint /usr/local/bin/GapCloser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GapCloser   -v ${PWD} -w ${PWD} <container> -c " $@"
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