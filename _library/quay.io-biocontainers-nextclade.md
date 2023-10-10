---
layout: container
name:  "quay.io/biocontainers/nextclade"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nextclade/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nextclade/container.yaml"
updated_at: "2023-10-10 02:56:40.141339"
latest: "2.14.0--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/nextclade"
aliases:
 - "nextclade"
versions:
 - "2.7.0--h9ee0642_0"
 - "2.8.0--h9ee0642_0"
 - "2.9.1--h9ee0642_0"
 - "2.11.0--h9ee0642_0"
 - "2.10.1--h9ee0642_0"
 - "2.13.0--h9ee0642_0"
 - "2.12.0--h9ee0642_0"
 - "2.13.1--h9ee0642_0"
 - "2.14.0--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for nextclade"
config: {"url": "https://biocontainers.pro/tools/nextclade", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nextclade", "latest": {"2.14.0--h9ee0642_1": "sha256:4bec08cff03c3d022174faf0c343a2b06725ff5004aaeed44f2cc42685d17147"}, "tags": {"2.7.0--h9ee0642_0": "sha256:4c252a1f1f9227e4dee96cbc2422ef82e4f921fac9c3ec9986ea357d4de74e57", "2.8.0--h9ee0642_0": "sha256:4cfde8d9b8080d97c4f9e36d0e30ad92d3b189bbfddfefe1e1cbbc04f7aaa2d3", "2.9.1--h9ee0642_0": "sha256:d7dcbb9f8172f3c3f3eaa8bd9f6b08c63f9f43f456fd37287ef7f4eaa47d68f5", "2.11.0--h9ee0642_0": "sha256:7b7fcd9e66e6f1e61658ae7e4d72fad91ca705756ef47e404c8f2a5d62db648a", "2.10.1--h9ee0642_0": "sha256:857019eeab04c02538914baa4ca59e6e00e2ffa201cacd02e3e52ff268e0f08d", "2.13.0--h9ee0642_0": "sha256:a67bad36b3129408309d1bc23211289c1d0d0a2ca2d8ac957e369f2d16ade7bc", "2.12.0--h9ee0642_0": "sha256:d1199847e7ab923cfb3d13d05212b09c7f1ba726af8265bbf1f107d9aec92263", "2.13.1--h9ee0642_0": "sha256:046d301f922f3ec2e75a22ac911356b5dd8949d8b7853e6643eff12dc1a0fbfd", "2.14.0--h9ee0642_1": "sha256:4bec08cff03c3d022174faf0c343a2b06725ff5004aaeed44f2cc42685d17147"}, "docker": "quay.io/biocontainers/nextclade", "aliases": {"nextclade": "/usr/local/bin/nextclade"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nextclade.
shpc-registry automated BioContainers addition for nextclade
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nextclade
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nextclade:2.14.0--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nextclade/2.14.0--h9ee0642_1
$ module help quay.io/biocontainers/nextclade/2.14.0--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nextclade-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nextclade-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nextclade-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nextclade-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nextclade-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nextclade-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nextclade

```bash
$ singularity exec <container> /usr/local/bin/nextclade
$ podman run --it --rm --entrypoint /usr/local/bin/nextclade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextclade   -v ${PWD} -w ${PWD} <container> -c " $@"
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