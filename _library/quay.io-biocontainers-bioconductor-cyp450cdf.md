---
layout: container
name:  "quay.io/biocontainers/bioconductor-cyp450cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cyp450cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cyp450cdf/container.yaml"
updated_at: "2024-06-23 02:52:46.749019"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-cyp450cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-cyp450cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cyp450cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cyp450cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:cb9251b17a2a1d1da8bc47d323ccdf51b31cde98d1acea6eb9a187ce0a284cf7"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:4edfa5ab04a005a6e5befd561f90d54bc1d9dd73fdf0cfa69deecd6db5f7eea0", "2.18.0--r42hdfd78af_10": "sha256:c8f0427a9cc03b1863b563db5a7f3ca9401132db21dfc59dd472b1a6fb76e447", "2.18.0--r43hdfd78af_11": "sha256:72f35e3b46aff626041c27040808f7317591535e870a3363e140ff72f0a80e68", "2.18.0--r43hdfd78af_12": "sha256:cb9251b17a2a1d1da8bc47d323ccdf51b31cde98d1acea6eb9a187ce0a284cf7"}, "docker": "quay.io/biocontainers/bioconductor-cyp450cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cyp450cdf.
shpc-registry automated BioContainers addition for bioconductor-cyp450cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cyp450cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cyp450cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cyp450cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-cyp450cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cyp450cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cyp450cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cyp450cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cyp450cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cyp450cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cyp450cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cyp450cdf

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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