---
layout: container
name:  "quay.io/biocontainers/bioconductor-omada"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-omada/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-omada/container.yaml"
updated_at: "2024-05-22 02:33:52.843599"
latest: "1.4.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-omada"

versions:
 - "1.0.0--r42hc247a5b_0"
 - "1.1.0--r43hf17093f_0"
 - "1.4.0--r43hf17093f_1"
description: "singularity registry hpc automated addition for bioconductor-omada"
config: {"url": "https://biocontainers.pro/tools/bioconductor-omada", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-omada", "latest": {"1.4.0--r43hf17093f_1": "sha256:2538591dd26b52c47826066ad531ebc2d631bbf23cfff0800a653e29e4d2894d"}, "tags": {"1.0.0--r42hc247a5b_0": "sha256:bd77b99037c6ef1be9dca2eb1ec475f74e60faeab009b3f3a7cd3c55b91a18ed", "1.1.0--r43hf17093f_0": "sha256:50a5a430c521be68207cb737575a4e52aee670644cb2054603d9f62a759655bf", "1.4.0--r43hf17093f_1": "sha256:2538591dd26b52c47826066ad531ebc2d631bbf23cfff0800a653e29e4d2894d"}, "docker": "quay.io/biocontainers/bioconductor-omada"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-omada.
singularity registry hpc automated addition for bioconductor-omada
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-omada
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-omada:1.4.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-omada/1.4.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-omada/1.4.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-omada-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omada-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omada-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-omada-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-omada-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-omada-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-omada

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