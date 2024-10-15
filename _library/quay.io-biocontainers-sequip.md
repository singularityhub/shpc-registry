---
layout: container
name:  "quay.io/biocontainers/sequip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sequip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sequip/container.yaml"
updated_at: "2024-10-15 03:16:07.611038"
latest: "0.10--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/sequip"
aliases:
 - "opts-example-required.pl"
 - "opts-example.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.09--hdfd78af_0"
 - "0.10--hdfd78af_0"
description: "singularity registry hpc automated addition for sequip"
config: {"url": "https://biocontainers.pro/tools/sequip", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sequip", "latest": {"0.10--hdfd78af_0": "sha256:933a58549ad7fdb3cf92ff90f08c77ac3dea25eebaf0c671d91ea3944404cd21"}, "tags": {"0.09--hdfd78af_0": "sha256:2d4e8c99a238d8835ddc9da4406dc3b9c5959f5bc29cabd31bf045a414f45eeb", "0.10--hdfd78af_0": "sha256:933a58549ad7fdb3cf92ff90f08c77ac3dea25eebaf0c671d91ea3944404cd21"}, "docker": "quay.io/biocontainers/sequip", "aliases": {"opts-example-required.pl": "/usr/local/bin/opts-example-required.pl", "opts-example.pl": "/usr/local/bin/opts-example.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sequip.
singularity registry hpc automated addition for sequip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sequip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sequip:0.10--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sequip/0.10--hdfd78af_0
$ module help quay.io/biocontainers/sequip/0.10--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sequip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sequip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sequip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sequip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sequip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sequip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### opts-example-required.pl

```bash
$ singularity exec <container> /usr/local/bin/opts-example-required.pl
$ podman run --it --rm --entrypoint /usr/local/bin/opts-example-required.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opts-example-required.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opts-example.pl

```bash
$ singularity exec <container> /usr/local/bin/opts-example.pl
$ podman run --it --rm --entrypoint /usr/local/bin/opts-example.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opts-example.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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