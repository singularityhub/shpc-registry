---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgug4112a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgug4112a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgug4112a.db/container.yaml"
updated_at: "2025-06-24 03:25:43.060885"
latest: "3.2.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgug4112a.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgug4112a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgug4112a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgug4112a.db", "latest": {"3.2.3--r44hdfd78af_13": "sha256:8a6485c20ff550f5be2329d26cb6b3c648d46aca56b2f039adbe570b1b352935"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:c75fd77ba4f5ae454d2f09bcca17d0de87eb276812780830898e5e3895bada70", "3.2.3--r42hdfd78af_10": "sha256:6555ff15c7a978b936b5b755ae5151f46d1fe6c343f84781ad70bdc2f27b8801", "3.2.3--r43hdfd78af_11": "sha256:9f127375ef665ef2124445f18952e1be401eff6d68ce50ce04fb9083f1b04fa5", "3.2.3--r43hdfd78af_12": "sha256:e4043a929c3011c5dc03b942612c44e0398bd08ef47ae15dbce83153c178748f", "3.2.3--r44hdfd78af_13": "sha256:8a6485c20ff550f5be2329d26cb6b3c648d46aca56b2f039adbe570b1b352935"}, "docker": "quay.io/biocontainers/bioconductor-hgug4112a.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgug4112a.db.
shpc-registry automated BioContainers addition for bioconductor-hgug4112a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4112a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4112a.db:3.2.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgug4112a.db/3.2.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgug4112a.db/3.2.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgug4112a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4112a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4112a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgug4112a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgug4112a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgug4112a.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgug4112a.db

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