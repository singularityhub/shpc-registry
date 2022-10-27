---
layout: container
name:  "quay.io/biocontainers/perl-parallel-forkmanager"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-parallel-forkmanager/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-parallel-forkmanager/container.yaml"
updated_at: "2022-10-27 01:15:24.980056"
latest: "2.02--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-parallel-forkmanager"

versions:
 - "2.02--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-parallel-forkmanager"
config: {"url": "https://biocontainers.pro/tools/perl-parallel-forkmanager", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-parallel-forkmanager", "latest": {"2.02--pl5321hdfd78af_1": "sha256:22b31e372afe1d28d15dd3ff10df015d709de5d40f09ff8f358ac1ce21578417"}, "tags": {"2.02--pl5321hdfd78af_1": "sha256:22b31e372afe1d28d15dd3ff10df015d709de5d40f09ff8f358ac1ce21578417"}, "docker": "quay.io/biocontainers/perl-parallel-forkmanager"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-parallel-forkmanager.
shpc-registry automated BioContainers addition for perl-parallel-forkmanager
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-parallel-forkmanager
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-parallel-forkmanager:2.02--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-parallel-forkmanager/2.02--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-parallel-forkmanager/2.02--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-parallel-forkmanager-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-parallel-forkmanager-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-parallel-forkmanager-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-parallel-forkmanager-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-parallel-forkmanager-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-parallel-forkmanager-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-parallel-forkmanager

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