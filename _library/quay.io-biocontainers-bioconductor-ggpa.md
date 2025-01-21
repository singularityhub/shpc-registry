---
layout: container
name:  "quay.io/biocontainers/bioconductor-ggpa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ggpa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ggpa/container.yaml"
updated_at: "2025-01-21 02:45:59.635004"
latest: "1.18.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ggpa"

versions:
 - "1.6.0--r41hc247a5b_2"
 - "1.10.0--r42hc247a5b_0"
 - "1.10.0--r42hf17093f_1"
 - "1.12.1--r43hf17093f_0"
 - "1.14.0--r43hf17093f_1"
 - "1.18.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ggpa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ggpa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ggpa", "latest": {"1.18.0--r44he5774e6_0": "sha256:9572977e88c98ff87fe7d02aad853e6f26b834d46ba16952bc41d08973feb75e"}, "tags": {"1.6.0--r41hc247a5b_2": "sha256:ed8655a9ff4c69795eaf44d23052dae88b3b3a6e9ad65f3ce041b4a5e59be7c8", "1.10.0--r42hc247a5b_0": "sha256:2d637859e9600e799d68472f11bb1e80c8f75c21722199bfc63065766d7c53e7", "1.10.0--r42hf17093f_1": "sha256:726ebdac659481f96944d6cb21ed0e03e68d5a82395994d7ef9872e69c397fae", "1.12.1--r43hf17093f_0": "sha256:841a8f3a0dc8f51a4888d997e0ea1461de4651b23a49a49df2c025373d9ad8ca", "1.14.0--r43hf17093f_1": "sha256:53c0f65512ae10baa3883934dad7552af7fa16c748f4e4f4b23b83ec11326a8e", "1.18.0--r44he5774e6_0": "sha256:9572977e88c98ff87fe7d02aad853e6f26b834d46ba16952bc41d08973feb75e"}, "docker": "quay.io/biocontainers/bioconductor-ggpa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ggpa.
shpc-registry automated BioContainers addition for bioconductor-ggpa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ggpa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ggpa:1.18.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ggpa/1.18.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-ggpa/1.18.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ggpa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggpa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggpa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ggpa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ggpa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ggpa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ggpa

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