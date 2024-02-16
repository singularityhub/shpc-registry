---
layout: container
name:  "quay.io/biocontainers/perl-crypt-openssl-random"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-crypt-openssl-random/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-crypt-openssl-random/container.yaml"
updated_at: "2024-02-16 02:30:43.595042"
latest: "0.11--pl5321h5076881_5"
container_url: "https://biocontainers.pro/tools/perl-crypt-openssl-random"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.11--pl5321h1f4ba0c_3"
 - "0.11--pl5321h5076881_5"
description: "shpc-registry automated BioContainers addition for perl-crypt-openssl-random"
config: {"url": "https://biocontainers.pro/tools/perl-crypt-openssl-random", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-crypt-openssl-random", "latest": {"0.11--pl5321h5076881_5": "sha256:6298ee879069611c1d5d1d6675acba4579bd1aecc94edc52b285fbdfbf71b3b1"}, "tags": {"0.11--pl5321h1f4ba0c_3": "sha256:4be3ecad1b8612df912e3c28bf4a9baa632b859f73cd8f2993f4aaad7cef224b", "0.11--pl5321h5076881_5": "sha256:6298ee879069611c1d5d1d6675acba4579bd1aecc94edc52b285fbdfbf71b3b1"}, "docker": "quay.io/biocontainers/perl-crypt-openssl-random", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-crypt-openssl-random.
shpc-registry automated BioContainers addition for perl-crypt-openssl-random
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-crypt-openssl-random
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-crypt-openssl-random:0.11--pl5321h5076881_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-crypt-openssl-random/0.11--pl5321h5076881_5
$ module help quay.io/biocontainers/perl-crypt-openssl-random/0.11--pl5321h5076881_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-crypt-openssl-random-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-crypt-openssl-random-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-crypt-openssl-random-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-crypt-openssl-random-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-crypt-openssl-random-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-crypt-openssl-random-inspect-deffile:

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