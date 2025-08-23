---
layout: container
name:  "quay.io/biocontainers/trim_isoseq_polya"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trim_isoseq_polya/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trim_isoseq_polya/container.yaml"
updated_at: "2025-08-23 03:05:57.880297"
latest: "0.0.3--h7c8eefc_0"
container_url: "https://biocontainers.pro/tools/trim_isoseq_polya"
aliases:
 - "trim_isoseq_polyA"
versions:
 - "0.0.3--h7c8eefc_0"
description: "shpc-registry automated BioContainers addition for trim_isoseq_polya"
config: {"url": "https://biocontainers.pro/tools/trim_isoseq_polya", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trim_isoseq_polya", "latest": {"0.0.3--h7c8eefc_0": "sha256:c26e41e3027585ae697972d4ebb4e3e0dfdcb8d23155d8fcd7a638c49a01567b"}, "tags": {"0.0.3--h7c8eefc_0": "sha256:c26e41e3027585ae697972d4ebb4e3e0dfdcb8d23155d8fcd7a638c49a01567b"}, "docker": "quay.io/biocontainers/trim_isoseq_polya", "aliases": {"trim_isoseq_polyA": "/usr/local/bin/trim_isoseq_polyA"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trim_isoseq_polya.
shpc-registry automated BioContainers addition for trim_isoseq_polya
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trim_isoseq_polya
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trim_isoseq_polya:0.0.3--h7c8eefc_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trim_isoseq_polya/0.0.3--h7c8eefc_0
$ module help quay.io/biocontainers/trim_isoseq_polya/0.0.3--h7c8eefc_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trim_isoseq_polya-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trim_isoseq_polya-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trim_isoseq_polya-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trim_isoseq_polya-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trim_isoseq_polya-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trim_isoseq_polya-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trim_isoseq_polyA

```bash
$ singularity exec <container> /usr/local/bin/trim_isoseq_polyA
$ podman run --it --rm --entrypoint /usr/local/bin/trim_isoseq_polyA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_isoseq_polyA   -v ${PWD} -w ${PWD} <container> -c " $@"
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