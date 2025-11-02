---
layout: container
name:  "quay.io/biocontainers/bioconductor-busparse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-busparse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-busparse/container.yaml"
updated_at: "2025-11-02 03:28:59.572463"
latest: "1.20.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-busparse"

versions:
 - "1.8.0--r41hc247a5b_2"
 - "1.12.0--r42hc247a5b_0"
 - "1.12.0--r42hf17093f_1"
 - "1.14.1--r43hf17093f_0"
 - "1.16.0--r43hf17093f_0"
 - "1.20.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-busparse"
config: {"url": "https://biocontainers.pro/tools/bioconductor-busparse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-busparse", "latest": {"1.20.0--r44he5774e6_0": "sha256:6b1e8dbba0551ad25a7fdbae7a24b54b42be7e776aa753d3fdd492fe537d76ef"}, "tags": {"1.8.0--r41hc247a5b_2": "sha256:fd5a91c33887f7ae6732147e467381b6d7071c6cdaa582f218c1ee3de8c760eb", "1.12.0--r42hc247a5b_0": "sha256:e1f57c7f81908581db0cd4ba0b470422ec972fce1daca95fa0d56abf0737573b", "1.12.0--r42hf17093f_1": "sha256:1251b211b8270846815c6ffca68c41a455a0dae63a5bc0149e1a6fe0b1842e62", "1.14.1--r43hf17093f_0": "sha256:b64e07a60deb429814b942698bab613629120f1953fb128f11989821e89a2a48", "1.16.0--r43hf17093f_0": "sha256:fe78b99b92b843a7f50dc73ff2f68053d8c749a4af16d49a946547a1a69bc890", "1.20.0--r44he5774e6_0": "sha256:6b1e8dbba0551ad25a7fdbae7a24b54b42be7e776aa753d3fdd492fe537d76ef"}, "docker": "quay.io/biocontainers/bioconductor-busparse"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-busparse.
shpc-registry automated BioContainers addition for bioconductor-busparse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-busparse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-busparse:1.20.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-busparse/1.20.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-busparse/1.20.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-busparse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-busparse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-busparse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-busparse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-busparse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-busparse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-busparse

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