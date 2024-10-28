---
layout: container
name:  "quay.io/biocontainers/perl-try-tiny"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-try-tiny/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-try-tiny/container.yaml"
updated_at: "2024-10-28 03:35:58.721949"
latest: "0.31--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-try-tiny"

versions:
 - "0.31--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-try-tiny"
config: {"url": "https://biocontainers.pro/tools/perl-try-tiny", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-try-tiny", "latest": {"0.31--pl5321hdfd78af_1": "sha256:8b9273784a9371146867ab8e00b24f1576efecff57af7ad6610eb8d7264a358d"}, "tags": {"0.31--pl5321hdfd78af_1": "sha256:8b9273784a9371146867ab8e00b24f1576efecff57af7ad6610eb8d7264a358d"}, "docker": "quay.io/biocontainers/perl-try-tiny"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-try-tiny.
shpc-registry automated BioContainers addition for perl-try-tiny
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-try-tiny
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-try-tiny:0.31--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-try-tiny/0.31--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-try-tiny/0.31--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-try-tiny-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-try-tiny-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-try-tiny-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-try-tiny-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-try-tiny-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-try-tiny-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-try-tiny

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