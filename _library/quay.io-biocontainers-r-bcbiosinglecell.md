---
layout: container
name:  "quay.io/biocontainers/r-bcbiosinglecell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-bcbiosinglecell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-bcbiosinglecell/container.yaml"
updated_at: "2023-01-27 03:25:58.062999"
latest: "0.6.2--r42hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-bcbiosinglecell"
aliases:
 - "pandoc"
versions:
 - "0.5.0--r41hdfd78af_0"
 - "0.6.2--r42hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-bcbiosinglecell"
config: {"url": "https://biocontainers.pro/tools/r-bcbiosinglecell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-bcbiosinglecell", "latest": {"0.6.2--r42hdfd78af_1": "sha256:c3bf8be79eaebdd37624d10659a6405b30cd69785507985b5754c83c58bce459"}, "tags": {"0.5.0--r41hdfd78af_0": "sha256:4c2a569223ad69aded39d480542e20da64feb1e9d5da7fa5b85b069f624633fe", "0.6.2--r42hdfd78af_1": "sha256:c3bf8be79eaebdd37624d10659a6405b30cd69785507985b5754c83c58bce459"}, "docker": "quay.io/biocontainers/r-bcbiosinglecell", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-bcbiosinglecell.
shpc-registry automated BioContainers addition for r-bcbiosinglecell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-bcbiosinglecell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-bcbiosinglecell:0.6.2--r42hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-bcbiosinglecell/0.6.2--r42hdfd78af_1
$ module help quay.io/biocontainers/r-bcbiosinglecell/0.6.2--r42hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-bcbiosinglecell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-bcbiosinglecell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-bcbiosinglecell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-bcbiosinglecell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-bcbiosinglecell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-bcbiosinglecell-inspect-deffile:

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