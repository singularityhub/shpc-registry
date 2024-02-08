---
layout: container
name:  "quay.io/biocontainers/mason"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mason/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mason/container.yaml"
updated_at: "2024-02-08 08:06:04.525768"
latest: "2.0.9--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/mason"
aliases:
 - "mason_frag_sequencing"
 - "mason_genome"
 - "mason_materializer"
 - "mason_methylation"
 - "mason_simulator"
 - "mason_splicing"
 - "mason_variator"
versions:
 - "2.0.9--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for mason"
config: {"url": "https://biocontainers.pro/tools/mason", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mason", "latest": {"2.0.9--h9ee0642_1": "sha256:5dab77b259bc4f6757616a83242eceaec141348048497fe18a30a24a85950d63"}, "tags": {"2.0.9--h9ee0642_1": "sha256:5dab77b259bc4f6757616a83242eceaec141348048497fe18a30a24a85950d63"}, "docker": "quay.io/biocontainers/mason", "aliases": {"mason_frag_sequencing": "/usr/local/bin/mason_frag_sequencing", "mason_genome": "/usr/local/bin/mason_genome", "mason_materializer": "/usr/local/bin/mason_materializer", "mason_methylation": "/usr/local/bin/mason_methylation", "mason_simulator": "/usr/local/bin/mason_simulator", "mason_splicing": "/usr/local/bin/mason_splicing", "mason_variator": "/usr/local/bin/mason_variator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mason.
shpc-registry automated BioContainers addition for mason
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mason
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mason:2.0.9--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mason/2.0.9--h9ee0642_1
$ module help quay.io/biocontainers/mason/2.0.9--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mason-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mason-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mason-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mason-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mason-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mason-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mason_frag_sequencing

```bash
$ singularity exec <container> /usr/local/bin/mason_frag_sequencing
$ podman run --it --rm --entrypoint /usr/local/bin/mason_frag_sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_frag_sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_genome

```bash
$ singularity exec <container> /usr/local/bin/mason_genome
$ podman run --it --rm --entrypoint /usr/local/bin/mason_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_materializer

```bash
$ singularity exec <container> /usr/local/bin/mason_materializer
$ podman run --it --rm --entrypoint /usr/local/bin/mason_materializer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_materializer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_methylation

```bash
$ singularity exec <container> /usr/local/bin/mason_methylation
$ podman run --it --rm --entrypoint /usr/local/bin/mason_methylation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_methylation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_simulator

```bash
$ singularity exec <container> /usr/local/bin/mason_simulator
$ podman run --it --rm --entrypoint /usr/local/bin/mason_simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_splicing

```bash
$ singularity exec <container> /usr/local/bin/mason_splicing
$ podman run --it --rm --entrypoint /usr/local/bin/mason_splicing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_splicing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_variator

```bash
$ singularity exec <container> /usr/local/bin/mason_variator
$ podman run --it --rm --entrypoint /usr/local/bin/mason_variator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_variator   -v ${PWD} -w ${PWD} <container> -c " $@"
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