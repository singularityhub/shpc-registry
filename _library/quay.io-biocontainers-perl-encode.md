---
layout: container
name:  "quay.io/biocontainers/perl-encode"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-encode/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-encode/container.yaml"
updated_at: "2025-11-09 03:21:28.923893"
latest: "3.19--pl5321hec16e2b_1"
container_url: "https://biocontainers.pro/tools/perl-encode"

versions:
 - "3.19--pl5321hec16e2b_1"
description: "shpc-registry automated BioContainers addition for perl-encode"
config: {"url": "https://biocontainers.pro/tools/perl-encode", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-encode", "latest": {"3.19--pl5321hec16e2b_1": "sha256:c28bda4248371aee0449c807e811eb8e657728ce69c9af62168b2eaa6dafac76"}, "tags": {"3.19--pl5321hec16e2b_1": "sha256:c28bda4248371aee0449c807e811eb8e657728ce69c9af62168b2eaa6dafac76"}, "docker": "quay.io/biocontainers/perl-encode"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-encode.
shpc-registry automated BioContainers addition for perl-encode
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-encode
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-encode:3.19--pl5321hec16e2b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-encode/3.19--pl5321hec16e2b_1
$ module help quay.io/biocontainers/perl-encode/3.19--pl5321hec16e2b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-encode-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-encode-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-encode-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-encode-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-encode-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-encode-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-encode

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