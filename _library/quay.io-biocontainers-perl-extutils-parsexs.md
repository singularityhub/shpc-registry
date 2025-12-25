---
layout: container
name:  "quay.io/biocontainers/perl-extutils-parsexs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-extutils-parsexs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-extutils-parsexs/container.yaml"
updated_at: "2025-12-25 03:49:47.669164"
latest: "3.60--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-extutils-parsexs"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "3.44--pl5321hdfd78af_0"
 - "3.57--pl5321hdfd78af_0"
 - "3.58--pl5321hdfd78af_0"
 - "3.59--pl5321hdfd78af_0"
 - "3.60--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-extutils-parsexs"
config: {"url": "https://biocontainers.pro/tools/perl-extutils-parsexs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-extutils-parsexs", "latest": {"3.60--pl5321hdfd78af_0": "sha256:d5d7a14bdea04f4061c7175f4ebbd4670872d78d47adc56d08029972fc424d77"}, "tags": {"3.44--pl5321hdfd78af_0": "sha256:76055a60a4345fee00f78b679d0417ee1f00c5eceda500ea77f9503f641831cd", "3.57--pl5321hdfd78af_0": "sha256:ca3a8797f1ed6370bc237a3b10c500885fc5c5180e3ef5fa56425eddb63f0acc", "3.58--pl5321hdfd78af_0": "sha256:3850f402842314a382f260c912c89569e92e5aeec79161b6c5e0072aee86e392", "3.59--pl5321hdfd78af_0": "sha256:50a670deec61aa4959f5384b01df547290bbd4ec13fefa264904284b276278ec", "3.60--pl5321hdfd78af_0": "sha256:d5d7a14bdea04f4061c7175f4ebbd4670872d78d47adc56d08029972fc424d77"}, "docker": "quay.io/biocontainers/perl-extutils-parsexs", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-extutils-parsexs.
shpc-registry automated BioContainers addition for perl-extutils-parsexs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-extutils-parsexs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-extutils-parsexs:3.60--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-extutils-parsexs/3.60--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-extutils-parsexs/3.60--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-extutils-parsexs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-extutils-parsexs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-extutils-parsexs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-extutils-parsexs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-extutils-parsexs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-extutils-parsexs-inspect-deffile:

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