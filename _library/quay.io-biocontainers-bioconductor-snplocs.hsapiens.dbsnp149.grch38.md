---
layout: container
name:  "quay.io/biocontainers/bioconductor-snplocs.hsapiens.dbsnp149.grch38"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snplocs.hsapiens.dbsnp149.grch38/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snplocs.hsapiens.dbsnp149.grch38/container.yaml"
updated_at: "2024-10-22 03:04:39.880609"
latest: "0.99.20--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-snplocs.hsapiens.dbsnp149.grch38"

versions:
 - "0.99.20--r41hdfd78af_9"
 - "0.99.20--r42hdfd78af_10"
 - "0.99.20--r43hdfd78af_11"
 - "0.99.20--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-snplocs.hsapiens.dbsnp149.grch38"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snplocs.hsapiens.dbsnp149.grch38", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snplocs.hsapiens.dbsnp149.grch38", "latest": {"0.99.20--r43hdfd78af_12": "sha256:2498d6f36aa515f068ec4e5578ba58c6b0d1c5b9dc0d8751c1ec9425f73231e4"}, "tags": {"0.99.20--r41hdfd78af_9": "sha256:f8238a91a44183cf8e03f54cb30e07ec9a8b4638b14e4f47b7232716c177622e", "0.99.20--r42hdfd78af_10": "sha256:30da9a2e6b3ab74b17eb8ef328ec4cf51deebca410a332c3911add61c909245f", "0.99.20--r43hdfd78af_11": "sha256:0012c74f1b38d4727229261e931c08546b35a8c2747435e186cf410541ecb0d2", "0.99.20--r43hdfd78af_12": "sha256:2498d6f36aa515f068ec4e5578ba58c6b0d1c5b9dc0d8751c1ec9425f73231e4"}, "docker": "quay.io/biocontainers/bioconductor-snplocs.hsapiens.dbsnp149.grch38"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snplocs.hsapiens.dbsnp149.grch38.
shpc-registry automated BioContainers addition for bioconductor-snplocs.hsapiens.dbsnp149.grch38
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snplocs.hsapiens.dbsnp149.grch38
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snplocs.hsapiens.dbsnp149.grch38:0.99.20--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snplocs.hsapiens.dbsnp149.grch38/0.99.20--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-snplocs.hsapiens.dbsnp149.grch38/0.99.20--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snplocs.hsapiens.dbsnp149.grch38-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snplocs.hsapiens.dbsnp149.grch38-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snplocs.hsapiens.dbsnp149.grch38-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snplocs.hsapiens.dbsnp149.grch38-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snplocs.hsapiens.dbsnp149.grch38-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snplocs.hsapiens.dbsnp149.grch38-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-snplocs.hsapiens.dbsnp149.grch38

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