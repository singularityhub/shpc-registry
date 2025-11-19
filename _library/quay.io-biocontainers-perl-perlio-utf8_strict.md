---
layout: container
name:  "quay.io/biocontainers/perl-perlio-utf8_strict"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-perlio-utf8_strict/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-perlio-utf8_strict/container.yaml"
updated_at: "2025-11-19 03:18:15.871670"
latest: "0.010--pl5321h9948957_0"
container_url: "https://biocontainers.pro/tools/perl-perlio-utf8_strict"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.009--pl5321h9f5acd7_1"
 - "0.010--pl5321h9948957_0"
 - "0.009--pl5321h9948957_2"
description: "shpc-registry automated BioContainers addition for perl-perlio-utf8_strict"
config: {"url": "https://biocontainers.pro/tools/perl-perlio-utf8_strict", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-perlio-utf8_strict", "latest": {"0.010--pl5321h9948957_0": "sha256:fe0b8e8f49210bfc7d31eac422e7de02232c4590b7595f21cd1d341c19ab0e7e"}, "tags": {"0.009--pl5321h9f5acd7_1": "sha256:17765cbebf8cfeaa26466c992c73779c1627cb83d0a21dac44f563177f2687c2", "0.010--pl5321h9948957_0": "sha256:fe0b8e8f49210bfc7d31eac422e7de02232c4590b7595f21cd1d341c19ab0e7e", "0.009--pl5321h9948957_2": "sha256:c02fc8359612a9b0a819d01b13fcce4eaab792eaa4920ec3f931a9afdf1f70d6"}, "docker": "quay.io/biocontainers/perl-perlio-utf8_strict", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-perlio-utf8_strict.
shpc-registry automated BioContainers addition for perl-perlio-utf8_strict
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-perlio-utf8_strict
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-perlio-utf8_strict:0.010--pl5321h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-perlio-utf8_strict/0.010--pl5321h9948957_0
$ module help quay.io/biocontainers/perl-perlio-utf8_strict/0.010--pl5321h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-perlio-utf8_strict-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-perlio-utf8_strict-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-perlio-utf8_strict-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-perlio-utf8_strict-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-perlio-utf8_strict-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-perlio-utf8_strict-inspect-deffile:

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