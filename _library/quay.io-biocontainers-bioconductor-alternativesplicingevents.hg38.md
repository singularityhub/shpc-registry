---
layout: container
name:  "quay.io/biocontainers/bioconductor-alternativesplicingevents.hg38"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-alternativesplicingevents.hg38/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-alternativesplicingevents.hg38/container.yaml"
updated_at: "2024-06-27 03:47:07.100207"
latest: "1.1.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-alternativesplicingevents.hg38"

versions:
 - "1.1.0--r41hdfd78af_1"
 - "1.1.0--r42hdfd78af_2"
 - "1.1.0--r43hdfd78af_3"
 - "1.1.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-alternativesplicingevents.hg38"
config: {"url": "https://biocontainers.pro/tools/bioconductor-alternativesplicingevents.hg38", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-alternativesplicingevents.hg38", "latest": {"1.1.0--r43hdfd78af_4": "sha256:4e5a1e82650479de9d3ce77ba64587cab3f39f01b22e3291ea71010be6b23e30"}, "tags": {"1.1.0--r41hdfd78af_1": "sha256:422f33a3b7ec1f10c70a217bd879ecf29946a27f3ad293ca4ee513c6a8ddc639", "1.1.0--r42hdfd78af_2": "sha256:25f6cb63d3276320d8cf88ffddcd5f7a705a6ef6bdaa43e2ca72d02b86e69f06", "1.1.0--r43hdfd78af_3": "sha256:d553dded2b2efe3ccade80d676d31a0e76d4aefb09cf223f564d026a604679e4", "1.1.0--r43hdfd78af_4": "sha256:4e5a1e82650479de9d3ce77ba64587cab3f39f01b22e3291ea71010be6b23e30"}, "docker": "quay.io/biocontainers/bioconductor-alternativesplicingevents.hg38"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-alternativesplicingevents.hg38.
shpc-registry automated BioContainers addition for bioconductor-alternativesplicingevents.hg38
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-alternativesplicingevents.hg38
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-alternativesplicingevents.hg38:1.1.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-alternativesplicingevents.hg38/1.1.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-alternativesplicingevents.hg38/1.1.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-alternativesplicingevents.hg38-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alternativesplicingevents.hg38-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alternativesplicingevents.hg38-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-alternativesplicingevents.hg38-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-alternativesplicingevents.hg38-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-alternativesplicingevents.hg38-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-alternativesplicingevents.hg38

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