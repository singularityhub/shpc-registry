---
layout: container
name:  "quay.io/biocontainers/bioconductor-nanotator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nanotator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nanotator/container.yaml"
updated_at: "2025-11-13 04:03:17.537665"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nanotator"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nanotator"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nanotator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nanotator", "latest": {"1.18.0--r43hdfd78af_0": "sha256:6db7b3a03b89326d6263f99d137ba4263b833db07cb86a31debffcf9e736bdd4"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:e729b789415026ee1dd5ebed85de1cc04319b84d809c7235b6072962b6de8685", "1.14.0--r42hdfd78af_0": "sha256:9bba0a9f53fa7e173ce44067b88177c1d3e88ba1088d2902c4d6dfb3cb8bd6ce", "1.10.0--r41hdfd78af_0": "sha256:35fbb8f8a0c1991494d8a430119ee4bfc0d8c887e9a647f937f59df3ce254d42", "1.16.0--r43hdfd78af_0": "sha256:9fa84fbc776aee5df533c18a181f34f235319b6bce1331cb663f94e885be0f6e", "1.18.0--r43hdfd78af_0": "sha256:6db7b3a03b89326d6263f99d137ba4263b833db07cb86a31debffcf9e736bdd4"}, "docker": "quay.io/biocontainers/bioconductor-nanotator", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nanotator.
shpc-registry automated BioContainers addition for bioconductor-nanotator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nanotator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nanotator:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nanotator/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nanotator/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nanotator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanotator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanotator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nanotator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nanotator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nanotator-inspect-deffile:

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