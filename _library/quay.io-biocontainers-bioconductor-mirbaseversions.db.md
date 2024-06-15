---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirbaseversions.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirbaseversions.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirbaseversions.db/container.yaml"
updated_at: "2024-06-15 02:35:47.984109"
latest: "1.1.0--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mirbaseversions.db"

versions:
 - "1.1.0--r41hdfd78af_9"
 - "1.1.0--r42hdfd78af_11"
 - "1.1.0--r43hdfd78af_12"
 - "1.1.0--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mirbaseversions.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirbaseversions.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirbaseversions.db", "latest": {"1.1.0--r43hdfd78af_13": "sha256:3222955c0dea6c81e92d714bcdd852199ddd07fda5d45e54aac2d80db5956323"}, "tags": {"1.1.0--r41hdfd78af_9": "sha256:0d4bb11653288d0dfc50fb48fdde0de08560565615831426a09ed65cb4c0b80a", "1.1.0--r42hdfd78af_11": "sha256:c5d3acc4ff8a944677e639de0886338d7a3cf5d0989efbcafb75e35e914a2b64", "1.1.0--r43hdfd78af_12": "sha256:4fbbdbacb2784e3093fb7650795c6dd279b0a9c54c18d8ba3011a5891e4dbae2", "1.1.0--r43hdfd78af_13": "sha256:3222955c0dea6c81e92d714bcdd852199ddd07fda5d45e54aac2d80db5956323"}, "docker": "quay.io/biocontainers/bioconductor-mirbaseversions.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirbaseversions.db.
shpc-registry automated BioContainers addition for bioconductor-mirbaseversions.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirbaseversions.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirbaseversions.db:1.1.0--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirbaseversions.db/1.1.0--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mirbaseversions.db/1.1.0--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirbaseversions.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirbaseversions.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirbaseversions.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirbaseversions.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirbaseversions.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirbaseversions.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirbaseversions.db

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