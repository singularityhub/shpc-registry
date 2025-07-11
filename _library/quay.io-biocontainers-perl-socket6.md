---
layout: container
name:  "quay.io/biocontainers/perl-socket6"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-socket6/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-socket6/container.yaml"
updated_at: "2025-07-11 04:13:45.711373"
latest: "0.29--pl5321h7b50bb2_6"
container_url: "https://biocontainers.pro/tools/perl-socket6"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.29--pl5321hec16e2b_2"
 - "0.29--pl5321h031d066_4"
 - "0.29--pl5321h031d066_5"
 - "0.29--pl5321h7b50bb2_6"
description: "shpc-registry automated BioContainers addition for perl-socket6"
config: {"url": "https://biocontainers.pro/tools/perl-socket6", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-socket6", "latest": {"0.29--pl5321h7b50bb2_6": "sha256:21dae2847739d685e29fdf59bbcfa15e621f0c9e1f4c161c8e02aeb7281e5874"}, "tags": {"0.29--pl5321hec16e2b_2": "sha256:01b248b1b460dd96a3c036273b7bc5771be44d3486d07e04751fe0ecf61edd14", "0.29--pl5321h031d066_4": "sha256:49853d3d0b267cb04fed7e6dfc637f75d8a28a3b748a0bf56054908ac19d0881", "0.29--pl5321h031d066_5": "sha256:f38c9ec4b092f419e8b04fc4b919e9cc3146419513b2bb0fdd254e18b1b7ca86", "0.29--pl5321h7b50bb2_6": "sha256:21dae2847739d685e29fdf59bbcfa15e621f0c9e1f4c161c8e02aeb7281e5874"}, "docker": "quay.io/biocontainers/perl-socket6", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-socket6.
shpc-registry automated BioContainers addition for perl-socket6
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-socket6
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-socket6:0.29--pl5321h7b50bb2_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-socket6/0.29--pl5321h7b50bb2_6
$ module help quay.io/biocontainers/perl-socket6/0.29--pl5321h7b50bb2_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-socket6-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-socket6-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-socket6-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-socket6-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-socket6-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-socket6-inspect-deffile:

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