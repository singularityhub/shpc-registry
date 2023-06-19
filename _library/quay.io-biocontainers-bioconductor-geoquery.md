---
layout: container
name:  "quay.io/biocontainers/bioconductor-geoquery"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geoquery/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geoquery/container.yaml"
updated_at: "2023-06-19 02:49:34.917788"
latest: "2.66.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geoquery"

versions:
 - "2.62.0--r41hdfd78af_0"
 - "2.66.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geoquery"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geoquery", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geoquery", "latest": {"2.66.0--r42hdfd78af_0": "sha256:65ede9b8a4f30704b350f11d9a664349a0ae78bfe72be951bac6b5e3e77d5492"}, "tags": {"2.62.0--r41hdfd78af_0": "sha256:4510fd8391009c823f6a2137684595bf7419c93494c96878428b038e23e93253", "2.66.0--r42hdfd78af_0": "sha256:65ede9b8a4f30704b350f11d9a664349a0ae78bfe72be951bac6b5e3e77d5492"}, "docker": "quay.io/biocontainers/bioconductor-geoquery"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geoquery.
shpc-registry automated BioContainers addition for bioconductor-geoquery
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geoquery
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geoquery:2.66.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geoquery/2.66.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geoquery/2.66.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geoquery-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geoquery-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geoquery-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geoquery-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geoquery-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geoquery-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geoquery

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