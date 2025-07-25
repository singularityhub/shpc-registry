---
layout: container
name:  "quay.io/biocontainers/perl-class-methodmaker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-class-methodmaker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-class-methodmaker/container.yaml"
updated_at: "2025-07-25 05:13:09.959547"
latest: "2.25--pl5321h7b50bb2_1"
container_url: "https://biocontainers.pro/tools/perl-class-methodmaker"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.24--pl5321hec16e2b_3"
 - "2.24--pl5321h031d066_4"
 - "2.25--pl5321h031d066_0"
 - "2.24--pl5321h031d066_5"
 - "2.25--pl5321h7b50bb2_1"
description: "shpc-registry automated BioContainers addition for perl-class-methodmaker"
config: {"url": "https://biocontainers.pro/tools/perl-class-methodmaker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-class-methodmaker", "latest": {"2.25--pl5321h7b50bb2_1": "sha256:9531cdcf43d8a22a8ee7b1be9d6c9823220b46c0c28ca95e9a37469773d75e68"}, "tags": {"2.24--pl5321hec16e2b_3": "sha256:b7dd4e291ef1d243b2394e689e603c7d4410d311dcd916a82c4b94e6af69ab4c", "2.24--pl5321h031d066_4": "sha256:1890add8af393388b3b4446ad8a924c61db71335eca4fd0b7a63e7981846fcdb", "2.25--pl5321h031d066_0": "sha256:1d2948db819367f928ff32f3a327a523819abc4a720bf0fa275592bfb02539f4", "2.24--pl5321h031d066_5": "sha256:bffb2136c0076aa8b91174e625a047c6cae9eab3359645be7545cb5d183678ad", "2.25--pl5321h7b50bb2_1": "sha256:9531cdcf43d8a22a8ee7b1be9d6c9823220b46c0c28ca95e9a37469773d75e68"}, "docker": "quay.io/biocontainers/perl-class-methodmaker", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-class-methodmaker.
shpc-registry automated BioContainers addition for perl-class-methodmaker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-class-methodmaker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-class-methodmaker:2.25--pl5321h7b50bb2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-class-methodmaker/2.25--pl5321h7b50bb2_1
$ module help quay.io/biocontainers/perl-class-methodmaker/2.25--pl5321h7b50bb2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-class-methodmaker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-class-methodmaker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-class-methodmaker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-class-methodmaker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-class-methodmaker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-class-methodmaker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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