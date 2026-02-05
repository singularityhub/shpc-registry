---
layout: container
name:  "quay.io/biocontainers/perl-acme-damn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-acme-damn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-acme-damn/container.yaml"
updated_at: "2026-02-05 04:48:07.650035"
latest: "0.08--pl5321h9948957_9"
container_url: "https://biocontainers.pro/tools/perl-acme-damn"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.08--pl5321h9f5acd7_5"
 - "0.08--pl5321h4ac6f70_7"
 - "0.08--pl5321h9948957_8"
 - "0.08--pl5321h9948957_9"
description: "shpc-registry automated BioContainers addition for perl-acme-damn"
config: {"url": "https://biocontainers.pro/tools/perl-acme-damn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-acme-damn", "latest": {"0.08--pl5321h9948957_9": "sha256:39aa4a04eec91f5fca4dbee4ecc8c17bc66502f04bee543bbfc01fd79195688e"}, "tags": {"0.08--pl5321h9f5acd7_5": "sha256:47c914004c81de0dd568063ece1a0599a34ebdfbdfce546776c54e44506e15ba", "0.08--pl5321h4ac6f70_7": "sha256:d58ba27d917f9e3f57cfd3657035703bd306537992f59e13e2a0081161af9676", "0.08--pl5321h9948957_8": "sha256:5d5410bd7617b1a9b3bbb453221f666b92e694e65829ec402ff888cb4f2cac26", "0.08--pl5321h9948957_9": "sha256:39aa4a04eec91f5fca4dbee4ecc8c17bc66502f04bee543bbfc01fd79195688e"}, "docker": "quay.io/biocontainers/perl-acme-damn", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-acme-damn.
shpc-registry automated BioContainers addition for perl-acme-damn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-acme-damn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-acme-damn:0.08--pl5321h9948957_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-acme-damn/0.08--pl5321h9948957_9
$ module help quay.io/biocontainers/perl-acme-damn/0.08--pl5321h9948957_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-acme-damn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-acme-damn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-acme-damn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-acme-damn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-acme-damn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-acme-damn-inspect-deffile:

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