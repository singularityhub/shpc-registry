---
layout: container
name:  "quay.io/biocontainers/pyslow5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyslow5/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyslow5/container.yaml"
updated_at: "2025-08-24 04:04:32.951874"
latest: "1.3.1--py310h9fea4d1_0"
container_url: "https://biocontainers.pro/tools/pyslow5"
aliases:
 - "x86_64-conda_cos7-linux-gnu-ld"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.7.0--py39h6471ffd_0"
 - "0.8.0--py310hdacdf33_0"
 - "1.1.0--py39h3f6da51_0"
 - "1.0.0--py310h1ae98be_3"
 - "0.9.0--py27h30f897e_0"
 - "0.8.0--py38h616c765_0"
 - "0.7.0--py27h30f897e_0"
 - "1.1.0--py311h591056c_1"
 - "1.2.0--py39h5219a86_0"
 - "1.3.0--py310h1c83a3d_1"
 - "1.3.0--py310h9fea4d1_2"
 - "1.3.1--py310h9fea4d1_0"
description: "shpc-registry automated BioContainers addition for pyslow5"
config: {"url": "https://biocontainers.pro/tools/pyslow5", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyslow5", "latest": {"1.3.1--py310h9fea4d1_0": "sha256:177f26e2a65143e9a994e58b0577c5940b1003508b787addc9434d53634ca3ca"}, "tags": {"0.7.0--py39h6471ffd_0": "sha256:e898c7978c38db51683ec354a8723040cef681c64f6e1f852978963e09eb86e7", "0.8.0--py310hdacdf33_0": "sha256:0a6f5e20e390c6c44c5a43e0668e352d6b0a070be5481cbd9ac8a37c4452525d", "1.1.0--py39h3f6da51_0": "sha256:64cee49cbae3bcef9b868eab28801f736bd084a30a7f006c9c5c5da5fdcd58bd", "1.0.0--py310h1ae98be_3": "sha256:4beeb26b487549e0b1111117f8e16f29f23d2f0f9a5acda9f33df1de9683cc4c", "0.9.0--py27h30f897e_0": "sha256:70eb036119ad79e17bc7dc451016c6e2800882ca3f40f151871ee6fd5f006b08", "0.8.0--py38h616c765_0": "sha256:3f38517c97077c4f1d35ba5dd46ee00c033695f5d7489b016bcbc220400b2090", "0.7.0--py27h30f897e_0": "sha256:6a0819e9ffb8133a72377873cf345be11c259056cf89543f7549d3ca196df163", "1.1.0--py311h591056c_1": "sha256:2c2ff4720b71c4ef7969b0a76302e082f78b81455590a23b2a967d4414cfc113", "1.2.0--py39h5219a86_0": "sha256:c06b2acea4af57974bfbfa1c518d23f0eea35374226f16710b1edcb6609ab747", "1.3.0--py310h1c83a3d_1": "sha256:ec22eb0067842ca3c53a70029412a808a5437173c7da6a12d27b5e3655f87917", "1.3.0--py310h9fea4d1_2": "sha256:c30fdf175b29ca2cf1f4ef2a532a6617ed70920519a106a63d36eb84597e6496", "1.3.1--py310h9fea4d1_0": "sha256:177f26e2a65143e9a994e58b0577c5940b1003508b787addc9434d53634ca3ca"}, "docker": "quay.io/biocontainers/pyslow5", "aliases": {"x86_64-conda_cos7-linux-gnu-ld": "/usr/local/bin/x86_64-conda_cos7-linux-gnu-ld", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyslow5.
shpc-registry automated BioContainers addition for pyslow5
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyslow5
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyslow5:1.3.1--py310h9fea4d1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyslow5/1.3.1--py310h9fea4d1_0
$ module help quay.io/biocontainers/pyslow5/1.3.1--py310h9fea4d1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyslow5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyslow5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyslow5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyslow5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyslow5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyslow5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda_cos7-linux-gnu-ld

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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