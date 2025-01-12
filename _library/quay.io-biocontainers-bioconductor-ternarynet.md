---
layout: container
name:  "quay.io/biocontainers/bioconductor-ternarynet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ternarynet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ternarynet/container.yaml"
updated_at: "2025-01-12 03:27:58.655063"
latest: "1.50.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ternarynet"
aliases:
 - "glpsol"
versions:
 - "1.38.0--r41hc247a5b_2"
 - "1.42.0--r42hc247a5b_0"
 - "1.42.0--r42hf17093f_1"
 - "1.44.0--r43hf17093f_0"
 - "1.46.0--r43hf17093f_0"
 - "1.50.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ternarynet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ternarynet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ternarynet", "latest": {"1.50.0--r44he5774e6_0": "sha256:8b3560fc0d4df6dfe61958d6cdb2994b972571313638b4eb8ca2a76bbb0260da"}, "tags": {"1.38.0--r41hc247a5b_2": "sha256:82aa58b7ad43d4b0d06d5dc27959539eba46f464817bfbb974361a0d658a5721", "1.42.0--r42hc247a5b_0": "sha256:178fa0cc8bc671cbe69da341956ef098eba0469b09970d3d4800f5b979d11d61", "1.42.0--r42hf17093f_1": "sha256:d085c215fee258f164ede4f78867b40b8f69a979308899ba0c2f096a7c6eba75", "1.44.0--r43hf17093f_0": "sha256:d3b37eee94bb6e231f5f182e3bec99c5f3eef288906263d1ed1c31ab59ba2250", "1.46.0--r43hf17093f_0": "sha256:927b2804bd86fa913f2ccf9aec3e2373f7a2ad10b7843fe5034e7fc5120b972d", "1.50.0--r44he5774e6_0": "sha256:8b3560fc0d4df6dfe61958d6cdb2994b972571313638b4eb8ca2a76bbb0260da"}, "docker": "quay.io/biocontainers/bioconductor-ternarynet", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ternarynet.
shpc-registry automated BioContainers addition for bioconductor-ternarynet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ternarynet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ternarynet:1.50.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ternarynet/1.50.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-ternarynet/1.50.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ternarynet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ternarynet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ternarynet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ternarynet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ternarynet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ternarynet-inspect-deffile:

```bash
$ singularity inspect -d <container>
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