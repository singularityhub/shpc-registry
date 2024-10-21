---
layout: container
name:  "quay.io/biocontainers/peekseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/peekseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/peekseq/container.yaml"
updated_at: "2024-10-21 03:34:11.861382"
latest: "0.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/peekseq"
aliases:
 - "peekseq.pl"
versions:
 - "0.0.1--hdfd78af_0"
description: "singularity registry hpc automated addition for peekseq"
config: {"url": "https://biocontainers.pro/tools/peekseq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for peekseq", "latest": {"0.0.1--hdfd78af_0": "sha256:029fc652a4ac31451b44a51f06ab55866a80ef009cfcb83cbfeed526a0e02ab5"}, "tags": {"0.0.1--hdfd78af_0": "sha256:029fc652a4ac31451b44a51f06ab55866a80ef009cfcb83cbfeed526a0e02ab5"}, "docker": "quay.io/biocontainers/peekseq", "aliases": {"peekseq.pl": "/usr/local/bin/peekseq.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/peekseq.
singularity registry hpc automated addition for peekseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/peekseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/peekseq:0.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/peekseq/0.0.1--hdfd78af_0
$ module help quay.io/biocontainers/peekseq/0.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### peekseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### peekseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### peekseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### peekseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### peekseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### peekseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### peekseq.pl

```bash
$ singularity exec <container> /usr/local/bin/peekseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/peekseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peekseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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