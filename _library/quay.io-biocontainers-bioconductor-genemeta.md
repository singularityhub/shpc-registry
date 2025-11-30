---
layout: container
name:  "quay.io/biocontainers/bioconductor-genemeta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genemeta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genemeta/container.yaml"
updated_at: "2025-11-30 04:00:03.855766"
latest: "1.78.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genemeta"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.78.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genemeta"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genemeta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genemeta", "latest": {"1.78.0--r44hdfd78af_0": "sha256:45c10f1f56ba1b5587cdac55967ef1f7483c3b0e9a9897442c75f90002adc4db"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:207ba77e7c439d1ceb3441aa2218401c9ce71c4df85428ff0e8ad8aabbee7921", "1.70.0--r42hdfd78af_0": "sha256:7ad0c9a3b163474db914651e345e21c9c68ec2c7d30ab2b383ce91e365a41424", "1.72.0--r43hdfd78af_0": "sha256:5673f4b353f76860f26f0ec5b8be4d956e0b72a4b4412a5a145eafad8414c009", "1.74.0--r43hdfd78af_0": "sha256:7959e7b788d4a43d9833d91451f2dd48e3abc4d4c01b14b5df3c78c4ca78dd90", "1.78.0--r44hdfd78af_0": "sha256:45c10f1f56ba1b5587cdac55967ef1f7483c3b0e9a9897442c75f90002adc4db"}, "docker": "quay.io/biocontainers/bioconductor-genemeta"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genemeta.
shpc-registry automated BioContainers addition for bioconductor-genemeta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genemeta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genemeta:1.78.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genemeta/1.78.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genemeta/1.78.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genemeta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genemeta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genemeta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genemeta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genemeta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genemeta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genemeta

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