---
layout: container
name:  "quay.io/biocontainers/perl-template-toolkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-template-toolkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-template-toolkit/container.yaml"
updated_at: "2025-03-23 03:36:53.788983"
latest: "3.102--pl5321h7b50bb2_1"
container_url: "https://biocontainers.pro/tools/perl-template-toolkit"
aliases:
 - "imgsize"
 - "tpage"
 - "ttree"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "3.100--pl5321hec16e2b_1"
 - "3.100--pl5321h031d066_2"
 - "3.100--pl5321h7b50bb2_3"
 - "3.102--pl5321h7b50bb2_1"
description: "shpc-registry automated BioContainers addition for perl-template-toolkit"
config: {"url": "https://biocontainers.pro/tools/perl-template-toolkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-template-toolkit", "latest": {"3.102--pl5321h7b50bb2_1": "sha256:d383b02521a84ca1833d540391189076463d8864040a3a02214867bb748fd8a3"}, "tags": {"3.100--pl5321hec16e2b_1": "sha256:f5424fe22b4d38393532e47778ad65dd06f776b2aa8d6bd0978a0b5b26ec11e4", "3.100--pl5321h031d066_2": "sha256:c73d964478aa17cb680a89b03acd8f37c1882fb87c5c4d83553a3defe7960b21", "3.100--pl5321h7b50bb2_3": "sha256:469201538f391d2aa7c3972971c62a29726e7744a7cab44f65b8d915e446b0da", "3.102--pl5321h7b50bb2_1": "sha256:d383b02521a84ca1833d540391189076463d8864040a3a02214867bb748fd8a3"}, "docker": "quay.io/biocontainers/perl-template-toolkit", "aliases": {"imgsize": "/usr/local/bin/imgsize", "tpage": "/usr/local/bin/tpage", "ttree": "/usr/local/bin/ttree", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-template-toolkit.
shpc-registry automated BioContainers addition for perl-template-toolkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-template-toolkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-template-toolkit:3.102--pl5321h7b50bb2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-template-toolkit/3.102--pl5321h7b50bb2_1
$ module help quay.io/biocontainers/perl-template-toolkit/3.102--pl5321h7b50bb2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-template-toolkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-template-toolkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-template-toolkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-template-toolkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-template-toolkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-template-toolkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### imgsize

```bash
$ singularity exec <container> /usr/local/bin/imgsize
$ podman run --it --rm --entrypoint /usr/local/bin/imgsize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imgsize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tpage

```bash
$ singularity exec <container> /usr/local/bin/tpage
$ podman run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttree

```bash
$ singularity exec <container> /usr/local/bin/ttree
$ podman run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
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