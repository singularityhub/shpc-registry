---
layout: container
name:  "quay.io/biocontainers/perl-time-hires"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-time-hires/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-time-hires/container.yaml"
updated_at: "2024-10-28 03:00:46.645972"
latest: "1.9764--pl5321h031d066_4"
container_url: "https://biocontainers.pro/tools/perl-time-hires"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.9764--pl5321hec16e2b_2"
 - "1.9764--pl5321h031d066_4"
description: "shpc-registry automated BioContainers addition for perl-time-hires"
config: {"url": "https://biocontainers.pro/tools/perl-time-hires", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-time-hires", "latest": {"1.9764--pl5321h031d066_4": "sha256:f2483c5f3a6209bc74f17f806e734dcd12a529714a9930117def4ad27a1b0fd1"}, "tags": {"1.9764--pl5321hec16e2b_2": "sha256:058b7110f15320ecbfd6c52bf18536c4f034eace8ec8740a8043b4091142fb40", "1.9764--pl5321h031d066_4": "sha256:f2483c5f3a6209bc74f17f806e734dcd12a529714a9930117def4ad27a1b0fd1"}, "docker": "quay.io/biocontainers/perl-time-hires", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-time-hires.
shpc-registry automated BioContainers addition for perl-time-hires
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-time-hires
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-time-hires:1.9764--pl5321h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-time-hires/1.9764--pl5321h031d066_4
$ module help quay.io/biocontainers/perl-time-hires/1.9764--pl5321h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-time-hires-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-time-hires-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-time-hires-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-time-hires-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-time-hires-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-time-hires-inspect-deffile:

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