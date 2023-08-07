---
layout: container
name:  "quay.io/biocontainers/orfquant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orfquant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/orfquant/container.yaml"
updated_at: "2023-08-07 04:13:55.322861"
latest: "1.1.0--r42h9ee0642_4"
container_url: "https://biocontainers.pro/tools/orfquant"
aliases:
 - "pandoc"
versions:
 - "1.1.0--r41h9ee0642_3"
 - "1.1.0--r42h9ee0642_4"
description: "shpc-registry automated BioContainers addition for orfquant"
config: {"url": "https://biocontainers.pro/tools/orfquant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for orfquant", "latest": {"1.1.0--r42h9ee0642_4": "sha256:351e60756e3c673266eb64251d10b238b063ce9a33ba5a463c8a554435d46475"}, "tags": {"1.1.0--r41h9ee0642_3": "sha256:7b4caab52c120bceb43065a9295adb12d376c509ece94af87a46bfbc4a17c74f", "1.1.0--r42h9ee0642_4": "sha256:351e60756e3c673266eb64251d10b238b063ce9a33ba5a463c8a554435d46475"}, "docker": "quay.io/biocontainers/orfquant", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orfquant.
shpc-registry automated BioContainers addition for orfquant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orfquant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orfquant:1.1.0--r42h9ee0642_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orfquant/1.1.0--r42h9ee0642_4
$ module help quay.io/biocontainers/orfquant/1.1.0--r42h9ee0642_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orfquant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orfquant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orfquant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orfquant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orfquant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orfquant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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