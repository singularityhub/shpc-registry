---
layout: container
name:  "quay.io/biocontainers/bioconductor-funchip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-funchip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-funchip/container.yaml"
updated_at: "2023-07-01 03:42:45.366120"
latest: "1.24.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-funchip"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351hf484d3e_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.16.0--r40h399db7b_1"
 - "1.14.0--r40h5f743cb_0"
 - "1.12.0--r36he1b5a44_0"
 - "1.24.0--r42hc247a5b_0"
 - "1.24.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-funchip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-funchip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-funchip", "latest": {"1.24.0--r42hf17093f_1": "sha256:a1820b34a7d7d67c7499949c1e19789b1a5b93f722f1f1ae559fea20de57ac03"}, "tags": {"1.8.0--r351hf484d3e_0": "sha256:d8296eadaf1491a5a1124089cbe6398e9ae0761af41926bc5e9ca4dd3191f566", "1.20.0--r41hc247a5b_2": "sha256:d0a4cd7e55ffec015fbe615a3e47c7113d36a5da335c37904d951bbf262e556d", "1.18.0--r41h399db7b_0": "sha256:9152073caaae7d2add662ad2eef9df2aaf8562180c34f928d1af36fddec6768b", "1.16.0--r40h399db7b_1": "sha256:375cd7c492ddad3d5206e649238b68d52fda9e47a8a3bebb088bb24aeef38dea", "1.14.0--r40h5f743cb_0": "sha256:3f814eec23cd33ba13ed903a9f83ee69af6ac7486d097cad471f7a810c27a965", "1.12.0--r36he1b5a44_0": "sha256:202bb4608087fde7aec04c2bef281e754df83424c828237339805c351eb3a751", "1.24.0--r42hc247a5b_0": "sha256:61848695e2c9249832d3edbd7e3f102c7b69db5b43a89ed655e1ece6c2804a75", "1.24.0--r42hf17093f_1": "sha256:a1820b34a7d7d67c7499949c1e19789b1a5b93f722f1f1ae559fea20de57ac03"}, "docker": "quay.io/biocontainers/bioconductor-funchip", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-funchip.
shpc-registry automated BioContainers addition for bioconductor-funchip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-funchip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-funchip:1.24.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-funchip/1.24.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-funchip/1.24.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-funchip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-funchip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-funchip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-funchip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-funchip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-funchip-inspect-deffile:

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