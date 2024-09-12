---
layout: container
name:  "quay.io/biocontainers/r-ggmsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ggmsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-ggmsa/container.yaml"
updated_at: "2024-09-12 02:58:11.523402"
latest: "1.0.2--r43h3121a25_3"
container_url: "https://biocontainers.pro/tools/r-ggmsa"
aliases:
 - "projsync"
 - "invgeod"
 - "invproj"
 - "projinfo"
 - "cct"
 - "gie"
 - "cs2cs"
 - "geod"
 - "proj"
versions:
 - "1.0.2--r41h3121a25_1"
 - "1.0.2--r42h3121a25_2"
 - "1.0.2--r43h3121a25_3"
description: "shpc-registry automated BioContainers addition for r-ggmsa"
config: {"url": "https://biocontainers.pro/tools/r-ggmsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ggmsa", "latest": {"1.0.2--r43h3121a25_3": "sha256:778ba6b2ecfc8a66069a9da4f15a55ead13dc5cf57e1581a7f37670bc83f02ce"}, "tags": {"1.0.2--r41h3121a25_1": "sha256:8318b4493108ec40b3afa091268689f770cb9747c80894e81eb98acb5bc6a98f", "1.0.2--r42h3121a25_2": "sha256:d16073153fd126d3799a4ef0a010bfa84de0baf2ccabde867ffe2d477161f925", "1.0.2--r43h3121a25_3": "sha256:778ba6b2ecfc8a66069a9da4f15a55ead13dc5cf57e1581a7f37670bc83f02ce"}, "docker": "quay.io/biocontainers/r-ggmsa", "aliases": {"projsync": "/usr/local/bin/projsync", "invgeod": "/usr/local/bin/invgeod", "invproj": "/usr/local/bin/invproj", "projinfo": "/usr/local/bin/projinfo", "cct": "/usr/local/bin/cct", "gie": "/usr/local/bin/gie", "cs2cs": "/usr/local/bin/cs2cs", "geod": "/usr/local/bin/geod", "proj": "/usr/local/bin/proj"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ggmsa.
shpc-registry automated BioContainers addition for r-ggmsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ggmsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ggmsa:1.0.2--r43h3121a25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ggmsa/1.0.2--r43h3121a25_3
$ module help quay.io/biocontainers/r-ggmsa/1.0.2--r43h3121a25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ggmsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ggmsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ggmsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ggmsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ggmsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ggmsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### projsync

```bash
$ singularity exec <container> /usr/local/bin/projsync
$ podman run --it --rm --entrypoint /usr/local/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invgeod

```bash
$ singularity exec <container> /usr/local/bin/invgeod
$ podman run --it --rm --entrypoint /usr/local/bin/invgeod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invgeod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invproj

```bash
$ singularity exec <container> /usr/local/bin/invproj
$ podman run --it --rm --entrypoint /usr/local/bin/invproj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invproj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### projinfo

```bash
$ singularity exec <container> /usr/local/bin/projinfo
$ podman run --it --rm --entrypoint /usr/local/bin/projinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/projinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cct

```bash
$ singularity exec <container> /usr/local/bin/cct
$ podman run --it --rm --entrypoint /usr/local/bin/cct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gie

```bash
$ singularity exec <container> /usr/local/bin/gie
$ podman run --it --rm --entrypoint /usr/local/bin/gie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cs2cs

```bash
$ singularity exec <container> /usr/local/bin/cs2cs
$ podman run --it --rm --entrypoint /usr/local/bin/cs2cs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cs2cs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geod

```bash
$ singularity exec <container> /usr/local/bin/geod
$ podman run --it --rm --entrypoint /usr/local/bin/geod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proj

```bash
$ singularity exec <container> /usr/local/bin/proj
$ podman run --it --rm --entrypoint /usr/local/bin/proj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proj   -v ${PWD} -w ${PWD} <container> -c " $@"
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