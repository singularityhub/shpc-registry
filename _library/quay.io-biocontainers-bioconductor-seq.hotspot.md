---
layout: container
name:  "quay.io/biocontainers/bioconductor-seq.hotspot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seq.hotspot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seq.hotspot/container.yaml"
updated_at: "2025-04-17 03:10:20.589273"
latest: "1.6.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seq.hotspot"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.0--r43hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.6.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-seq.hotspot"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seq.hotspot", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-seq.hotspot", "latest": {"1.6.0--r44hdfd78af_0": "sha256:a53450ca6c1af0825d9b41ed498ffbe94132e4d61e962fe428f71b78123aa9fd"}, "tags": {"1.0.0--r43hdfd78af_0": "sha256:4003525a36b89a8781db886620e6e05741fb2b74a7570c1d9d2c801b7059cd03", "1.2.0--r43hdfd78af_0": "sha256:5a7ad050a94c9c8a5ccebf3d84f2854397f9a81a3c3f2a966ff99e43c2b0914a", "1.6.0--r44hdfd78af_0": "sha256:a53450ca6c1af0825d9b41ed498ffbe94132e4d61e962fe428f71b78123aa9fd"}, "docker": "quay.io/biocontainers/bioconductor-seq.hotspot", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seq.hotspot.
singularity registry hpc automated addition for bioconductor-seq.hotspot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seq.hotspot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seq.hotspot:1.6.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seq.hotspot/1.6.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seq.hotspot/1.6.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seq.hotspot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seq.hotspot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seq.hotspot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seq.hotspot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seq.hotspot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seq.hotspot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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