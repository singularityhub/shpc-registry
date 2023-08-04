---
layout: container
name:  "quay.io/biocontainers/kmer-jellyfish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmer-jellyfish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmer-jellyfish/container.yaml"
updated_at: "2023-08-04 02:52:19.367528"
latest: "2.3.0--h9f5acd7_3"
container_url: "https://biocontainers.pro/tools/kmer-jellyfish"
aliases:
 - "jellyfish"
versions:
 - "2.3.0--h9f5acd7_3"
description: "shpc-registry automated BioContainers addition for kmer-jellyfish"
config: {"url": "https://biocontainers.pro/tools/kmer-jellyfish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kmer-jellyfish", "latest": {"2.3.0--h9f5acd7_3": "sha256:8b656996004664483c1960d2202a2badf6b567687733e76fd32fb9c8389c7480"}, "tags": {"2.3.0--h9f5acd7_3": "sha256:8b656996004664483c1960d2202a2badf6b567687733e76fd32fb9c8389c7480"}, "docker": "quay.io/biocontainers/kmer-jellyfish", "aliases": {"jellyfish": "/usr/local/bin/jellyfish"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmer-jellyfish.
shpc-registry automated BioContainers addition for kmer-jellyfish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmer-jellyfish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmer-jellyfish:2.3.0--h9f5acd7_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmer-jellyfish/2.3.0--h9f5acd7_3
$ module help quay.io/biocontainers/kmer-jellyfish/2.3.0--h9f5acd7_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmer-jellyfish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmer-jellyfish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmer-jellyfish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmer-jellyfish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmer-jellyfish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmer-jellyfish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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