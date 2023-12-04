---
layout: container
name:  "quay.io/biocontainers/bioconductor-clariomdhumantranscriptcluster.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clariomdhumantranscriptcluster.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clariomdhumantranscriptcluster.db/container.yaml"
updated_at: "2023-12-04 02:50:34.511964"
latest: "8.8.0--r43hdfd78af_3"
container_url: "https://biocontainers.pro/tools/bioconductor-clariomdhumantranscriptcluster.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
description: "shpc-registry automated BioContainers addition for bioconductor-clariomdhumantranscriptcluster.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clariomdhumantranscriptcluster.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clariomdhumantranscriptcluster.db", "latest": {"8.8.0--r43hdfd78af_3": "sha256:ab40d1466c3da99f3d904b8eaa7d0dec49a2ba488d6b2ec4f64d28df37009eb1"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:1677bb460b94b9afd5ca43b8cbb5beddea1c6d168aace34c9b132665bb2a9743", "8.8.0--r42hdfd78af_2": "sha256:675dfdb9400fe98c631d00a696f7b6307b14a5a806a3c1fdef74187a9eaac368", "8.8.0--r43hdfd78af_3": "sha256:ab40d1466c3da99f3d904b8eaa7d0dec49a2ba488d6b2ec4f64d28df37009eb1"}, "docker": "quay.io/biocontainers/bioconductor-clariomdhumantranscriptcluster.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clariomdhumantranscriptcluster.db.
shpc-registry automated BioContainers addition for bioconductor-clariomdhumantranscriptcluster.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clariomdhumantranscriptcluster.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clariomdhumantranscriptcluster.db:8.8.0--r43hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clariomdhumantranscriptcluster.db/8.8.0--r43hdfd78af_3
$ module help quay.io/biocontainers/bioconductor-clariomdhumantranscriptcluster.db/8.8.0--r43hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clariomdhumantranscriptcluster.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clariomdhumantranscriptcluster.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clariomdhumantranscriptcluster.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clariomdhumantranscriptcluster.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clariomdhumantranscriptcluster.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clariomdhumantranscriptcluster.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clariomdhumantranscriptcluster.db

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