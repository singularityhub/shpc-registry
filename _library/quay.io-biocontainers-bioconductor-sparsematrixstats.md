---
layout: container
name:  "quay.io/biocontainers/bioconductor-sparsematrixstats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sparsematrixstats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sparsematrixstats/container.yaml"
updated_at: "2025-05-05 03:18:40.574692"
latest: "1.18.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sparsematrixstats"

versions:
 - "1.6.0--r41hc247a5b_2"
 - "1.10.0--r42hc247a5b_0"
 - "1.10.0--r42hf17093f_1"
 - "1.12.2--r43hf17093f_0"
 - "1.14.0--r43hf17093f_0"
 - "1.14.0--r43hf17093f_1"
 - "1.18.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sparsematrixstats"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sparsematrixstats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sparsematrixstats", "latest": {"1.18.0--r44he5774e6_0": "sha256:178bbbb998c41a5113da49a541dc8b70a8669e448e63fa459d3f48f409765e1f"}, "tags": {"1.6.0--r41hc247a5b_2": "sha256:a8ff49c3961f7ed73c9d8e5b5ce94f036cd93dd94347e9272752b383a8a69431", "1.10.0--r42hc247a5b_0": "sha256:82de2dd3dbd8cc934ca9c53ad3de321e6f3f0adf0899e47d4dbb353acda7b818", "1.10.0--r42hf17093f_1": "sha256:41cbe2dc321f4be2925ab4677c087992a7d2c3f86068325c56dec1b5a3fb77f6", "1.12.2--r43hf17093f_0": "sha256:fe7a9933e883ac162244bd9911217125ed5b5b0a2012259ff865c67790b4b4be", "1.14.0--r43hf17093f_0": "sha256:0fd0ec2c4508567a228783f3578fb3d19ebe594bd97cb91520053bebe1dc747f", "1.14.0--r43hf17093f_1": "sha256:e62a3213b5e88f3d8399482183cff05e55fb0f2958d3e8305ec8c68594383a5f", "1.18.0--r44he5774e6_0": "sha256:178bbbb998c41a5113da49a541dc8b70a8669e448e63fa459d3f48f409765e1f"}, "docker": "quay.io/biocontainers/bioconductor-sparsematrixstats"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sparsematrixstats.
shpc-registry automated BioContainers addition for bioconductor-sparsematrixstats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsematrixstats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsematrixstats:1.18.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sparsematrixstats/1.18.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-sparsematrixstats/1.18.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sparsematrixstats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsematrixstats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsematrixstats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sparsematrixstats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sparsematrixstats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sparsematrixstats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sparsematrixstats

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