---
layout: container
name:  "quay.io/biocontainers/bioconductor-nearbynding"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nearbynding/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nearbynding/container.yaml"
updated_at: "2024-09-02 02:55:34.947454"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nearbynding"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nearbynding"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nearbynding", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nearbynding", "latest": {"1.12.0--r43hdfd78af_0": "sha256:14005c7c4cf747a471a4d9c476b046dd6c29dc0d197d6268df4084f8e2130b5c"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:752f84cfd902beeab98f2e84810b0ce77752509710a079e46ff7a6bca6068ea6", "1.8.0--r42hdfd78af_0": "sha256:9b2aaac6bcdad960556faf4a52ceb81c855025f785b14892bda0a9af5e384542", "1.10.0--r43hdfd78af_0": "sha256:49f5a89fd750630cae1c633f97116a7e97616c3553d0bd29ec61563442171b6d", "1.12.0--r43hdfd78af_0": "sha256:14005c7c4cf747a471a4d9c476b046dd6c29dc0d197d6268df4084f8e2130b5c"}, "docker": "quay.io/biocontainers/bioconductor-nearbynding"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nearbynding.
shpc-registry automated BioContainers addition for bioconductor-nearbynding
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nearbynding
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nearbynding:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nearbynding/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nearbynding/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nearbynding-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nearbynding-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nearbynding-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nearbynding-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nearbynding-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nearbynding-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nearbynding

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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