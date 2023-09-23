---
layout: container
name:  "quay.io/biocontainers/legsta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/legsta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/legsta/container.yaml"
updated_at: "2023-09-23 03:22:14.837497"
latest: "0.5.1--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/legsta"
aliases:
 - "gfPcr"
 - "gfServer"
 - "isPcr"
 - "legsta"
 - "any2fasta"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.5.1--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for legsta"
config: {"url": "https://biocontainers.pro/tools/legsta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for legsta", "latest": {"0.5.1--hdfd78af_2": "sha256:af7e0130449459de66f65b9b305caae35987bddd181953ca2653f4ac1cff2072"}, "tags": {"0.5.1--hdfd78af_2": "sha256:af7e0130449459de66f65b9b305caae35987bddd181953ca2653f4ac1cff2072"}, "docker": "quay.io/biocontainers/legsta", "aliases": {"gfPcr": "/usr/local/bin/gfPcr", "gfServer": "/usr/local/bin/gfServer", "isPcr": "/usr/local/bin/isPcr", "legsta": "/usr/local/bin/legsta", "any2fasta": "/usr/local/bin/any2fasta", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/legsta.
shpc-registry automated BioContainers addition for legsta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/legsta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/legsta:0.5.1--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/legsta/0.5.1--hdfd78af_2
$ module help quay.io/biocontainers/legsta/0.5.1--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### legsta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### legsta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### legsta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### legsta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### legsta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### legsta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfPcr

```bash
$ singularity exec <container> /usr/local/bin/gfPcr
$ podman run --it --rm --entrypoint /usr/local/bin/gfPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfServer

```bash
$ singularity exec <container> /usr/local/bin/gfServer
$ podman run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isPcr

```bash
$ singularity exec <container> /usr/local/bin/isPcr
$ podman run --it --rm --entrypoint /usr/local/bin/isPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### legsta

```bash
$ singularity exec <container> /usr/local/bin/legsta
$ podman run --it --rm --entrypoint /usr/local/bin/legsta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/legsta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
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