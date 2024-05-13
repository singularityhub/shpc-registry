---
layout: container
name:  "quay.io/biocontainers/bioconductor-scde"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scde/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scde/container.yaml"
updated_at: "2024-05-13 03:17:20.681118"
latest: "2.30.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scde"

versions:
 - "2.8.0--r351hfc679d8_0"
 - "2.22.0--r41hc247a5b_2"
 - "2.20.0--r41h399db7b_0"
 - "2.18.0--r40h399db7b_1"
 - "2.16.0--r40h5f743cb_0"
 - "2.14.0--r36he1b5a44_0"
 - "2.26.0--r42hc247a5b_0"
 - "2.26.0--r42hf17093f_1"
 - "2.28.2--r43hf17093f_0"
 - "2.30.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scde"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scde", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scde", "latest": {"2.30.0--r43hf17093f_0": "sha256:fd80d4a4c999e94e96cb9c89c39c21e1a7c0008b555b7168c688af84e94e6add"}, "tags": {"2.8.0--r351hfc679d8_0": "sha256:6a6401ace0c9addc36dc3e3cef15b8ad83495f315b9b4a58fb3edaeb39806444", "2.22.0--r41hc247a5b_2": "sha256:5d14f8e617d9c1894900e3ea17505bfb8de849c7ef41be9bee2154c66ed1cc58", "2.20.0--r41h399db7b_0": "sha256:ff8c396ab88811e4f5a07139e5996cfd7c5bf156c7f174f894e22ccd6ed53f16", "2.18.0--r40h399db7b_1": "sha256:292997b727a3507b0ee153669d254fc9184da39014db7578536b16fdf498a1e6", "2.16.0--r40h5f743cb_0": "sha256:288c00ce23da011e71d0819a6bbf65ca829203dd64a2f566ee7aced99b74cf10", "2.14.0--r36he1b5a44_0": "sha256:50e2bb76daf75c8dcc5e765ca1c5430710adacd9cda21c4784b683e266fc2504", "2.26.0--r42hc247a5b_0": "sha256:0286e9a6c3c2a4242539a5b6db31a35d70a1376a3bbad456c2faea3c3bc235fb", "2.26.0--r42hf17093f_1": "sha256:72fc275b08649ced3b271bf50e3699f001681353220a7a4efec4e5543d8f81e9", "2.28.2--r43hf17093f_0": "sha256:50ebc9059c883072c8cee310ba9c0d4a07669d8cff2710aa44f298e8b55e4fc4", "2.30.0--r43hf17093f_0": "sha256:fd80d4a4c999e94e96cb9c89c39c21e1a7c0008b555b7168c688af84e94e6add"}, "docker": "quay.io/biocontainers/bioconductor-scde"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scde.
shpc-registry automated BioContainers addition for bioconductor-scde
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scde
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scde:2.30.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scde/2.30.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-scde/2.30.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scde-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scde-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scde-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scde-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scde-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scde-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scde

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