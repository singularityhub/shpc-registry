---
layout: container
name:  "quay.io/biocontainers/bioconductor-motifdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-motifdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-motifdb/container.yaml"
updated_at: "2024-08-15 02:46:11.533478"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-motifdb"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-motifdb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-motifdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-motifdb", "latest": {"1.44.0--r43hdfd78af_0": "sha256:11e33cc40274b1fa6b0fda1d8367cac5183aa335b5c2c8556acb34b3224e7214"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:7c9d826ea1844851c22f124b384ee8ea5e99e66b82d3084ee8f37fd5460ec978", "1.40.0--r42hdfd78af_0": "sha256:be6b55f5f6f8c366a2dc6c1d737191d7a5b5ca8e38c91d50090b87d6ed122814", "1.42.0--r43hdfd78af_0": "sha256:ee5c8844faf634d8fc4bd58f1dae1b7378525cb185e151ad4a65f38b60a3e795", "1.44.0--r43hdfd78af_0": "sha256:11e33cc40274b1fa6b0fda1d8367cac5183aa335b5c2c8556acb34b3224e7214"}, "docker": "quay.io/biocontainers/bioconductor-motifdb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-motifdb.
shpc-registry automated BioContainers addition for bioconductor-motifdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-motifdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-motifdb:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-motifdb/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-motifdb/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-motifdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-motifdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-motifdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-motifdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-motifdb

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