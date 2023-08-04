---
layout: container
name:  "quay.io/biocontainers/bioconductor-msigdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msigdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msigdb/container.yaml"
updated_at: "2023-08-04 02:43:51.824446"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msigdb"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msigdb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msigdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msigdb", "latest": {"1.8.0--r43hdfd78af_0": "sha256:2e1fe667031089af37ba30de84c0f65bd2125a804caf2e70114b76d8fffdc762"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:105b75f44eb682c377b06dcf11879d1f0e8df04b3e0eb6f722130e81981b35d4", "1.6.0--r42hdfd78af_0": "sha256:5ae148f6b21c1ef28254b8b3a4454b624b062c4e2c4d7c550ef0c30716daa144", "1.8.0--r43hdfd78af_0": "sha256:2e1fe667031089af37ba30de84c0f65bd2125a804caf2e70114b76d8fffdc762"}, "docker": "quay.io/biocontainers/bioconductor-msigdb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msigdb.
shpc-registry automated BioContainers addition for bioconductor-msigdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msigdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msigdb:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msigdb/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msigdb/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msigdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msigdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msigdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msigdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msigdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msigdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msigdb

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