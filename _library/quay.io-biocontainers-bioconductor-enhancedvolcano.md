---
layout: container
name:  "quay.io/biocontainers/bioconductor-enhancedvolcano"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-enhancedvolcano/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-enhancedvolcano/container.yaml"
updated_at: "2023-03-20 03:02:24.136461"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-enhancedvolcano"
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
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-enhancedvolcano"
config: {"url": "https://biocontainers.pro/tools/bioconductor-enhancedvolcano", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-enhancedvolcano", "latest": {"1.16.0--r42hdfd78af_0": "sha256:b1c792bbf29813bc0f3a747511efc059a55f5371fd8c8b8df4160458db1f33de"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:ee6850f58a53822b67fafab3464b0dd1c77e1edec8cdaa5056e06be300613ba5", "1.16.0--r42hdfd78af_0": "sha256:b1c792bbf29813bc0f3a747511efc059a55f5371fd8c8b8df4160458db1f33de", "1.12.0--r41hdfd78af_0": "sha256:fd14ea02afbe0ecb29a79e2ad73c3c3781898fdd5323e53280fd66495d6d0927", "1.10.0--r41hdfd78af_0": "sha256:111f783780e05ce24579b324932b9f92ef02af978814636f221c13eebdb2d93f"}, "docker": "quay.io/biocontainers/bioconductor-enhancedvolcano", "aliases": {"projsync": "/usr/local/bin/projsync", "invgeod": "/usr/local/bin/invgeod", "invproj": "/usr/local/bin/invproj", "projinfo": "/usr/local/bin/projinfo", "cct": "/usr/local/bin/cct", "gie": "/usr/local/bin/gie", "cs2cs": "/usr/local/bin/cs2cs", "geod": "/usr/local/bin/geod", "proj": "/usr/local/bin/proj", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-enhancedvolcano.
shpc-registry automated BioContainers addition for bioconductor-enhancedvolcano
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-enhancedvolcano
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-enhancedvolcano:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-enhancedvolcano/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-enhancedvolcano/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-enhancedvolcano-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enhancedvolcano-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enhancedvolcano-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-enhancedvolcano-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-enhancedvolcano-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-enhancedvolcano-inspect-deffile:

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


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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