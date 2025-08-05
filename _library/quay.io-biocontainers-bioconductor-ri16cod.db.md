---
layout: container
name:  "quay.io/biocontainers/bioconductor-ri16cod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ri16cod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ri16cod.db/container.yaml"
updated_at: "2025-08-05 04:29:20.477575"
latest: "3.4.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-ri16cod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
 - "3.4.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-ri16cod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ri16cod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ri16cod.db", "latest": {"3.4.0--r44hdfd78af_13": "sha256:a46ffa416226d3a8887b376e4939885b96854f8075c0e2547b93aae45f8f95bc"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:b58b7c57b1125963c967eb04b56a0410bff78ee44b8f115110f5bc01a0b3f425", "3.4.0--r42hdfd78af_10": "sha256:1ed4d020c2df1455654e78992fab660d47b44c8a1e6da62d99251e23d3258f24", "3.4.0--r43hdfd78af_11": "sha256:1b1a01dcb16c3da673b2a0d9918eb8cc62ffd3960a66c8db3e2bfe10d134d731", "3.4.0--r43hdfd78af_12": "sha256:d3eb712eb5c3edb8cde1f7f7d09b4c92c2f1769414cd383ee6ddac2baad0dd40", "3.4.0--r44hdfd78af_13": "sha256:a46ffa416226d3a8887b376e4939885b96854f8075c0e2547b93aae45f8f95bc"}, "docker": "quay.io/biocontainers/bioconductor-ri16cod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ri16cod.db.
shpc-registry automated BioContainers addition for bioconductor-ri16cod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ri16cod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ri16cod.db:3.4.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ri16cod.db/3.4.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-ri16cod.db/3.4.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ri16cod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ri16cod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ri16cod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ri16cod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ri16cod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ri16cod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ri16cod.db

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