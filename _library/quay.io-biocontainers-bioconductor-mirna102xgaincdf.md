---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirna102xgaincdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirna102xgaincdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirna102xgaincdf/container.yaml"
updated_at: "2025-04-04 03:07:09.920733"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mirna102xgaincdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mirna102xgaincdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirna102xgaincdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirna102xgaincdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:7bd756c56c777c721eaf4cd27b290cf4b246a2ef676b2f04474cb73111aaface"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:e2cebeee7d8224b725c9b4d9509f7b3fdd81ecf438670b26c86c3ca08ce93683", "2.18.0--r42hdfd78af_10": "sha256:b11ea1b67b21c5f7472eaaf24ddd210e16c5dffff7830afe94b57390ebea9473", "2.18.0--r43hdfd78af_11": "sha256:8efb8075884e7789486db45db0e90344e71b38deb94572dc36184726773ef790", "2.18.0--r43hdfd78af_12": "sha256:3ea782202aed6d34f7f12362a9536daf2b5ff8b06155ec8f06871abbc3b5bdc1", "2.18.0--r44hdfd78af_13": "sha256:7bd756c56c777c721eaf4cd27b290cf4b246a2ef676b2f04474cb73111aaface"}, "docker": "quay.io/biocontainers/bioconductor-mirna102xgaincdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirna102xgaincdf.
shpc-registry automated BioContainers addition for bioconductor-mirna102xgaincdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirna102xgaincdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirna102xgaincdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirna102xgaincdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mirna102xgaincdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirna102xgaincdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirna102xgaincdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirna102xgaincdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirna102xgaincdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirna102xgaincdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirna102xgaincdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirna102xgaincdf

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