---
layout: container
name:  "quay.io/biocontainers/sixgill"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sixgill/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sixgill/container.yaml"
updated_at: "2022-10-27 01:09:51.179618"
latest: "0.2.4--py_3"
container_url: "https://biocontainers.pro/tools/sixgill"
aliases:
 - "sixgill_build"
 - "sixgill_filter"
 - "sixgill_makefasta"
 - "sixgill_merge"
versions:
 - "0.2.4--py_3"
description: "shpc-registry automated BioContainers addition for sixgill"
config: {"url": "https://biocontainers.pro/tools/sixgill", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sixgill", "latest": {"0.2.4--py_3": "sha256:c4ff3e41f2af17e3a2ac0e540c3438950a62a7f5cf48b5ffa16abd3377b17007"}, "tags": {"0.2.4--py_3": "sha256:c4ff3e41f2af17e3a2ac0e540c3438950a62a7f5cf48b5ffa16abd3377b17007"}, "docker": "quay.io/biocontainers/sixgill", "aliases": {"sixgill_build": "/usr/local/bin/sixgill_build", "sixgill_filter": "/usr/local/bin/sixgill_filter", "sixgill_makefasta": "/usr/local/bin/sixgill_makefasta", "sixgill_merge": "/usr/local/bin/sixgill_merge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sixgill.
shpc-registry automated BioContainers addition for sixgill
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sixgill
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sixgill:0.2.4--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sixgill/0.2.4--py_3
$ module help quay.io/biocontainers/sixgill/0.2.4--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sixgill-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sixgill-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sixgill-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sixgill-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sixgill-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sixgill-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sixgill_build

```bash
$ singularity exec <container> /usr/local/bin/sixgill_build
$ podman run --it --rm --entrypoint /usr/local/bin/sixgill_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sixgill_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sixgill_filter

```bash
$ singularity exec <container> /usr/local/bin/sixgill_filter
$ podman run --it --rm --entrypoint /usr/local/bin/sixgill_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sixgill_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sixgill_makefasta

```bash
$ singularity exec <container> /usr/local/bin/sixgill_makefasta
$ podman run --it --rm --entrypoint /usr/local/bin/sixgill_makefasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sixgill_makefasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sixgill_merge

```bash
$ singularity exec <container> /usr/local/bin/sixgill_merge
$ podman run --it --rm --entrypoint /usr/local/bin/sixgill_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sixgill_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
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