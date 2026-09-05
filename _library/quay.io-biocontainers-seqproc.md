---
layout: container
name:  "quay.io/biocontainers/seqproc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqproc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqproc/container.yaml"
updated_at: "2026-09-05 07:04:56.751545"
latest: "0.1.1--h4bf21ff_0"
container_url: "https://biocontainers.pro/tools/seqproc"
aliases:
 - "seqproc"
versions:
 - "0.1.1--h4bf21ff_0"
description: "singularity registry hpc automated addition for seqproc"
config: {"url": "https://biocontainers.pro/tools/seqproc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for seqproc", "latest": {"0.1.1--h4bf21ff_0": "sha256:df60f318c2d2eac83d55ad8274ba4d679f83df0280d4300cf7bb651e7bfc7407"}, "tags": {"0.1.1--h4bf21ff_0": "sha256:df60f318c2d2eac83d55ad8274ba4d679f83df0280d4300cf7bb651e7bfc7407"}, "docker": "quay.io/biocontainers/seqproc", "aliases": {"seqproc": "/usr/local/bin/seqproc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqproc.
singularity registry hpc automated addition for seqproc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqproc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqproc:0.1.1--h4bf21ff_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqproc/0.1.1--h4bf21ff_0
$ module help quay.io/biocontainers/seqproc/0.1.1--h4bf21ff_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqproc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqproc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqproc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqproc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqproc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqproc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqproc

```bash
$ singularity exec <container> /usr/local/bin/seqproc
$ podman run --it --rm --entrypoint /usr/local/bin/seqproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqproc   -v ${PWD} -w ${PWD} <container> -c " $@"
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