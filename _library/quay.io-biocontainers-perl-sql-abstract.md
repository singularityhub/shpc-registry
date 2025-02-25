---
layout: container
name:  "quay.io/biocontainers/perl-sql-abstract"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-sql-abstract/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-sql-abstract/container.yaml"
updated_at: "2025-02-25 03:12:09.856155"
latest: "2.000001--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-sql-abstract"
aliases:
 - "config_data"
versions:
 - "2.000001--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for perl-sql-abstract"
config: {"url": "https://biocontainers.pro/tools/perl-sql-abstract", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-sql-abstract", "latest": {"2.000001--pl5321hdfd78af_0": "sha256:52c5e7641d1ee128fc1725b622430f4fe0df2291e81c2dd00b663b7e1faa2b68"}, "tags": {"2.000001--pl5321hdfd78af_0": "sha256:52c5e7641d1ee128fc1725b622430f4fe0df2291e81c2dd00b663b7e1faa2b68"}, "docker": "quay.io/biocontainers/perl-sql-abstract", "aliases": {"config_data": "/usr/local/bin/config_data"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-sql-abstract.
singularity registry hpc automated addition for perl-sql-abstract
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-sql-abstract
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-sql-abstract:2.000001--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-sql-abstract/2.000001--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-sql-abstract/2.000001--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-sql-abstract-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-sql-abstract-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-sql-abstract-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-sql-abstract-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-sql-abstract-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-sql-abstract-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### config_data

```bash
$ singularity exec <container> /usr/local/bin/config_data
$ podman run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
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