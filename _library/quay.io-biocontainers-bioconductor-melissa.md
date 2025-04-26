---
layout: container
name:  "quay.io/biocontainers/bioconductor-melissa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-melissa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-melissa/container.yaml"
updated_at: "2025-04-26 03:06:09.365978"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-melissa"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-melissa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-melissa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-melissa", "latest": {"1.22.0--r44hdfd78af_0": "sha256:c71a24df5ddba8be4b01fbbeb26cba5eecc05388c90acf2a3f9f6a20b27c7f95"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:1fc4198d6dfcbe21d94fd51ce0e3fc18226479f8dd0253dc569c860b5983fb2c", "1.10.0--r41hdfd78af_0": "sha256:12fd37e0271f4be8b437b51a44ec918ca99a15526567bbb1798acccd84a0edc8", "1.14.0--r42hdfd78af_0": "sha256:8a06366405427896ce1917ade8f6aec666b366b7acd490bc4f15ca4ba4800a88", "1.16.0--r43hdfd78af_0": "sha256:ecc09fd1a986fc9f1b6bd57614933dec6c18dc1afc8a03c648bd4376b38ef388", "1.18.0--r43hdfd78af_0": "sha256:d037df4fc7df48d22eeec3f536af01abc46c03c6d2c97ae199f49ed468f1cb8b", "1.22.0--r44hdfd78af_0": "sha256:c71a24df5ddba8be4b01fbbeb26cba5eecc05388c90acf2a3f9f6a20b27c7f95"}, "docker": "quay.io/biocontainers/bioconductor-melissa", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-melissa.
shpc-registry automated BioContainers addition for bioconductor-melissa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-melissa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-melissa:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-melissa/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-melissa/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-melissa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-melissa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-melissa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-melissa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-melissa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-melissa-inspect-deffile:

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