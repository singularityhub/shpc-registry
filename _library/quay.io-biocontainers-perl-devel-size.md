---
layout: container
name:  "quay.io/biocontainers/perl-devel-size"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-devel-size/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-devel-size/container.yaml"
updated_at: "2023-11-03 03:19:58.187473"
latest: "0.83--pl5321h031d066_4"
container_url: "https://biocontainers.pro/tools/perl-devel-size"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.83--pl5321hec16e2b_2"
 - "0.83--pl5321h031d066_4"
description: "shpc-registry automated BioContainers addition for perl-devel-size"
config: {"url": "https://biocontainers.pro/tools/perl-devel-size", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-devel-size", "latest": {"0.83--pl5321h031d066_4": "sha256:ecb9c9ab7bde911d422868561dbab7a266ed8f777c79bfeb0fb3a05a21870f7b"}, "tags": {"0.83--pl5321hec16e2b_2": "sha256:78e2a7daddff55951a9f3dc8c200b0fb9d8cfab58a7f2e36cfa4772489bc28a4", "0.83--pl5321h031d066_4": "sha256:ecb9c9ab7bde911d422868561dbab7a266ed8f777c79bfeb0fb3a05a21870f7b"}, "docker": "quay.io/biocontainers/perl-devel-size", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-devel-size.
shpc-registry automated BioContainers addition for perl-devel-size
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-devel-size
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-devel-size:0.83--pl5321h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-devel-size/0.83--pl5321h031d066_4
$ module help quay.io/biocontainers/perl-devel-size/0.83--pl5321h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-devel-size-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-devel-size-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-devel-size-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-devel-size-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-devel-size-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-devel-size-inspect-deffile:

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