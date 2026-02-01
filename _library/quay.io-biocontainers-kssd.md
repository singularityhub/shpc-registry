---
layout: container
name:  "quay.io/biocontainers/kssd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kssd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kssd/container.yaml"
updated_at: "2026-02-01 04:38:07.896844"
latest: "2.21--h577a1d6_3"
container_url: "https://biocontainers.pro/tools/kssd"
aliases:
 - "kssd"
versions:
 - "2.21--h7132678_0"
 - "2.21--h7132678_1"
 - "2.21--he4a0461_2"
 - "2.21--h577a1d6_3"
description: "shpc-registry automated BioContainers addition for kssd"
config: {"url": "https://biocontainers.pro/tools/kssd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kssd", "latest": {"2.21--h577a1d6_3": "sha256:59bc0e0b1011ec4b1c6932225e9503693ff542d279f8cdd6d2bc5d83f9d412a4"}, "tags": {"2.21--h7132678_0": "sha256:0689f82346b3e9c007f48baa8d1dfa0558b01ff66d26e09dc0693032ae608f16", "2.21--h7132678_1": "sha256:2f1c6d168303359e09d69149b9546519277b4c48b97653f20896b251db4ef7a1", "2.21--he4a0461_2": "sha256:dd1d9f16ac714ef3e395cca68fdcb5112d354e6c1a9a5a4a80c41686e8556853", "2.21--h577a1d6_3": "sha256:59bc0e0b1011ec4b1c6932225e9503693ff542d279f8cdd6d2bc5d83f9d412a4"}, "docker": "quay.io/biocontainers/kssd", "aliases": {"kssd": "/usr/local/bin/kssd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kssd.
shpc-registry automated BioContainers addition for kssd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kssd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kssd:2.21--h577a1d6_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kssd/2.21--h577a1d6_3
$ module help quay.io/biocontainers/kssd/2.21--h577a1d6_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kssd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kssd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kssd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kssd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kssd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kssd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kssd

```bash
$ singularity exec <container> /usr/local/bin/kssd
$ podman run --it --rm --entrypoint /usr/local/bin/kssd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kssd   -v ${PWD} -w ${PWD} <container> -c " $@"
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