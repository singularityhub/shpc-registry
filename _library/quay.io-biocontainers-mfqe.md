---
layout: container
name:  "quay.io/biocontainers/mfqe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mfqe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mfqe/container.yaml"
updated_at: "2024-04-21 02:33:00.055709"
latest: "0.5.0--h031d066_4"
container_url: "https://biocontainers.pro/tools/mfqe"
aliases:
 - "mfqe"
versions:
 - "0.5.0--hec16e2b_2"
 - "0.5.0--hec16e2b_3"
 - "0.5.0--h031d066_4"
description: "shpc-registry automated BioContainers addition for mfqe"
config: {"url": "https://biocontainers.pro/tools/mfqe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mfqe", "latest": {"0.5.0--h031d066_4": "sha256:18f3804069167df4fd978e70ad8918944943104c73a55b25eaac52e3a541dab8"}, "tags": {"0.5.0--hec16e2b_2": "sha256:06bd33e40788e21d2cc388596c705dbe1cd00e36e1f62c06d2fe60e41ac81d6f", "0.5.0--hec16e2b_3": "sha256:e2a1c0dd9dbd2a4bdf090565fb33f919af2ae93b6828a5f2fb043ac27d89cc7f", "0.5.0--h031d066_4": "sha256:18f3804069167df4fd978e70ad8918944943104c73a55b25eaac52e3a541dab8"}, "docker": "quay.io/biocontainers/mfqe", "aliases": {"mfqe": "/usr/local/bin/mfqe"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mfqe.
shpc-registry automated BioContainers addition for mfqe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mfqe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mfqe:0.5.0--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mfqe/0.5.0--h031d066_4
$ module help quay.io/biocontainers/mfqe/0.5.0--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mfqe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mfqe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mfqe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mfqe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mfqe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mfqe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mfqe

```bash
$ singularity exec <container> /usr/local/bin/mfqe
$ podman run --it --rm --entrypoint /usr/local/bin/mfqe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mfqe   -v ${PWD} -w ${PWD} <container> -c " $@"
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