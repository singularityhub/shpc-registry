---
layout: container
name:  "quay.io/biocontainers/bioconductor-gcatest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gcatest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gcatest/container.yaml"
updated_at: "2025-08-08 04:34:29.973825"
latest: "2.6.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gcatest"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hc0cfd56_0"
 - "1.24.0--r41hc0cfd56_2"
 - "1.22.0--r41hd029910_0"
 - "1.20.0--r40hd029910_1"
 - "1.18.0--r40h037d062_0"
 - "1.28.0--r42ha9d7317_1"
 - "2.0.7--r43hdfd78af_0"
 - "2.2.0--r43hdfd78af_0"
 - "2.6.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gcatest"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gcatest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gcatest", "latest": {"2.6.0--r44hdfd78af_0": "sha256:01c4b8ba55820fa6c332b6639fdddf39b1ec9384d33986acf88137b389344c63"}, "tags": {"1.8.0--r3.4.1_0": "sha256:929a4a2ea858ee2b86c1152b42643a7a3b45145e5f2483094726f325770647fe", "1.28.0--r42hc0cfd56_0": "sha256:d6f1dafaa0f76d5eba4546df24e4dde1f43eb638a9e90941b14415e395e711d7", "1.24.0--r41hc0cfd56_2": "sha256:bcb0722f8646cdc2049156202949eb0419f3d8b9015880aebb61f53ae150c5f4", "1.22.0--r41hd029910_0": "sha256:58882f4de666117bc1aa4c404a9f27a6ed698160b6e25f30f7dbbf6b4fa436b1", "1.20.0--r40hd029910_1": "sha256:420e19790ac452957f9ba14730d4fc44e0938feba970f497a6a5797942138dba", "1.18.0--r40h037d062_0": "sha256:da4714df7e1a57c4ecd7cfba19a4fe234a9223a8e644285046c1ed5f64a6e456", "1.28.0--r42ha9d7317_1": "sha256:70592ffd21d20fd3fc26b4b90fd9a4ef59689b1ba08c62f65862bd630c25a98d", "2.0.7--r43hdfd78af_0": "sha256:7a9fc2940e33a957ef45b9ecbabbaa72db03d51ba3db95766e235d094cfd3cac", "2.2.0--r43hdfd78af_0": "sha256:c4b8e52bbdaf6a945f493a9a1797837d58f3cf2be864b41ec586ea9e4ad4a960", "2.6.0--r44hdfd78af_0": "sha256:01c4b8ba55820fa6c332b6639fdddf39b1ec9384d33986acf88137b389344c63"}, "docker": "quay.io/biocontainers/bioconductor-gcatest", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gcatest.
shpc-registry automated BioContainers addition for bioconductor-gcatest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gcatest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gcatest:2.6.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gcatest/2.6.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gcatest/2.6.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gcatest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcatest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcatest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gcatest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gcatest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gcatest-inspect-deffile:

```bash
$ singularity inspect -d <container>
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