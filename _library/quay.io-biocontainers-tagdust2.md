---
layout: container
name:  "quay.io/biocontainers/tagdust2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tagdust2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tagdust2/container.yaml"
updated_at: "2026-01-03 03:40:55.361567"
latest: "2.33.1--h503566f_0"
container_url: "https://biocontainers.pro/tools/tagdust2"
aliases:
 - "evalres"
 - "merge"
 - "rename_qiime"
 - "simreads"
 - "tagdust"
versions:
 - "2.33.1--h503566f_0"
description: "singularity registry hpc automated addition for tagdust2"
config: {"url": "https://biocontainers.pro/tools/tagdust2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tagdust2", "latest": {"2.33.1--h503566f_0": "sha256:ec917d64096166ef79c397ffea1ace92c481db0a64808aef5553d59eebc75f46"}, "tags": {"2.33.1--h503566f_0": "sha256:ec917d64096166ef79c397ffea1ace92c481db0a64808aef5553d59eebc75f46"}, "docker": "quay.io/biocontainers/tagdust2", "aliases": {"evalres": "/usr/local/bin/evalres", "merge": "/usr/local/bin/merge", "rename_qiime": "/usr/local/bin/rename_qiime", "simreads": "/usr/local/bin/simreads", "tagdust": "/usr/local/bin/tagdust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tagdust2.
singularity registry hpc automated addition for tagdust2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tagdust2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tagdust2:2.33.1--h503566f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tagdust2/2.33.1--h503566f_0
$ module help quay.io/biocontainers/tagdust2/2.33.1--h503566f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tagdust2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tagdust2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tagdust2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tagdust2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tagdust2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tagdust2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### evalres

```bash
$ singularity exec <container> /usr/local/bin/evalres
$ podman run --it --rm --entrypoint /usr/local/bin/evalres   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evalres   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge

```bash
$ singularity exec <container> /usr/local/bin/merge
$ podman run --it --rm --entrypoint /usr/local/bin/merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_qiime

```bash
$ singularity exec <container> /usr/local/bin/rename_qiime
$ podman run --it --rm --entrypoint /usr/local/bin/rename_qiime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_qiime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simreads

```bash
$ singularity exec <container> /usr/local/bin/simreads
$ podman run --it --rm --entrypoint /usr/local/bin/simreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tagdust

```bash
$ singularity exec <container> /usr/local/bin/tagdust
$ podman run --it --rm --entrypoint /usr/local/bin/tagdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tagdust   -v ${PWD} -w ${PWD} <container> -c " $@"
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