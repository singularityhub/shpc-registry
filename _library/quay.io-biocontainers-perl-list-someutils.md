---
layout: container
name:  "quay.io/biocontainers/perl-list-someutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-list-someutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-list-someutils/container.yaml"
updated_at: "2023-12-04 03:46:18.676192"
latest: "0.59--pl5321h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/perl-list-someutils"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.58--pl5321h9f5acd7_1"
 - "0.59--pl5321h9f5acd7_0"
 - "0.59--pl5321h4ac6f70_2"
description: "shpc-registry automated BioContainers addition for perl-list-someutils"
config: {"url": "https://biocontainers.pro/tools/perl-list-someutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-list-someutils", "latest": {"0.59--pl5321h4ac6f70_2": "sha256:75a413ed24d8d16e0852c0166b64f495a29fea1d5664bd5fd85934e0e3f0a77c"}, "tags": {"0.58--pl5321h9f5acd7_1": "sha256:951f0ddf081115e1c804c91f02179a4ee190d14023ab6627f153d633a49a8e8e", "0.59--pl5321h9f5acd7_0": "sha256:11d31a8ab3ae8b7218128bedec7751cbf63932b019e6306f2bbff7bffe6b4d0e", "0.59--pl5321h4ac6f70_2": "sha256:75a413ed24d8d16e0852c0166b64f495a29fea1d5664bd5fd85934e0e3f0a77c"}, "docker": "quay.io/biocontainers/perl-list-someutils", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-list-someutils.
shpc-registry automated BioContainers addition for perl-list-someutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-list-someutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-list-someutils:0.59--pl5321h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-list-someutils/0.59--pl5321h4ac6f70_2
$ module help quay.io/biocontainers/perl-list-someutils/0.59--pl5321h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-list-someutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-list-someutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-list-someutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-list-someutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-list-someutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-list-someutils-inspect-deffile:

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