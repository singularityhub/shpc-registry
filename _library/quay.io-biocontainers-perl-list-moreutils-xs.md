---
layout: container
name:  "quay.io/biocontainers/perl-list-moreutils-xs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-list-moreutils-xs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-list-moreutils-xs/container.yaml"
updated_at: "2023-04-21 03:00:12.538048"
latest: "0.430--pl5321hec16e2b_1"
container_url: "https://biocontainers.pro/tools/perl-list-moreutils-xs"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.430--pl5321hec16e2b_1"
description: "shpc-registry automated BioContainers addition for perl-list-moreutils-xs"
config: {"url": "https://biocontainers.pro/tools/perl-list-moreutils-xs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-list-moreutils-xs", "latest": {"0.430--pl5321hec16e2b_1": "sha256:ab8439bcda9bc85ec3fe88cc63102a124035312e17f4810380d149534bc3d71c"}, "tags": {"0.430--pl5321hec16e2b_1": "sha256:ab8439bcda9bc85ec3fe88cc63102a124035312e17f4810380d149534bc3d71c"}, "docker": "quay.io/biocontainers/perl-list-moreutils-xs", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-list-moreutils-xs.
shpc-registry automated BioContainers addition for perl-list-moreutils-xs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-list-moreutils-xs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-list-moreutils-xs:0.430--pl5321hec16e2b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-list-moreutils-xs/0.430--pl5321hec16e2b_1
$ module help quay.io/biocontainers/perl-list-moreutils-xs/0.430--pl5321hec16e2b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-list-moreutils-xs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-list-moreutils-xs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-list-moreutils-xs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-list-moreutils-xs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-list-moreutils-xs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-list-moreutils-xs-inspect-deffile:

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