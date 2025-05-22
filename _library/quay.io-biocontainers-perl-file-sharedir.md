---
layout: container
name:  "quay.io/biocontainers/perl-file-sharedir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-file-sharedir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-file-sharedir/container.yaml"
updated_at: "2025-05-22 03:54:44.048982"
latest: "1.118--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-file-sharedir"

versions:
 - "1.118--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-file-sharedir"
config: {"url": "https://biocontainers.pro/tools/perl-file-sharedir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-file-sharedir", "latest": {"1.118--pl5321hdfd78af_0": "sha256:23bf0db30b54285180a4b77fecb2ce9180d6e24f247d0d15dafc4316482e3ea3"}, "tags": {"1.118--pl5321hdfd78af_0": "sha256:23bf0db30b54285180a4b77fecb2ce9180d6e24f247d0d15dafc4316482e3ea3"}, "docker": "quay.io/biocontainers/perl-file-sharedir"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-file-sharedir.
shpc-registry automated BioContainers addition for perl-file-sharedir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-file-sharedir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-file-sharedir:1.118--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-file-sharedir/1.118--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-file-sharedir/1.118--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-file-sharedir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-file-sharedir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-file-sharedir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-file-sharedir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-file-sharedir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-file-sharedir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-file-sharedir

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