---
layout: container
name:  "quay.io/biocontainers/perl-datetime"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-datetime/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-datetime/container.yaml"
updated_at: "2023-06-04 03:50:32.690880"
latest: "1.59--pl5321h4ac6f70_1"
container_url: "https://biocontainers.pro/tools/perl-datetime"

versions:
 - "1.58--pl5321h9f5acd7_1"
 - "1.59--pl5321h9f5acd7_0"
 - "1.59--pl5321h4ac6f70_1"
description: "shpc-registry automated BioContainers addition for perl-datetime"
config: {"url": "https://biocontainers.pro/tools/perl-datetime", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-datetime", "latest": {"1.59--pl5321h4ac6f70_1": "sha256:372a1f48112bddfd78d1c5cbdf4ffc87436ab6c53a9b44ee8a14940036f05136"}, "tags": {"1.58--pl5321h9f5acd7_1": "sha256:a6b4f54183fa36f387096f5d0566d7d376af7ce413bb5fdb0f369f550dfd70cc", "1.59--pl5321h9f5acd7_0": "sha256:829050a5ac76481ae22af618b416d93101929dd1f55427a4306b02bb3ded3375", "1.59--pl5321h4ac6f70_1": "sha256:372a1f48112bddfd78d1c5cbdf4ffc87436ab6c53a9b44ee8a14940036f05136"}, "docker": "quay.io/biocontainers/perl-datetime"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-datetime.
shpc-registry automated BioContainers addition for perl-datetime
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-datetime
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-datetime:1.59--pl5321h4ac6f70_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-datetime/1.59--pl5321h4ac6f70_1
$ module help quay.io/biocontainers/perl-datetime/1.59--pl5321h4ac6f70_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-datetime-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-datetime-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-datetime-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-datetime-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-datetime-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-datetime-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-datetime

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