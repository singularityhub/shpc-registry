---
layout: container
name:  "quay.io/biocontainers/cansam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cansam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cansam/container.yaml"
updated_at: "2023-10-16 02:34:26.649127"
latest: "21d64bb--h21ec9f0_7"
container_url: "https://biocontainers.pro/tools/cansam"
aliases:
 - "samcat"
 - "samcount"
 - "samgroupbyname"
 - "samhead"
 - "samsort"
 - "samsplit"
versions:
 - "21d64bb--h7ff8a90_5"
 - "21d64bb--h7ff8a90_6"
 - "21d64bb--h21ec9f0_7"
description: "shpc-registry automated BioContainers addition for cansam"
config: {"url": "https://biocontainers.pro/tools/cansam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cansam", "latest": {"21d64bb--h21ec9f0_7": "sha256:b8a9e02eb067d9ae12824d4595394207134563587b9fa5352ee07d2838854094"}, "tags": {"21d64bb--h7ff8a90_5": "sha256:246cc80e1455e0681994be5e15b285f58350fd78774b6ad952cb3c0ab800a940", "21d64bb--h7ff8a90_6": "sha256:fddfb6d7013f696b5aa41197e202388c1dc04b3b4e15b0df6d6027f002ad5592", "21d64bb--h21ec9f0_7": "sha256:b8a9e02eb067d9ae12824d4595394207134563587b9fa5352ee07d2838854094"}, "docker": "quay.io/biocontainers/cansam", "aliases": {"samcat": "/usr/local/bin/samcat", "samcount": "/usr/local/bin/samcount", "samgroupbyname": "/usr/local/bin/samgroupbyname", "samhead": "/usr/local/bin/samhead", "samsort": "/usr/local/bin/samsort", "samsplit": "/usr/local/bin/samsplit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cansam.
shpc-registry automated BioContainers addition for cansam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cansam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cansam:21d64bb--h21ec9f0_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cansam/21d64bb--h21ec9f0_7
$ module help quay.io/biocontainers/cansam/21d64bb--h21ec9f0_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cansam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cansam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cansam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cansam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cansam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cansam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### samcat

```bash
$ singularity exec <container> /usr/local/bin/samcat
$ podman run --it --rm --entrypoint /usr/local/bin/samcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samcount

```bash
$ singularity exec <container> /usr/local/bin/samcount
$ podman run --it --rm --entrypoint /usr/local/bin/samcount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samcount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samgroupbyname

```bash
$ singularity exec <container> /usr/local/bin/samgroupbyname
$ podman run --it --rm --entrypoint /usr/local/bin/samgroupbyname   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samgroupbyname   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samhead

```bash
$ singularity exec <container> /usr/local/bin/samhead
$ podman run --it --rm --entrypoint /usr/local/bin/samhead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samhead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samsort

```bash
$ singularity exec <container> /usr/local/bin/samsort
$ podman run --it --rm --entrypoint /usr/local/bin/samsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samsplit

```bash
$ singularity exec <container> /usr/local/bin/samsplit
$ podman run --it --rm --entrypoint /usr/local/bin/samsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
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