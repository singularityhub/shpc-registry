---
layout: container
name:  "quay.io/biocontainers/snikt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snikt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snikt/container.yaml"
updated_at: "2024-11-28 03:37:27.737941"
latest: "0.5.0--r43hdfd78af_2"
container_url: "https://biocontainers.pro/tools/snikt"
aliases:
 - "snikt.R"
 - "seqtk"
 - "pandoc"
versions:
 - "0.5.0--r41hdfd78af_0"
 - "0.5.0--r42hdfd78af_1"
 - "0.5.0--r43hdfd78af_2"
description: "shpc-registry automated BioContainers addition for snikt"
config: {"url": "https://biocontainers.pro/tools/snikt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snikt", "latest": {"0.5.0--r43hdfd78af_2": "sha256:c35173b682ae55a5cc99d44b4e7d7b1c8c4b1e756fe6a4ef371d0c84da87a67b"}, "tags": {"0.5.0--r41hdfd78af_0": "sha256:269918776ab7e236c31ee209cd815e5a11dc5ed4620aeb5090263914fd9def9d", "0.5.0--r42hdfd78af_1": "sha256:31e40c36c138f5a5b3b40464d6a9b6ec0d316e3ce5b8762b21412fdef5040185", "0.5.0--r43hdfd78af_2": "sha256:c35173b682ae55a5cc99d44b4e7d7b1c8c4b1e756fe6a4ef371d0c84da87a67b"}, "docker": "quay.io/biocontainers/snikt", "aliases": {"snikt.R": "/usr/local/bin/snikt.R", "seqtk": "/usr/local/bin/seqtk", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snikt.
shpc-registry automated BioContainers addition for snikt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snikt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snikt:0.5.0--r43hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snikt/0.5.0--r43hdfd78af_2
$ module help quay.io/biocontainers/snikt/0.5.0--r43hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snikt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snikt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snikt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snikt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snikt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snikt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snikt.R

```bash
$ singularity exec <container> /usr/local/bin/snikt.R
$ podman run --it --rm --entrypoint /usr/local/bin/snikt.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snikt.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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