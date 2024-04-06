---
layout: container
name:  "quay.io/biocontainers/pyspoa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyspoa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyspoa/container.yaml"
updated_at: "2024-04-06 02:35:48.091942"
latest: "0.2.1--py310h2b6aa90_1"
container_url: "https://biocontainers.pro/tools/pyspoa"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.0.3--py39h67e14b5_3"
 - "0.0.3--py310h068649b_6"
 - "0.0.9--py310h0dbaff4_0"
 - "0.0.10--py38h2494328_0"
 - "0.0.10--py38he0f268d_1"
 - "0.2.1--py310h2b6aa90_0"
 - "0.2.1--py310h2b6aa90_1"
 - "0.0.10--py310h2b6aa90_1"
description: "shpc-registry automated BioContainers addition for pyspoa"
config: {"url": "https://biocontainers.pro/tools/pyspoa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyspoa", "latest": {"0.2.1--py310h2b6aa90_1": "sha256:bb852112f7c4a339823a9d5c80805f4226e205e68a3d15579fa51bd834501e31"}, "tags": {"0.0.3--py39h67e14b5_3": "sha256:1149aa0fc68f54033020f3a57f78d5f7f2843cf44da20099f8d406232eb6dc06", "0.0.3--py310h068649b_6": "sha256:c7dcbeed6726e2381b61856242eb9fcf4b72e48e884585df0003861e8df11e4b", "0.0.9--py310h0dbaff4_0": "sha256:50879b603c0727e6283c68cff3cca6b922860a526624c48de563f81401a4d23b", "0.0.10--py38h2494328_0": "sha256:60dbaa4c7e17dbb91f29547089281b5f2a48c8993c13da4f6f230108ea946cf4", "0.0.10--py38he0f268d_1": "sha256:7a77747d2d59aa7985d1b57cecad25384bc257c98bef8c290fccb7ca35a2d14f", "0.2.1--py310h2b6aa90_0": "sha256:3190f2cc2e64a9daa0a9d77483870c8d3d3eb16fb94e775001283f3450ed2017", "0.2.1--py310h2b6aa90_1": "sha256:bb852112f7c4a339823a9d5c80805f4226e205e68a3d15579fa51bd834501e31", "0.0.10--py310h2b6aa90_1": "sha256:531d373cfa4566278e5e257da362648db91cfb5346fecd176b37c3fc77a65aac"}, "docker": "quay.io/biocontainers/pyspoa", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyspoa.
shpc-registry automated BioContainers addition for pyspoa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyspoa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyspoa:0.2.1--py310h2b6aa90_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyspoa/0.2.1--py310h2b6aa90_1
$ module help quay.io/biocontainers/pyspoa/0.2.1--py310h2b6aa90_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyspoa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyspoa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyspoa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyspoa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyspoa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyspoa-inspect-deffile:

```bash
$ singularity inspect -d <container>
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