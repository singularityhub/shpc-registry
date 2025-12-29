---
layout: container
name:  "quay.io/biocontainers/pywfa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pywfa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pywfa/container.yaml"
updated_at: "2025-12-29 04:20:48.939497"
latest: "0.5.1--py39hbcbf7aa_4"
container_url: "https://biocontainers.pro/tools/pywfa"

versions:
 - "0.4.1--hec16e2b_0"
 - "0.5.0--hec16e2b_0"
 - "0.4.2--hec16e2b_0"
 - "0.5.1--h031d066_0"
 - "0.5.1--py39hf95cd2a_2"
 - "0.5.1--py38he5da3d1_2"
 - "0.5.1--py39hbcbf7aa_4"
description: "singularity registry hpc automated addition for pywfa"
config: {"url": "https://biocontainers.pro/tools/pywfa", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pywfa", "latest": {"0.5.1--py39hbcbf7aa_4": "sha256:bda2c9f24d6bfb3d54edbdaaab46896c6572de2b6d100b33f95caedc0f7a379c"}, "tags": {"0.4.1--hec16e2b_0": "sha256:ef0edf82a8c6820a94c47e9dab04fab06779d537aa80982e773a73579c0f59c0", "0.5.0--hec16e2b_0": "sha256:f082c548ed89a70b89e3fe84f6ff07f1f845bc3076e2734396e3b7532517170b", "0.4.2--hec16e2b_0": "sha256:7cbec4a01b3f5a878e45a0e4595445817485880239baaf0062aa0427ea447918", "0.5.1--h031d066_0": "sha256:0f2df4d48e6deb216cbcb612bf044bbd993633d4f7f8b3947fd13d6ebd3783d9", "0.5.1--py39hf95cd2a_2": "sha256:d91581773bac49fc732a921390def212faf02a7768c9c626fa7d1564400bff9a", "0.5.1--py38he5da3d1_2": "sha256:25ce1a807427aeb51c1b850205aad535ff4932ce84d008e6843682a51dede1cf", "0.5.1--py39hbcbf7aa_4": "sha256:bda2c9f24d6bfb3d54edbdaaab46896c6572de2b6d100b33f95caedc0f7a379c"}, "docker": "quay.io/biocontainers/pywfa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pywfa.
singularity registry hpc automated addition for pywfa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pywfa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pywfa:0.5.1--py39hbcbf7aa_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pywfa/0.5.1--py39hbcbf7aa_4
$ module help quay.io/biocontainers/pywfa/0.5.1--py39hbcbf7aa_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pywfa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pywfa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pywfa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pywfa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pywfa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pywfa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pywfa

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