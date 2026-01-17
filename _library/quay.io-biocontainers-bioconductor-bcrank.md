---
layout: container
name:  "quay.io/biocontainers/bioconductor-bcrank"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bcrank/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bcrank/container.yaml"
updated_at: "2026-01-17 04:14:00.437833"
latest: "1.68.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bcrank"

versions:
 - "1.56.0--r41hc0cfd56_2"
 - "1.60.0--r42hc0cfd56_0"
 - "1.60.0--r42ha9d7317_1"
 - "1.62.0--r43ha9d7317_0"
 - "1.64.0--r43ha9d7317_0"
 - "1.64.0--r43ha9d7317_1"
 - "1.68.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bcrank"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bcrank", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bcrank", "latest": {"1.68.0--r44h3df3fcb_0": "sha256:66e17593a4c7970df9093b39d2f1ebfb6fe43c37088ca29f1e0a7e936010ff45"}, "tags": {"1.56.0--r41hc0cfd56_2": "sha256:46932b601f4b18124dfe16e0915ae5f7789ebaba748dba7973ba5440eaeb26cb", "1.60.0--r42hc0cfd56_0": "sha256:4bdae8a9e0ce56015ede356a06a36af8145bdc0e433a10306616ac3ee115f74e", "1.60.0--r42ha9d7317_1": "sha256:2578ee22a85ab7a996010911844b64e99cbb550be4b97c6ccaf4883f8a54730e", "1.62.0--r43ha9d7317_0": "sha256:4de24e78605d6eba64685c8cc03f2ea575c85376364bd912c76dd7893fabd042", "1.64.0--r43ha9d7317_0": "sha256:977e75929ca4ef786f6144a5a0488e91ee0fa31dc7ef395c949c1f93238a1cbe", "1.64.0--r43ha9d7317_1": "sha256:1ed87f0d2f830e7cd107082f2351ff20f1ab7c2d9a54bb9b9157f2d937f7fd4b", "1.68.0--r44h3df3fcb_0": "sha256:66e17593a4c7970df9093b39d2f1ebfb6fe43c37088ca29f1e0a7e936010ff45"}, "docker": "quay.io/biocontainers/bioconductor-bcrank"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bcrank.
shpc-registry automated BioContainers addition for bioconductor-bcrank
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bcrank
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bcrank:1.68.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bcrank/1.68.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-bcrank/1.68.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bcrank-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bcrank-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bcrank-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bcrank-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bcrank-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bcrank-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bcrank

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