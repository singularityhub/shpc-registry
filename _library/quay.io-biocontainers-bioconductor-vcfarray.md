---
layout: container
name:  "quay.io/biocontainers/bioconductor-vcfarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vcfarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vcfarray/container.yaml"
updated_at: "2024-06-24 03:33:24.240102"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-vcfarray"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-vcfarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vcfarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vcfarray", "latest": {"1.18.0--r43hdfd78af_0": "sha256:70895e920cd270b881c5ef5242b105f92688fbadf38a928a089132126e49edf8"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:e14e6e6d6c2e49f7bdd88222c7a5d94097b84e2432a22b91f3d69162687e8a13", "1.10.0--r41hdfd78af_0": "sha256:8fc8ed6c1b17a35e493d904edf2ac91f2884501545bb8d77e8fc3f1ebb185b0c", "1.14.0--r42hdfd78af_0": "sha256:847726f69b73dde60d677078e4c351174a5753cfde0a5653070e9c950f6b536e", "1.16.0--r43hdfd78af_0": "sha256:4e5650db46819dd47a423a745eacca91cdb2514bff7b7f8588d9ecc1702490c0", "1.18.0--r43hdfd78af_0": "sha256:70895e920cd270b881c5ef5242b105f92688fbadf38a928a089132126e49edf8"}, "docker": "quay.io/biocontainers/bioconductor-vcfarray", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vcfarray.
shpc-registry automated BioContainers addition for bioconductor-vcfarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vcfarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vcfarray:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vcfarray/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-vcfarray/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vcfarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vcfarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vcfarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vcfarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vcfarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vcfarray-inspect-deffile:

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