---
layout: container
name:  "quay.io/biocontainers/metachip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metachip/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metachip/container.yaml"
updated_at: "2022-10-29 05:56:16.115439"
latest: "1.10.9--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/metachip"
aliases:
 - "MetaCHIP"
 - "2to3-3.8"
 - "FastTree"
 - "FastTree-2.1.10.c"
 - "FastTreeMP"
 - "accn-at-a-time"
 - "align-columns"
 - "alimask"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "aserver"
versions:
 - "1.10.9--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for metachip"
config: {"url": "https://biocontainers.pro/tools/metachip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metachip", "latest": {"1.10.9--pyh5e36f6f_0": "sha256:82cf7e556b9a4453582fcbcc366841436e3a9ebcfa7e72de87617995c83da413"}, "tags": {"1.10.9--pyh5e36f6f_0": "sha256:82cf7e556b9a4453582fcbcc366841436e3a9ebcfa7e72de87617995c83da413"}, "docker": "quay.io/biocontainers/metachip", "aliases": {"MetaCHIP": "/usr/local/bin/MetaCHIP", "2to3-3.8": "/usr/local/bin/2to3-3.8", "FastTree": "/usr/local/bin/FastTree", "FastTree-2.1.10.c": "/usr/local/bin/FastTree-2.1.10.c", "FastTreeMP": "/usr/local/bin/FastTreeMP", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "align-columns": "/usr/local/bin/align-columns", "alimask": "/usr/local/bin/alimask", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "aserver": "/usr/local/bin/aserver"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metachip.
shpc-registry automated BioContainers addition for metachip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metachip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metachip:1.10.9--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metachip/1.10.9--pyh5e36f6f_0
$ module help quay.io/biocontainers/metachip/1.10.9--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metachip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metachip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metachip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metachip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metachip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metachip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MetaCHIP

```bash
$ singularity exec <container> /usr/local/bin/MetaCHIP
$ podman run --it --rm --entrypoint /usr/local/bin/MetaCHIP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetaCHIP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree-2.1.10.c

```bash
$ singularity exec <container> /usr/local/bin/FastTree-2.1.10.c
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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