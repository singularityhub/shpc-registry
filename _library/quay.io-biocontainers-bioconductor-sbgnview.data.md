---
layout: container
name:  "quay.io/biocontainers/bioconductor-sbgnview.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sbgnview.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sbgnview.data/container.yaml"
updated_at: "2024-02-20 03:02:40.657490"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sbgnview.data"
aliases:
 - "pandoc"
versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.11.0--r42hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sbgnview.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sbgnview.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sbgnview.data", "latest": {"1.16.0--r43hdfd78af_0": "sha256:427f1ae9256396ec5976027d31f6be9050bc4192dfc6718d93c744728a7d89c8"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:ffba595c6f77d715baa46715de4c437d2da057d6ed39a9f5ae30afa1d4c10489", "1.11.0--r42hdfd78af_0": "sha256:ae7f1f20fe9f5a2e63abce977bfcc4c8c72eccaa4056f457e120d69733d1aeeb", "1.12.0--r42hdfd78af_0": "sha256:014608cf9376b2408a2f1d51848dac25a3c685d49e69b2b3251b2bc5fcc224c7", "1.14.0--r43hdfd78af_0": "sha256:21d7db77257fdd981856fe13d515654c5910a0135fe815b79fd5e8099d7a89a3", "1.16.0--r43hdfd78af_0": "sha256:427f1ae9256396ec5976027d31f6be9050bc4192dfc6718d93c744728a7d89c8"}, "docker": "quay.io/biocontainers/bioconductor-sbgnview.data", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sbgnview.data.
shpc-registry automated BioContainers addition for bioconductor-sbgnview.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sbgnview.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sbgnview.data:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sbgnview.data/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sbgnview.data/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sbgnview.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sbgnview.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sbgnview.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sbgnview.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sbgnview.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sbgnview.data-inspect-deffile:

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