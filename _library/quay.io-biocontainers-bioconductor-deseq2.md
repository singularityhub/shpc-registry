---
layout: container
name:  "quay.io/biocontainers/bioconductor-deseq2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-deseq2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-deseq2/container.yaml"
updated_at: "2024-08-31 03:17:11.013026"
latest: "1.42.0--r43hf17093f_2"
container_url: "https://biocontainers.pro/tools/bioconductor-deseq2"

versions:
 - "1.34.0--r41hc247a5b_3"
 - "1.38.0--r42hc247a5b_0"
 - "1.38.0--r42hf17093f_1"
 - "1.40.2--r43hf17093f_0"
 - "1.42.0--r43hf17093f_0"
 - "1.42.0--r43hf17093f_1"
 - "1.42.0--r43hf17093f_2"
description: "shpc-registry automated BioContainers addition for bioconductor-deseq2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-deseq2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-deseq2", "latest": {"1.42.0--r43hf17093f_2": "sha256:2d299c5f045c65879e8da189bba17857963d50703af5410003e7e84883deef13"}, "tags": {"1.34.0--r41hc247a5b_3": "sha256:c06884d353effb957123c0e966554f0690fb6ae1ecce8c02919a1877a82339f4", "1.38.0--r42hc247a5b_0": "sha256:bfa2b49c155c117a0cb48db177c030d175cdb427b3d111017e2559981f47de01", "1.38.0--r42hf17093f_1": "sha256:ceeb8b9e66bcef07cf465adb75cb112d9c38b460fd523a47addd90e168f86ddd", "1.40.2--r43hf17093f_0": "sha256:505015440c7fe39d47f0ec05f6ab40f3dce21e23a06299963641a1e2048b525b", "1.42.0--r43hf17093f_0": "sha256:7685bd96cbffdfcd705f1d27a4108f9573444c2de4227863f9d8875ccf328055", "1.42.0--r43hf17093f_1": "sha256:80b2dea3b2b280dad957eed4bd07cf7679afddacadc125b616d56b6c9da12902", "1.42.0--r43hf17093f_2": "sha256:2d299c5f045c65879e8da189bba17857963d50703af5410003e7e84883deef13"}, "docker": "quay.io/biocontainers/bioconductor-deseq2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-deseq2.
shpc-registry automated BioContainers addition for bioconductor-deseq2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-deseq2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-deseq2:1.42.0--r43hf17093f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-deseq2/1.42.0--r43hf17093f_2
$ module help quay.io/biocontainers/bioconductor-deseq2/1.42.0--r43hf17093f_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-deseq2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deseq2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deseq2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-deseq2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-deseq2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-deseq2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-deseq2

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