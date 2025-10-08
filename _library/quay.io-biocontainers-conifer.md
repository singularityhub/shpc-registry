---
layout: container
name:  "quay.io/biocontainers/conifer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/conifer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/conifer/container.yaml"
updated_at: "2025-10-08 03:30:04.400250"
latest: "1.0.2--h577a1d6_2"
container_url: "https://biocontainers.pro/tools/conifer"
aliases:
 - "conifer"
 - "is_a_parent_of_b"
 - "show_ancestors"
 - "taxid_name"
versions:
 - "1.0.2--he4a0461_0"
 - "1.0.2--h577a1d6_1"
 - "1.0.2--h577a1d6_2"
description: "singularity registry hpc automated addition for conifer"
config: {"url": "https://biocontainers.pro/tools/conifer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for conifer", "latest": {"1.0.2--h577a1d6_2": "sha256:77c7987e88a4a6cdd5bf162ce147a88b0b44acafaac2c87f920197b5d1c53526"}, "tags": {"1.0.2--he4a0461_0": "sha256:579bb7052d2535e466c2cd20263da086409f44a78d4858339e06f77d615ca227", "1.0.2--h577a1d6_1": "sha256:f03434f9cd3e2b886e58aa7d9823d642a352609e592b953221627a879cd765a2", "1.0.2--h577a1d6_2": "sha256:77c7987e88a4a6cdd5bf162ce147a88b0b44acafaac2c87f920197b5d1c53526"}, "docker": "quay.io/biocontainers/conifer", "aliases": {"conifer": "/usr/local/bin/conifer", "is_a_parent_of_b": "/usr/local/bin/is_a_parent_of_b", "show_ancestors": "/usr/local/bin/show_ancestors", "taxid_name": "/usr/local/bin/taxid_name"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/conifer.
singularity registry hpc automated addition for conifer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/conifer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/conifer:1.0.2--h577a1d6_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/conifer/1.0.2--h577a1d6_2
$ module help quay.io/biocontainers/conifer/1.0.2--h577a1d6_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### conifer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### conifer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### conifer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### conifer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### conifer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### conifer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### conifer

```bash
$ singularity exec <container> /usr/local/bin/conifer
$ podman run --it --rm --entrypoint /usr/local/bin/conifer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conifer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### is_a_parent_of_b

```bash
$ singularity exec <container> /usr/local/bin/is_a_parent_of_b
$ podman run --it --rm --entrypoint /usr/local/bin/is_a_parent_of_b   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/is_a_parent_of_b   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show_ancestors

```bash
$ singularity exec <container> /usr/local/bin/show_ancestors
$ podman run --it --rm --entrypoint /usr/local/bin/show_ancestors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show_ancestors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxid_name

```bash
$ singularity exec <container> /usr/local/bin/taxid_name
$ podman run --it --rm --entrypoint /usr/local/bin/taxid_name   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxid_name   -v ${PWD} -w ${PWD} <container> -c " $@"
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