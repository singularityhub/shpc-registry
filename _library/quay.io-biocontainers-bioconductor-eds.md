---
layout: container
name:  "quay.io/biocontainers/bioconductor-eds"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-eds/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-eds/container.yaml"
updated_at: "2025-07-31 11:32:36.970541"
latest: "1.8.0--r44h77050f0_0"
container_url: "https://biocontainers.pro/tools/bioconductor-eds"

versions:
 - "1.0.0--r42hc247a5b_0"
 - "1.0.0--r42hf17093f_2"
 - "1.2.0--r43hf17093f_0"
 - "1.4.0--r43hf17093f_0"
 - "1.8.0--r44h77050f0_0"
description: "singularity registry hpc automated addition for bioconductor-eds"
config: {"url": "https://biocontainers.pro/tools/bioconductor-eds", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-eds", "latest": {"1.8.0--r44h77050f0_0": "sha256:d46b0fb13140212fcc69c9ad7d70f5ffb40f2b8c754d6a03a3219adca08c46d6"}, "tags": {"1.0.0--r42hc247a5b_0": "sha256:efa21a1e35c167b58584d770a79297ba6ba96b49e6aac7fd7face2afe9aae86d", "1.0.0--r42hf17093f_2": "sha256:b98e6ca4ec6e0b4c4c6310db15ac7550baaed67e0f56cababac8d4d09f36146e", "1.2.0--r43hf17093f_0": "sha256:b2daba6a5a6e325d86ab9eaa79d5efbf49fdc7646e74eeccfb7ef7822038080e", "1.4.0--r43hf17093f_0": "sha256:554f98ba7ef68870596db01b9c1d60a501934a114a95be7f881c26cbd9bacc8e", "1.8.0--r44h77050f0_0": "sha256:d46b0fb13140212fcc69c9ad7d70f5ffb40f2b8c754d6a03a3219adca08c46d6"}, "docker": "quay.io/biocontainers/bioconductor-eds"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-eds.
singularity registry hpc automated addition for bioconductor-eds
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-eds
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-eds:1.8.0--r44h77050f0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-eds/1.8.0--r44h77050f0_0
$ module help quay.io/biocontainers/bioconductor-eds/1.8.0--r44h77050f0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-eds-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eds-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eds-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-eds-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-eds-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-eds-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-eds

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