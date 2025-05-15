---
layout: container
name:  "quay.io/biocontainers/bioconductor-descan2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-descan2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-descan2/container.yaml"
updated_at: "2025-05-15 04:06:13.665775"
latest: "1.26.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-descan2"
aliases:
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r40h5f743cb_0"
 - "1.18.0--r42hc247a5b_0"
 - "1.14.1--r41hc247a5b_1"
 - "1.12.0--r41h399db7b_0"
 - "1.10.0--r40h399db7b_1"
 - "1.18.0--r42hf17093f_1"
 - "1.20.1--r43hf17093f_0"
 - "1.22.0--r43hf17093f_0"
 - "1.22.0--r43hf17093f_1"
 - "1.26.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-descan2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-descan2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-descan2", "latest": {"1.26.0--r44he5774e6_0": "sha256:f06fbfdeae90872daf60f93ae159bacd9e49915601c60ea5ac8ee1a6b7b9246a"}, "tags": {"1.8.0--r40h5f743cb_0": "sha256:37641c2f246075aa60efea422e8ba3b677d69cc50aded25cd5a53ea421fdf77d", "1.18.0--r42hc247a5b_0": "sha256:647f77a3981c66c3774869acde64d659ce30a2e0869a6d26cea4a60d9c5e8afd", "1.14.1--r41hc247a5b_1": "sha256:0e8143baefbff06d59962a5648ed9ac5d619ac71745503e50f773e54351347f0", "1.12.0--r41h399db7b_0": "sha256:1ed401e5a7e65071d0a367f8b51cdcb1de8eef6daa4f8fe63e5c0f18885bc2dd", "1.10.0--r40h399db7b_1": "sha256:53b7767dfc09f1a7f21d13f21d8fb2d42b3891ceac932950519f500602dc3215", "1.18.0--r42hf17093f_1": "sha256:f07a3dd88965af0623a493d704d9d5e6a521de37a05455d27d085778debaf993", "1.20.1--r43hf17093f_0": "sha256:cd1020b724340fed7a47a360c1500d5cc783c1565b8c133629f776b01bf34606", "1.22.0--r43hf17093f_0": "sha256:9da11e19241b04dea20d9aced4b95a161fc303ac764114ed01d3581424ca040d", "1.22.0--r43hf17093f_1": "sha256:657c6d2c531364aa2141f51ef24d3f7904a7ad493a4db73b6922fd1cfa882142", "1.26.0--r44he5774e6_0": "sha256:f06fbfdeae90872daf60f93ae159bacd9e49915601c60ea5ac8ee1a6b7b9246a"}, "docker": "quay.io/biocontainers/bioconductor-descan2", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-descan2.
shpc-registry automated BioContainers addition for bioconductor-descan2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-descan2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-descan2:1.26.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-descan2/1.26.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-descan2/1.26.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-descan2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-descan2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-descan2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-descan2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-descan2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-descan2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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