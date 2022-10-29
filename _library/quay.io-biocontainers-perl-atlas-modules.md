---
layout: container
name:  "quay.io/biocontainers/perl-atlas-modules"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-atlas-modules/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-atlas-modules/container.yaml"
updated_at: "2022-10-29 05:39:54.661745"
latest: "0.3.1--pl5262h87f3376_3"
container_url: "https://biocontainers.pro/tools/perl-atlas-modules"
aliases:
 - "crc32"
 - "dm_date"
 - "dm_zdump"
 - "validjson"
 - "2to3-3.10"
 - "acyclic"
 - "annotate"
 - "bcomps"
 - "bdftogd"
 - "ccomps"
 - "circo"
 - "cluster"
 - "clusterdb"
 - "config_data"
versions:
 - "0.3.1--pl5262h87f3376_3"
description: "shpc-registry automated BioContainers addition for perl-atlas-modules"
config: {"url": "https://biocontainers.pro/tools/perl-atlas-modules", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-atlas-modules", "latest": {"0.3.1--pl5262h87f3376_3": "sha256:36423ff98bcd6b1ee25252f3fc42c7d2312cbadc8629ecd5045120ac1eceb5de"}, "tags": {"0.3.1--pl5262h87f3376_3": "sha256:36423ff98bcd6b1ee25252f3fc42c7d2312cbadc8629ecd5045120ac1eceb5de"}, "docker": "quay.io/biocontainers/perl-atlas-modules", "aliases": {"crc32": "/usr/local/bin/crc32", "dm_date": "/usr/local/bin/dm_date", "dm_zdump": "/usr/local/bin/dm_zdump", "validjson": "/usr/local/bin/validjson", "2to3-3.10": "/usr/local/bin/2to3-3.10", "acyclic": "/usr/local/bin/acyclic", "annotate": "/usr/local/bin/annotate", "bcomps": "/usr/local/bin/bcomps", "bdftogd": "/usr/local/bin/bdftogd", "ccomps": "/usr/local/bin/ccomps", "circo": "/usr/local/bin/circo", "cluster": "/usr/local/bin/cluster", "clusterdb": "/usr/local/bin/clusterdb", "config_data": "/usr/local/bin/config_data"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-atlas-modules.
shpc-registry automated BioContainers addition for perl-atlas-modules
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-atlas-modules
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-atlas-modules:0.3.1--pl5262h87f3376_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-atlas-modules/0.3.1--pl5262h87f3376_3
$ module help quay.io/biocontainers/perl-atlas-modules/0.3.1--pl5262h87f3376_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-atlas-modules-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-atlas-modules-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-atlas-modules-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-atlas-modules-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-atlas-modules-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-atlas-modules-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crc32

```bash
$ singularity exec <container> /usr/local/bin/crc32
$ podman run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dm_date

```bash
$ singularity exec <container> /usr/local/bin/dm_date
$ podman run --it --rm --entrypoint /usr/local/bin/dm_date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dm_date   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dm_zdump

```bash
$ singularity exec <container> /usr/local/bin/dm_zdump
$ podman run --it --rm --entrypoint /usr/local/bin/dm_zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dm_zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validjson

```bash
$ singularity exec <container> /usr/local/bin/validjson
$ podman run --it --rm --entrypoint /usr/local/bin/validjson   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validjson   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccomps

```bash
$ singularity exec <container> /usr/local/bin/ccomps
$ podman run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circo

```bash
$ singularity exec <container> /usr/local/bin/circo
$ podman run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster

```bash
$ singularity exec <container> /usr/local/bin/cluster
$ podman run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterdb

```bash
$ singularity exec <container> /usr/local/bin/clusterdb
$ podman run --it --rm --entrypoint /usr/local/bin/clusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config_data

```bash
$ singularity exec <container> /usr/local/bin/config_data
$ podman run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
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