---
layout: container
name:  "quay.io/biocontainers/bioconductor-assessorf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-assessorf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-assessorf/container.yaml"
updated_at: "2025-10-05 03:14:35.654843"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-assessorf"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-assessorf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-assessorf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-assessorf", "latest": {"1.24.0--r44hdfd78af_0": "sha256:d584e75506d93a79be284e9faccfa2eddf9a5b561227a283ea74dac3e1228991"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:8bcafd7b0da83e1397b57a52a47dca0f8a8d3e2d402b3a5def9ba2fc5b5dd7f8", "1.16.0--r42hdfd78af_0": "sha256:0665a278ebb89d1c0aa4feb292893312bfbbbd476bce4f843fdef6d5982f555a", "1.12.0--r41hdfd78af_0": "sha256:615d0556f67f9bbc33ca6bddae6e73bc53ef822c3c43356d98ec9758fb76e1fd", "1.10.0--r41hdfd78af_0": "sha256:2e6206e02f9a79f6441ebb53c5437a15ad75f9e32b50b43d22cb04133424ffce", "1.18.0--r43hdfd78af_0": "sha256:ddc3f284a251f967277d2859a105ac7c3bc63c3c0c91ed6dae8c4443567d0e5e", "1.20.0--r43hdfd78af_0": "sha256:c54a9524d5472079246c470c751b42c2dc0deb6734ffb28c9e03c3258de1b850", "1.24.0--r44hdfd78af_0": "sha256:d584e75506d93a79be284e9faccfa2eddf9a5b561227a283ea74dac3e1228991"}, "docker": "quay.io/biocontainers/bioconductor-assessorf", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-assessorf.
shpc-registry automated BioContainers addition for bioconductor-assessorf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-assessorf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-assessorf:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-assessorf/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-assessorf/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-assessorf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-assessorf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-assessorf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-assessorf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-assessorf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-assessorf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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