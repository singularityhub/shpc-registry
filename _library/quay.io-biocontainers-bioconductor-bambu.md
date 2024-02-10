---
layout: container
name:  "quay.io/biocontainers/bioconductor-bambu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bambu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bambu/container.yaml"
updated_at: "2024-02-10 02:50:38.038885"
latest: "3.4.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bambu"
aliases:
 - "xgboost"
versions:
 - "2.0.6--r41hc247a5b_1"
 - "3.0.1--r42hc247a5b_0"
 - "3.0.5--r42hc247a5b_0"
 - "3.0.6--r42hc247a5b_0"
 - "3.0.8--r42hc247a5b_0"
 - "3.0.8--r42hf17093f_1"
 - "3.2.4--r43hf17093f_0"
 - "3.4.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bambu"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bambu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bambu", "latest": {"3.4.0--r43hf17093f_0": "sha256:02e0481d9a1dd87d517147f6cce3159484b67caead2e66f12c4c5171e25a6693"}, "tags": {"2.0.6--r41hc247a5b_1": "sha256:dc456fb2c0abfeb865104670cade38e62205daeb15347b24fe5c3f0d4d9b93d5", "3.0.1--r42hc247a5b_0": "sha256:15e9236ba5abe34941a3106b28684765c37748b82e9722811a1b4e6749b21304", "3.0.5--r42hc247a5b_0": "sha256:bcbac11f98154c82436dae8f9dbe0820f5d1e39f31f2dd4cb59d887ff50ac33f", "3.0.6--r42hc247a5b_0": "sha256:93b63b7d752a33a20d864810828d1d30eaaa43be34c79eb38add2d11d2dc25ae", "3.0.8--r42hc247a5b_0": "sha256:6a79bba2c1abc9a7c3a2d71e3a2aefd3ab86c6cdb8152ae96c71d5b6242508a2", "3.0.8--r42hf17093f_1": "sha256:f3471d69e85010d27a52830b87d3c894eae2fe6dcecbecb871be43817099f540", "3.2.4--r43hf17093f_0": "sha256:d9527137be709d1960b58f9b2ca5a2949bc73193f8239ca7ccdea0ff64794323", "3.4.0--r43hf17093f_0": "sha256:02e0481d9a1dd87d517147f6cce3159484b67caead2e66f12c4c5171e25a6693"}, "docker": "quay.io/biocontainers/bioconductor-bambu", "aliases": {"xgboost": "/usr/local/bin/xgboost"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bambu.
shpc-registry automated BioContainers addition for bioconductor-bambu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bambu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bambu:3.4.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bambu/3.4.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-bambu/3.4.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bambu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bambu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bambu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bambu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bambu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bambu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xgboost

```bash
$ singularity exec <container> /usr/local/bin/xgboost
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
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