---
layout: container
name:  "quay.io/biocontainers/soapdenovo-trans"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/soapdenovo-trans/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/soapdenovo-trans/container.yaml"
updated_at: "2025-08-07 04:20:40.069743"
latest: "1.04--h577a1d6_7"
container_url: "https://biocontainers.pro/tools/soapdenovo-trans"
aliases:
 - "SOAPdenovo-Trans-127mer"
 - "SOAPdenovo-Trans-31mer"
versions:
 - "1.04--h7132678_5"
 - "1.04--he4a0461_6"
 - "1.04--h577a1d6_7"
description: "shpc-registry automated BioContainers addition for soapdenovo-trans"
config: {"url": "https://biocontainers.pro/tools/soapdenovo-trans", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for soapdenovo-trans", "latest": {"1.04--h577a1d6_7": "sha256:326b86aa7e65ff2bcc380e9dbb2597e1bddb06116dd2abf8125e13e8b75e571c"}, "tags": {"1.04--h7132678_5": "sha256:dc453fa932869384698ba29b5cbf4772da90d8516a311c5a6b8d1da939b8c042", "1.04--he4a0461_6": "sha256:cb0418465bfaf830cb338b4883f1b7ce334cf551988e28b3e16b29fe2a962144", "1.04--h577a1d6_7": "sha256:326b86aa7e65ff2bcc380e9dbb2597e1bddb06116dd2abf8125e13e8b75e571c"}, "docker": "quay.io/biocontainers/soapdenovo-trans", "aliases": {"SOAPdenovo-Trans-127mer": "/usr/local/bin/SOAPdenovo-Trans-127mer", "SOAPdenovo-Trans-31mer": "/usr/local/bin/SOAPdenovo-Trans-31mer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/soapdenovo-trans.
shpc-registry automated BioContainers addition for soapdenovo-trans
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/soapdenovo-trans
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/soapdenovo-trans:1.04--h577a1d6_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/soapdenovo-trans/1.04--h577a1d6_7
$ module help quay.io/biocontainers/soapdenovo-trans/1.04--h577a1d6_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### soapdenovo-trans-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo-trans-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo-trans-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### soapdenovo-trans-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### soapdenovo-trans-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### soapdenovo-trans-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SOAPdenovo-Trans-127mer

```bash
$ singularity exec <container> /usr/local/bin/SOAPdenovo-Trans-127mer
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPdenovo-Trans-127mer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPdenovo-Trans-127mer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPdenovo-Trans-31mer

```bash
$ singularity exec <container> /usr/local/bin/SOAPdenovo-Trans-31mer
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPdenovo-Trans-31mer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPdenovo-Trans-31mer   -v ${PWD} -w ${PWD} <container> -c " $@"
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