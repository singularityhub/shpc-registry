---
layout: container
name:  "quay.io/biocontainers/fgbio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fgbio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fgbio/container.yaml"
updated_at: "2025-09-23 05:11:07.350679"
latest: "3.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/fgbio"
aliases:
 - "fgbio"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
versions:
 - "2.0.2--hdfd78af_0"
 - "2.1.0--hdfd78af_0"
 - "2.2.1--hdfd78af_0"
 - "2.3.0--hdfd78af_0"
 - "2.4.0--hdfd78af_0"
 - "2.5.0--hdfd78af_0"
 - "2.5.21--hdfd78af_0"
 - "3.0.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for fgbio"
config: {"url": "https://biocontainers.pro/tools/fgbio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fgbio", "latest": {"3.0.0--hdfd78af_0": "sha256:81a9447ffed0ad662d3c5f51424193e0da9c889be057ae5cbefcd57eadb9ad4b"}, "tags": {"2.0.2--hdfd78af_0": "sha256:135dd9bcd5d2819b93b69d7c9433c80f0ff4bc40f9cbd911b638ee98183f2dc8", "2.1.0--hdfd78af_0": "sha256:3342c92a9f76980f4ad6b3387188ba723813802bdda628be3a04e9a30bce4678", "2.2.1--hdfd78af_0": "sha256:cc44fe9e72af1232907caa322284bed80f48c57313503e25fa8fac150719aebb", "2.3.0--hdfd78af_0": "sha256:81a17cd5ab75c4bb85a64f1ed913b05403e539fc99323970800da8b84f1449dc", "2.4.0--hdfd78af_0": "sha256:ad405ce298ea9aafc95d402f6d66945a06ee4df5a3398d31b353a75e1402aa69", "2.5.0--hdfd78af_0": "sha256:a82e5df9da9350cdc79701a5afd3c88a9c4416291da2544bee8169a94f72f0cc", "2.5.21--hdfd78af_0": "sha256:29c5b2570ff644ff38a8a165513d86961c67a4642a0fddf90796141b3797b53d", "3.0.0--hdfd78af_0": "sha256:81a9447ffed0ad662d3c5f51424193e0da9c889be057ae5cbefcd57eadb9ad4b"}, "docker": "quay.io/biocontainers/fgbio", "aliases": {"fgbio": "/usr/local/bin/fgbio", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fgbio.
shpc-registry automated BioContainers addition for fgbio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fgbio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fgbio:3.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fgbio/3.0.0--hdfd78af_0
$ module help quay.io/biocontainers/fgbio/3.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fgbio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fgbio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fgbio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fgbio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fgbio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fgbio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fgbio

```bash
$ singularity exec <container> /usr/local/bin/fgbio
$ podman run --it --rm --entrypoint /usr/local/bin/fgbio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgbio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
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