---
layout: container
name:  "quay.io/biocontainers/bioconductor-trnadbimport"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-trnadbimport/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-trnadbimport/container.yaml"
updated_at: "2024-08-09 02:56:40.702607"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-trnadbimport"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-trnadbimport"
config: {"url": "https://biocontainers.pro/tools/bioconductor-trnadbimport", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-trnadbimport", "latest": {"1.20.0--r43hdfd78af_0": "sha256:5d0a32d6665c9b5274bdddf4b6f3bfe415a12371e599517dd625bf252e7942be"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:8ae6e1daf09f6370170f98a11526c2bf0cc86ed0ff28e14fce23a78e0840e37b", "1.16.0--r42hdfd78af_0": "sha256:c90f1057ee7ad3c83febb361a1db4afbc98c441fe7337ad49e50caed4372123b", "1.12.0--r41hdfd78af_0": "sha256:87c0a63cc737d26139c1e0cf1b0fca1264334baf9370ee2afce2d69f717dbe43", "1.10.0--r41hdfd78af_0": "sha256:ba07f60d00970076d6d2699d0b152156375ae63c70951d1a658119439deacccd", "1.18.0--r43hdfd78af_0": "sha256:25248939062678f01fa4cc76e591c02ab268755f3a1234395a592c26b1f5d996", "1.20.0--r43hdfd78af_0": "sha256:5d0a32d6665c9b5274bdddf4b6f3bfe415a12371e599517dd625bf252e7942be"}, "docker": "quay.io/biocontainers/bioconductor-trnadbimport", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-trnadbimport.
shpc-registry automated BioContainers addition for bioconductor-trnadbimport
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-trnadbimport
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-trnadbimport:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-trnadbimport/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-trnadbimport/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-trnadbimport-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trnadbimport-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trnadbimport-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-trnadbimport-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-trnadbimport-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-trnadbimport-inspect-deffile:

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