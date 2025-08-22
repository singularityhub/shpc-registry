---
layout: container
name:  "quay.io/biocontainers/varlociraptor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/varlociraptor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/varlociraptor/container.yaml"
updated_at: "2025-08-22 03:57:11.156232"
latest: "8.7.3--ha8ac579_2"
container_url: "https://biocontainers.pro/tools/varlociraptor"
aliases:
 - "varlociraptor"
versions:
 - "4.1.1--hd302352_0"
 - "8.4.5--h769f52f_0"
 - "8.3.0--h769f52f_1"
 - "8.2.0--h769f52f_0"
 - "8.1.1--h769f52f_2"
 - "8.0.0--hc349b7f_0"
 - "8.5.1--ha8ac579_0"
 - "8.4.14--ha8ac579_0"
 - "8.6.0--ha8ac579_0"
 - "8.6.1--ha8ac579_0"
 - "8.7.1--ha8ac579_0"
 - "8.7.3--ha8ac579_0"
 - "8.7.3--ha8ac579_2"
description: "shpc-registry automated BioContainers addition for varlociraptor"
config: {"url": "https://biocontainers.pro/tools/varlociraptor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for varlociraptor", "latest": {"8.7.3--ha8ac579_2": "sha256:2ad35f504fd128f6f9ab6963023701fa4c3c2ee20bbf073f15b6924b00e03577"}, "tags": {"4.1.1--hd302352_0": "sha256:9500634306b22a73461702cf1ae68aabc2ad10c51f4661f0f5d99ab8cdb1802c", "8.4.5--h769f52f_0": "sha256:9e98dce19b151b38ae753793b43904bfb3bd2a27c8179987a6f855c28a07015e", "8.3.0--h769f52f_1": "sha256:1c32506165b2a2b10df6a819a784875342e40a2e1de6afabed84ef18d0ed3eda", "8.2.0--h769f52f_0": "sha256:68fd2eef8ea389d41b187552109eeb30209664a9815d1e143f6c52e6d8a134b7", "8.1.1--h769f52f_2": "sha256:be313bb79975cd68e49ed722b2ad7a36ee9cf7278b30ff79f8280a95c0ccb2db", "8.0.0--hc349b7f_0": "sha256:bb13b24a8ac4a33960012d755273fbdd3cf28308f341d00b3c0abd5f83641d30", "8.5.1--ha8ac579_0": "sha256:0c248b9f81ed94ec2de05b3a8be859095e80fb5a0271d9e8d6f34a4cd15a7a2f", "8.4.14--ha8ac579_0": "sha256:85ef881a7630f62525317d88db6bb3c32764257dae888a51643874cab2d143db", "8.6.0--ha8ac579_0": "sha256:bf76b903a5c53e9692de1a78bde30881922f0e1bfb16678ad84cfcf0063fa8d8", "8.6.1--ha8ac579_0": "sha256:128d97c39c67c11078f144ec6e689be4e2db9c95001feb956b8ee5e46596ea9c", "8.7.1--ha8ac579_0": "sha256:37436f7698ff36901226ac171e9b71648e8c2960d89d645e75ca57f12bfeb1dd", "8.7.3--ha8ac579_0": "sha256:512749ed1c7cf80882965080887d3dfb26781f9060cf0016e833144b9c934080", "8.7.3--ha8ac579_2": "sha256:2ad35f504fd128f6f9ab6963023701fa4c3c2ee20bbf073f15b6924b00e03577"}, "docker": "quay.io/biocontainers/varlociraptor", "aliases": {"varlociraptor": "/usr/local/bin/varlociraptor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/varlociraptor.
shpc-registry automated BioContainers addition for varlociraptor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/varlociraptor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/varlociraptor:8.7.3--ha8ac579_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/varlociraptor/8.7.3--ha8ac579_2
$ module help quay.io/biocontainers/varlociraptor/8.7.3--ha8ac579_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### varlociraptor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### varlociraptor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### varlociraptor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### varlociraptor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### varlociraptor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### varlociraptor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### varlociraptor

```bash
$ singularity exec <container> /usr/local/bin/varlociraptor
$ podman run --it --rm --entrypoint /usr/local/bin/varlociraptor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varlociraptor   -v ${PWD} -w ${PWD} <container> -c " $@"
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