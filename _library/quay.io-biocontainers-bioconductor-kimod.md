---
layout: container
name:  "quay.io/biocontainers/bioconductor-kimod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-kimod/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-kimod/container.yaml"
updated_at: "2023-04-15 02:32:52.101961"
latest: "1.15.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-kimod"

versions:
 - "1.8.0--r351_0"
 - "1.15.0--r40_0"
 - "1.14.0--r36_0"
 - "1.12.0--r36_1"
 - "1.10.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-kimod"
config: {"url": "https://biocontainers.pro/tools/bioconductor-kimod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-kimod", "latest": {"1.15.0--r40_0": "sha256:621ee0a4ceca20409a7d9c09d71fda39722f6172b55352d7e763737d685d8836"}, "tags": {"1.8.0--r351_0": "sha256:dec288df1090f703076c9ce884eae19d07d6ccec4cd96fd7c8af87ecf151d272", "1.15.0--r40_0": "sha256:621ee0a4ceca20409a7d9c09d71fda39722f6172b55352d7e763737d685d8836", "1.14.0--r36_0": "sha256:35b7f389d4fd71fff48d10cc560e009f714bd8697e5a730195cf4dd9d58c75e0", "1.12.0--r36_1": "sha256:43fa8825d556edad09f094b0fb78e46abf6a3b636e3313d1a57bbf0c3477da61", "1.10.0--r351_0": "sha256:7febb52d7d5bbbd4dfcf098f04b527d6a66442b449b5e0d5ecfa11cbeb156ce5"}, "docker": "quay.io/biocontainers/bioconductor-kimod"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-kimod.
shpc-registry automated BioContainers addition for bioconductor-kimod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-kimod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-kimod:1.15.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-kimod/1.15.0--r40_0
$ module help quay.io/biocontainers/bioconductor-kimod/1.15.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-kimod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kimod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kimod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-kimod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-kimod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-kimod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-kimod

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