---
layout: container
name:  "quay.io/biocontainers/pyhmmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyhmmer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyhmmer/container.yaml"
updated_at: "2025-05-15 03:12:25.914972"
latest: "0.11.0--py39hbcbf7aa_0"
container_url: "https://biocontainers.pro/tools/pyhmmer"
aliases:
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.4.7--py38h4a8c8d9_0"
 - "0.10.10--py310h4b81fae_0"
 - "0.9.0--py38he5da3d1_0"
 - "0.8.2--py38he5da3d1_0"
 - "0.7.2--py310h1425a21_0"
 - "0.6.3--py310h1425a21_0"
 - "0.10.11--py38he5da3d1_0"
 - "0.10.12--py39hf95cd2a_0"
 - "0.10.12--py38h0020b31_1"
 - "0.10.14--py39hff71179_0"
 - "0.10.14--py310h7c593f9_1"
 - "0.10.15--py310h7c593f9_0"
 - "0.10.15--py310h1fe012e_1"
 - "0.11.0--py39hbcbf7aa_0"
description: "shpc-registry automated BioContainers addition for pyhmmer"
config: {"url": "https://biocontainers.pro/tools/pyhmmer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyhmmer", "latest": {"0.11.0--py39hbcbf7aa_0": "sha256:3b240f701cdf817baf82efcb4c8af00bbe308114a591dc404cba090cfee20080"}, "tags": {"0.4.7--py38h4a8c8d9_0": "sha256:43edb82a437e456dd4c1dd7b2d4d614381c43b8d7c8423eb497d019a4fc2c554", "0.10.10--py310h4b81fae_0": "sha256:a77de384451422d056c2fec89c29416031c5eaa566dbf2ca43941ba1def97c46", "0.9.0--py38he5da3d1_0": "sha256:b63934e4a9dc6d66d8966563d9b466abed56dae35357bef8614e71f33b976990", "0.8.2--py38he5da3d1_0": "sha256:d163d5ec67827b5b8c424530be2b40978407e74a00dcea94e676a9b973cab88f", "0.7.2--py310h1425a21_0": "sha256:82bb9e44ad593cd0f83b58957605805ed9a12c71d6323718f11e7bc5525d8cc9", "0.6.3--py310h1425a21_0": "sha256:80af1b41a52127def5714369b04b45cf926d82cb19ae0d311fb78298a6c98f41", "0.10.11--py38he5da3d1_0": "sha256:8009e0699920a23fb2c6cb2b23d446a8d2dd91666dfab03c6155c9c97511b123", "0.10.12--py39hf95cd2a_0": "sha256:30272de4223fdb6dbe6c1954f65f2852a4c8586054b0a5fe4b52a9a3d7919d35", "0.10.12--py38h0020b31_1": "sha256:5c66f63948ff995012f961bac8cb51c60db5801a3e2c2933c1b214dbd54d484c", "0.10.14--py39hff71179_0": "sha256:0f443cca236f0e98d92880bba9934a05c954ef969bebc542ad23c12c86b36fb5", "0.10.14--py310h7c593f9_1": "sha256:fc2432209e9804c9aeb4c9c080bdc1984a61f06600247d19647cd7ea742962e5", "0.10.15--py310h7c593f9_0": "sha256:9af3cd194c80593e8b0f85c401b9c87e21255c45efdfff91804e4b159b82fd21", "0.10.15--py310h1fe012e_1": "sha256:8d5a56d4af11694e6147d59c4841115a7e275f95f259d9b3617c834db47f3b4e", "0.11.0--py39hbcbf7aa_0": "sha256:3b240f701cdf817baf82efcb4c8af00bbe308114a591dc404cba090cfee20080"}, "docker": "quay.io/biocontainers/pyhmmer", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyhmmer.
shpc-registry automated BioContainers addition for pyhmmer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyhmmer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyhmmer:0.11.0--py39hbcbf7aa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyhmmer/0.11.0--py39hbcbf7aa_0
$ module help quay.io/biocontainers/pyhmmer/0.11.0--py39hbcbf7aa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyhmmer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyhmmer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyhmmer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyhmmer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyhmmer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyhmmer-inspect-deffile:

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