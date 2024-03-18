---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.hsapiens.biomart.igis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.biomart.igis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.biomart.igis/container.yaml"
updated_at: "2024-03-18 23:23:27.206435"
latest: "2.3.2--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.biomart.igis"

versions:
 - "2.3.2--r41hdfd78af_9"
 - "2.3.2--r42hdfd78af_11"
 - "2.3.2--r43hdfd78af_12"
 - "2.3.2--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.biomart.igis"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.biomart.igis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.biomart.igis", "latest": {"2.3.2--r43hdfd78af_13": "sha256:4ba700f371ceca7170bed1161f210cb167f482f976d9abc5f0aaa9d421522222"}, "tags": {"2.3.2--r41hdfd78af_9": "sha256:939adc37ef13ac6fa489de25b8e06ccf7c6d1b78f676865fcb18797d8dec6ec9", "2.3.2--r42hdfd78af_11": "sha256:7f3a54a216ee7e85d2eaa31452019041cf0d0cc3958fdd24a0ae34e83584b6cc", "2.3.2--r43hdfd78af_12": "sha256:4d888fdc6e59afb8d5ccad775b54554f6155f8f972a9e7e811a95626aaee2f23", "2.3.2--r43hdfd78af_13": "sha256:4ba700f371ceca7170bed1161f210cb167f482f976d9abc5f0aaa9d421522222"}, "docker": "quay.io/biocontainers/bioconductor-txdb.hsapiens.biomart.igis"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.hsapiens.biomart.igis.
shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.biomart.igis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.biomart.igis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.biomart.igis:2.3.2--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.hsapiens.biomart.igis/2.3.2--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-txdb.hsapiens.biomart.igis/2.3.2--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.hsapiens.biomart.igis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.biomart.igis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.biomart.igis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.hsapiens.biomart.igis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.hsapiens.biomart.igis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.hsapiens.biomart.igis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.hsapiens.biomart.igis

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