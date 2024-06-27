---
layout: container
name:  "quay.io/biocontainers/bioconductor-tximport"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tximport/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tximport/container.yaml"
updated_at: "2024-06-27 03:26:44.735746"
latest: "1.30.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-tximport"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-tximport"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tximport", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tximport", "latest": {"1.30.0--r43hdfd78af_1": "sha256:3a6663ff73393808dba1a4da38138d51aab592026712251c70ee74ffedf85356"}, "tags": {"1.8.0--r341_0": "sha256:ebfc58e2f4fcaa0cbf9e78052d1254475aa132d602b3f2f903c922475724e150", "1.26.0--r42hdfd78af_0": "sha256:244fb166517c9f4823a8088449adda9192f183aa752972c20180013ea2331469", "1.22.0--r41hdfd78af_0": "sha256:213e81fb2d1134b824e43a4be4bd8092319bdefcaeef2a2f9eef19cfc4b271fe", "1.20.0--r41hdfd78af_0": "sha256:857cc40b706b4c0e4d594e9c63d30a943d01d4f0ba2e34db60c629741de1bbe0", "1.18.0--r40hdfd78af_1": "sha256:234b431e0a2644f7c1f6ccb726ecd8ce11e110c5f42bd35a7690d7ca8812aeac", "1.16.0--r40_0": "sha256:4da3cdd54275745bb2c73c44e33c988742befd3adbbfa486a1fb16fb13aa4e44", "1.28.0--r43hdfd78af_0": "sha256:f2247712c572e2450e514ddcb416b4ef31b378a826e7f57d91544bcda52473b6", "1.30.0--r43hdfd78af_1": "sha256:3a6663ff73393808dba1a4da38138d51aab592026712251c70ee74ffedf85356"}, "docker": "quay.io/biocontainers/bioconductor-tximport", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tximport.
shpc-registry automated BioContainers addition for bioconductor-tximport
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tximport
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tximport:1.30.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tximport/1.30.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-tximport/1.30.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tximport-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tximport-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tximport-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tximport-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tximport-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tximport-inspect-deffile:

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