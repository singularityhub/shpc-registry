---
layout: container
name:  "quay.io/biocontainers/bioconductor-somaticsignatures"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-somaticsignatures/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-somaticsignatures/container.yaml"
updated_at: "2023-12-01 03:07:18.116397"
latest: "2.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-somaticsignatures"

versions:
 - "2.30.0--r41hdfd78af_0"
 - "2.34.0--r42hdfd78af_0"
 - "2.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-somaticsignatures"
config: {"url": "https://biocontainers.pro/tools/bioconductor-somaticsignatures", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-somaticsignatures", "latest": {"2.36.0--r43hdfd78af_0": "sha256:003bf5840fc0f4476a6aa94eb0998ccecdb4536cf64367c88ad629be1f4a0643"}, "tags": {"2.30.0--r41hdfd78af_0": "sha256:508e24cb5ea45495663141d097e07ef47853b2675eee63ebb733fce956249bb8", "2.34.0--r42hdfd78af_0": "sha256:dbb60d917a79aa4de91509a7108e74c8992eb5c5420c7cb2bfb2496324b20444", "2.36.0--r43hdfd78af_0": "sha256:003bf5840fc0f4476a6aa94eb0998ccecdb4536cf64367c88ad629be1f4a0643"}, "docker": "quay.io/biocontainers/bioconductor-somaticsignatures"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-somaticsignatures.
shpc-registry automated BioContainers addition for bioconductor-somaticsignatures
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-somaticsignatures
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-somaticsignatures:2.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-somaticsignatures/2.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-somaticsignatures/2.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-somaticsignatures-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-somaticsignatures-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-somaticsignatures-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-somaticsignatures-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-somaticsignatures-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-somaticsignatures-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-somaticsignatures

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