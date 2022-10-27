---
layout: container
name:  "quay.io/biocontainers/samstats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samstats/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/samstats/container.yaml"
updated_at: "2022-10-27 00:30:29.835636"
latest: "0.2.2--py_0"
container_url: "https://biocontainers.pro/tools/samstats"
aliases:
 - "SAMstats"
 - "SAMstatsParallel"
versions:
 - "0.2.2--py_0"
description: "shpc-registry automated BioContainers addition for samstats"
config: {"url": "https://biocontainers.pro/tools/samstats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samstats", "latest": {"0.2.2--py_0": "sha256:cc397b097bcd1e7dd1f0f25348ca397c3919c71009b607fe13aa709dc3568e63"}, "tags": {"0.2.2--py_0": "sha256:cc397b097bcd1e7dd1f0f25348ca397c3919c71009b607fe13aa709dc3568e63"}, "docker": "quay.io/biocontainers/samstats", "aliases": {"SAMstats": "/usr/local/bin/SAMstats", "SAMstatsParallel": "/usr/local/bin/SAMstatsParallel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samstats.
shpc-registry automated BioContainers addition for samstats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samstats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samstats:0.2.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samstats/0.2.2--py_0
$ module help quay.io/biocontainers/samstats/0.2.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samstats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samstats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samstats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samstats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samstats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samstats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SAMstats

```bash
$ singularity exec <container> /usr/local/bin/SAMstats
$ podman run --it --rm --entrypoint /usr/local/bin/SAMstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAMstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAMstatsParallel

```bash
$ singularity exec <container> /usr/local/bin/SAMstatsParallel
$ podman run --it --rm --entrypoint /usr/local/bin/SAMstatsParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAMstatsParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
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