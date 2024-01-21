---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133a2frmavecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133a2frmavecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133a2frmavecs/container.yaml"
updated_at: "2024-01-21 03:06:34.741787"
latest: "1.2.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133a2frmavecs"

versions:
 - "1.2.0--r41hdfd78af_9"
 - "1.2.0--r42hdfd78af_10"
 - "1.2.0--r43hdfd78af_11"
 - "1.2.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133a2frmavecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133a2frmavecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133a2frmavecs", "latest": {"1.2.0--r43hdfd78af_12": "sha256:c8b3f6991ecbb36f747ef056da60477d3767cdb3a2e460052b4057a20097d675"}, "tags": {"1.2.0--r41hdfd78af_9": "sha256:5605b4a217a3009e34b1e7608d5f573b06768c1aef98ffffc35d897cd780a480", "1.2.0--r42hdfd78af_10": "sha256:c897d8ebc95d27af7464dc7be27045476438d2e86162ec10533d9711e8adc4e7", "1.2.0--r43hdfd78af_11": "sha256:0e4266ade3b9ca4a5fbf31c1cb00b7e31b74fec589554f81d7282fa59860f775", "1.2.0--r43hdfd78af_12": "sha256:c8b3f6991ecbb36f747ef056da60477d3767cdb3a2e460052b4057a20097d675"}, "docker": "quay.io/biocontainers/bioconductor-hgu133a2frmavecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133a2frmavecs.
shpc-registry automated BioContainers addition for bioconductor-hgu133a2frmavecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a2frmavecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a2frmavecs:1.2.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133a2frmavecs/1.2.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgu133a2frmavecs/1.2.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133a2frmavecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a2frmavecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a2frmavecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133a2frmavecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133a2frmavecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133a2frmavecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133a2frmavecs

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