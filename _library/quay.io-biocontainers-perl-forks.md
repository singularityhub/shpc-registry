---
layout: container
name:  "quay.io/biocontainers/perl-forks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-forks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-forks/container.yaml"
updated_at: "2025-10-18 03:27:36.371544"
latest: "0.36--pl5321h7b50bb2_10"
container_url: "https://biocontainers.pro/tools/perl-forks"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.36--pl5321hec16e2b_7"
 - "0.36--pl5321h031d066_8"
 - "0.36--pl5321h7b50bb2_9"
 - "0.36--pl5321h7b50bb2_10"
description: "shpc-registry automated BioContainers addition for perl-forks"
config: {"url": "https://biocontainers.pro/tools/perl-forks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-forks", "latest": {"0.36--pl5321h7b50bb2_10": "sha256:87c86d671851ef5c19e2e85f261ff061fec2249580da01bac340a1bc916de2e0"}, "tags": {"0.36--pl5321hec16e2b_7": "sha256:ff54359bed5d1c77d428947dd46914a94a597b75f1ce9b7e7329b54895069f70", "0.36--pl5321h031d066_8": "sha256:93a4675476150411440dc6b5525fb0258bba27dee93ccb77f0b289dfe167b1b5", "0.36--pl5321h7b50bb2_9": "sha256:16f7f05a037b3da949734aba21f256012660bf9753f9da5b4dc67a25027858af", "0.36--pl5321h7b50bb2_10": "sha256:87c86d671851ef5c19e2e85f261ff061fec2249580da01bac340a1bc916de2e0"}, "docker": "quay.io/biocontainers/perl-forks", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-forks.
shpc-registry automated BioContainers addition for perl-forks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-forks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-forks:0.36--pl5321h7b50bb2_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-forks/0.36--pl5321h7b50bb2_10
$ module help quay.io/biocontainers/perl-forks/0.36--pl5321h7b50bb2_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-forks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-forks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-forks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-forks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-forks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-forks-inspect-deffile:

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