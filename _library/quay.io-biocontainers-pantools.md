---
layout: container
name:  "quay.io/biocontainers/pantools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pantools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pantools/container.yaml"
updated_at: "2024-04-03 03:06:00.438228"
latest: "4.3.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pantools"
aliases:
 - "pantools"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "kmc"
 - "kmc_dump"
 - "kmc_tools"
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
versions:
 - "3.3.3--hdfd78af_0"
 - "3.4.0--hdfd78af_0"
 - "4.1.0--hdfd78af_0"
 - "4.0.0--ha11b4f6_1"
 - "4.1.1--hdfd78af_0"
 - "4.2.0--hdfd78af_0"
 - "4.2.1--hdfd78af_0"
 - "4.2.2--hdfd78af_0"
 - "4.2.3--hdfd78af_0"
 - "4.2.3--hdfd78af_1"
 - "4.3.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for pantools"
config: {"url": "https://biocontainers.pro/tools/pantools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pantools", "latest": {"4.3.1--hdfd78af_0": "sha256:25facf0bcaf4cca750f52b1d2a63f3d48117829a1fce52193f1d9ea9eb738d2f"}, "tags": {"3.3.3--hdfd78af_0": "sha256:0818dc6a8f863fe62feb9e1e3558be44c2cf3175ff1412a5b6ed4bf775f57559", "3.4.0--hdfd78af_0": "sha256:1cc614cf02205cd8ccddf1215af915dde1e8db3cee6dc4a1d3df6b516d4fe85d", "4.1.0--hdfd78af_0": "sha256:6945cab3e9726e6fae54c53bca3f431a97da7f2246982b562e5f65a74b812be6", "4.0.0--ha11b4f6_1": "sha256:3900d137519b36d5b21296b7a41111f17a0c13e8ef1febe42ecc94ba41f1667d", "4.1.1--hdfd78af_0": "sha256:b3bd31de490ba8694def1eafb0e3b0756e2b6e307e958bc4ccdcad240b267799", "4.2.0--hdfd78af_0": "sha256:9b9775656a164f75d34f9faf738f89dd8ba276a274b00c2581de8830e1190e3e", "4.2.1--hdfd78af_0": "sha256:6a076e72e773eaecaed4f7185e9289a4eadf7fe7892dfee5ed679fdab1fc6745", "4.2.2--hdfd78af_0": "sha256:b6e460ee2eec354e76f53607304e977e79f03313e558d21c774d618e4d405928", "4.2.3--hdfd78af_0": "sha256:c96166613df9fe0955d024fe642a2a8dfe73ef3b8b970c3533e0842ba0acc1d2", "4.2.3--hdfd78af_1": "sha256:cadcaba3e0f85e489668e4795e26408c83bd3adf2b037bfed75bc1286b71c157", "4.3.1--hdfd78af_0": "sha256:25facf0bcaf4cca750f52b1d2a63f3d48117829a1fce52193f1d9ea9eb738d2f"}, "docker": "quay.io/biocontainers/pantools", "aliases": {"pantools": "/usr/local/bin/pantools", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "kmc": "/usr/local/bin/kmc", "kmc_dump": "/usr/local/bin/kmc_dump", "kmc_tools": "/usr/local/bin/kmc_tools", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pantools.
shpc-registry automated BioContainers addition for pantools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pantools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pantools:4.3.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pantools/4.3.1--hdfd78af_0
$ module help quay.io/biocontainers/pantools/4.3.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pantools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pantools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pantools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pantools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pantools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pantools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pantools

```bash
$ singularity exec <container> /usr/local/bin/pantools
$ podman run --it --rm --entrypoint /usr/local/bin/pantools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pantools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc

```bash
$ singularity exec <container> /usr/local/bin/kmc
$ podman run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_dump

```bash
$ singularity exec <container> /usr/local/bin/kmc_dump
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_tools

```bash
$ singularity exec <container> /usr/local/bin/kmc_tools
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclcm

```bash
$ singularity exec <container> /usr/local/bin/mclcm
$ podman run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclpipeline

```bash
$ singularity exec <container> /usr/local/bin/mclpipeline
$ podman run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
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