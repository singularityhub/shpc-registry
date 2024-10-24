---
layout: container
name:  "quay.io/biocontainers/blend-bio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blend-bio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blend-bio/container.yaml"
updated_at: "2024-10-24 03:40:25.720674"
latest: "1.0.0--he4a0461_2"
container_url: "https://biocontainers.pro/tools/blend-bio"
aliases:
 - "blend"
 - "sdust"
versions:
 - "1.0.0--h7132678_0"
 - "1.0.0--he4a0461_2"
description: "singularity registry hpc automated addition for blend-bio"
config: {"url": "https://biocontainers.pro/tools/blend-bio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for blend-bio", "latest": {"1.0.0--he4a0461_2": "sha256:c617f7e585ebb4ad924fccac22dfae86daa30d373657ba0cf74ae641ca1cf1d7"}, "tags": {"1.0.0--h7132678_0": "sha256:065a1dad5fa04908aa223561f10958b87a451ba47a083cf97ee6f5203bd37146", "1.0.0--he4a0461_2": "sha256:c617f7e585ebb4ad924fccac22dfae86daa30d373657ba0cf74ae641ca1cf1d7"}, "docker": "quay.io/biocontainers/blend-bio", "aliases": {"blend": "/usr/local/bin/blend", "sdust": "/usr/local/bin/sdust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blend-bio.
singularity registry hpc automated addition for blend-bio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blend-bio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blend-bio:1.0.0--he4a0461_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blend-bio/1.0.0--he4a0461_2
$ module help quay.io/biocontainers/blend-bio/1.0.0--he4a0461_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blend-bio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blend-bio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blend-bio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blend-bio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blend-bio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blend-bio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blend

```bash
$ singularity exec <container> /usr/local/bin/blend
$ podman run --it --rm --entrypoint /usr/local/bin/blend   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blend   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
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