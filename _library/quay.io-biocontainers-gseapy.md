---
layout: container
name:  "quay.io/biocontainers/gseapy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gseapy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gseapy/container.yaml"
updated_at: "2025-03-21 03:43:49.472851"
latest: "1.1.5--py310hec43fc7_0"
container_url: "https://biocontainers.pro/tools/gseapy"

versions:
 - "0.9.9--py_0"
 - "0.10.3--py_0"
 - "0.9.19--py_0"
 - "1.1.2--py39h0d4550d_0"
 - "1.0.6--py310hbee2dd9_0"
 - "0.14.0--py310hbee2dd9_0"
 - "0.13.0--py310hbee2dd9_0"
 - "0.12.1--py37h792ed70_0"
 - "1.1.2--py39h0d4550d_1"
 - "1.1.3--py38h4bed0b0_0"
 - "1.1.3--py311h5e00ca1_1"
 - "1.1.4--py311h5e00ca1_0"
 - "1.1.4--py310hec43fc7_1"
 - "1.1.5--py310hec43fc7_0"
description: "shpc-registry automated BioContainers addition for gseapy"
config: {"url": "https://biocontainers.pro/tools/gseapy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gseapy", "latest": {"1.1.5--py310hec43fc7_0": "sha256:6ce07e70de0ffacc8f4f12d5fe98f8f7cdaa54c5ea3e94d5533bb0ce5512af51"}, "tags": {"0.9.9--py_0": "sha256:14e74a8b356765826c2b202a7b99928fa3d5ff901f59e7d6be98191da394fe23", "0.10.3--py_0": "sha256:cf64de5b410f92683a319199a544b52f364c15263d996660b9c5dd703725e72e", "0.9.19--py_0": "sha256:dfc12e9063073cc1feecb68f06a3537f6d5f8fab06a2e099690f9d4540a9d395", "1.1.2--py39h0d4550d_0": "sha256:12a7205cdd03856abdcfb98d1ffe756c8d139bf4b8e42157e06b79c8aa5853cd", "1.0.6--py310hbee2dd9_0": "sha256:4db772d105540c49af8029d5fb8ebec87293bf28cc7baa16a91d2b393f5e0de2", "0.14.0--py310hbee2dd9_0": "sha256:39fa87ce51d0e8778140123aebe5c2a899cf25cc3019b4f2dfc3ccb6895a844a", "0.13.0--py310hbee2dd9_0": "sha256:071cc1007f7c6ee1fd2f3a97475727ccec4f10d5877baf9e51816e3e2d7b893b", "0.12.1--py37h792ed70_0": "sha256:9e8f8b70b83594a5bb85a76fee698812f368cc399f0e4af4bde1db72c4af51ef", "1.1.2--py39h0d4550d_1": "sha256:a222035f19d974f493181c1f28c9d1b6aa1d42ce858620e0c8d185aa362df820", "1.1.3--py38h4bed0b0_0": "sha256:20cf08718be4d4bd19cc271a35d893b82853c942d89015e1daf8df0d0c61a24b", "1.1.3--py311h5e00ca1_1": "sha256:d98e657c82073c3a092ec789d473ef7c0dc2ee5ccf523535e25d3e739925e723", "1.1.4--py311h5e00ca1_0": "sha256:a1e1fe5a4a7c65ad29df0a8e94cc96a766ea152c090ab752dff212b3eba67418", "1.1.4--py310hec43fc7_1": "sha256:49a255a77452c1084a03bfb18829431536009d89ed0aa92a90703eb93ee0cd4c", "1.1.5--py310hec43fc7_0": "sha256:6ce07e70de0ffacc8f4f12d5fe98f8f7cdaa54c5ea3e94d5533bb0ce5512af51"}, "docker": "quay.io/biocontainers/gseapy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gseapy.
shpc-registry automated BioContainers addition for gseapy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gseapy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gseapy:1.1.5--py310hec43fc7_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gseapy/1.1.5--py310hec43fc7_0
$ module help quay.io/biocontainers/gseapy/1.1.5--py310hec43fc7_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gseapy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gseapy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gseapy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gseapy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gseapy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gseapy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gseapy

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