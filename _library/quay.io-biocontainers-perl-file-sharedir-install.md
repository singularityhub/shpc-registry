---
layout: container
name:  "quay.io/biocontainers/perl-file-sharedir-install"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-file-sharedir-install/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-file-sharedir-install/container.yaml"
updated_at: "2024-11-29 03:04:51.738382"
latest: "0.13--pl526_0"
container_url: "https://biocontainers.pro/tools/perl-file-sharedir-install"
aliases:
 - "perl5.26.2"
 - "podselect"
versions:
 - "0.13--pl526_0"
description: "shpc-registry automated BioContainers addition for perl-file-sharedir-install"
config: {"url": "https://biocontainers.pro/tools/perl-file-sharedir-install", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-file-sharedir-install", "latest": {"0.13--pl526_0": "sha256:8bbd73190eb1483715caf4a7f3c03cc39b32586050f9c0f7033cef94cc76cff1"}, "tags": {"0.13--pl526_0": "sha256:8bbd73190eb1483715caf4a7f3c03cc39b32586050f9c0f7033cef94cc76cff1"}, "docker": "quay.io/biocontainers/perl-file-sharedir-install", "aliases": {"perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-file-sharedir-install.
shpc-registry automated BioContainers addition for perl-file-sharedir-install
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-file-sharedir-install
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-file-sharedir-install:0.13--pl526_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-file-sharedir-install/0.13--pl526_0
$ module help quay.io/biocontainers/perl-file-sharedir-install/0.13--pl526_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-file-sharedir-install-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-file-sharedir-install-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-file-sharedir-install-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-file-sharedir-install-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-file-sharedir-install-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-file-sharedir-install-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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