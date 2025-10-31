---
layout: container
name:  "quay.io/biocontainers/kmertools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmertools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmertools/container.yaml"
updated_at: "2025-10-31 04:07:44.664545"
latest: "0.2.1--h5e00ca1_0"
container_url: "https://biocontainers.pro/tools/kmertools"
aliases:
 - "kmertools"
versions:
 - "0.1.0--h4349ce8_0"
 - "0.1.3--h5b94c0b_0"
 - "0.1.4--h5e00ca1_0"
 - "0.1.5--hec43fc7_0"
 - "0.2.1--h5e00ca1_0"
description: "singularity registry hpc automated addition for kmertools"
config: {"url": "https://biocontainers.pro/tools/kmertools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kmertools", "latest": {"0.2.1--h5e00ca1_0": "sha256:af9bef9acfe3636cd85d7de1dc0c55289f2463853fc5368cb127966413235d3a"}, "tags": {"0.1.0--h4349ce8_0": "sha256:8f89ef8335c3b1fcb89a6fc3afc07f862fd61aef3001b53770ae5080e89c6d59", "0.1.3--h5b94c0b_0": "sha256:c60d1f26d0a685425b6646fc19d88cca07d6cff958d6bd1ac72f5bb64932d73a", "0.1.4--h5e00ca1_0": "sha256:c351608d821ce7d8f9aea4ea67418459d75ba96c478f74f34ae88e33d8dbb7cb", "0.1.5--hec43fc7_0": "sha256:7f1acd2d2be12f955d4b5aaff5e0e0f0d676fbc0f809c98ea2810d9001a101e6", "0.2.1--h5e00ca1_0": "sha256:af9bef9acfe3636cd85d7de1dc0c55289f2463853fc5368cb127966413235d3a"}, "docker": "quay.io/biocontainers/kmertools", "aliases": {"kmertools": "/usr/local/bin/kmertools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmertools.
singularity registry hpc automated addition for kmertools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmertools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmertools:0.2.1--h5e00ca1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmertools/0.2.1--h5e00ca1_0
$ module help quay.io/biocontainers/kmertools/0.2.1--h5e00ca1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmertools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmertools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmertools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmertools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmertools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmertools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmertools

```bash
$ singularity exec <container> /usr/local/bin/kmertools
$ podman run --it --rm --entrypoint /usr/local/bin/kmertools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmertools   -v ${PWD} -w ${PWD} <container> -c " $@"
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