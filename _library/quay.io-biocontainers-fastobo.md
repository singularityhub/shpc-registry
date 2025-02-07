---
layout: container
name:  "quay.io/biocontainers/fastobo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastobo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastobo/container.yaml"
updated_at: "2025-02-07 03:20:27.361349"
latest: "0.12.3--py310h13f1c22_3"
container_url: "https://biocontainers.pro/tools/fastobo"
aliases:
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "pyvenv"
versions:
 - "0.9.3--py37hfa133b6_0"
 - "0.12.1--py39h67e14b5_0"
 - "0.11.1--py37h675a0cb_1"
 - "0.10.1--py38h6ed170a_0"
 - "0.12.2--py39h67e14b5_0"
 - "0.12.2--py39h67e14b5_1"
 - "0.12.3--py39he10ea66_0"
 - "0.11.1--py36h4aaaa08_1"
 - "0.10.1--py37hfa133b6_0"
 - "0.9.3--py36hf0b53f7_0"
 - "0.12.3--py38hcbe9525_1"
 - "0.12.3--py38hda86a2d_2"
 - "0.12.3--py310h13f1c22_3"
description: "shpc-registry automated BioContainers addition for fastobo"
config: {"url": "https://biocontainers.pro/tools/fastobo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastobo", "latest": {"0.12.3--py310h13f1c22_3": "sha256:76cf55b69d5cea8d371ec24726055c5fd7240a62dc86f8b41aedf141665458aa"}, "tags": {"0.9.3--py37hfa133b6_0": "sha256:198362f9416f7adef5678bf2cc4da2c9807c0ba5e1affdb8b71339157089cacd", "0.12.1--py39h67e14b5_0": "sha256:895c619807741a5fede2803f5e31c75674584a009a8f1a8a3dfc6140956c1dc4", "0.11.1--py37h675a0cb_1": "sha256:f7e05ca04e1a4016a20c649f1e4bb567c9c9346f8db944b1c4bf0f915b3ee37a", "0.10.1--py38h6ed170a_0": "sha256:f6746300cd2e15cd312c3dde32850a6ecc4dbb263593335c6ca32b224834aab5", "0.12.2--py39h67e14b5_0": "sha256:cd22d7caa9fb316568a89ac6b12612500c002811a31831282f3d0b788e8dd232", "0.12.2--py39h67e14b5_1": "sha256:8761cffce96d433f755a9438cc6c7e203fe966fd4ce55889f39aa2084e70533c", "0.12.3--py39he10ea66_0": "sha256:f3e40730ad2f8d3a027213b442a8d548ceaeb5df4371827c0b2c41fdaa52ee55", "0.11.1--py36h4aaaa08_1": "sha256:682ed00e48cbfe7d514a4e73ca77f667d73616f722e35c71dc1c72be6bf8b130", "0.10.1--py37hfa133b6_0": "sha256:a75fab0a1f90eace15e65dd6173f1d22997b3be8f615d47fca6c6a1f5966cb87", "0.9.3--py36hf0b53f7_0": "sha256:04edb0dcbae847fc647bad271e17d7b86667c8a7c230e665ab29e0107445d102", "0.12.3--py38hcbe9525_1": "sha256:a8d7c12725ce7e9f6a5d7ae0102c5b2f8798ff13e7629289f1d96256c1a37246", "0.12.3--py38hda86a2d_2": "sha256:5b614e382f3e0a9246d8b666d85967e6cee28d03cc1cafeeb8eacb185907f1c1", "0.12.3--py310h13f1c22_3": "sha256:76cf55b69d5cea8d371ec24726055c5fd7240a62dc86f8b41aedf141665458aa"}, "docker": "quay.io/biocontainers/fastobo", "aliases": {"2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastobo.
shpc-registry automated BioContainers addition for fastobo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastobo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastobo:0.12.3--py310h13f1c22_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastobo/0.12.3--py310h13f1c22_3
$ module help quay.io/biocontainers/fastobo/0.12.3--py310h13f1c22_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastobo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastobo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastobo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastobo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastobo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastobo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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