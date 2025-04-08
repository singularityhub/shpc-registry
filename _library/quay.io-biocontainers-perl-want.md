---
layout: container
name:  "quay.io/biocontainers/perl-want"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-want/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-want/container.yaml"
updated_at: "2025-04-08 03:27:59.000015"
latest: "0.29--pl5321h7b50bb2_6"
container_url: "https://biocontainers.pro/tools/perl-want"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.29--pl5321hec16e2b_3"
 - "0.29--pl5321h031d066_5"
 - "0.29--pl5321h7b50bb2_6"
description: "shpc-registry automated BioContainers addition for perl-want"
config: {"url": "https://biocontainers.pro/tools/perl-want", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-want", "latest": {"0.29--pl5321h7b50bb2_6": "sha256:ac44c746afe29ac0e4787c90ac486b8e64b4a660a51a49d03449e2469f17f475"}, "tags": {"0.29--pl5321hec16e2b_3": "sha256:52f511288075ee05e6b2982d995c03374e8aeb70d302b38d12d62891d0c067ad", "0.29--pl5321h031d066_5": "sha256:75df7a9db5ae7cc7d5fa61565368cbd6a4ed27f6040ab38325488c8d82d69140", "0.29--pl5321h7b50bb2_6": "sha256:ac44c746afe29ac0e4787c90ac486b8e64b4a660a51a49d03449e2469f17f475"}, "docker": "quay.io/biocontainers/perl-want", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-want.
shpc-registry automated BioContainers addition for perl-want
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-want
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-want:0.29--pl5321h7b50bb2_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-want/0.29--pl5321h7b50bb2_6
$ module help quay.io/biocontainers/perl-want/0.29--pl5321h7b50bb2_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-want-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-want-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-want-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-want-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-want-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-want-inspect-deffile:

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