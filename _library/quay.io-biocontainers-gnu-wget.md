---
layout: container
name:  "quay.io/biocontainers/gnu-wget"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gnu-wget/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gnu-wget/container.yaml"
updated_at: "2025-04-06 03:12:49.783607"
latest: "1.18--hb829ee6_10"
container_url: "https://biocontainers.pro/tools/gnu-wget"
aliases:
 - "idn2"
 - "wget"
versions:
 - "1.18--h60da905_7"
 - "1.18--h36e9172_9"
 - "1.18--hb829ee6_10"
description: "shpc-registry automated BioContainers addition for gnu-wget"
config: {"url": "https://biocontainers.pro/tools/gnu-wget", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gnu-wget", "latest": {"1.18--hb829ee6_10": "sha256:7b5420aa13becd719943c8cc3a8d3913b28483fc9524706d86648dc9ac3cbd98"}, "tags": {"1.18--h60da905_7": "sha256:578b143b3a2a7377605f726d49336b32617ec6d010f19bb39a885a156617d9ab", "1.18--h36e9172_9": "sha256:a7253d598eb7aa4a826f56b5da6079f1176d2c8cad584ee1a6c06f9f9b25d8b0", "1.18--hb829ee6_10": "sha256:7b5420aa13becd719943c8cc3a8d3913b28483fc9524706d86648dc9ac3cbd98"}, "docker": "quay.io/biocontainers/gnu-wget", "aliases": {"idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gnu-wget.
shpc-registry automated BioContainers addition for gnu-wget
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gnu-wget
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gnu-wget:1.18--hb829ee6_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gnu-wget/1.18--hb829ee6_10
$ module help quay.io/biocontainers/gnu-wget/1.18--hb829ee6_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gnu-wget-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gnu-wget-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gnu-wget-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gnu-wget-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gnu-wget-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gnu-wget-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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