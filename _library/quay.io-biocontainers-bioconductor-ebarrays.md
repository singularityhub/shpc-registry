---
layout: container
name:  "quay.io/biocontainers/bioconductor-ebarrays"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ebarrays/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ebarrays/container.yaml"
updated_at: "2024-10-27 03:08:55.439756"
latest: "2.66.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-ebarrays"

versions:
 - "2.58.0--r41hc0cfd56_2"
 - "2.62.0--r42hc0cfd56_0"
 - "2.62.0--r42ha9d7317_1"
 - "2.64.0--r43ha9d7317_0"
 - "2.66.0--r43ha9d7317_0"
 - "2.66.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-ebarrays"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ebarrays", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ebarrays", "latest": {"2.66.0--r43ha9d7317_1": "sha256:05a2b97e50936844d93b871b56e52cf2df4da0d7815761525d4aa62202740de6"}, "tags": {"2.58.0--r41hc0cfd56_2": "sha256:33b1d46cbff32e9aa14d918ab97b366f58da70739d16c60997a871226ac6dcfa", "2.62.0--r42hc0cfd56_0": "sha256:658fb16ff8cb1ff517fa70a6919e787e8410ecf09ed3fb6decfbf7afe8fe22db", "2.62.0--r42ha9d7317_1": "sha256:82dd6d99e868fdf040170fae1e92ce7d88f4fe276fb0839e41929ac0fd5f6091", "2.64.0--r43ha9d7317_0": "sha256:26e7ff8e93d38ffd5fb2def3bd20b7ba0f9c6f4e65b16216ee9c64d7dade5b7c", "2.66.0--r43ha9d7317_0": "sha256:517a4ea2542493bdd1f34ae4c80c6ba04b109f4be68677fc39337a838abac0ad", "2.66.0--r43ha9d7317_1": "sha256:05a2b97e50936844d93b871b56e52cf2df4da0d7815761525d4aa62202740de6"}, "docker": "quay.io/biocontainers/bioconductor-ebarrays"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ebarrays.
shpc-registry automated BioContainers addition for bioconductor-ebarrays
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ebarrays
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ebarrays:2.66.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ebarrays/2.66.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-ebarrays/2.66.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ebarrays-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ebarrays-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ebarrays-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ebarrays-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ebarrays-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ebarrays-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ebarrays

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