---
layout: container
name:  "quay.io/biocontainers/bioconductor-minet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-minet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-minet/container.yaml"
updated_at: "2025-08-01 10:58:03.366159"
latest: "3.64.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-minet"

versions:
 - "3.52.0--r41hc247a5b_2"
 - "3.56.0--r42hc247a5b_0"
 - "3.56.0--r42hf17093f_2"
 - "3.58.0--r43hf17093f_0"
 - "3.60.0--r43hf17093f_0"
 - "3.60.0--r43hf17093f_1"
 - "3.64.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-minet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-minet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-minet", "latest": {"3.64.0--r44he5774e6_0": "sha256:847e50b895e6aa78e7bb63273cf58410bee4f8e21625e42d8e2f8a6988940d26"}, "tags": {"3.52.0--r41hc247a5b_2": "sha256:4181941308d592f74492ee9f275e3eb0ef8871167bf5c03c35c691141aefaab9", "3.56.0--r42hc247a5b_0": "sha256:6a7b549554de48e108b28b47f0606faf996ead45dc6e490a229af7d2184b19ac", "3.56.0--r42hf17093f_2": "sha256:72e65e2314026167155bde2c4aad00256c0a737ed6a78bf6b3745bc14b90c3a1", "3.58.0--r43hf17093f_0": "sha256:4221e4a8090bac6e8c9dc5bb94ae11411765ef654aa0bd863d6ed22993f50035", "3.60.0--r43hf17093f_0": "sha256:5f186b4247464ef8089e0f399cd2f64db5c81982314f1eff35dc1e4f92eda426", "3.60.0--r43hf17093f_1": "sha256:8940f0441b850cb022e824dd5ff3cfb9669f66d9f650132fdeef09255a7a9de1", "3.64.0--r44he5774e6_0": "sha256:847e50b895e6aa78e7bb63273cf58410bee4f8e21625e42d8e2f8a6988940d26"}, "docker": "quay.io/biocontainers/bioconductor-minet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-minet.
shpc-registry automated BioContainers addition for bioconductor-minet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-minet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-minet:3.64.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-minet/3.64.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-minet/3.64.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-minet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-minet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-minet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-minet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-minet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-minet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-minet

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