---
layout: container
name:  "quay.io/biocontainers/bioconductor-ncdfflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ncdfflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ncdfflow/container.yaml"
updated_at: "2025-10-29 03:54:18.012243"
latest: "2.52.0--r44h77050f0_1"
container_url: "https://biocontainers.pro/tools/bioconductor-ncdfflow"

versions:
 - "2.40.0--r41hc247a5b_2"
 - "2.44.0--r42hc247a5b_0"
 - "2.44.0--r42hf17093f_1"
 - "2.46.0--r43hf17093f_0"
 - "2.48.0--r43hf17093f_0"
 - "2.52.0--r44h77050f0_0"
 - "2.52.0--r44h77050f0_1"
description: "shpc-registry automated BioContainers addition for bioconductor-ncdfflow"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ncdfflow", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ncdfflow", "latest": {"2.52.0--r44h77050f0_1": "sha256:a2ec654eac0f9c108a32ef84651add6e09d94bc51706313ee61e938752e9a7ab"}, "tags": {"2.40.0--r41hc247a5b_2": "sha256:35cfb1c68c05d707316e8c88cf3a3bbbaaa8dd37a8914abea34f8cbc2ebafcae", "2.44.0--r42hc247a5b_0": "sha256:df96d4f77405c01df67923d10a5d85de3344fd106b37185c87757961ce4d24e1", "2.44.0--r42hf17093f_1": "sha256:2a80a64590c1f1f7f37b229e98a03b0123c21b6eab220aa686be603997336d73", "2.46.0--r43hf17093f_0": "sha256:ef4c40347f9ac6795384359f49214a9328749b35d62fc03d65f79b163b7da1e5", "2.48.0--r43hf17093f_0": "sha256:100f7ec531f5ebf9b3098e1e6908baa9ec9a3c7be3511f3a1623b6f25d088532", "2.52.0--r44h77050f0_0": "sha256:eab88dc8ac2df5e1ddbb01fe6ddc213beef05b92b3fba40a86e0ddbb93af5b20", "2.52.0--r44h77050f0_1": "sha256:a2ec654eac0f9c108a32ef84651add6e09d94bc51706313ee61e938752e9a7ab"}, "docker": "quay.io/biocontainers/bioconductor-ncdfflow"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ncdfflow.
shpc-registry automated BioContainers addition for bioconductor-ncdfflow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ncdfflow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ncdfflow:2.52.0--r44h77050f0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ncdfflow/2.52.0--r44h77050f0_1
$ module help quay.io/biocontainers/bioconductor-ncdfflow/2.52.0--r44h77050f0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ncdfflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ncdfflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ncdfflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ncdfflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ncdfflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ncdfflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ncdfflow

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