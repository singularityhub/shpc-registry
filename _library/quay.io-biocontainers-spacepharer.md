---
layout: container
name:  "quay.io/biocontainers/spacepharer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spacepharer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spacepharer/container.yaml"
updated_at: "2024-01-08 02:59:33.818562"
latest: "5.c2e680a--pl5321h6a68c12_3"
container_url: "https://biocontainers.pro/tools/spacepharer"
aliases:
 - "spacepharer"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "idn2"
 - "wget"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "5.c2e680a--pl5321hf1761c0_1"
 - "5.c2e680a--pl5321h6a68c12_3"
description: "shpc-registry automated BioContainers addition for spacepharer"
config: {"url": "https://biocontainers.pro/tools/spacepharer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spacepharer", "latest": {"5.c2e680a--pl5321h6a68c12_3": "sha256:f7d6be0037c30122995fbd289733003345e43187ecd6477d311f28b794fd5e65"}, "tags": {"5.c2e680a--pl5321hf1761c0_1": "sha256:2d65181967a4d8ff4db3f48d7980fa2195545d6439bfed56fe59cd8c5b26c704", "5.c2e680a--pl5321h6a68c12_3": "sha256:f7d6be0037c30122995fbd289733003345e43187ecd6477d311f28b794fd5e65"}, "docker": "quay.io/biocontainers/spacepharer", "aliases": {"spacepharer": "/usr/local/bin/spacepharer", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spacepharer.
shpc-registry automated BioContainers addition for spacepharer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spacepharer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spacepharer:5.c2e680a--pl5321h6a68c12_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spacepharer/5.c2e680a--pl5321h6a68c12_3
$ module help quay.io/biocontainers/spacepharer/5.c2e680a--pl5321h6a68c12_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spacepharer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spacepharer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spacepharer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spacepharer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spacepharer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spacepharer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spacepharer

```bash
$ singularity exec <container> /usr/local/bin/spacepharer
$ podman run --it --rm --entrypoint /usr/local/bin/spacepharer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spacepharer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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