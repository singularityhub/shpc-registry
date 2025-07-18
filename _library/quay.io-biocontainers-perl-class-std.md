---
layout: container
name:  "quay.io/biocontainers/perl-class-std"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-class-std/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-class-std/container.yaml"
updated_at: "2025-07-18 10:33:05.449200"
latest: "0.013--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-class-std"

versions:
 - "0.013--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-class-std"
config: {"url": "https://biocontainers.pro/tools/perl-class-std", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-class-std", "latest": {"0.013--pl5321hdfd78af_2": "sha256:9489a4e329e793cfffaa2008f76b3fb087a9ce10259552855783d9e541705bc1"}, "tags": {"0.013--pl5321hdfd78af_2": "sha256:9489a4e329e793cfffaa2008f76b3fb087a9ce10259552855783d9e541705bc1"}, "docker": "quay.io/biocontainers/perl-class-std"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-class-std.
shpc-registry automated BioContainers addition for perl-class-std
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-class-std
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-class-std:0.013--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-class-std/0.013--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-class-std/0.013--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-class-std-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-class-std-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-class-std-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-class-std-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-class-std-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-class-std-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-class-std

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