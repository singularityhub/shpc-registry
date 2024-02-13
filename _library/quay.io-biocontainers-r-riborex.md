---
layout: container
name:  "quay.io/biocontainers/r-riborex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-riborex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-riborex/container.yaml"
updated_at: "2024-02-13 02:36:37.148213"
latest: "2.4.0--r43hdfd78af_6"
container_url: "https://biocontainers.pro/tools/r-riborex"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.4.0--r41hdfd78af_4"
 - "2.4.0--r42hdfd78af_5"
 - "2.4.0--r43hdfd78af_6"
description: "shpc-registry automated BioContainers addition for r-riborex"
config: {"url": "https://biocontainers.pro/tools/r-riborex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-riborex", "latest": {"2.4.0--r43hdfd78af_6": "sha256:3bc330538d52456f8a31a570d406498bf645f04f76801dd59d6272d2bb0ffb81"}, "tags": {"2.4.0--r41hdfd78af_4": "sha256:5badb161dee10a0fda67424b48590b053c5cdac90d1d872401c1608aa137edbf", "2.4.0--r42hdfd78af_5": "sha256:fb9ee3cadec743b2e647abcfb8cc6b7d1fea168090c14c3e599adc34cf18bc4b", "2.4.0--r43hdfd78af_6": "sha256:3bc330538d52456f8a31a570d406498bf645f04f76801dd59d6272d2bb0ffb81"}, "docker": "quay.io/biocontainers/r-riborex", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-riborex.
shpc-registry automated BioContainers addition for r-riborex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-riborex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-riborex:2.4.0--r43hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-riborex/2.4.0--r43hdfd78af_6
$ module help quay.io/biocontainers/r-riborex/2.4.0--r43hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-riborex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-riborex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-riborex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-riborex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-riborex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-riborex-inspect-deffile:

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