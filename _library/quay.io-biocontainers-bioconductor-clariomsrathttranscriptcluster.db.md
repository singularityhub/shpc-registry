---
layout: container
name:  "quay.io/biocontainers/bioconductor-clariomsrathttranscriptcluster.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clariomsrathttranscriptcluster.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clariomsrathttranscriptcluster.db/container.yaml"
updated_at: "2025-08-23 03:46:18.164605"
latest: "8.8.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-clariomsrathttranscriptcluster.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
 - "8.8.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-clariomsrathttranscriptcluster.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clariomsrathttranscriptcluster.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clariomsrathttranscriptcluster.db", "latest": {"8.8.0--r44hdfd78af_5": "sha256:89dd061e80c08bd09ae19b1d061556e32343a040d1a16e465769662b957e9a9f"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:ebbee41051384a5872c422615d00d0f63ecefbe518d925a6d9b5ad1f1b253895", "8.8.0--r42hdfd78af_2": "sha256:ce0ea7eefdb2717d041b788501576706392b767d0251cb0f6540a460316d2952", "8.8.0--r43hdfd78af_3": "sha256:874be30950fa546720aad46a7053b9c36e34e2883cf21a0231d5de95856b05fb", "8.8.0--r43hdfd78af_4": "sha256:2b541eb0bdb8d31faca33f4c93fb44cbb31aa75fb6771674bd25cc82f92da042", "8.8.0--r44hdfd78af_5": "sha256:89dd061e80c08bd09ae19b1d061556e32343a040d1a16e465769662b957e9a9f"}, "docker": "quay.io/biocontainers/bioconductor-clariomsrathttranscriptcluster.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clariomsrathttranscriptcluster.db.
shpc-registry automated BioContainers addition for bioconductor-clariomsrathttranscriptcluster.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clariomsrathttranscriptcluster.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clariomsrathttranscriptcluster.db:8.8.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clariomsrathttranscriptcluster.db/8.8.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-clariomsrathttranscriptcluster.db/8.8.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clariomsrathttranscriptcluster.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clariomsrathttranscriptcluster.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clariomsrathttranscriptcluster.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clariomsrathttranscriptcluster.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clariomsrathttranscriptcluster.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clariomsrathttranscriptcluster.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clariomsrathttranscriptcluster.db

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