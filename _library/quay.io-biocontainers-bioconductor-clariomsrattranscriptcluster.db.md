---
layout: container
name:  "quay.io/biocontainers/bioconductor-clariomsrattranscriptcluster.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clariomsrattranscriptcluster.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clariomsrattranscriptcluster.db/container.yaml"
updated_at: "2025-08-28 11:57:03.124864"
latest: "8.8.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-clariomsrattranscriptcluster.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
 - "8.8.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-clariomsrattranscriptcluster.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clariomsrattranscriptcluster.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clariomsrattranscriptcluster.db", "latest": {"8.8.0--r44hdfd78af_5": "sha256:a2c89d1bb060af8ec9e31f9a7a3df03b050d3c77e254cd2a32955314ebb665d0"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:189658ddc5090e08008ae762634f02f58e41480c586cc45868b69d5d4e308516", "8.8.0--r42hdfd78af_2": "sha256:e2f0d9807306fb0bd65c6aa601a0bc35f3f9f159adf242ba192715654aa9abb2", "8.8.0--r43hdfd78af_3": "sha256:808fa5507058140f5aa15a9a0d40171259c0c449e83757d8ef2d4ce758eed929", "8.8.0--r43hdfd78af_4": "sha256:3ab400582544bb5d5b677008c2b52a864bee69469e47190bc1334c3dcd4085c5", "8.8.0--r44hdfd78af_5": "sha256:a2c89d1bb060af8ec9e31f9a7a3df03b050d3c77e254cd2a32955314ebb665d0"}, "docker": "quay.io/biocontainers/bioconductor-clariomsrattranscriptcluster.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clariomsrattranscriptcluster.db.
shpc-registry automated BioContainers addition for bioconductor-clariomsrattranscriptcluster.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clariomsrattranscriptcluster.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clariomsrattranscriptcluster.db:8.8.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clariomsrattranscriptcluster.db/8.8.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-clariomsrattranscriptcluster.db/8.8.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clariomsrattranscriptcluster.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clariomsrattranscriptcluster.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clariomsrattranscriptcluster.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clariomsrattranscriptcluster.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clariomsrattranscriptcluster.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clariomsrattranscriptcluster.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clariomsrattranscriptcluster.db

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