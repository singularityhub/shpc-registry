---
layout: container
name:  "quay.io/biocontainers/perl-fastx-reader"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-fastx-reader/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-fastx-reader/container.yaml"
updated_at: "2025-10-24 03:50:08.170869"
latest: "1.12.0--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-fastx-reader"
aliases:
 - "fqc"
 - "fqlen.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.5.0--pl5321hdfd78af_0"
 - "1.7.0--pl5321hdfd78af_0"
 - "1.6.1--pl5321hdfd78af_0"
 - "1.9.0--pl5321hdfd78af_0"
 - "1.8.1--pl5321hdfd78af_0"
 - "1.10.0--pl5321hdfd78af_0"
 - "1.11.0--pl5321hdfd78af_0"
 - "1.12.0--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-fastx-reader"
config: {"url": "https://biocontainers.pro/tools/perl-fastx-reader", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-fastx-reader", "latest": {"1.12.0--pl5321hdfd78af_0": "sha256:7f37c66d757adabd126d366c34cb78d0f62ea0e0c19e4e07a20804fec0711a4d"}, "tags": {"1.5.0--pl5321hdfd78af_0": "sha256:7ea34d7e48895807d3f458f805cc459e0a7d67971071f9332935bac8335beb48", "1.7.0--pl5321hdfd78af_0": "sha256:8ae382c504cb1b25d0b205de70b4b4f6a2a415bd469504a0c80ec0303f37618d", "1.6.1--pl5321hdfd78af_0": "sha256:d8a7744dd3637e24cff70d55df97a6e901963043af7eceb714e6c0cf3f4021f7", "1.9.0--pl5321hdfd78af_0": "sha256:d9b221143f610117afd97b23e417063ba21c99de07816f473fa6e0861c958b26", "1.8.1--pl5321hdfd78af_0": "sha256:05e95db320d4cf8f7bf8fcde69d93cb3ad8ec1c0823e82629288c9065817318e", "1.10.0--pl5321hdfd78af_0": "sha256:08ea075cb34c861b41709b630db5f5e41f08c98625160b98732f85838471bef0", "1.11.0--pl5321hdfd78af_0": "sha256:094bf347563fdac11e98e4db41ae79968acc624813993a0437042ca778f38a70", "1.12.0--pl5321hdfd78af_0": "sha256:7f37c66d757adabd126d366c34cb78d0f62ea0e0c19e4e07a20804fec0711a4d"}, "docker": "quay.io/biocontainers/perl-fastx-reader", "aliases": {"fqc": "/usr/local/bin/fqc", "fqlen.pl": "/usr/local/bin/fqlen.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-fastx-reader.
shpc-registry automated BioContainers addition for perl-fastx-reader
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-fastx-reader
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-fastx-reader:1.12.0--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-fastx-reader/1.12.0--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-fastx-reader/1.12.0--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-fastx-reader-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-fastx-reader-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-fastx-reader-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-fastx-reader-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-fastx-reader-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-fastx-reader-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fqc

```bash
$ singularity exec <container> /usr/local/bin/fqc
$ podman run --it --rm --entrypoint /usr/local/bin/fqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fqlen.pl

```bash
$ singularity exec <container> /usr/local/bin/fqlen.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fqlen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqlen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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