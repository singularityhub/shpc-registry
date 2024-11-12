---
layout: container
name:  "quay.io/biocontainers/hifihla"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hifihla/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hifihla/container.yaml"
updated_at: "2024-11-12 03:19:43.244862"
latest: "0.3.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hifihla"
aliases:
 - "hifihla"
versions:
 - "0.2.2--hdfd78af_0"
 - "0.2.3--hdfd78af_0"
 - "0.3.1--hdfd78af_0"
description: "singularity registry hpc automated addition for hifihla"
config: {"url": "https://biocontainers.pro/tools/hifihla", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hifihla", "latest": {"0.3.1--hdfd78af_0": "sha256:0a3807a7d5537293c3456ce03dcd1fa39a013bd3235e15c798821584c37736e4"}, "tags": {"0.2.2--hdfd78af_0": "sha256:f5efb93d34dea99aed8d8de49295279ee7685b6ce84a57b16f2008be5af8b0ac", "0.2.3--hdfd78af_0": "sha256:90a0fd81202c4bc91a8abdbd43cdf9bc679ed7b6ceeee599b496b49e0d2010cd", "0.3.1--hdfd78af_0": "sha256:0a3807a7d5537293c3456ce03dcd1fa39a013bd3235e15c798821584c37736e4"}, "docker": "quay.io/biocontainers/hifihla", "aliases": {"hifihla": "/usr/local/bin/hifihla"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hifihla.
singularity registry hpc automated addition for hifihla
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hifihla
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hifihla:0.3.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hifihla/0.3.1--hdfd78af_0
$ module help quay.io/biocontainers/hifihla/0.3.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hifihla-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hifihla-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hifihla-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hifihla-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hifihla-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hifihla-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hifihla

```bash
$ singularity exec <container> /usr/local/bin/hifihla
$ podman run --it --rm --entrypoint /usr/local/bin/hifihla   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifihla   -v ${PWD} -w ${PWD} <container> -c " $@"
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