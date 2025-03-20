---
layout: container
name:  "quay.io/biocontainers/bioconductor-mogene11sttranscriptcluster.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mogene11sttranscriptcluster.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mogene11sttranscriptcluster.db/container.yaml"
updated_at: "2025-03-20 03:22:49.990999"
latest: "8.8.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-mogene11sttranscriptcluster.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
 - "8.8.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-mogene11sttranscriptcluster.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mogene11sttranscriptcluster.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mogene11sttranscriptcluster.db", "latest": {"8.8.0--r44hdfd78af_5": "sha256:3d12409fe070f3d3c1bee2fa5fbc1dd4db830a8adcc8eda71fcc7486554ed71a"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:66989358ba2576555c1ba9961f4cd54db1dd4625f3ee850fcec03f10f95dd3d6", "8.8.0--r42hdfd78af_2": "sha256:a013c75ff4de4a44ebdfb6773bd57d9e103c6e62b10513e1b302e7f4c3855a4a", "8.8.0--r43hdfd78af_3": "sha256:b75c23fc0974c12cf0fe63531f775ba52cdfea0eaf87d226da1d28d7b9c57cb9", "8.8.0--r43hdfd78af_4": "sha256:57bb5f269958889f88534c76f5b9249053612eedd51c549d3917bc5f3be1b24e", "8.8.0--r44hdfd78af_5": "sha256:3d12409fe070f3d3c1bee2fa5fbc1dd4db830a8adcc8eda71fcc7486554ed71a"}, "docker": "quay.io/biocontainers/bioconductor-mogene11sttranscriptcluster.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mogene11sttranscriptcluster.db.
shpc-registry automated BioContainers addition for bioconductor-mogene11sttranscriptcluster.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene11sttranscriptcluster.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene11sttranscriptcluster.db:8.8.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mogene11sttranscriptcluster.db/8.8.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-mogene11sttranscriptcluster.db/8.8.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mogene11sttranscriptcluster.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene11sttranscriptcluster.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene11sttranscriptcluster.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mogene11sttranscriptcluster.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mogene11sttranscriptcluster.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mogene11sttranscriptcluster.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mogene11sttranscriptcluster.db

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