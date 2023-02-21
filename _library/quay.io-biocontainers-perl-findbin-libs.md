---
layout: container
name:  "quay.io/biocontainers/perl-findbin-libs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-findbin-libs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-findbin-libs/container.yaml"
updated_at: "2023-02-21 02:59:15.570728"
latest: "2.017008--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-findbin-libs"
aliases:
 - "perl-reversion"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.017008--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-findbin-libs"
config: {"url": "https://biocontainers.pro/tools/perl-findbin-libs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-findbin-libs", "latest": {"2.017008--pl5321hdfd78af_2": "sha256:50ab6f7a62072b596fb8abb83e2049e46bd7b6c3369083ed2d69e84e6ed95b2f"}, "tags": {"2.017008--pl5321hdfd78af_2": "sha256:50ab6f7a62072b596fb8abb83e2049e46bd7b6c3369083ed2d69e84e6ed95b2f"}, "docker": "quay.io/biocontainers/perl-findbin-libs", "aliases": {"perl-reversion": "/usr/local/bin/perl-reversion", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-findbin-libs.
shpc-registry automated BioContainers addition for perl-findbin-libs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-findbin-libs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-findbin-libs:2.017008--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-findbin-libs/2.017008--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-findbin-libs/2.017008--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-findbin-libs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-findbin-libs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-findbin-libs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-findbin-libs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-findbin-libs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-findbin-libs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl-reversion

```bash
$ singularity exec <container> /usr/local/bin/perl-reversion
$ podman run --it --rm --entrypoint /usr/local/bin/perl-reversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl-reversion   -v ${PWD} -w ${PWD} <container> -c " $@"
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