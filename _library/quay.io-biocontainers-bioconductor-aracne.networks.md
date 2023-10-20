---
layout: container
name:  "quay.io/biocontainers/bioconductor-aracne.networks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-aracne.networks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-aracne.networks/container.yaml"
updated_at: "2023-10-20 02:41:25.237938"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-aracne.networks"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.15.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-aracne.networks"
config: {"url": "https://biocontainers.pro/tools/bioconductor-aracne.networks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-aracne.networks", "latest": {"1.26.0--r43hdfd78af_0": "sha256:d6efe9e038337d3dbd8566a4997bafccb98576f8b944d56f34db28de2d2f0456"}, "tags": {"1.8.0--r351_0": "sha256:32c360e32c0aa860ab3a857c9011365348178dbba2ad1dd84933c41927986c47", "1.24.0--r42hdfd78af_0": "sha256:525edb1e63db3d08b9929d4c08cf17ab02a5e7c1d38cbfbf8942560c73486732", "1.20.0--r41hdfd78af_1": "sha256:8462003ca910dbb4f88adb98745a5f66b74a691b2c94eefd2183fa551b309bf2", "1.18.0--r41hdfd78af_0": "sha256:055b69db012c5bef78200704b11dfcc0ab37bcd1e599e0f6dd6391489f48885c", "1.16.0--r40hdfd78af_1": "sha256:99148e4d4104c18e0703a34f9075c4b8747908e3cb0717544999a7be0c626bd1", "1.15.0--r40_0": "sha256:71b2ff39ebe1722960d9cde92cb4a78adbe28938f904f0a848afb3462f11403f", "1.26.0--r43hdfd78af_0": "sha256:d6efe9e038337d3dbd8566a4997bafccb98576f8b944d56f34db28de2d2f0456"}, "docker": "quay.io/biocontainers/bioconductor-aracne.networks", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-aracne.networks.
shpc-registry automated BioContainers addition for bioconductor-aracne.networks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-aracne.networks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-aracne.networks:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-aracne.networks/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-aracne.networks/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-aracne.networks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aracne.networks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aracne.networks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-aracne.networks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-aracne.networks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-aracne.networks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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