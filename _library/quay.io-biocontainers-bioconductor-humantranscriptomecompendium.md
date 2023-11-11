---
layout: container
name:  "quay.io/biocontainers/bioconductor-humantranscriptomecompendium"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-humantranscriptomecompendium/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-humantranscriptomecompendium/container.yaml"
updated_at: "2023-11-11 02:58:36.074392"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-humantranscriptomecompendium"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-humantranscriptomecompendium"
config: {"url": "https://biocontainers.pro/tools/bioconductor-humantranscriptomecompendium", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-humantranscriptomecompendium", "latest": {"1.16.0--r43hdfd78af_0": "sha256:8f3eba0b497c4d1ed0699614d3b2033e0ac4fd8f64c47826d4ab9e3499c10edf"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:a910dfb4b51ae42c2dd932cffae1edf08fcba38964b96d5e58ace19d6351c8d6", "1.14.0--r42hdfd78af_0": "sha256:a41e421b191454a930527a9ac86b972f24027ed49b77f3df029cf36fe648a345", "1.10.0--r41hdfd78af_0": "sha256:af5c68984f5ad6310c73cb7ff60e47906f047431acb94cc0b0eee09ff659f77e", "1.16.0--r43hdfd78af_0": "sha256:8f3eba0b497c4d1ed0699614d3b2033e0ac4fd8f64c47826d4ab9e3499c10edf"}, "docker": "quay.io/biocontainers/bioconductor-humantranscriptomecompendium", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-humantranscriptomecompendium.
shpc-registry automated BioContainers addition for bioconductor-humantranscriptomecompendium
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-humantranscriptomecompendium
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-humantranscriptomecompendium:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-humantranscriptomecompendium/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-humantranscriptomecompendium/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-humantranscriptomecompendium-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humantranscriptomecompendium-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humantranscriptomecompendium-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-humantranscriptomecompendium-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-humantranscriptomecompendium-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-humantranscriptomecompendium-inspect-deffile:

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