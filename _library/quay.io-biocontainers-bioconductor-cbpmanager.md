---
layout: container
name:  "quay.io/biocontainers/bioconductor-cbpmanager"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cbpmanager/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cbpmanager/container.yaml"
updated_at: "2025-04-05 03:06:03.769024"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cbpmanager"
aliases:
 - "pandoc"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cbpmanager"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cbpmanager", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cbpmanager", "latest": {"1.14.0--r44hdfd78af_0": "sha256:c4941f18ea382feacc056fd0a735f97e91faaeaaf75c78a148e15e2d9b1d2975"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:47136786aabc12b8aa3441eb8cc24fa03c190141fff42eef838fc626ad43648b", "1.6.0--r42hdfd78af_0": "sha256:d8c4f8c3b14926c9c6ef1728997c8766e75ff328870dde6b718027eaa7efa7ee", "1.8.0--r43hdfd78af_0": "sha256:da07e340491ff740d2fa8a124a7a900013f43efe08b47f96c4b83155ee7025c3", "1.10.0--r43hdfd78af_0": "sha256:c22133562dcad3b104a39f79ff6f06029e305eedfe2e9d91cfbe0bdd1a7483b4", "1.14.0--r44hdfd78af_0": "sha256:c4941f18ea382feacc056fd0a735f97e91faaeaaf75c78a148e15e2d9b1d2975"}, "docker": "quay.io/biocontainers/bioconductor-cbpmanager", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cbpmanager.
shpc-registry automated BioContainers addition for bioconductor-cbpmanager
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cbpmanager
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cbpmanager:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cbpmanager/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cbpmanager/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cbpmanager-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cbpmanager-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cbpmanager-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cbpmanager-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cbpmanager-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cbpmanager-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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