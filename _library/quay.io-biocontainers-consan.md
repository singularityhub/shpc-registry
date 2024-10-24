---
layout: container
name:  "quay.io/biocontainers/consan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/consan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/consan/container.yaml"
updated_at: "2024-10-24 11:05:57.052773"
latest: "1.2--h031d066_5"
container_url: "https://biocontainers.pro/tools/consan"
aliases:
 - "bstats"
 - "comppair"
 - "conus_compare"
 - "conus_train"
 - "pModel"
 - "scompare"
 - "sfold"
 - "strain_ml"
versions:
 - "1.2--hec16e2b_3"
 - "1.2--h031d066_5"
description: "shpc-registry automated BioContainers addition for consan"
config: {"url": "https://biocontainers.pro/tools/consan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for consan", "latest": {"1.2--h031d066_5": "sha256:0d0d6a06a7028b2749737530591b4b280ba1ead1611b216dbbdc8570ea40fdec"}, "tags": {"1.2--hec16e2b_3": "sha256:80ccd27c6c491b5ca514c48296a1f5523a60a5d43d9032d9c4c7402424fe6045", "1.2--h031d066_5": "sha256:0d0d6a06a7028b2749737530591b4b280ba1ead1611b216dbbdc8570ea40fdec"}, "docker": "quay.io/biocontainers/consan", "aliases": {"bstats": "/usr/local/bin/bstats", "comppair": "/usr/local/bin/comppair", "conus_compare": "/usr/local/bin/conus_compare", "conus_train": "/usr/local/bin/conus_train", "pModel": "/usr/local/bin/pModel", "scompare": "/usr/local/bin/scompare", "sfold": "/usr/local/bin/sfold", "strain_ml": "/usr/local/bin/strain_ml"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/consan.
shpc-registry automated BioContainers addition for consan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/consan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/consan:1.2--h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/consan/1.2--h031d066_5
$ module help quay.io/biocontainers/consan/1.2--h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### consan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### consan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### consan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### consan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### consan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### consan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bstats

```bash
$ singularity exec <container> /usr/local/bin/bstats
$ podman run --it --rm --entrypoint /usr/local/bin/bstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comppair

```bash
$ singularity exec <container> /usr/local/bin/comppair
$ podman run --it --rm --entrypoint /usr/local/bin/comppair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comppair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conus_compare

```bash
$ singularity exec <container> /usr/local/bin/conus_compare
$ podman run --it --rm --entrypoint /usr/local/bin/conus_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conus_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conus_train

```bash
$ singularity exec <container> /usr/local/bin/conus_train
$ podman run --it --rm --entrypoint /usr/local/bin/conus_train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conus_train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pModel

```bash
$ singularity exec <container> /usr/local/bin/pModel
$ podman run --it --rm --entrypoint /usr/local/bin/pModel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pModel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scompare

```bash
$ singularity exec <container> /usr/local/bin/scompare
$ podman run --it --rm --entrypoint /usr/local/bin/scompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfold

```bash
$ singularity exec <container> /usr/local/bin/sfold
$ podman run --it --rm --entrypoint /usr/local/bin/sfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strain_ml

```bash
$ singularity exec <container> /usr/local/bin/strain_ml
$ podman run --it --rm --entrypoint /usr/local/bin/strain_ml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strain_ml   -v ${PWD} -w ${PWD} <container> -c " $@"
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