---
layout: container
name:  "quay.io/biocontainers/bioconductor-amaretto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-amaretto/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-amaretto/container.yaml"
updated_at: "2024-12-10 03:36:06.996334"
latest: "1.18.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-amaretto"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.13.0--r42hc247a5b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.16.0--r43hf17093f_0"
 - "1.18.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-amaretto"
config: {"url": "https://biocontainers.pro/tools/bioconductor-amaretto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-amaretto", "latest": {"1.18.0--r43hf17093f_0": "sha256:4eb46292b93b839c6e60ea2ad823c8c2a1ffbf6d656490371f2a111ce8ac5525"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:49355276bdea97b7e66499fe76661ebe36d729e51f05642cbb6f6e54279a198b", "1.13.0--r42hc247a5b_0": "sha256:0e98bbc89881b4af5f37d1e63cfe9aa48993d5cbc1e0f3a1b1dd7a01f7398ead", "1.10.0--r41hc247a5b_2": "sha256:7001198fe654f446517ba9a7e4caaec0d887b9265dc06c34e73b7a4a7a44906b", "1.16.0--r43hf17093f_0": "sha256:47c54667e76381e772c77b941783ef3c9164257d53311d521b1b629582d7d1d0", "1.18.0--r43hf17093f_0": "sha256:4eb46292b93b839c6e60ea2ad823c8c2a1ffbf6d656490371f2a111ce8ac5525"}, "docker": "quay.io/biocontainers/bioconductor-amaretto", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-amaretto.
shpc-registry automated BioContainers addition for bioconductor-amaretto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-amaretto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-amaretto:1.18.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-amaretto/1.18.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-amaretto/1.18.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-amaretto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-amaretto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-amaretto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-amaretto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-amaretto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-amaretto-inspect-deffile:

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