---
layout: container
name:  "quay.io/biocontainers/gembs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gembs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gembs/container.yaml"
updated_at: "2022-10-27 00:34:48.548196"
latest: "3.5.5_IHEC--py310h125d12e_5"
container_url: "https://biocontainers.pro/tools/gembs"
aliases:
 - "bs_call"
 - "dbSNP_idx"
 - "gem-indexer"
 - "gem-mapper"
 - "gem-retriever"
 - "gemBS"
versions:
 - "3.5.5_IHEC--py310h125d12e_5"
description: "shpc-registry automated BioContainers addition for gembs"
config: {"url": "https://biocontainers.pro/tools/gembs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gembs", "latest": {"3.5.5_IHEC--py310h125d12e_5": "sha256:01005849bd3135f29d0ef6186cbad00314f0d8bcea39d5ecdc651f6886e31299"}, "tags": {"3.5.5_IHEC--py310h125d12e_5": "sha256:01005849bd3135f29d0ef6186cbad00314f0d8bcea39d5ecdc651f6886e31299"}, "docker": "quay.io/biocontainers/gembs", "aliases": {"bs_call": "/usr/local/bin/bs_call", "dbSNP_idx": "/usr/local/bin/dbSNP_idx", "gem-indexer": "/usr/local/bin/gem-indexer", "gem-mapper": "/usr/local/bin/gem-mapper", "gem-retriever": "/usr/local/bin/gem-retriever", "gemBS": "/usr/local/bin/gemBS"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gembs.
shpc-registry automated BioContainers addition for gembs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gembs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gembs:3.5.5_IHEC--py310h125d12e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gembs/3.5.5_IHEC--py310h125d12e_5
$ module help quay.io/biocontainers/gembs/3.5.5_IHEC--py310h125d12e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gembs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gembs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gembs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gembs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gembs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gembs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bs_call

```bash
$ singularity exec <container> /usr/local/bin/bs_call
$ podman run --it --rm --entrypoint /usr/local/bin/bs_call   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bs_call   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbSNP_idx

```bash
$ singularity exec <container> /usr/local/bin/dbSNP_idx
$ podman run --it --rm --entrypoint /usr/local/bin/dbSNP_idx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbSNP_idx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem-indexer

```bash
$ singularity exec <container> /usr/local/bin/gem-indexer
$ podman run --it --rm --entrypoint /usr/local/bin/gem-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem-mapper

```bash
$ singularity exec <container> /usr/local/bin/gem-mapper
$ podman run --it --rm --entrypoint /usr/local/bin/gem-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem-retriever

```bash
$ singularity exec <container> /usr/local/bin/gem-retriever
$ podman run --it --rm --entrypoint /usr/local/bin/gem-retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gemBS

```bash
$ singularity exec <container> /usr/local/bin/gemBS
$ podman run --it --rm --entrypoint /usr/local/bin/gemBS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gemBS   -v ${PWD} -w ${PWD} <container> -c " $@"
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