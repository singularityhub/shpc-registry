---
layout: container
name:  "quay.io/biocontainers/bioconductor-mafdb.topmed.freeze5.hg38"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mafdb.topmed.freeze5.hg38/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mafdb.topmed.freeze5.hg38/container.yaml"
updated_at: "2025-07-28 04:24:26.677259"
latest: "3.10.0--r43hdfd78af_9"
container_url: "https://biocontainers.pro/tools/bioconductor-mafdb.topmed.freeze5.hg38"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.9.0--r36_1"
 - "3.10.0--r41hdfd78af_6"
 - "3.10.0--r42hdfd78af_7"
 - "3.10.0--r43hdfd78af_8"
 - "3.10.0--r43hdfd78af_9"
description: "shpc-registry automated BioContainers addition for bioconductor-mafdb.topmed.freeze5.hg38"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mafdb.topmed.freeze5.hg38", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mafdb.topmed.freeze5.hg38", "latest": {"3.10.0--r43hdfd78af_9": "sha256:27a5a9a5ec2cb097222edac689edb034eae2e3b5623a2c65415179e5a3d6ad9a"}, "tags": {"3.9.0--r36_1": "sha256:6ea840942c00d7a2a77ced39b4c67b492828b004a0f1ab6890985bd8c1fc3756", "3.10.0--r41hdfd78af_6": "sha256:70c6059962766b16b6f4edbbe3a7d97f104e86eac5137d504d028ce2ce01a317", "3.10.0--r42hdfd78af_7": "sha256:9c7106b3ce8c5c0281bb3c0b03275b8065f00e03d658869b706d49a1a650ff99", "3.10.0--r43hdfd78af_8": "sha256:d9d7e899daa99ff48407d02748e8b323c801f9a7c2af1bcd3205e24829d5ca81", "3.10.0--r43hdfd78af_9": "sha256:27a5a9a5ec2cb097222edac689edb034eae2e3b5623a2c65415179e5a3d6ad9a"}, "docker": "quay.io/biocontainers/bioconductor-mafdb.topmed.freeze5.hg38", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mafdb.topmed.freeze5.hg38.
shpc-registry automated BioContainers addition for bioconductor-mafdb.topmed.freeze5.hg38
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.topmed.freeze5.hg38
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.topmed.freeze5.hg38:3.10.0--r43hdfd78af_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mafdb.topmed.freeze5.hg38/3.10.0--r43hdfd78af_9
$ module help quay.io/biocontainers/bioconductor-mafdb.topmed.freeze5.hg38/3.10.0--r43hdfd78af_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mafdb.topmed.freeze5.hg38-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.topmed.freeze5.hg38-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.topmed.freeze5.hg38-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mafdb.topmed.freeze5.hg38-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mafdb.topmed.freeze5.hg38-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mafdb.topmed.freeze5.hg38-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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