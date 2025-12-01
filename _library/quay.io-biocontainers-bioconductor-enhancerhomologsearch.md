---
layout: container
name:  "quay.io/biocontainers/bioconductor-enhancerhomologsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-enhancerhomologsearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-enhancerhomologsearch/container.yaml"
updated_at: "2025-12-01 05:09:51.428510"
latest: "1.12.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-enhancerhomologsearch"

versions:
 - "1.0.1--r41hc247a5b_0"
 - "1.4.0--r42hc247a5b_0"
 - "1.6.1--r43hf17093f_0"
 - "1.8.2--r43hf17093f_0"
 - "1.12.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-enhancerhomologsearch"
config: {"url": "https://biocontainers.pro/tools/bioconductor-enhancerhomologsearch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-enhancerhomologsearch", "latest": {"1.12.0--r44he5774e6_0": "sha256:7e1c800548dc0e92c33c09cd76597dd47713fb74f853128b9baf757a87987c4a"}, "tags": {"1.0.1--r41hc247a5b_0": "sha256:b6adcc10de7eefdf9bb9d0cc2585062793d17a844c317652d866759a5397215c", "1.4.0--r42hc247a5b_0": "sha256:969e72a414f190c5dc487627a9039c35f910b3174675e86732ed7a9abb626b6b", "1.6.1--r43hf17093f_0": "sha256:5b88e1f86833b8773a5c58208a1305d527379b1c900508c07bbdbb3bc8e777dd", "1.8.2--r43hf17093f_0": "sha256:f127f6ffecba489f5866fa4f0886269311ab7037ca6e5bf34a6a9b509112b6bf", "1.12.0--r44he5774e6_0": "sha256:7e1c800548dc0e92c33c09cd76597dd47713fb74f853128b9baf757a87987c4a"}, "docker": "quay.io/biocontainers/bioconductor-enhancerhomologsearch"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-enhancerhomologsearch.
shpc-registry automated BioContainers addition for bioconductor-enhancerhomologsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-enhancerhomologsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-enhancerhomologsearch:1.12.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-enhancerhomologsearch/1.12.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-enhancerhomologsearch/1.12.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-enhancerhomologsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enhancerhomologsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enhancerhomologsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-enhancerhomologsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-enhancerhomologsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-enhancerhomologsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-enhancerhomologsearch

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