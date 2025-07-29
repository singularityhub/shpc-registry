---
layout: container
name:  "quay.io/biocontainers/libcifpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libcifpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libcifpp/container.yaml"
updated_at: "2025-07-29 04:35:19.543111"
latest: "8.0.1--h077b44d_3"
container_url: "https://biocontainers.pro/tools/libcifpp"

versions:
 - "5.0.0--h46c59ee_0"
 - "5.0.0--hd9a51b5_2"
 - "7.0.4--h2202e69_0"
 - "7.0.4--h43eeafb_1"
 - "7.0.5--h43eeafb_0"
 - "7.0.7--h43eeafb_0"
 - "7.0.8--h43eeafb_0"
 - "7.0.8--h5ca1c30_1"
 - "7.0.9--h5ca1c30_0"
 - "8.0.0--h077b44d_1"
 - "8.0.1--h077b44d_0"
 - "8.0.1--h077b44d_3"
description: "singularity registry hpc automated addition for libcifpp"
config: {"url": "https://biocontainers.pro/tools/libcifpp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for libcifpp", "latest": {"8.0.1--h077b44d_3": "sha256:188bc743a6edf8dc2658670bfb8784feae557a20ba1836ea4ed633d12a1c959b"}, "tags": {"5.0.0--h46c59ee_0": "sha256:339abdd36e61aeb29221d0de8d0ceb05f96eec657ca3ffb0d4ba86cb568f2734", "5.0.0--hd9a51b5_2": "sha256:f5870c8cea236d1e532de1024f55ec92a8b0b29cc2e4e55b2b5609cf42578cef", "7.0.4--h2202e69_0": "sha256:6111bbf564d63390387efc6c9652b409594587ab8fdd120169463ed5e21b8142", "7.0.4--h43eeafb_1": "sha256:d6b7ca791e5c1d30fd8797323dd8b6599bc3df4f1c0d82ce094cd7f997691798", "7.0.5--h43eeafb_0": "sha256:99f1431883aa04214e90d2ea50f43efa974a997b91d108d433b30f90f017bb25", "7.0.7--h43eeafb_0": "sha256:764fc4263a884bed707e77270fe40679ca1c9ee5fa733e89125a48fd5c8e9406", "7.0.8--h43eeafb_0": "sha256:87c7d72bebf5c377fcdce79252fd803073ded26ff39c00fbef1e6f75247bc890", "7.0.8--h5ca1c30_1": "sha256:51bd6c53b5eb965b52c17876f07c5fab7285db327ca6cb10ea5cf5feb531541f", "7.0.9--h5ca1c30_0": "sha256:43f38159e1b4d75b00e84f7ba4a03cdff88ae5183addcf05b750914e286e3c71", "8.0.0--h077b44d_1": "sha256:b235831f02df3a672dbb7aee27519817f1a8d67659a3b376df1829e9da524375", "8.0.1--h077b44d_0": "sha256:567ef1285c1046d712643266fc2c09a3dd7e4bd0000dcc515f60c53a175b5a8b", "8.0.1--h077b44d_3": "sha256:188bc743a6edf8dc2658670bfb8784feae557a20ba1836ea4ed633d12a1c959b"}, "docker": "quay.io/biocontainers/libcifpp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libcifpp.
singularity registry hpc automated addition for libcifpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libcifpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libcifpp:8.0.1--h077b44d_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libcifpp/8.0.1--h077b44d_3
$ module help quay.io/biocontainers/libcifpp/8.0.1--h077b44d_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libcifpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libcifpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libcifpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libcifpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libcifpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libcifpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libcifpp

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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