---
layout: container
name:  "quay.io/biocontainers/bioconductor-bloodgen3module"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bloodgen3module/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bloodgen3module/container.yaml"
updated_at: "2023-11-02 02:47:37.123231"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bloodgen3module"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bloodgen3module"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bloodgen3module", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bloodgen3module", "latest": {"1.8.0--r43hdfd78af_0": "sha256:fb3f8ec0b92d26dc4f33790fa34de5c800560ea95f34ad5a855a1d64500b1f9d"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:8c461765947d56f7ce100df00bd03a9034e46175f8f55e112f6bc3293bcc7ec2", "1.6.0--r42hdfd78af_0": "sha256:5414f3a6aabc6ad1604e4012166ac0e4b06cb2a01b159f6d678f29ca4a27d93b", "1.8.0--r43hdfd78af_0": "sha256:fb3f8ec0b92d26dc4f33790fa34de5c800560ea95f34ad5a855a1d64500b1f9d"}, "docker": "quay.io/biocontainers/bioconductor-bloodgen3module", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bloodgen3module.
shpc-registry automated BioContainers addition for bioconductor-bloodgen3module
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bloodgen3module
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bloodgen3module:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bloodgen3module/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bloodgen3module/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bloodgen3module-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bloodgen3module-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bloodgen3module-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bloodgen3module-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bloodgen3module-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bloodgen3module-inspect-deffile:

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