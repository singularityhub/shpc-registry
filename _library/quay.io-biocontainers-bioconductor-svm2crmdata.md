---
layout: container
name:  "quay.io/biocontainers/bioconductor-svm2crmdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-svm2crmdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-svm2crmdata/container.yaml"
updated_at: "2025-05-19 03:26:46.754831"
latest: "1.38.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-svm2crmdata"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.29.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.38.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-svm2crmdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-svm2crmdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-svm2crmdata", "latest": {"1.38.0--r44hdfd78af_0": "sha256:59b437c928fa4680560086693b6a7a70c1c9cebcae471047425c828a5ef597cf"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:8fdc532945c19b531a400ff8ca15c7f1885bd8c494c387e5bdbde36d14fd045a", "1.29.0--r42hdfd78af_0": "sha256:ff36da0b7e868e679e8523711d4b289b3cba9d955d9762bed977efe649f024fb", "1.32.0--r43hdfd78af_0": "sha256:e5f1e9fa4f40a3e7fe0007e1a8db4496a9d85df175c06ab8ed04550acddfe3c2", "1.34.0--r43hdfd78af_0": "sha256:ec7301ac44294343ada4bc5c0b72c4de50d0a37c5839ac200df7a8c0e8b9cb8c", "1.38.0--r44hdfd78af_0": "sha256:59b437c928fa4680560086693b6a7a70c1c9cebcae471047425c828a5ef597cf"}, "docker": "quay.io/biocontainers/bioconductor-svm2crmdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-svm2crmdata.
shpc-registry automated BioContainers addition for bioconductor-svm2crmdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-svm2crmdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-svm2crmdata:1.38.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-svm2crmdata/1.38.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-svm2crmdata/1.38.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-svm2crmdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-svm2crmdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-svm2crmdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-svm2crmdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-svm2crmdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-svm2crmdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-svm2crmdata

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