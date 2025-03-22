---
layout: container
name:  "quay.io/biocontainers/perl-ipc-run"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-ipc-run/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-ipc-run/container.yaml"
updated_at: "2025-03-22 03:40:01.615238"
latest: "20200505.0--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-ipc-run"

versions:
 - "20200505.0--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-ipc-run"
config: {"url": "https://biocontainers.pro/tools/perl-ipc-run", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-ipc-run", "latest": {"20200505.0--pl5321hdfd78af_0": "sha256:6c6e6fb061f995933b527f98afb56b0d8aa10cc0d517aa4cb554d49d2cc29958"}, "tags": {"20200505.0--pl5321hdfd78af_0": "sha256:6c6e6fb061f995933b527f98afb56b0d8aa10cc0d517aa4cb554d49d2cc29958"}, "docker": "quay.io/biocontainers/perl-ipc-run"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-ipc-run.
shpc-registry automated BioContainers addition for perl-ipc-run
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-ipc-run
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-ipc-run:20200505.0--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-ipc-run/20200505.0--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-ipc-run/20200505.0--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-ipc-run-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-ipc-run-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-ipc-run-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-ipc-run-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-ipc-run-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-ipc-run-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-ipc-run

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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