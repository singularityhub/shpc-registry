---
layout: container
name:  "quay.io/biocontainers/perl-parallel-iterator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-parallel-iterator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-parallel-iterator/container.yaml"
updated_at: "2025-12-10 04:13:47.862033"
latest: "1.002--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-parallel-iterator"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.00--pl5321hdfd78af_1"
 - "1.002--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-parallel-iterator"
config: {"url": "https://biocontainers.pro/tools/perl-parallel-iterator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-parallel-iterator", "latest": {"1.002--pl5321hdfd78af_0": "sha256:4a8e5287b2e3a25ee2a31965e3cd2609aefaec3684140df66d1bbcc8bba0b36e"}, "tags": {"1.00--pl5321hdfd78af_1": "sha256:a5de0d3aa9a23c89b052264857668d3daa8e01814b889288aedf5387a3c9f64a", "1.002--pl5321hdfd78af_0": "sha256:4a8e5287b2e3a25ee2a31965e3cd2609aefaec3684140df66d1bbcc8bba0b36e"}, "docker": "quay.io/biocontainers/perl-parallel-iterator", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-parallel-iterator.
shpc-registry automated BioContainers addition for perl-parallel-iterator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-parallel-iterator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-parallel-iterator:1.002--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-parallel-iterator/1.002--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-parallel-iterator/1.002--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-parallel-iterator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-parallel-iterator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-parallel-iterator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-parallel-iterator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-parallel-iterator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-parallel-iterator-inspect-deffile:

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