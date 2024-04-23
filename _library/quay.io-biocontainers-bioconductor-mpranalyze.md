---
layout: container
name:  "quay.io/biocontainers/bioconductor-mpranalyze"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mpranalyze/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mpranalyze/container.yaml"
updated_at: "2024-04-23 03:08:03.764498"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mpranalyze"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mpranalyze"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mpranalyze", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mpranalyze", "latest": {"1.20.0--r43hdfd78af_0": "sha256:22f1232771f5db146974204fd9311569fa3f4a70081474631531d435af3f4ed8"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:a4d8d593d82bb3143a2a6f34918b152cbef6e95e1a6aa8430684f983d6773b94", "1.16.0--r42hdfd78af_0": "sha256:df3d918ef217c510308933c1bfbe07999869be0541f2369bb3516a07392979c2", "1.12.0--r41hdfd78af_0": "sha256:a576246055c96d7ae368630ace69172f72b63431e4ab6a9854dda9570e2d80a4", "1.10.0--r41hdfd78af_0": "sha256:6568bfe9e2903981adcc79260c177eac07d85ee737d097290c25f877a0c4c1e0", "1.18.0--r43hdfd78af_0": "sha256:be10a5623ff53f4f949cb4fcc9bcb96db5513901e6b7e6f808d096e680374cd9", "1.20.0--r43hdfd78af_0": "sha256:22f1232771f5db146974204fd9311569fa3f4a70081474631531d435af3f4ed8"}, "docker": "quay.io/biocontainers/bioconductor-mpranalyze", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mpranalyze.
shpc-registry automated BioContainers addition for bioconductor-mpranalyze
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mpranalyze
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mpranalyze:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mpranalyze/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mpranalyze/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mpranalyze-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mpranalyze-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mpranalyze-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mpranalyze-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mpranalyze-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mpranalyze-inspect-deffile:

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