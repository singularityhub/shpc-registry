---
layout: container
name:  "quay.io/biocontainers/perl-alien-build"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-alien-build/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-alien-build/container.yaml"
updated_at: "2025-09-08 03:11:37.173881"
latest: "2.84--pl5321h7b50bb2_1"
container_url: "https://biocontainers.pro/tools/perl-alien-build"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.53--pl5321hec16e2b_0"
 - "2.84--pl5321h7b50bb2_0"
 - "2.84--pl5321h7b50bb2_1"
description: "singularity registry hpc automated addition for perl-alien-build"
config: {"url": "https://biocontainers.pro/tools/perl-alien-build", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-alien-build", "latest": {"2.84--pl5321h7b50bb2_1": "sha256:678d9ac57f3f54c6f590f2590417a245aff7b316f6964416818ce06a53a1173d"}, "tags": {"2.53--pl5321hec16e2b_0": "sha256:766b9dd14778f802b418403163105f81c3d456dba8e8ceff492ffd31ed21de67", "2.84--pl5321h7b50bb2_0": "sha256:f6303e9c9c7e2e64bfc9fe15df9790a21763e874eaf52abebf776045eb3032ca", "2.84--pl5321h7b50bb2_1": "sha256:678d9ac57f3f54c6f590f2590417a245aff7b316f6964416818ce06a53a1173d"}, "docker": "quay.io/biocontainers/perl-alien-build", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-alien-build.
singularity registry hpc automated addition for perl-alien-build
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-alien-build
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-alien-build:2.84--pl5321h7b50bb2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-alien-build/2.84--pl5321h7b50bb2_1
$ module help quay.io/biocontainers/perl-alien-build/2.84--pl5321h7b50bb2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-alien-build-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-alien-build-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-alien-build-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-alien-build-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-alien-build-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-alien-build-inspect-deffile:

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