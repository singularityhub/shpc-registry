---
layout: container
name:  "quay.io/biocontainers/bioconductor-cytoml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cytoml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cytoml/container.yaml"
updated_at: "2024-05-30 04:17:51.815785"
latest: "2.14.0--r43h4605cfd_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cytoml"

versions:
 - "2.6.0--r41hbe66c35_2"
 - "2.10.0--r42hbe66c35_0"
 - "2.12.0--r43h4605cfd_0"
 - "2.14.0--r43h4605cfd_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cytoml"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cytoml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cytoml", "latest": {"2.14.0--r43h4605cfd_0": "sha256:81cb923fbb5eb7c3f60c12ad3364c847d93e177b4c79167d13c84d4109e2f29f"}, "tags": {"2.6.0--r41hbe66c35_2": "sha256:c7b96f10ed9224fea19ef630b3e0e61c16d644b6185d18a58f5c554794e53e4e", "2.10.0--r42hbe66c35_0": "sha256:eb650138707419d929ed5426fa4c3dcfc02c9e326fc82b899e7937ab5ee8fc01", "2.12.0--r43h4605cfd_0": "sha256:899db6ca58ad75c80ecf10157ee557c1ecd42b0cd0426f107ca8c28db7941542", "2.14.0--r43h4605cfd_0": "sha256:81cb923fbb5eb7c3f60c12ad3364c847d93e177b4c79167d13c84d4109e2f29f"}, "docker": "quay.io/biocontainers/bioconductor-cytoml"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cytoml.
shpc-registry automated BioContainers addition for bioconductor-cytoml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cytoml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cytoml:2.14.0--r43h4605cfd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cytoml/2.14.0--r43h4605cfd_0
$ module help quay.io/biocontainers/bioconductor-cytoml/2.14.0--r43h4605cfd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cytoml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytoml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytoml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cytoml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cytoml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cytoml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cytoml

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