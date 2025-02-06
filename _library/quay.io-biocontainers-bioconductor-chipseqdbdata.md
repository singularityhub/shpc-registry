---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipseqdbdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipseqdbdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipseqdbdata/container.yaml"
updated_at: "2025-02-06 02:50:20.417393"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipseqdbdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipseqdbdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipseqdbdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipseqdbdata", "latest": {"1.22.0--r44hdfd78af_0": "sha256:5f0fd81a6029bd4ae5e68f9b95d188cb37ef37f05032b63a478d4fdc9d4fc5ba"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:1798d36de69a42f2c3225255bad93d5421dedc908baf21d844deab8599e188ea", "1.14.0--r42hdfd78af_0": "sha256:e29afec74570ed887e76f6b3e7e920fe33018cd014a6b9ebc9a462352375201e", "1.10.0--r41hdfd78af_1": "sha256:8983da645500ef2e1fb8532bb49a59c6a85505b2558544fbe927b849e0fce084", "1.16.0--r43hdfd78af_0": "sha256:c874b9d93187cb59def46d0b04b60e474e79b760ff3ec99f690eed73154ad9d6", "1.18.0--r43hdfd78af_0": "sha256:e19f9d687ce8505e6359f5414a22ff6767a9daa251746fb5633e9b7562ad5efc", "1.22.0--r44hdfd78af_0": "sha256:5f0fd81a6029bd4ae5e68f9b95d188cb37ef37f05032b63a478d4fdc9d4fc5ba"}, "docker": "quay.io/biocontainers/bioconductor-chipseqdbdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipseqdbdata.
shpc-registry automated BioContainers addition for bioconductor-chipseqdbdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipseqdbdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipseqdbdata:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipseqdbdata/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chipseqdbdata/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipseqdbdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipseqdbdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipseqdbdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipseqdbdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipseqdbdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipseqdbdata-inspect-deffile:

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