---
layout: container
name:  "quay.io/biocontainers/bioconductor-hyper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hyper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hyper/container.yaml"
updated_at: "2024-03-19 02:42:09.505683"
latest: "2.0.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hyper"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "2.0.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hyper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hyper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hyper", "latest": {"2.0.0--r43hdfd78af_0": "sha256:964b03f75a160e2faa35caece309dadc67095b12feabdd1b9a664ad7b98b74a7"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:0b163476a3c66ecd48d81d9440bc0eb902a6cc162077688a8b0f9ba5371c85e4", "1.14.0--r42hdfd78af_0": "sha256:8b7a8e000e78fcfa6f3242e2d17bd577921e73a6570f2d7d369f483d6370f9db", "1.10.0--r41hdfd78af_0": "sha256:73b95b67e3e04a0d6bd143936135295457a761fca3b0eaeadac0f0658efb5beb", "2.0.0--r43hdfd78af_0": "sha256:964b03f75a160e2faa35caece309dadc67095b12feabdd1b9a664ad7b98b74a7"}, "docker": "quay.io/biocontainers/bioconductor-hyper", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hyper.
shpc-registry automated BioContainers addition for bioconductor-hyper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hyper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hyper:2.0.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hyper/2.0.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hyper/2.0.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hyper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hyper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hyper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hyper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hyper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hyper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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