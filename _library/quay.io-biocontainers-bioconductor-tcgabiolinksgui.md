---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcgabiolinksgui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcgabiolinksgui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcgabiolinksgui/container.yaml"
updated_at: "2022-11-20 23:55:17.532905"
latest: "1.23.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tcgabiolinksgui"

versions:
 - "1.8.0--r351_0"
 - "1.23.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tcgabiolinksgui"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcgabiolinksgui", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcgabiolinksgui", "latest": {"1.23.0--r42hdfd78af_0": "sha256:fcdf30e7bb34ce710bb12632f8056fc181bc3904f8ec84804f48a9f57c143199"}, "tags": {"1.8.0--r351_0": "sha256:b4572cfc65fb7d4b04d7c2f2687467f16b22f11dd670acdfc500c546dbf06f90", "1.23.0--r42hdfd78af_0": "sha256:fcdf30e7bb34ce710bb12632f8056fc181bc3904f8ec84804f48a9f57c143199", "1.20.0--r41hdfd78af_0": "sha256:f172f542ddd1e06f99271eda3cbbd6e9b40ec02f8a2806db167e92c452f8a475", "1.18.0--r41hdfd78af_0": "sha256:fa098d933c83fe8dd3f728ca26bf0259d3aa0df56a0052a3a7d0314b85473858", "1.16.0--r40hdfd78af_1": "sha256:730934ac0c284498ea724e14b83077f470043080a2ff01342f59979db1a3a23b", "1.14.0--r40_0": "sha256:be7b5cc83c539bcc13648b867d7e646d18a7d80ae6cef4c9f42625bccf28529b"}, "docker": "quay.io/biocontainers/bioconductor-tcgabiolinksgui"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcgabiolinksgui.
shpc-registry automated BioContainers addition for bioconductor-tcgabiolinksgui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgabiolinksgui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgabiolinksgui:1.23.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcgabiolinksgui/1.23.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tcgabiolinksgui/1.23.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcgabiolinksgui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgabiolinksgui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgabiolinksgui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcgabiolinksgui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcgabiolinksgui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcgabiolinksgui-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tcgabiolinksgui

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