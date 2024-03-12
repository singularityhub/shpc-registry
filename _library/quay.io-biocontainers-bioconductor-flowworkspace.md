---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowworkspace"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowworkspace/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowworkspace/container.yaml"
updated_at: "2024-03-12 02:32:14.212615"
latest: "4.14.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowworkspace"

versions:
 - "4.6.0--r41hc247a5b_2"
 - "4.10.0--r42hc247a5b_0"
 - "4.10.0--r42hf17093f_1"
 - "4.12.0--r43hf17093f_0"
 - "4.14.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowworkspace"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowworkspace", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowworkspace", "latest": {"4.14.0--r43hf17093f_0": "sha256:8d3947206330096ff16fab54fd03de373f54017fb08a95661f8631ae373de6bc"}, "tags": {"4.6.0--r41hc247a5b_2": "sha256:9b86d8f42c41e0fbe654a85586c9135e183ec6de91f468c08fa55127b3c2a371", "4.10.0--r42hc247a5b_0": "sha256:c0a21d6fd0d1477e40ecdf05797aae8d6d01c901da8db182d2d0ffdef8902dee", "4.10.0--r42hf17093f_1": "sha256:6d3e8d297c1716e2e82bf65a01bf3d7ba835d9b8e4ebb34915483c49658a24b3", "4.12.0--r43hf17093f_0": "sha256:a42d9dc3de7de746be1d3d6a018189f62abaf9f9800a3c4ba8d31c98dd0df360", "4.14.0--r43hf17093f_0": "sha256:8d3947206330096ff16fab54fd03de373f54017fb08a95661f8631ae373de6bc"}, "docker": "quay.io/biocontainers/bioconductor-flowworkspace"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowworkspace.
shpc-registry automated BioContainers addition for bioconductor-flowworkspace
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowworkspace
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowworkspace:4.14.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowworkspace/4.14.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-flowworkspace/4.14.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowworkspace-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowworkspace-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowworkspace-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowworkspace-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowworkspace-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowworkspace-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowworkspace

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