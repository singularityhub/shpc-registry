---
layout: container
name:  "quay.io/biocontainers/bioconductor-cispath"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cispath/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cispath/container.yaml"
updated_at: "2025-05-04 03:36:09.401710"
latest: "1.46.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cispath"

versions:
 - "1.34.0--r41hc247a5b_2"
 - "1.38.0--r42hc247a5b_0"
 - "1.38.0--r42hc247a5b_1"
 - "1.38.0--r42hf17093f_2"
 - "1.40.0--r43hf17093f_0"
 - "1.42.0--r43hf17093f_1"
 - "1.46.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cispath"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cispath", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cispath", "latest": {"1.46.0--r44he5774e6_0": "sha256:54efc7c557af215a6ced8a63dfffc94b90f414c27919f26a642e57265a9272cd"}, "tags": {"1.34.0--r41hc247a5b_2": "sha256:5fb1c643bd4f9fedf159806793a9473db91d3f62cb7007b3c95db105b91297d5", "1.38.0--r42hc247a5b_0": "sha256:ef78b9e29badcc41743ae56b54b2e76484ab97eed45fa9a126dd301cf4300525", "1.38.0--r42hc247a5b_1": "sha256:65acba7923e8036702e6130c4d8a1b361c91d91bc2a75c0d8cff0f328cfc51a7", "1.38.0--r42hf17093f_2": "sha256:f6a2213ed1b470a8e67844bc1c517f0c5841ed5850ecd0cb9356d1dee853e270", "1.40.0--r43hf17093f_0": "sha256:feb36906d1b09dbca54d2368323e3d4907ecfa644cdd5ec52d50b9b4d45bee86", "1.42.0--r43hf17093f_1": "sha256:8365ea5595f5c8a3a1d141424fc9ff43b1250ae5f49b7942062828d524c87b0e", "1.46.0--r44he5774e6_0": "sha256:54efc7c557af215a6ced8a63dfffc94b90f414c27919f26a642e57265a9272cd"}, "docker": "quay.io/biocontainers/bioconductor-cispath"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cispath.
shpc-registry automated BioContainers addition for bioconductor-cispath
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cispath
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cispath:1.46.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cispath/1.46.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-cispath/1.46.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cispath-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cispath-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cispath-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cispath-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cispath-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cispath-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cispath

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