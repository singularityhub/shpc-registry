---
layout: container
name:  "quay.io/biocontainers/perl-bioperl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bioperl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bioperl/container.yaml"
updated_at: "2024-05-27 03:16:42.101832"
latest: "1.7.8--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-bioperl"

versions:
 - "1.7.8--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-bioperl"
config: {"url": "https://biocontainers.pro/tools/perl-bioperl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bioperl", "latest": {"1.7.8--hdfd78af_1": "sha256:c63603023e10d3a47395a6dac15f434e646b7135f38c185b77325b1b640e2195"}, "tags": {"1.7.8--hdfd78af_1": "sha256:c63603023e10d3a47395a6dac15f434e646b7135f38c185b77325b1b640e2195"}, "docker": "quay.io/biocontainers/perl-bioperl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bioperl.
shpc-registry automated BioContainers addition for perl-bioperl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bioperl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bioperl:1.7.8--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bioperl/1.7.8--hdfd78af_1
$ module help quay.io/biocontainers/perl-bioperl/1.7.8--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bioperl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bioperl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bioperl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bioperl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bioperl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bioperl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-bioperl

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