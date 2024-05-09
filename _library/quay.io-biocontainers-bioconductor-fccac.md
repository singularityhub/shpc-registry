---
layout: container
name:  "quay.io/biocontainers/bioconductor-fccac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fccac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fccac/container.yaml"
updated_at: "2024-05-09 03:07:47.502180"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fccac"
aliases:
 - "wget"
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
description: "shpc-registry automated BioContainers addition for bioconductor-fccac"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fccac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fccac", "latest": {"1.28.0--r43hdfd78af_0": "sha256:c076990b420bc13c8a50164a5e7c49dfcc0bac6a976b2cbf45762b9f2a676e0e"}, "tags": {"1.8.0--r351_0": "sha256:6f97236a6cf9429fea4eb2755b63a2fcd0a407aed7b8993fbcd324f3fda3edcd", "1.24.0--r42hdfd78af_0": "sha256:6ffa7ab16add93bbc6a680a7665c95719a99619c9818fc461730d3b24630cf81", "1.20.0--r41hdfd78af_0": "sha256:2449ce32785c67947b9bc7fb7f334c18da8663039be4dc0faa49625514e2ef91", "1.18.0--r41hdfd78af_0": "sha256:8bb8220f9f86a5ee3f27cd545fd840f6b8a694bad08ef4b7be0bd92939a2c941", "1.16.0--r40hdfd78af_1": "sha256:7e75ac8e54ea3db08e0afb4dbf8c34a55ddc150edefc25415d81b0fe98aafca5", "1.14.0--r40_0": "sha256:f32ccfabff45400dd8b3034c5fa78f2efcc51dadb325251b84decfa1140527e8", "1.26.0--r43hdfd78af_0": "sha256:3c3418aaf12946d4c091397b328c7003b5f7ad041045fd4341672676a4e9a062", "1.28.0--r43hdfd78af_0": "sha256:c076990b420bc13c8a50164a5e7c49dfcc0bac6a976b2cbf45762b9f2a676e0e"}, "docker": "quay.io/biocontainers/bioconductor-fccac", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fccac.
shpc-registry automated BioContainers addition for bioconductor-fccac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fccac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fccac:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fccac/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fccac/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fccac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fccac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fccac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fccac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fccac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fccac-inspect-deffile:

```bash
$ singularity inspect -d <container>
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