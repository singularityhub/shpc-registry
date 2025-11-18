---
layout: container
name:  "quay.io/biocontainers/bioconductor-manor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-manor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-manor/container.yaml"
updated_at: "2025-11-18 04:06:34.234865"
latest: "1.78.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-manor"

versions:
 - "1.66.0--r41hc0cfd56_2"
 - "1.70.0--r42hc0cfd56_0"
 - "1.70.0--r42ha9d7317_1"
 - "1.72.0--r43ha9d7317_0"
 - "1.74.0--r43ha9d7317_0"
 - "1.78.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-manor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-manor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-manor", "latest": {"1.78.0--r44h3df3fcb_0": "sha256:0875dbbdf44bbee9d2dceef6f57253191337d357ba55f97ce4289d241f61d7b6"}, "tags": {"1.66.0--r41hc0cfd56_2": "sha256:79b8ef18b7fd494c5d00b545db7ae3acd8795a8d04dce7c1f2f82edb5dabc7b5", "1.70.0--r42hc0cfd56_0": "sha256:3c1dae10354315004730edd26e6487047fe7a2f1d014da71adc662b43e61a4eb", "1.70.0--r42ha9d7317_1": "sha256:020b741afa0b1aa6716439921e9b587e3695e56d101ac95b1812438ab28fec0a", "1.72.0--r43ha9d7317_0": "sha256:e4f44473c8aadb59eac2be72f80ed24dff83cfbdea5ee9ce82aab5dcf05f04be", "1.74.0--r43ha9d7317_0": "sha256:8c4778483ccb8aa2bce5996c292d2fe5617652d9d42474489d19e35e82133d6a", "1.78.0--r44h3df3fcb_0": "sha256:0875dbbdf44bbee9d2dceef6f57253191337d357ba55f97ce4289d241f61d7b6"}, "docker": "quay.io/biocontainers/bioconductor-manor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-manor.
shpc-registry automated BioContainers addition for bioconductor-manor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-manor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-manor:1.78.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-manor/1.78.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-manor/1.78.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-manor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-manor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-manor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-manor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-manor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-manor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-manor

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