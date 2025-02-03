---
layout: container
name:  "quay.io/biocontainers/bioconductor-bprmeth"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bprmeth/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bprmeth/container.yaml"
updated_at: "2025-02-03 03:27:23.510507"
latest: "1.32.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bprmeth"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351hf484d3e_0"
 - "1.24.0--r42hc247a5b_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.16.0--r40h399db7b_1"
 - "1.14.0--r40h5f743cb_0"
 - "1.24.0--r42hf17093f_1"
 - "1.26.1--r43hf17093f_0"
 - "1.28.0--r43hf17093f_0"
 - "1.32.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bprmeth"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bprmeth", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bprmeth", "latest": {"1.32.0--r44he5774e6_0": "sha256:a1955964bf603a85e5d0d2948e421b48c795b3906697abd52b40b07286b8957a"}, "tags": {"1.8.1--r351hf484d3e_0": "sha256:9b448315694d85549a54313a1ee2737f389a18a99040629abb34270c7c2d8dac", "1.24.0--r42hc247a5b_0": "sha256:4908b9f454916b4c16f8c96f079457590b0b2cc45e857ad8dd9033d18ccd502f", "1.20.0--r41hc247a5b_2": "sha256:f045e76b9d91f0b422fdd7fb5b0e26f5dac2ea5def06463340818a8c4b67275a", "1.18.0--r41h399db7b_0": "sha256:60485ac087a55dade00b0cf7290b12a82337e6e2fa7500f83a838f0b66679e4b", "1.16.0--r40h399db7b_1": "sha256:3c1f5cdc7f55182a3d3445bb13ff4e095a86a46f3154873708e0f2c8f5e115a1", "1.14.0--r40h5f743cb_0": "sha256:128d0539f792563e39712065000afdcf5f58289fac7dcfcb277699c2551c4054", "1.24.0--r42hf17093f_1": "sha256:27fbdaeb461bb114ee8445a6759762740afb9d8bae1fcaf0d93e2893daa07d0b", "1.26.1--r43hf17093f_0": "sha256:05f352997f0a12091b04952c33ae7f40d718b7d59832c7726c5dcec150ecb3fa", "1.28.0--r43hf17093f_0": "sha256:6215a0d70744c2196da6f6bee367350e830d2a3c58d032c4518fe258046d20f3", "1.32.0--r44he5774e6_0": "sha256:a1955964bf603a85e5d0d2948e421b48c795b3906697abd52b40b07286b8957a"}, "docker": "quay.io/biocontainers/bioconductor-bprmeth", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bprmeth.
shpc-registry automated BioContainers addition for bioconductor-bprmeth
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bprmeth
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bprmeth:1.32.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bprmeth/1.32.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-bprmeth/1.32.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bprmeth-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bprmeth-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bprmeth-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bprmeth-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bprmeth-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bprmeth-inspect-deffile:

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


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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