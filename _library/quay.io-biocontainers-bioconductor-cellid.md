---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellid/container.yaml"
updated_at: "2025-03-16 03:21:38.517225"
latest: "1.14.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellid"
aliases:
 - "geosop"
 - "geos-config"
 - "glpsol"
versions:
 - "1.2.1--r41hc247a5b_1"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_1"
 - "1.8.1--r43hf17093f_0"
 - "1.10.1--r43hf17093f_0"
 - "1.14.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellid"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellid", "latest": {"1.14.0--r44he5774e6_0": "sha256:c653bcf7b64b7fac32524e8ff4c13110de01db06c9a5a8a33368a4d957005c7c"}, "tags": {"1.2.1--r41hc247a5b_1": "sha256:b7d4f7626574dbf0d4761fbc663e08275d0aa4b9bc991eda538bcc3fbf40ae46", "1.6.0--r42hc247a5b_0": "sha256:0caf6533c1c42684d5ad13debf5e4e2250ed989f98e207a6bf2cea961f504a78", "1.6.0--r42hf17093f_1": "sha256:e135e8dffc5831fce9b20de0074371ccde1243d37f4dbf72c6e7b8c931cc424f", "1.8.1--r43hf17093f_0": "sha256:2028a74173b813016f735912515a7e7147adc02baab24820524e1c78933d33ad", "1.10.1--r43hf17093f_0": "sha256:029ad0af577cf280a790c5619d2a3ef6fd327d138098c1c79e3f35e5f0f9c037", "1.14.0--r44he5774e6_0": "sha256:c653bcf7b64b7fac32524e8ff4c13110de01db06c9a5a8a33368a4d957005c7c"}, "docker": "quay.io/biocontainers/bioconductor-cellid", "aliases": {"geosop": "/usr/local/bin/geosop", "geos-config": "/usr/local/bin/geos-config", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellid.
shpc-registry automated BioContainers addition for bioconductor-cellid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellid:1.14.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellid/1.14.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-cellid/1.14.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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