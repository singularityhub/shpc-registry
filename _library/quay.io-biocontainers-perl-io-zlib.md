---
layout: container
name:  "quay.io/biocontainers/perl-io-zlib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-io-zlib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-io-zlib/container.yaml"
updated_at: "2024-04-04 04:23:11.912056"
latest: "1.14--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-io-zlib"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.11--pl5321hdfd78af_0"
 - "1.12--pl5321hdfd78af_0"
 - "1.14--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-io-zlib"
config: {"url": "https://biocontainers.pro/tools/perl-io-zlib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-io-zlib", "latest": {"1.14--pl5321hdfd78af_0": "sha256:efaabdd99929647cafc414012268a9c7486201cbe863bf5598241a1bbaddbbb2"}, "tags": {"1.11--pl5321hdfd78af_0": "sha256:cb3197271930e7058d691a60ec6716c75aa4a7b6f5ea194092120594c303dfcc", "1.12--pl5321hdfd78af_0": "sha256:8492b6344b044d2f6a72353d5a1728f74b33f6b8268fdac4a9a161bfb9eb7260", "1.14--pl5321hdfd78af_0": "sha256:efaabdd99929647cafc414012268a9c7486201cbe863bf5598241a1bbaddbbb2"}, "docker": "quay.io/biocontainers/perl-io-zlib", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-io-zlib.
shpc-registry automated BioContainers addition for perl-io-zlib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-io-zlib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-io-zlib:1.14--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-io-zlib/1.14--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-io-zlib/1.14--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-io-zlib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-io-zlib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-io-zlib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-io-zlib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-io-zlib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-io-zlib-inspect-deffile:

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