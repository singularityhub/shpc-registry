---
layout: container
name:  "quay.io/biocontainers/bioconductor-glad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-glad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-glad/container.yaml"
updated_at: "2025-09-18 05:46:24.329865"
latest: "2.70.0--r44h310a8c3_0"
container_url: "https://biocontainers.pro/tools/bioconductor-glad"

versions:
 - "2.58.0--r41hd4b0f26_3"
 - "2.62.0--r42hd4b0f26_0"
 - "2.62.0--r42h7c4fd5e_2"
 - "2.64.0--r43h7c4fd5e_0"
 - "2.66.0--r43h7c4fd5e_0"
 - "2.70.0--r44h310a8c3_0"
description: "shpc-registry automated BioContainers addition for bioconductor-glad"
config: {"url": "https://biocontainers.pro/tools/bioconductor-glad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-glad", "latest": {"2.70.0--r44h310a8c3_0": "sha256:b27a02572c4728b246d36deb1c37f1fc8b91e7aa65bdafacb2ab93d7e02407c7"}, "tags": {"2.58.0--r41hd4b0f26_3": "sha256:86f1d3508a046245b5c9fc463fcccd1fcb5830182b95e638479c192b7819c48c", "2.62.0--r42hd4b0f26_0": "sha256:6a61fdc25a7c1c40f282297cd94624e59460a446c5cbf4abbd89f3cfc7cae106", "2.62.0--r42h7c4fd5e_2": "sha256:1a3f905e0aa4aec26d0963b506d1ee5749b64f0cfeb27945e64e35084d4e03f9", "2.64.0--r43h7c4fd5e_0": "sha256:723cc087e3c97e063a4b4ae24343ba7e76d3625592ae7e7ee1dc7baf95be4344", "2.66.0--r43h7c4fd5e_0": "sha256:abc0674a4a954bb67f1a80c42b9fa09658b6a4b42b2a55a6ce66acd1e6ee2084", "2.70.0--r44h310a8c3_0": "sha256:b27a02572c4728b246d36deb1c37f1fc8b91e7aa65bdafacb2ab93d7e02407c7"}, "docker": "quay.io/biocontainers/bioconductor-glad"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-glad.
shpc-registry automated BioContainers addition for bioconductor-glad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-glad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-glad:2.70.0--r44h310a8c3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-glad/2.70.0--r44h310a8c3_0
$ module help quay.io/biocontainers/bioconductor-glad/2.70.0--r44h310a8c3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-glad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-glad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-glad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-glad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-glad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-glad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-glad

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