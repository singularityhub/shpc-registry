---
layout: container
name:  "quay.io/biocontainers/bioconductor-ncigraphdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ncigraphdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ncigraphdata/container.yaml"
updated_at: "2024-06-06 02:52:18.593431"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ncigraphdata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ncigraphdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ncigraphdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ncigraphdata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:1f4b534afcd4504c23164c0a8e6b6bf83401cf951b5891443c941d3f59f07640"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:63f7beabdcaeefd7b2930e83b127af9b7153890ce2c12d6d5f1eb63e956e9ba9", "1.33.0--r42hdfd78af_0": "sha256:aff0422e1a825b9d4a482528940a5cd6fed5c4b0e796ac27623ab779078752b7", "1.36.0--r43hdfd78af_0": "sha256:7854165d3a8f3d5e1d10b685f3cb4423a5f07b9e97f06256170dcdd201a71a57", "1.38.0--r43hdfd78af_0": "sha256:1f4b534afcd4504c23164c0a8e6b6bf83401cf951b5891443c941d3f59f07640"}, "docker": "quay.io/biocontainers/bioconductor-ncigraphdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ncigraphdata.
shpc-registry automated BioContainers addition for bioconductor-ncigraphdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ncigraphdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ncigraphdata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ncigraphdata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ncigraphdata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ncigraphdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ncigraphdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ncigraphdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ncigraphdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ncigraphdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ncigraphdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ncigraphdata

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