---
layout: container
name:  "quay.io/biocontainers/knotinframe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/knotinframe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/knotinframe/container.yaml"
updated_at: "2023-11-23 02:31:24.313084"
latest: "2.2.14--pl5321h4ac6f70_1"
container_url: "https://biocontainers.pro/tools/knotinframe"
aliases:
 - "addRNAoptions.pl"
 - "gapc"
 - "knotinframe"
 - "knotinframe_knotted"
 - "knotinframe_nested"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.2.14--pl5321h9f5acd7_0"
 - "2.2.14--pl5321h4ac6f70_1"
description: "singularity registry hpc automated addition for knotinframe"
config: {"url": "https://biocontainers.pro/tools/knotinframe", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for knotinframe", "latest": {"2.2.14--pl5321h4ac6f70_1": "sha256:8aa6f03fa14453064ed8f1436f187ba849cf79074eeb5464ae5416f237aacf19"}, "tags": {"2.2.14--pl5321h9f5acd7_0": "sha256:99b15a33cd982b2e72e14365fe820b883ac07228c32a941e7665894164496e9e", "2.2.14--pl5321h4ac6f70_1": "sha256:8aa6f03fa14453064ed8f1436f187ba849cf79074eeb5464ae5416f237aacf19"}, "docker": "quay.io/biocontainers/knotinframe", "aliases": {"addRNAoptions.pl": "/usr/local/bin/addRNAoptions.pl", "gapc": "/usr/local/bin/gapc", "knotinframe": "/usr/local/bin/knotinframe", "knotinframe_knotted": "/usr/local/bin/knotinframe_knotted", "knotinframe_nested": "/usr/local/bin/knotinframe_nested", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/knotinframe.
singularity registry hpc automated addition for knotinframe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/knotinframe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/knotinframe:2.2.14--pl5321h4ac6f70_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/knotinframe/2.2.14--pl5321h4ac6f70_1
$ module help quay.io/biocontainers/knotinframe/2.2.14--pl5321h4ac6f70_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### knotinframe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### knotinframe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### knotinframe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### knotinframe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### knotinframe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### knotinframe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addRNAoptions.pl

```bash
$ singularity exec <container> /usr/local/bin/addRNAoptions.pl
$ podman run --it --rm --entrypoint /usr/local/bin/addRNAoptions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addRNAoptions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gapc

```bash
$ singularity exec <container> /usr/local/bin/gapc
$ podman run --it --rm --entrypoint /usr/local/bin/gapc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gapc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knotinframe

```bash
$ singularity exec <container> /usr/local/bin/knotinframe
$ podman run --it --rm --entrypoint /usr/local/bin/knotinframe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knotinframe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knotinframe_knotted

```bash
$ singularity exec <container> /usr/local/bin/knotinframe_knotted
$ podman run --it --rm --entrypoint /usr/local/bin/knotinframe_knotted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knotinframe_knotted   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knotinframe_nested

```bash
$ singularity exec <container> /usr/local/bin/knotinframe_nested
$ podman run --it --rm --entrypoint /usr/local/bin/knotinframe_nested   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knotinframe_nested   -v ${PWD} -w ${PWD} <container> -c " $@"
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