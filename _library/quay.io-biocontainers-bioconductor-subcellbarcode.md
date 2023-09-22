---
layout: container
name:  "quay.io/biocontainers/bioconductor-subcellbarcode"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-subcellbarcode/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-subcellbarcode/container.yaml"
updated_at: "2023-09-22 04:24:59.954684"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-subcellbarcode"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-subcellbarcode"
config: {"url": "https://biocontainers.pro/tools/bioconductor-subcellbarcode", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-subcellbarcode", "latest": {"1.16.0--r43hdfd78af_0": "sha256:bb2c8d9be9cb8f1f89830602319271fed6740e3f3f0501ad28316097af3ca743"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:87d95b32a81f52a6c5bfe7e5524124d7f9721ea62995c498d34ea5b71070a129", "1.14.0--r42hdfd78af_0": "sha256:2cee52d8223da45f20e5f79871367eeae4358e7f76d3abc840bd9e39c6c0d558", "1.10.0--r41hdfd78af_0": "sha256:1a367fe71da58e50c3617b66ef7222b87832e1b65be3353ff23c3f4c32349fe3", "1.16.0--r43hdfd78af_0": "sha256:bb2c8d9be9cb8f1f89830602319271fed6740e3f3f0501ad28316097af3ca743"}, "docker": "quay.io/biocontainers/bioconductor-subcellbarcode", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-subcellbarcode.
shpc-registry automated BioContainers addition for bioconductor-subcellbarcode
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-subcellbarcode
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-subcellbarcode:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-subcellbarcode/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-subcellbarcode/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-subcellbarcode-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-subcellbarcode-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-subcellbarcode-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-subcellbarcode-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-subcellbarcode-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-subcellbarcode-inspect-deffile:

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