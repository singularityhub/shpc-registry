---
layout: container
name:  "quay.io/biocontainers/bioconductor-dmrcatedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dmrcatedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dmrcatedata/container.yaml"
updated_at: "2022-11-21 14:11:48.167037"
latest: "2.12.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-dmrcatedata"
aliases:
 - ".bioconductor-dmrcatedata-post-link.sh"
 - ".bioconductor-dmrcatedata-pre-unlink.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.2--r40hdfd78af_0"
 - "2.12.0--r41hdfd78af_1"
 - "2.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dmrcatedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dmrcatedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dmrcatedata", "latest": {"2.12.0--r41hdfd78af_1": "sha256:31ad58455c867a9d0202511a063d302e7d386f3142832b469b07eccca1995110"}, "tags": {"2.8.2--r40hdfd78af_0": "sha256:c7ef6b53cad4c69d79a11e3aaa797be3e4c7c32d116061464e7bba4ca9ad50c3", "2.12.0--r41hdfd78af_1": "sha256:31ad58455c867a9d0202511a063d302e7d386f3142832b469b07eccca1995110", "2.10.0--r41hdfd78af_0": "sha256:610e15a7a78ad53df655be17c775f821aa7d694dcbb786f4d55e96a46c9000d0"}, "docker": "quay.io/biocontainers/bioconductor-dmrcatedata", "aliases": {".bioconductor-dmrcatedata-post-link.sh": "/usr/local/bin/.bioconductor-dmrcatedata-post-link.sh", ".bioconductor-dmrcatedata-pre-unlink.sh": "/usr/local/bin/.bioconductor-dmrcatedata-pre-unlink.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dmrcatedata.
shpc-registry automated BioContainers addition for bioconductor-dmrcatedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dmrcatedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dmrcatedata:2.12.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dmrcatedata/2.12.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-dmrcatedata/2.12.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dmrcatedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmrcatedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmrcatedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dmrcatedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dmrcatedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dmrcatedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-dmrcatedata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-dmrcatedata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-dmrcatedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-dmrcatedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-dmrcatedata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-dmrcatedata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-dmrcatedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-dmrcatedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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