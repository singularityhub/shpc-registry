---
layout: container
name:  "quay.io/biocontainers/bioconductor-orfik"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-orfik/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-orfik/container.yaml"
updated_at: "2024-01-28 03:43:01.265200"
latest: "1.22.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-orfik"
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
 - "1.8.1--r40h5f743cb_0"
 - "1.18.0--r42hc247a5b_0"
 - "1.14.7--r41hc247a5b_1"
 - "1.12.0--r41h399db7b_0"
 - "1.10.1--r40h5f743cb_0"
 - "1.18.0--r42hf17093f_1"
 - "1.20.0--r43hf17093f_0"
 - "1.22.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-orfik"
config: {"url": "https://biocontainers.pro/tools/bioconductor-orfik", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-orfik", "latest": {"1.22.0--r43hf17093f_0": "sha256:d1384326b5b520240a24d78015b73b73a02629ad9e376a6b57dc846c21055f55"}, "tags": {"1.8.1--r40h5f743cb_0": "sha256:7c8261edc73a588ea1847ea8a620626a12074f546b56a811845dc7799cdb66d2", "1.18.0--r42hc247a5b_0": "sha256:b8a88ed977639ae95196a797548e37823b5c4d0e64c3c7ed5c01e8b828ead521", "1.14.7--r41hc247a5b_1": "sha256:b8c3679fa112a5353bcf9137e4a2f6e2677e8b6b877da984414387b9dd47e8cc", "1.12.0--r41h399db7b_0": "sha256:73b03791fd14af6d6216ce409d2d16432fa2403da1aec9aa524ba6f87b57025a", "1.10.1--r40h5f743cb_0": "sha256:49a1b9fc409266c525b4c1fe69d7cf8c2ccf99d872bd1b90c9f4b58ce930b5de", "1.18.0--r42hf17093f_1": "sha256:9873b713e7aa82311c8afcf95cf3b46d33af84a452a5cb72b3cd1ea6b99ddd38", "1.20.0--r43hf17093f_0": "sha256:02cad29c59853a9d07df419505abe09d7cb34262cc5fafc7a01a300cf4c6ba22", "1.22.0--r43hf17093f_0": "sha256:d1384326b5b520240a24d78015b73b73a02629ad9e376a6b57dc846c21055f55"}, "docker": "quay.io/biocontainers/bioconductor-orfik", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-orfik.
shpc-registry automated BioContainers addition for bioconductor-orfik
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-orfik
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-orfik:1.22.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-orfik/1.22.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-orfik/1.22.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-orfik-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orfik-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orfik-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-orfik-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-orfik-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-orfik-inspect-deffile:

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