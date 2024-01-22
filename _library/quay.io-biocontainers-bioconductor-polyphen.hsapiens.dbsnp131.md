---
layout: container
name:  "quay.io/biocontainers/bioconductor-polyphen.hsapiens.dbsnp131"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-polyphen.hsapiens.dbsnp131/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-polyphen.hsapiens.dbsnp131/container.yaml"
updated_at: "2024-01-22 03:24:47.796430"
latest: "1.0.2--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-polyphen.hsapiens.dbsnp131"

versions:
 - "1.0.2--r41hdfd78af_9"
 - "1.0.2--r42hdfd78af_10"
 - "1.0.2--r43hdfd78af_11"
 - "1.0.2--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-polyphen.hsapiens.dbsnp131"
config: {"url": "https://biocontainers.pro/tools/bioconductor-polyphen.hsapiens.dbsnp131", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-polyphen.hsapiens.dbsnp131", "latest": {"1.0.2--r43hdfd78af_12": "sha256:3c66cf546039496ee09010229a817e00510f06a302797fd67f72cdd839cb4bbd"}, "tags": {"1.0.2--r41hdfd78af_9": "sha256:3868cfc91b29b7a379f1d2a93395273367a2bae06dfc555a2ca1357d34633949", "1.0.2--r42hdfd78af_10": "sha256:4e008e69c2ca355972813fc0a135dedaebb690f00f13f3185f867d8ca8454ae7", "1.0.2--r43hdfd78af_11": "sha256:e638024460b64df358ac3a24a03e9c105288cf1f02bfe444b6e101c64dbecfea", "1.0.2--r43hdfd78af_12": "sha256:3c66cf546039496ee09010229a817e00510f06a302797fd67f72cdd839cb4bbd"}, "docker": "quay.io/biocontainers/bioconductor-polyphen.hsapiens.dbsnp131"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-polyphen.hsapiens.dbsnp131.
shpc-registry automated BioContainers addition for bioconductor-polyphen.hsapiens.dbsnp131
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-polyphen.hsapiens.dbsnp131
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-polyphen.hsapiens.dbsnp131:1.0.2--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-polyphen.hsapiens.dbsnp131/1.0.2--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-polyphen.hsapiens.dbsnp131/1.0.2--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-polyphen.hsapiens.dbsnp131-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-polyphen.hsapiens.dbsnp131-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-polyphen.hsapiens.dbsnp131-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-polyphen.hsapiens.dbsnp131-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-polyphen.hsapiens.dbsnp131-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-polyphen.hsapiens.dbsnp131-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-polyphen.hsapiens.dbsnp131

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