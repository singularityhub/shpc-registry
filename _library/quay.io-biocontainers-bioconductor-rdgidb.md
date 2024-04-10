---
layout: container
name:  "quay.io/biocontainers/bioconductor-rdgidb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rdgidb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rdgidb/container.yaml"
updated_at: "2024-04-10 03:00:38.163412"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rdgidb"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rdgidb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rdgidb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rdgidb", "latest": {"1.28.0--r43hdfd78af_0": "sha256:b9d73352113e6205373c5d211b0d95afbd44392b735059bcccd49a04dcef75ca"}, "tags": {"1.8.0--r351_0": "sha256:03d4a258693bb5a22c87be151e96c7f872e168f5f1bec93f29bc80ab439ea056", "1.24.0--r42hdfd78af_0": "sha256:a7645123876dfb1cd987bfe196e6d861b7ba3cf65011ee702143923984750ab3", "1.20.0--r41hdfd78af_0": "sha256:6e25c02c051d5b3c1179cd035723ab13db6b0936c2002ce7e727d9808a9256b2", "1.18.0--r41hdfd78af_0": "sha256:323b6ad64f6b3ac64e611290a4897ed4435573fa17e7a729648446616170eac7", "1.16.0--r40hdfd78af_1": "sha256:4dcbfa7cf01d7e4c86c9b3d9415a89596412c85148c97d91b8e77a18c094625a", "1.14.0--r40_0": "sha256:2eedba1f3df26532034236d2d717801ba324650b02d32b998bf96d208af1fe18", "1.26.0--r43hdfd78af_0": "sha256:50d3efd8ed8a9d7d46402d31e6f37c89d97338d0769cc83884ae2ce73654ebdf", "1.28.0--r43hdfd78af_0": "sha256:b9d73352113e6205373c5d211b0d95afbd44392b735059bcccd49a04dcef75ca"}, "docker": "quay.io/biocontainers/bioconductor-rdgidb", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rdgidb.
shpc-registry automated BioContainers addition for bioconductor-rdgidb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rdgidb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rdgidb:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rdgidb/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rdgidb/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rdgidb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rdgidb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rdgidb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rdgidb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rdgidb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rdgidb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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