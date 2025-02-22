---
layout: container
name:  "quay.io/biocontainers/purge_dups"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/purge_dups/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/purge_dups/container.yaml"
updated_at: "2025-02-22 03:13:21.066826"
latest: "1.2.6--h577a1d6_2"
container_url: "https://biocontainers.pro/tools/purge_dups"
aliases:
 - "calcuts"
 - "get_seqs"
 - "ngscstat"
 - "pbcstat"
 - "purge_dups"
 - "split_fa"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
versions:
 - "1.2.6--h7132678_0"
 - "1.2.6--py39h7132678_1"
 - "1.2.6--h577a1d6_2"
description: "shpc-registry automated BioContainers addition for purge_dups"
config: {"url": "https://biocontainers.pro/tools/purge_dups", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for purge_dups", "latest": {"1.2.6--h577a1d6_2": "sha256:40300568fa354a3209435f402f75761c3cee39a8529fd761ed33fd67ff06abb8"}, "tags": {"1.2.6--h7132678_0": "sha256:37b9aa9084c2486c98159830170a94a403e07c1a7760d45bbe2c4b4c3edb3696", "1.2.6--py39h7132678_1": "sha256:52094ca5831f19e9b410949bce3ce7c410bd9fd21cd4392e22ca68cf9b708ab4", "1.2.6--h577a1d6_2": "sha256:40300568fa354a3209435f402f75761c3cee39a8529fd761ed33fd67ff06abb8"}, "docker": "quay.io/biocontainers/purge_dups", "aliases": {"calcuts": "/usr/local/bin/calcuts", "get_seqs": "/usr/local/bin/get_seqs", "ngscstat": "/usr/local/bin/ngscstat", "pbcstat": "/usr/local/bin/pbcstat", "purge_dups": "/usr/local/bin/purge_dups", "split_fa": "/usr/local/bin/split_fa", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/purge_dups.
shpc-registry automated BioContainers addition for purge_dups
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/purge_dups
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/purge_dups:1.2.6--h577a1d6_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/purge_dups/1.2.6--h577a1d6_2
$ module help quay.io/biocontainers/purge_dups/1.2.6--h577a1d6_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### purge_dups-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### purge_dups-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### purge_dups-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### purge_dups-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### purge_dups-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### purge_dups-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### calcuts

```bash
$ singularity exec <container> /usr/local/bin/calcuts
$ podman run --it --rm --entrypoint /usr/local/bin/calcuts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calcuts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_seqs

```bash
$ singularity exec <container> /usr/local/bin/get_seqs
$ podman run --it --rm --entrypoint /usr/local/bin/get_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngscstat

```bash
$ singularity exec <container> /usr/local/bin/ngscstat
$ podman run --it --rm --entrypoint /usr/local/bin/ngscstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngscstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbcstat

```bash
$ singularity exec <container> /usr/local/bin/pbcstat
$ podman run --it --rm --entrypoint /usr/local/bin/pbcstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbcstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### purge_dups

```bash
$ singularity exec <container> /usr/local/bin/purge_dups
$ podman run --it --rm --entrypoint /usr/local/bin/purge_dups   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/purge_dups   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_fa

```bash
$ singularity exec <container> /usr/local/bin/split_fa
$ podman run --it --rm --entrypoint /usr/local/bin/split_fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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