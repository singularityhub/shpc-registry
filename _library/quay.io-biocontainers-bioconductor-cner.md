---
layout: container
name:  "quay.io/biocontainers/bioconductor-cner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cner/container.yaml"
updated_at: "2025-10-21 03:22:18.189336"
latest: "1.43.0--r44h15a9599_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cner"

versions:
 - "1.30.0--r41hc0cfd56_2"
 - "1.34.0--r42hc0cfd56_0"
 - "1.34.0--r42ha9d7317_1"
 - "1.36.0--r43ha9d7317_0"
 - "1.38.0--r43ha9d7317_0"
 - "1.42.0--r44h15a9599_0"
 - "1.43.0--r44h15a9599_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cner"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cner", "latest": {"1.43.0--r44h15a9599_0": "sha256:b3be425e521c765a41d3215fbe5ddb72975f9524c20ffa747d435fb22b1855f3"}, "tags": {"1.30.0--r41hc0cfd56_2": "sha256:67698a758bc0d3e18c293bb5bdfb92366f9adf266763e8671f5c60d9590de951", "1.34.0--r42hc0cfd56_0": "sha256:c06076f605bfd723b05dff033d450b4c4b687da09c2ddd4b62ae81bafede8529", "1.34.0--r42ha9d7317_1": "sha256:6c492bf92442502cd55ee52811eafad8516be8260dac199373f4035aadfcefc6", "1.36.0--r43ha9d7317_0": "sha256:83dbac0ab552bc8e55e221f7179c709e0aace9142359105a5ddc43c436af82ba", "1.38.0--r43ha9d7317_0": "sha256:c88830e041ad6e1e9f7c1a514599ee98cfe24d8af67f50bfb58bcddca94836ae", "1.42.0--r44h15a9599_0": "sha256:932888c52d1c4e63eabda73b456a985420faad52a7c5b58aaf46dcf10579afdd", "1.43.0--r44h15a9599_0": "sha256:b3be425e521c765a41d3215fbe5ddb72975f9524c20ffa747d435fb22b1855f3"}, "docker": "quay.io/biocontainers/bioconductor-cner"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cner.
shpc-registry automated BioContainers addition for bioconductor-cner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cner:1.43.0--r44h15a9599_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cner/1.43.0--r44h15a9599_0
$ module help quay.io/biocontainers/bioconductor-cner/1.43.0--r44h15a9599_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cner

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