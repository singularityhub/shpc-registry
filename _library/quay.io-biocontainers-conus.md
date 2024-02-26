---
layout: container
name:  "quay.io/biocontainers/conus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/conus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/conus/container.yaml"
updated_at: "2024-02-26 03:07:06.900594"
latest: "1.0--h031d066_5"
container_url: "https://biocontainers.pro/tools/conus"
aliases:
 - "ambtest"
 - "conus_compare"
 - "conus_fold"
 - "conus_train"
 - "findopt"
 - "pocheck"
 - "reorder"
 - "scheck"
 - "stk2ct"
 - "weedamb"
versions:
 - "1.0--hec16e2b_3"
 - "1.0--hec16e2b_4"
 - "1.0--h031d066_5"
description: "shpc-registry automated BioContainers addition for conus"
config: {"url": "https://biocontainers.pro/tools/conus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for conus", "latest": {"1.0--h031d066_5": "sha256:6cb51319c4f8945d17763f5fccec058473c7cf7e836379b11a28df777014f190"}, "tags": {"1.0--hec16e2b_3": "sha256:023454dfb3eff56eba8120e57ad9676f43db6a540a8256a1790f430c3bd35901", "1.0--hec16e2b_4": "sha256:97d5be833eb1f96ab3f952a8947c9004759417bb47c2565db17d99a7a4ae16e7", "1.0--h031d066_5": "sha256:6cb51319c4f8945d17763f5fccec058473c7cf7e836379b11a28df777014f190"}, "docker": "quay.io/biocontainers/conus", "aliases": {"ambtest": "/usr/local/bin/ambtest", "conus_compare": "/usr/local/bin/conus_compare", "conus_fold": "/usr/local/bin/conus_fold", "conus_train": "/usr/local/bin/conus_train", "findopt": "/usr/local/bin/findopt", "pocheck": "/usr/local/bin/pocheck", "reorder": "/usr/local/bin/reorder", "scheck": "/usr/local/bin/scheck", "stk2ct": "/usr/local/bin/stk2ct", "weedamb": "/usr/local/bin/weedamb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/conus.
shpc-registry automated BioContainers addition for conus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/conus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/conus:1.0--h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/conus/1.0--h031d066_5
$ module help quay.io/biocontainers/conus/1.0--h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### conus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### conus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### conus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### conus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### conus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### conus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ambtest

```bash
$ singularity exec <container> /usr/local/bin/ambtest
$ podman run --it --rm --entrypoint /usr/local/bin/ambtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ambtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conus_compare

```bash
$ singularity exec <container> /usr/local/bin/conus_compare
$ podman run --it --rm --entrypoint /usr/local/bin/conus_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conus_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conus_fold

```bash
$ singularity exec <container> /usr/local/bin/conus_fold
$ podman run --it --rm --entrypoint /usr/local/bin/conus_fold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conus_fold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conus_train

```bash
$ singularity exec <container> /usr/local/bin/conus_train
$ podman run --it --rm --entrypoint /usr/local/bin/conus_train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conus_train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findopt

```bash
$ singularity exec <container> /usr/local/bin/findopt
$ podman run --it --rm --entrypoint /usr/local/bin/findopt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findopt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pocheck

```bash
$ singularity exec <container> /usr/local/bin/pocheck
$ podman run --it --rm --entrypoint /usr/local/bin/pocheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pocheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reorder

```bash
$ singularity exec <container> /usr/local/bin/reorder
$ podman run --it --rm --entrypoint /usr/local/bin/reorder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reorder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scheck

```bash
$ singularity exec <container> /usr/local/bin/scheck
$ podman run --it --rm --entrypoint /usr/local/bin/scheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stk2ct

```bash
$ singularity exec <container> /usr/local/bin/stk2ct
$ podman run --it --rm --entrypoint /usr/local/bin/stk2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stk2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weedamb

```bash
$ singularity exec <container> /usr/local/bin/weedamb
$ podman run --it --rm --entrypoint /usr/local/bin/weedamb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weedamb   -v ${PWD} -w ${PWD} <container> -c " $@"
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