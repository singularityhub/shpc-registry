---
layout: container
name:  "quay.io/biocontainers/bioconductor-apeglm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-apeglm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-apeglm/container.yaml"
updated_at: "2025-05-10 03:23:30.358142"
latest: "1.28.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-apeglm"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
 - "1.20.0--r42hf17093f_1"
 - "1.22.1--r43hf17093f_0"
 - "1.24.0--r43hf17093f_0"
 - "1.24.0--r43hf17093f_1"
 - "1.28.0--r44he5774e6_0"
 - "1.28.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-apeglm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-apeglm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-apeglm", "latest": {"1.28.0--r44he5774e6_1": "sha256:0ab3e97e2fd56b43fa22a2b207a9b634cfc34a0583f600a60523213aabbe68f9"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:a456ba3aaeca914384d1434113b183100f81f8e6f0b23b57733c09fedbdf18fc", "1.20.0--r42hc247a5b_0": "sha256:e64fde9ccf4db404b61b98db2ff6544fc345fc23970e75ce3809a78b6992f8f4", "1.16.0--r41hc247a5b_2": "sha256:928feb1d766aa96ab8fb56e7c23d2acde94a36ac1de834dc03cf0494aa8e9b59", "1.14.0--r41h399db7b_0": "sha256:a212ad3664cd6925c4124126cb07aa115f9a2c26f02d495ab814916da4ca4438", "1.12.0--r40h399db7b_1": "sha256:bdb87b987dbd2e8d28e0695d296c99152a1b81d5ead4af4c14c397c64bc27343", "1.10.0--r40h5f743cb_0": "sha256:d1e1d9b68910907967e3b0a9480560f60c1e25752363e6997178c261d5b2c493", "1.20.0--r42hf17093f_1": "sha256:eca8f5762bdbd0a2be8f2cf608e5f2dbe098fdf9a3b20db183733fc3ad50c52a", "1.22.1--r43hf17093f_0": "sha256:d896d3dad053d87eb11f58efc2bd9d79f89af148e43d5fc7db50711b4982a59c", "1.24.0--r43hf17093f_0": "sha256:b15689171879341c54568116e90a3717bd440aa85dea3c1618c62efb9beca1cb", "1.24.0--r43hf17093f_1": "sha256:02dfd9ee511c70a4db5f4e0553bbf0309a832c74e5be707f748bbbe75f9bf611", "1.28.0--r44he5774e6_0": "sha256:5fb87382f3d02978d2c03849c4f8ccc201ca50313b16876c6c1fd29219ecce59", "1.28.0--r44he5774e6_1": "sha256:0ab3e97e2fd56b43fa22a2b207a9b634cfc34a0583f600a60523213aabbe68f9"}, "docker": "quay.io/biocontainers/bioconductor-apeglm", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-apeglm.
shpc-registry automated BioContainers addition for bioconductor-apeglm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-apeglm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-apeglm:1.28.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-apeglm/1.28.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-apeglm/1.28.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-apeglm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-apeglm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-apeglm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-apeglm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-apeglm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-apeglm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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