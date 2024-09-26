---
layout: container
name:  "quay.io/biocontainers/poa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/poa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/poa/container.yaml"
updated_at: "2024-09-26 10:40:07.906929"
latest: "2.0--h031d066_5"
container_url: "https://biocontainers.pro/tools/poa"
aliases:
 - "make_pscores.pl"
 - "poa"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
 - "fastacmd"
 - "formatdb"
 - "formatrpsdb"
 - "impala"
 - "makemat"
versions:
 - "2.0--hec16e2b_4"
 - "2.0--h031d066_5"
description: "shpc-registry automated BioContainers addition for poa"
config: {"url": "https://biocontainers.pro/tools/poa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for poa", "latest": {"2.0--h031d066_5": "sha256:05c85e531ab68c0477693a3f8d6c6d03abb7de5e84d51dbfa6fe20b503e47316"}, "tags": {"2.0--hec16e2b_4": "sha256:2311720a9b49e750d7bb220659e5850edb5f1fb06b56a5375b0ecb477368e01f", "2.0--h031d066_5": "sha256:05c85e531ab68c0477693a3f8d6c6d03abb7de5e84d51dbfa6fe20b503e47316"}, "docker": "quay.io/biocontainers/poa", "aliases": {"make_pscores.pl": "/usr/local/bin/make_pscores.pl", "poa": "/usr/local/bin/poa", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat", "fastacmd": "/usr/local/bin/fastacmd", "formatdb": "/usr/local/bin/formatdb", "formatrpsdb": "/usr/local/bin/formatrpsdb", "impala": "/usr/local/bin/impala", "makemat": "/usr/local/bin/makemat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/poa.
shpc-registry automated BioContainers addition for poa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/poa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/poa:2.0--h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/poa/2.0--h031d066_5
$ module help quay.io/biocontainers/poa/2.0--h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### poa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### poa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### poa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### poa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### poa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### poa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### make_pscores.pl

```bash
$ singularity exec <container> /usr/local/bin/make_pscores.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poa

```bash
$ singularity exec <container> /usr/local/bin/poa
$ podman run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacmd

```bash
$ singularity exec <container> /usr/local/bin/fastacmd
$ podman run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatdb

```bash
$ singularity exec <container> /usr/local/bin/formatdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatrpsdb

```bash
$ singularity exec <container> /usr/local/bin/formatrpsdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impala

```bash
$ singularity exec <container> /usr/local/bin/impala
$ podman run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makemat

```bash
$ singularity exec <container> /usr/local/bin/makemat
$ podman run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
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