---
layout: container
name:  "quay.io/biocontainers/bioconductor-scruff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scruff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scruff/container.yaml"
updated_at: "2024-05-20 03:06:48.307649"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scruff"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.3--r40hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scruff"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scruff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scruff", "latest": {"1.20.0--r43hdfd78af_0": "sha256:4cae317298021202b6f19d7f7f46d53eb153c9ac92f32c40d3bd42d3aeb4affc"}, "tags": {"1.8.3--r40hdfd78af_0": "sha256:9c1966ee7352b7f2b2bdeb23a825f8d37b66442da151cc87d635c3ce5049de01", "1.16.0--r42hdfd78af_0": "sha256:522044f27136c39958a2f0f58286b728305920fc36225960d180666b2e4a04fd", "1.12.0--r41hdfd78af_0": "sha256:65b114ae97f04f318e0b2529c61274c9ed4b52b2731ccc8dfe6d6a5e24a7c621", "1.10.0--r41hdfd78af_0": "sha256:e863f1f408534c5b9578eeea216ed6bd58ac10147bdf744b7d30c63cd82d95f4", "1.18.0--r43hdfd78af_0": "sha256:3d53c279e39885590ae549f4baaba3e99effb005e6be170e40647f659aa93ac0", "1.20.0--r43hdfd78af_0": "sha256:4cae317298021202b6f19d7f7f46d53eb153c9ac92f32c40d3bd42d3aeb4affc"}, "docker": "quay.io/biocontainers/bioconductor-scruff", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scruff.
shpc-registry automated BioContainers addition for bioconductor-scruff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scruff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scruff:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scruff/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scruff/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scruff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scruff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scruff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scruff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scruff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scruff-inspect-deffile:

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