---
layout: container
name:  "quay.io/biocontainers/bioconductor-chromdraw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chromdraw/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chromdraw/container.yaml"
updated_at: "2024-02-17 02:25:44.960357"
latest: "2.32.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chromdraw"
aliases:
 - "wget"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.0--r3.4.1_0"
 - "2.28.0--r42hc247a5b_0"
 - "2.24.0--r41hc247a5b_2"
 - "2.22.0--r41h399db7b_0"
 - "2.20.0--r40h399db7b_1"
 - "2.18.0--r40h5f743cb_0"
 - "2.28.0--r42hf17093f_1"
 - "2.30.0--r43hf17093f_0"
 - "2.32.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chromdraw"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chromdraw", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chromdraw", "latest": {"2.32.0--r43hf17093f_0": "sha256:c034db9f7a715f7afa7707262643f9d591e7544ce9a7373bec87aa245901c902"}, "tags": {"2.8.0--r3.4.1_0": "sha256:dbdc1702a3c869418a860a4007d3156e31e3a2065931c6dc2f55576e7f402075", "2.28.0--r42hc247a5b_0": "sha256:992f8f2bef7632975a3e3254f3c21c12aef9730c455ed8ab357f545592ef1ffc", "2.24.0--r41hc247a5b_2": "sha256:b7ea68912677a8c1c0cb654293e6cb935131dd6378feb424dbd7d646c29aace6", "2.22.0--r41h399db7b_0": "sha256:d8f089465e3d61bb53f5f5e3a9d78464ddbbad47f45f5e28a4908608e8052a23", "2.20.0--r40h399db7b_1": "sha256:3951d9fe820b057a8c9b6d63bac46cd0aa612311e18ff46456a62c713f668ecc", "2.18.0--r40h5f743cb_0": "sha256:76a0699ce60cba793143930d83c696f25121ad61777e33e4b18deb5d02bbff3f", "2.28.0--r42hf17093f_1": "sha256:9882938f6168596b2ac4b8876252da9e208dd564fbbfa54f8cf72957370a29d1", "2.30.0--r43hf17093f_0": "sha256:ab43f3395f9a527a1a5e25a8f0cf09faa45c190e780bbd744e93d8d571aed484", "2.32.0--r43hf17093f_0": "sha256:c034db9f7a715f7afa7707262643f9d591e7544ce9a7373bec87aa245901c902"}, "docker": "quay.io/biocontainers/bioconductor-chromdraw", "aliases": {"wget": "/usr/local/bin/wget", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chromdraw.
shpc-registry automated BioContainers addition for bioconductor-chromdraw
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chromdraw
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chromdraw:2.32.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chromdraw/2.32.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-chromdraw/2.32.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chromdraw-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromdraw-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromdraw-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chromdraw-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chromdraw-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chromdraw-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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