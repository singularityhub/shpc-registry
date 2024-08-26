---
layout: container
name:  "quay.io/biocontainers/bioconductor-contibait"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-contibait/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-contibait/container.yaml"
updated_at: "2024-08-26 03:23:17.228305"
latest: "1.30.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-contibait"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341hfc679d8_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h399db7b_1"
 - "1.15.0--r40h5f743cb_0"
 - "1.14.0--r36he1b5a44_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-contibait"
config: {"url": "https://biocontainers.pro/tools/bioconductor-contibait", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-contibait", "latest": {"1.30.0--r43hf17093f_1": "sha256:9db2a3b24198ca6885043e3eb9c69a493c70f55233c7b206b04dcf0e8960407a"}, "tags": {"1.8.0--r341hfc679d8_0": "sha256:188ed116bef3a0382f08a6b665dd8ac735c44fbc2fa85fcb0ffdb1b719a42600", "1.22.0--r41hc247a5b_2": "sha256:93544750937522ee15a0789a45b598859be3a7b9a5c69e83d3f6da7feb33a317", "1.20.0--r41h399db7b_0": "sha256:ff666f8ee50b8574e2ec1b2ac46639f5fb542a5523400ba16dde5679a97ede0d", "1.18.0--r40h399db7b_1": "sha256:50b3d2511106ad0ce915d70d7a3f31529827a68c0e90059b0acc4624e60fd5cb", "1.15.0--r40h5f743cb_0": "sha256:08bc5b9d0b679adeac2966ec24c1c04a29db864f291390e9f4b0b24ce391d78e", "1.14.0--r36he1b5a44_0": "sha256:39694871a0420465f7c2c01c4f4d457ee5e5a752d08e52b4a9a2e877d52f0c04", "1.26.0--r42hc247a5b_0": "sha256:c7fa5878f2ee401c20d8e4ccff5417765440780fee87d27ff6a1980fda30e7d6", "1.26.0--r42hf17093f_1": "sha256:b364b750e0f24a9105d87f90dbf4950da0400b8fdb4dafc71356f06dbe5f8309", "1.28.0--r43hf17093f_0": "sha256:870b4e1ed328e3e94081eeeabedc256a903507de8c35ae1720f8d13086ec208d", "1.30.0--r43hf17093f_0": "sha256:9e400844801a5ec4579f3d0a1e4e53d652a923eccc5454df0aaa878f85682923", "1.30.0--r43hf17093f_1": "sha256:9db2a3b24198ca6885043e3eb9c69a493c70f55233c7b206b04dcf0e8960407a"}, "docker": "quay.io/biocontainers/bioconductor-contibait", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-contibait.
shpc-registry automated BioContainers addition for bioconductor-contibait
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-contibait
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-contibait:1.30.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-contibait/1.30.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-contibait/1.30.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-contibait-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-contibait-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-contibait-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-contibait-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-contibait-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-contibait-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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