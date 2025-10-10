---
layout: container
name:  "quay.io/biocontainers/bioconductor-bloodcancermultiomics2017"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bloodcancermultiomics2017/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bloodcancermultiomics2017/container.yaml"
updated_at: "2025-10-10 03:44:23.161879"
latest: "1.26.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bloodcancermultiomics2017"
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
 - "1.8.0--r40_0"
 - "1.18.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.26.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bloodcancermultiomics2017"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bloodcancermultiomics2017", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bloodcancermultiomics2017", "latest": {"1.26.0--r44hdfd78af_0": "sha256:a462e4de71654ae5bf4d280c12301701c16d8b6aba4c77e00a037f2863924af5"}, "tags": {"1.8.0--r40_0": "sha256:b6728b6f8186cb323cf83c5a22ebacb4b9881bc8a8aba972e821ebd5062429ad", "1.18.0--r42hdfd78af_0": "sha256:64591edf483b5aaed1b3b8b79f5cf03eaceb2051fca3196c9c553837850d4625", "1.14.0--r41hdfd78af_1": "sha256:069b29c6dbe37a199feb45b0f87c1b0bae519eca0165b89913da18cc54eb8e94", "1.12.0--r41hdfd78af_0": "sha256:15ed07eac37231d726d76bdd6f1d851b86a1e93ea8c17f683081ab562f19691d", "1.10.0--r40hdfd78af_1": "sha256:cd6b3d7ab202bd84daca4f1fd79bdd7d1606164dd13af6e227343f0a42e59347", "1.20.0--r43hdfd78af_0": "sha256:285bab8ce7fc6b875e18ee59564f27038a2a4ae5877bf92e73f060b19fa194e2", "1.22.0--r43hdfd78af_0": "sha256:b5611ffe0b3cb7c1e17ec62ea41704b143f431a0e65332460cd9e076b5b6c475", "1.26.0--r44hdfd78af_0": "sha256:a462e4de71654ae5bf4d280c12301701c16d8b6aba4c77e00a037f2863924af5"}, "docker": "quay.io/biocontainers/bioconductor-bloodcancermultiomics2017", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bloodcancermultiomics2017.
shpc-registry automated BioContainers addition for bioconductor-bloodcancermultiomics2017
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bloodcancermultiomics2017
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bloodcancermultiomics2017:1.26.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bloodcancermultiomics2017/1.26.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bloodcancermultiomics2017/1.26.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bloodcancermultiomics2017-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bloodcancermultiomics2017-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bloodcancermultiomics2017-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bloodcancermultiomics2017-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bloodcancermultiomics2017-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bloodcancermultiomics2017-inspect-deffile:

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