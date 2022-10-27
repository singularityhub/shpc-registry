---
layout: container
name:  "quay.io/biocontainers/perl-devel-cover"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-devel-cover/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-devel-cover/container.yaml"
updated_at: "2022-10-27 01:15:43.112567"
latest: "1.33--pl526h14c3975_0"
container_url: "https://biocontainers.pro/tools/perl-devel-cover"
aliases:
 - "cover"
 - "cpancover"
 - "gcov2perl"
versions:
 - "1.33--pl526h14c3975_0"
description: "shpc-registry automated BioContainers addition for perl-devel-cover"
config: {"url": "https://biocontainers.pro/tools/perl-devel-cover", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-devel-cover", "latest": {"1.33--pl526h14c3975_0": "sha256:002aba4e9df855891c1defc66a00b2ff19c5112e29045c1821dff714ca7d0fd8"}, "tags": {"1.33--pl526h14c3975_0": "sha256:002aba4e9df855891c1defc66a00b2ff19c5112e29045c1821dff714ca7d0fd8"}, "docker": "quay.io/biocontainers/perl-devel-cover", "aliases": {"cover": "/usr/local/bin/cover", "cpancover": "/usr/local/bin/cpancover", "gcov2perl": "/usr/local/bin/gcov2perl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-devel-cover.
shpc-registry automated BioContainers addition for perl-devel-cover
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-devel-cover
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-devel-cover:1.33--pl526h14c3975_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-devel-cover/1.33--pl526h14c3975_0
$ module help quay.io/biocontainers/perl-devel-cover/1.33--pl526h14c3975_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-devel-cover-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-devel-cover-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-devel-cover-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-devel-cover-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-devel-cover-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-devel-cover-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cover

```bash
$ singularity exec <container> /usr/local/bin/cover
$ podman run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpancover

```bash
$ singularity exec <container> /usr/local/bin/cpancover
$ podman run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov2perl

```bash
$ singularity exec <container> /usr/local/bin/gcov2perl
$ podman run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
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