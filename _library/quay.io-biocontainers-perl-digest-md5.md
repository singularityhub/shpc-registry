---
layout: container
name:  "quay.io/biocontainers/perl-digest-md5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-digest-md5/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-digest-md5/container.yaml"
updated_at: "2024-03-06 03:02:04.506097"
latest: "2.58--pl5321hec16e2b_1"
container_url: "https://biocontainers.pro/tools/perl-digest-md5"

versions:
 - "2.58--pl5321hec16e2b_1"
description: "shpc-registry automated BioContainers addition for perl-digest-md5"
config: {"url": "https://biocontainers.pro/tools/perl-digest-md5", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-digest-md5", "latest": {"2.58--pl5321hec16e2b_1": "sha256:04c941cf64a2b62ff2f362101fcb5a645c0cd1d0e3833a8f1187a47ad424e715"}, "tags": {"2.58--pl5321hec16e2b_1": "sha256:04c941cf64a2b62ff2f362101fcb5a645c0cd1d0e3833a8f1187a47ad424e715"}, "docker": "quay.io/biocontainers/perl-digest-md5"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-digest-md5.
shpc-registry automated BioContainers addition for perl-digest-md5
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-digest-md5
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-digest-md5:2.58--pl5321hec16e2b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-digest-md5/2.58--pl5321hec16e2b_1
$ module help quay.io/biocontainers/perl-digest-md5/2.58--pl5321hec16e2b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-digest-md5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-digest-md5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-digest-md5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-digest-md5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-digest-md5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-digest-md5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-digest-md5

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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