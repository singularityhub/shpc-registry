---
layout: container
name:  "quay.io/biocontainers/bioconductor-scuttle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scuttle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scuttle/container.yaml"
updated_at: "2025-08-04 04:37:48.870791"
latest: "1.16.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-scuttle"

versions:
 - "1.4.0--r41hc247a5b_2"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
 - "1.10.1--r43hf17093f_0"
 - "1.12.0--r43hf17093f_0"
 - "1.12.0--r43hf17093f_1"
 - "1.16.0--r44he5774e6_0"
 - "1.16.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-scuttle"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scuttle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scuttle", "latest": {"1.16.0--r44he5774e6_1": "sha256:3b5c09ef2a9f234d0ee103307d02df7b5373abbe9458505d0e2be20f3821731c"}, "tags": {"1.4.0--r41hc247a5b_2": "sha256:ea539dbb54472123fddc2403600b90a210e75922f97b467e4816b0fc8b830a8e", "1.8.0--r42hc247a5b_0": "sha256:bf089e4a3db722bfa369f9c36d4dd61191c1a0548e4b0e34a7b709738a11cd6f", "1.8.0--r42hf17093f_1": "sha256:9c326597115d7610f25acff1ffb3e8d2c96808fea62c17537a8cbbf6ca909bd3", "1.10.1--r43hf17093f_0": "sha256:4548ad99bc9ecb620f9a7fd145e237f76d1ac0df7bce9416bfe7709efcead34d", "1.12.0--r43hf17093f_0": "sha256:aa4882db1603753a95595f678b7e3fda6cc644252f2f1493128447b47431648a", "1.12.0--r43hf17093f_1": "sha256:3ea0b6f1071394d65efe33d77a84330d01c16affe6b1358cbf4612dc3f5fbc96", "1.16.0--r44he5774e6_0": "sha256:e2b1cd9472da535f9a952179e4e770c6898805c2ed99aac63ad90290fd2ec109", "1.16.0--r44he5774e6_1": "sha256:3b5c09ef2a9f234d0ee103307d02df7b5373abbe9458505d0e2be20f3821731c"}, "docker": "quay.io/biocontainers/bioconductor-scuttle"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scuttle.
shpc-registry automated BioContainers addition for bioconductor-scuttle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scuttle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scuttle:1.16.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scuttle/1.16.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-scuttle/1.16.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scuttle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scuttle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scuttle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scuttle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scuttle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scuttle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scuttle

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