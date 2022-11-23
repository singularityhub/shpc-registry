---
layout: container
name:  "quay.io/biocontainers/multiz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/multiz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/multiz/container.yaml"
updated_at: "2022-11-23 00:47:43.354558"
latest: "11.2--hec16e2b_3"
container_url: "https://biocontainers.pro/tools/multiz"
aliases:
 - "all_bz"
 - "blastzWrapper"
 - "get_covered"
 - "get_standard_headers"
 - "lav2maf"
 - "maf2fasta"
 - "maf2lav"
 - "mafFind"
 - "maf_checkThread"
 - "maf_order"
 - "maf_project"
 - "maf_sort"
 - "multic"
 - "multiz"
 - "pair2tb"
 - "roast"
 - "single_cov2"
 - "tba"
versions:
 - "11.2--hec16e2b_3"
description: "shpc-registry automated BioContainers addition for multiz"
config: {"url": "https://biocontainers.pro/tools/multiz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for multiz", "latest": {"11.2--hec16e2b_3": "sha256:abc1b8e9323a83320bf967f869ad2c15cbcd14c0242e7952d866de3c949e8b69"}, "tags": {"11.2--hec16e2b_3": "sha256:abc1b8e9323a83320bf967f869ad2c15cbcd14c0242e7952d866de3c949e8b69"}, "docker": "quay.io/biocontainers/multiz", "aliases": {"all_bz": "/usr/local/bin/all_bz", "blastzWrapper": "/usr/local/bin/blastzWrapper", "get_covered": "/usr/local/bin/get_covered", "get_standard_headers": "/usr/local/bin/get_standard_headers", "lav2maf": "/usr/local/bin/lav2maf", "maf2fasta": "/usr/local/bin/maf2fasta", "maf2lav": "/usr/local/bin/maf2lav", "mafFind": "/usr/local/bin/mafFind", "maf_checkThread": "/usr/local/bin/maf_checkThread", "maf_order": "/usr/local/bin/maf_order", "maf_project": "/usr/local/bin/maf_project", "maf_sort": "/usr/local/bin/maf_sort", "multic": "/usr/local/bin/multic", "multiz": "/usr/local/bin/multiz", "pair2tb": "/usr/local/bin/pair2tb", "roast": "/usr/local/bin/roast", "single_cov2": "/usr/local/bin/single_cov2", "tba": "/usr/local/bin/tba"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/multiz.
shpc-registry automated BioContainers addition for multiz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/multiz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/multiz:11.2--hec16e2b_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/multiz/11.2--hec16e2b_3
$ module help quay.io/biocontainers/multiz/11.2--hec16e2b_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### multiz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### multiz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### multiz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### multiz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### multiz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### multiz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### all_bz

```bash
$ singularity exec <container> /usr/local/bin/all_bz
$ podman run --it --rm --entrypoint /usr/local/bin/all_bz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/all_bz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastzWrapper

```bash
$ singularity exec <container> /usr/local/bin/blastzWrapper
$ podman run --it --rm --entrypoint /usr/local/bin/blastzWrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastzWrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_covered

```bash
$ singularity exec <container> /usr/local/bin/get_covered
$ podman run --it --rm --entrypoint /usr/local/bin/get_covered   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_covered   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_standard_headers

```bash
$ singularity exec <container> /usr/local/bin/get_standard_headers
$ podman run --it --rm --entrypoint /usr/local/bin/get_standard_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_standard_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lav2maf

```bash
$ singularity exec <container> /usr/local/bin/lav2maf
$ podman run --it --rm --entrypoint /usr/local/bin/lav2maf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lav2maf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf2fasta

```bash
$ singularity exec <container> /usr/local/bin/maf2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/maf2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf2lav

```bash
$ singularity exec <container> /usr/local/bin/maf2lav
$ podman run --it --rm --entrypoint /usr/local/bin/maf2lav   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf2lav   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafFind

```bash
$ singularity exec <container> /usr/local/bin/mafFind
$ podman run --it --rm --entrypoint /usr/local/bin/mafFind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafFind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf_checkThread

```bash
$ singularity exec <container> /usr/local/bin/maf_checkThread
$ podman run --it --rm --entrypoint /usr/local/bin/maf_checkThread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf_checkThread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf_order

```bash
$ singularity exec <container> /usr/local/bin/maf_order
$ podman run --it --rm --entrypoint /usr/local/bin/maf_order   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf_order   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf_project

```bash
$ singularity exec <container> /usr/local/bin/maf_project
$ podman run --it --rm --entrypoint /usr/local/bin/maf_project   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf_project   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf_sort

```bash
$ singularity exec <container> /usr/local/bin/maf_sort
$ podman run --it --rm --entrypoint /usr/local/bin/maf_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multic

```bash
$ singularity exec <container> /usr/local/bin/multic
$ podman run --it --rm --entrypoint /usr/local/bin/multic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiz

```bash
$ singularity exec <container> /usr/local/bin/multiz
$ podman run --it --rm --entrypoint /usr/local/bin/multiz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pair2tb

```bash
$ singularity exec <container> /usr/local/bin/pair2tb
$ podman run --it --rm --entrypoint /usr/local/bin/pair2tb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pair2tb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roast

```bash
$ singularity exec <container> /usr/local/bin/roast
$ podman run --it --rm --entrypoint /usr/local/bin/roast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### single_cov2

```bash
$ singularity exec <container> /usr/local/bin/single_cov2
$ podman run --it --rm --entrypoint /usr/local/bin/single_cov2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/single_cov2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tba

```bash
$ singularity exec <container> /usr/local/bin/tba
$ podman run --it --rm --entrypoint /usr/local/bin/tba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tba   -v ${PWD} -w ${PWD} <container> -c " $@"
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