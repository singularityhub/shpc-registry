---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellmixs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellmixs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellmixs/container.yaml"
updated_at: "2024-06-26 02:53:50.206580"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellmixs"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellmixs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellmixs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellmixs", "latest": {"1.18.0--r43hdfd78af_0": "sha256:edc653f92f67985da0557072f6847d363e2bf261abe142561ae96e29b88ae624"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:b8b39cbc552026a2ba902a10f94ab80b1831d78f861c4cce8dde9ef06e5c3b33", "1.14.0--r42hdfd78af_0": "sha256:6f987aaf0a0382ee040cf0e7b42f16a244db3a5106e00e7aef115f8593c03fde", "1.10.0--r41hdfd78af_0": "sha256:201c6683ad16559140f9abd858d9cb206a52297b1d7e04bb6115eef2f100ccc6", "1.16.0--r43hdfd78af_0": "sha256:77958c944587417fd93f8efb201bb53c08da3f25b05b3ecdc0617389d0f68acb", "1.18.0--r43hdfd78af_0": "sha256:edc653f92f67985da0557072f6847d363e2bf261abe142561ae96e29b88ae624"}, "docker": "quay.io/biocontainers/bioconductor-cellmixs", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellmixs.
shpc-registry automated BioContainers addition for bioconductor-cellmixs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellmixs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellmixs:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellmixs/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellmixs/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellmixs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellmixs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellmixs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellmixs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellmixs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellmixs-inspect-deffile:

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