---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgug4101a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgug4101a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgug4101a.db/container.yaml"
updated_at: "2024-05-27 03:03:46.074726"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgug4101a.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgug4101a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgug4101a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgug4101a.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:88248d7b77a5e51c585a637fd267d1f61d0f98253acd4e53df8bf0c8b8b6901b"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:8912ddf1ef5f8dea264dc725dae5c7fb7aa41cc6e3956b2b52b7fcc8f4bc2241", "3.2.3--r42hdfd78af_10": "sha256:3249eb9d9850e42426446a42b035c09a69ab258672667075acf42b9c8100c911", "3.2.3--r43hdfd78af_11": "sha256:288370bea7b69c5ef2f2e52dfc106c115b208b06c6a59c5c42f27ed65740d896", "3.2.3--r43hdfd78af_12": "sha256:88248d7b77a5e51c585a637fd267d1f61d0f98253acd4e53df8bf0c8b8b6901b"}, "docker": "quay.io/biocontainers/bioconductor-hgug4101a.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgug4101a.db.
shpc-registry automated BioContainers addition for bioconductor-hgug4101a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4101a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4101a.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgug4101a.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgug4101a.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgug4101a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4101a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4101a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgug4101a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgug4101a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgug4101a.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgug4101a.db

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