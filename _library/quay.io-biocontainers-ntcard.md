---
layout: container
name:  "quay.io/biocontainers/ntcard"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ntcard/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ntcard/container.yaml"
updated_at: "2025-05-20 03:59:09.065657"
latest: "1.2.2--pl5321h077b44d_6"
container_url: "https://biocontainers.pro/tools/ntcard"
aliases:
 - "ntcard"
 - "nthll"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.2.2--pl5321hd03093a_2"
 - "1.2.2--pl5321hdcf5f25_4"
 - "1.2.2--pl5321hdcf5f25_5"
 - "1.2.2--pl5321h077b44d_6"
description: "shpc-registry automated BioContainers addition for ntcard"
config: {"url": "https://biocontainers.pro/tools/ntcard", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ntcard", "latest": {"1.2.2--pl5321h077b44d_6": "sha256:69d9f372b5294c455814fb5dce45cfcd8749f1d02831f76a0c5177a11cebbcd1"}, "tags": {"1.2.2--pl5321hd03093a_2": "sha256:a445aa915d02f930ae426e19ddb2b1656da3db034b3b5ecde8a9e4d5256026cd", "1.2.2--pl5321hdcf5f25_4": "sha256:6a792af561e9ab6437cbba3e341d81a41790f651401e8d2944b98f7ab68d585c", "1.2.2--pl5321hdcf5f25_5": "sha256:425e77544c4de84ba8cd285af01d8b001ac8f8b8e8e892a578ac6091bc0c054e", "1.2.2--pl5321h077b44d_6": "sha256:69d9f372b5294c455814fb5dce45cfcd8749f1d02831f76a0c5177a11cebbcd1"}, "docker": "quay.io/biocontainers/ntcard", "aliases": {"ntcard": "/usr/local/bin/ntcard", "nthll": "/usr/local/bin/nthll", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ntcard.
shpc-registry automated BioContainers addition for ntcard
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ntcard
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ntcard:1.2.2--pl5321h077b44d_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ntcard/1.2.2--pl5321h077b44d_6
$ module help quay.io/biocontainers/ntcard/1.2.2--pl5321h077b44d_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ntcard-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ntcard-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ntcard-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ntcard-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ntcard-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ntcard-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ntcard

```bash
$ singularity exec <container> /usr/local/bin/ntcard
$ podman run --it --rm --entrypoint /usr/local/bin/ntcard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntcard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nthll

```bash
$ singularity exec <container> /usr/local/bin/nthll
$ podman run --it --rm --entrypoint /usr/local/bin/nthll   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nthll   -v ${PWD} -w ${PWD} <container> -c " $@"
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