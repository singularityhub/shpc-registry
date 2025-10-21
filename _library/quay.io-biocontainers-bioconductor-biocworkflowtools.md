---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocworkflowtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocworkflowtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocworkflowtools/container.yaml"
updated_at: "2025-10-21 03:33:00.952087"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocworkflowtools"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocworkflowtools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocworkflowtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocworkflowtools", "latest": {"1.32.0--r44hdfd78af_0": "sha256:2e3d12454a2204f8671474b114d5ede5a6f725a0386a95b6535ce22c5046a1fe"}, "tags": {"1.8.0--r351_0": "sha256:48c24b5cbcf6b037f316dd69a5e4a52a04e96cd42f2b545612001dcaad168a4f", "1.24.0--r42hdfd78af_0": "sha256:9ad3370b7c4280edede3efd8cd033171c831aa883064bdd9738162b99fb6b9d9", "1.20.0--r41hdfd78af_0": "sha256:8194294c9c82360c52b8f15ec5b217b62eae9e508bec754c0a5aadc0d9826e85", "1.18.0--r41hdfd78af_0": "sha256:913793ea2afa9fb16499678952de801b1c114fa662423a45df9ad1beaf0c0a0b", "1.16.0--r40hdfd78af_1": "sha256:e8d7317dea9e2b15bb5eccdaa3d2a22354a32e6b52b7f7b5e8bc9fe8afc2a69e", "1.14.0--r40_0": "sha256:f253fbfc0ddbf4fe47e020556964f00b256df7c7ff9fe0171fa5bd9ca32355d4", "1.26.0--r43hdfd78af_0": "sha256:8c3baf1e6f3696961e62b08f654efa1e49e4105193a21e259e97032495780fa9", "1.28.0--r43hdfd78af_0": "sha256:df6b0c33dead8852bc8ec2c8349eae5b321c0f3da6f19e120ebf81e24e928033", "1.32.0--r44hdfd78af_0": "sha256:2e3d12454a2204f8671474b114d5ede5a6f725a0386a95b6535ce22c5046a1fe"}, "docker": "quay.io/biocontainers/bioconductor-biocworkflowtools", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocworkflowtools.
shpc-registry automated BioContainers addition for bioconductor-biocworkflowtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocworkflowtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocworkflowtools:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocworkflowtools/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocworkflowtools/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocworkflowtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocworkflowtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocworkflowtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocworkflowtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocworkflowtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocworkflowtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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