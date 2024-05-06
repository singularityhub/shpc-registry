---
layout: container
name:  "quay.io/biocontainers/bioconductor-cytokernel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cytokernel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cytokernel/container.yaml"
updated_at: "2024-05-06 18:59:25.885957"
latest: "1.8.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cytokernel"

versions:
 - "1.0.0--r41hc247a5b_2"
 - "1.4.0--r42hc247a5b_0"
 - "1.4.0--r42hf17093f_1"
 - "1.6.0--r43hf17093f_0"
 - "1.8.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cytokernel"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cytokernel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cytokernel", "latest": {"1.8.0--r43hf17093f_0": "sha256:f095bbd85bead5975065e2f4570fe74e572cdc0dd0d4a3fddc1e47f2304a6eb7"}, "tags": {"1.0.0--r41hc247a5b_2": "sha256:8096ffe932d2046d6b09407a7c570af1303d220271845d27133be8c728ccd557", "1.4.0--r42hc247a5b_0": "sha256:6d8639891afc5fb013f31cc8ea96e58ce23ec5010f835e4d5934115f29ffff07", "1.4.0--r42hf17093f_1": "sha256:deb0d807bf8495f8be731eb06ccc8c8527b92eb9bed2f30d7c389a1cb0bd85c7", "1.6.0--r43hf17093f_0": "sha256:77497ce95fd810a08c3fa33b3328ef3210b82157bed483d51ceb6d166ccb5160", "1.8.0--r43hf17093f_0": "sha256:f095bbd85bead5975065e2f4570fe74e572cdc0dd0d4a3fddc1e47f2304a6eb7"}, "docker": "quay.io/biocontainers/bioconductor-cytokernel"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cytokernel.
shpc-registry automated BioContainers addition for bioconductor-cytokernel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cytokernel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cytokernel:1.8.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cytokernel/1.8.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-cytokernel/1.8.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cytokernel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytokernel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytokernel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cytokernel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cytokernel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cytokernel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cytokernel

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