---
layout: container
name:  "quay.io/biocontainers/bioconductor-mvcclass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mvcclass/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mvcclass/container.yaml"
updated_at: "2025-02-19 02:52:00.662930"
latest: "1.80.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mvcclass"

versions:
 - "1.68.0--r41hdfd78af_0"
 - "1.72.0--r42hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
 - "1.80.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mvcclass"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mvcclass", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mvcclass", "latest": {"1.80.0--r44hdfd78af_0": "sha256:6d904db059df07014984e3c72e686f3e64e713821c278f16016c69026870b02e"}, "tags": {"1.68.0--r41hdfd78af_0": "sha256:dceaed4e36de46f76d578e0152c1088fd7c46c8f63e808190d701fcb0772d363", "1.72.0--r42hdfd78af_0": "sha256:22b9ca515ec5143e6e12282bb55dec64f2030bd514492f6ff0359f6ede97b388", "1.74.0--r43hdfd78af_0": "sha256:7c2afb4dbd3ee040e8abcc7e0c2b5c49910e93f2845eb3c2d9dac1f02a164688", "1.76.0--r43hdfd78af_0": "sha256:7befa7cc80a3df2fb4770e42fadd834f0881ea1777d2d849f582fac21ce13948", "1.80.0--r44hdfd78af_0": "sha256:6d904db059df07014984e3c72e686f3e64e713821c278f16016c69026870b02e"}, "docker": "quay.io/biocontainers/bioconductor-mvcclass"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mvcclass.
shpc-registry automated BioContainers addition for bioconductor-mvcclass
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mvcclass
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mvcclass:1.80.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mvcclass/1.80.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mvcclass/1.80.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mvcclass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mvcclass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mvcclass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mvcclass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mvcclass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mvcclass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mvcclass

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