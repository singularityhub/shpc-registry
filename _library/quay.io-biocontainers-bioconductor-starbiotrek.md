---
layout: container
name:  "quay.io/biocontainers/bioconductor-starbiotrek"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-starbiotrek/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-starbiotrek/container.yaml"
updated_at: "2024-05-10 02:43:22.350079"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-starbiotrek"
aliases:
 - "idn2"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_1"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-starbiotrek"
config: {"url": "https://biocontainers.pro/tools/bioconductor-starbiotrek", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-starbiotrek", "latest": {"1.28.0--r43hdfd78af_0": "sha256:80f6c602537be2be31e67b8a37ae769eb387e3e15863a5df1959d68d01104f51"}, "tags": {"1.8.1--r351_1": "sha256:b9c2577145e28b0891c6c58b14a0c9ef908c79c76adf85f5b55262032865211d", "1.24.0--r42hdfd78af_0": "sha256:deed92f2a9e4b932c1707a9f95b9e0c96981fda77ab50d691630a877f44a8897", "1.20.0--r41hdfd78af_0": "sha256:eb2b5d31a4996112f914ba4b67d488f1a5279508021fa24306d10a931e0deae4", "1.18.0--r41hdfd78af_0": "sha256:62d12172d36035a23fd7994498df92020694ffc2d3bdde288473e44c7cdab598", "1.16.0--r40hdfd78af_1": "sha256:27531451e0d16f67af3afa2f4b0945ceda37f4a55d35bdc0ee9799f3ed3aa846", "1.14.0--r40_0": "sha256:16292d737035ee34565815ac6186d376fbc3b490208e621bed2825fd4f4172e3", "1.26.0--r43hdfd78af_0": "sha256:603f378509cb776532ce5dc68ceaaeecaaab4c921b2f9b2f560c8baf6f4020b5", "1.28.0--r43hdfd78af_0": "sha256:80f6c602537be2be31e67b8a37ae769eb387e3e15863a5df1959d68d01104f51"}, "docker": "quay.io/biocontainers/bioconductor-starbiotrek", "aliases": {"idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-starbiotrek.
shpc-registry automated BioContainers addition for bioconductor-starbiotrek
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-starbiotrek
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-starbiotrek:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-starbiotrek/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-starbiotrek/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-starbiotrek-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-starbiotrek-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-starbiotrek-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-starbiotrek-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-starbiotrek-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-starbiotrek-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
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