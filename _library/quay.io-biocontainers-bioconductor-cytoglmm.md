---
layout: container
name:  "quay.io/biocontainers/bioconductor-cytoglmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cytoglmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cytoglmm/container.yaml"
updated_at: "2023-11-02 03:05:43.244857"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cytoglmm"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cytoglmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cytoglmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cytoglmm", "latest": {"1.8.0--r43hdfd78af_0": "sha256:81f0525adcca147a9bf754253df763460c750ece1402a52b23c644559854cdc1"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:d352afa441bdc906aacec2646ed65879183a1682cbf090be89870ad2b4e3f674", "1.6.0--r42hdfd78af_0": "sha256:bc1ffc1cde0e239093482f466c80cd5bf167897b83ba14f75c97f2f44c34264c", "1.8.0--r43hdfd78af_0": "sha256:81f0525adcca147a9bf754253df763460c750ece1402a52b23c644559854cdc1"}, "docker": "quay.io/biocontainers/bioconductor-cytoglmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cytoglmm.
shpc-registry automated BioContainers addition for bioconductor-cytoglmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cytoglmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cytoglmm:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cytoglmm/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cytoglmm/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cytoglmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytoglmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytoglmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cytoglmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cytoglmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cytoglmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cytoglmm

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