---
layout: container
name:  "quay.io/biocontainers/bioconductor-oscope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-oscope/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-oscope/container.yaml"
updated_at: "2025-04-25 02:43:37.042052"
latest: "1.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-oscope"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-oscope"
config: {"url": "https://biocontainers.pro/tools/bioconductor-oscope", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-oscope", "latest": {"1.36.0--r44hdfd78af_0": "sha256:5f3f8d0024e785935e1c64d18c171d631d99556bc2ccd7e256455438037b5329"}, "tags": {"1.8.0--r3.4.1_0": "sha256:de9bae7792f862b69d389d79baf1171584c56c380ce046fb970fda0958ec1a3b", "1.28.0--r42hdfd78af_0": "sha256:16163eaa30d74868e23c0c80c59af81c0efe0203cec040adbe698d0816092e6a", "1.24.0--r41hdfd78af_0": "sha256:68394d01ff9be85703d852d5bb354023c9c2ffb7992240d6f1c411ae331bd376", "1.22.0--r41hdfd78af_0": "sha256:6847c00cb64114b3c5d1a0ded7b1ecf28924ba90f5d98a7d1c40b84c578f1f53", "1.20.0--r40hdfd78af_1": "sha256:7b56f12cd1c2b89adfa1f8df2ba57440171c72d9eb40c8d38dfd3de1bf3f66f8", "1.18.0--r40_0": "sha256:db691db4bfaaae911fc3d0c3f1d47846726cf373706b7f253b7a636e8544efcf", "1.30.0--r43hdfd78af_0": "sha256:4babe8607a90987745b8542c1c3d01b1f18a13e3cd5ea76e44902bdf560eeb16", "1.32.0--r43hdfd78af_0": "sha256:be5429f6f3020ca87f84302634f2c0834de695219bfc1074132d26b2a1b6e48c", "1.36.0--r44hdfd78af_0": "sha256:5f3f8d0024e785935e1c64d18c171d631d99556bc2ccd7e256455438037b5329"}, "docker": "quay.io/biocontainers/bioconductor-oscope", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-oscope.
shpc-registry automated BioContainers addition for bioconductor-oscope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-oscope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-oscope:1.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-oscope/1.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-oscope/1.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-oscope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oscope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oscope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-oscope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-oscope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-oscope-inspect-deffile:

```bash
$ singularity inspect -d <container>
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