---
layout: container
name:  "quay.io/biocontainers/odgi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/odgi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/odgi/container.yaml"
updated_at: "2024-08-13 03:10:14.192587"
latest: "0.8.6--py312hc60241a_2"
container_url: "https://biocontainers.pro/tools/odgi"
aliases:
 - "odgi"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "pyvenv"
versions:
 - "v0.3--py36h8b12597_0"
 - "0.7.2--py39h2add14b_1"
 - "0.6.3--py39h2add14b_1"
 - "0.4.1--py36h61628e2_1"
 - "0.3--py36hd181a71_1"
 - "0.8.6--py310h6cc9453_0"
 - "0.7.3--py39h2add14b_1"
 - "0.6.3--py36hcac48a8_1"
 - "0.4.1--py38h8e3bb3f_1"
 - "0.3--py38h8162308_1"
 - "0.8.6--py310hdf79db3_1"
 - "0.8.6--py312hc60241a_2"
description: "shpc-registry automated BioContainers addition for odgi"
config: {"url": "https://biocontainers.pro/tools/odgi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for odgi", "latest": {"0.8.6--py312hc60241a_2": "sha256:b8aa75b92ee750d026500f2110dcc677fea5a22bd19645b24f54f7089a562cf3"}, "tags": {"v0.3--py36h8b12597_0": "sha256:1c2f5509378972e116f35ec672feea0cfaf9b940f4feef807235dd91975f9f7d", "0.7.2--py39h2add14b_1": "sha256:b5c38e28fb36084a52e311e642cdf6c8c10a515211bb19ceecb17ffb0437ed44", "0.6.3--py39h2add14b_1": "sha256:217a98d601a2c2068ba515d86ce835bb328262257634895b451b1332e2ae5f9b", "0.4.1--py36h61628e2_1": "sha256:3ff2613f3894075263f2dedf0e0d49227717168661898b8d6605b5b46e066430", "0.3--py36hd181a71_1": "sha256:09a73f020c4483325e01cefd7e67291fde8d9af9a6bf1eda2c143ba0c8c40757", "0.8.6--py310h6cc9453_0": "sha256:976b3413c95ea5210063fa57ff10440800f9080eb197b8c8aa70361f421d429b", "0.7.3--py39h2add14b_1": "sha256:bbc56e03fdb356d071a007d300790f4b1e9330111776a4b31d72afcd99c779f8", "0.6.3--py36hcac48a8_1": "sha256:6ff430cedf04030fdb893a0e3284f4ac962a8056f924a56400a11c7391146abe", "0.4.1--py38h8e3bb3f_1": "sha256:c109c4d5c30df735c15a0d45533795f105507af83297e09c03bfda3ee5c194c4", "0.3--py38h8162308_1": "sha256:e4d081044909db90bc3c3eacc0e734c415a07469783727bb3a3e09bf822e5550", "0.8.6--py310hdf79db3_1": "sha256:804005aa667f63e043587347687358588b6e81c7c221f8d60d6c526e1df1b849", "0.8.6--py312hc60241a_2": "sha256:b8aa75b92ee750d026500f2110dcc677fea5a22bd19645b24f54f7089a562cf3"}, "docker": "quay.io/biocontainers/odgi", "aliases": {"odgi": "/usr/local/bin/odgi", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/odgi.
shpc-registry automated BioContainers addition for odgi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/odgi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/odgi:0.8.6--py312hc60241a_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/odgi/0.8.6--py312hc60241a_2
$ module help quay.io/biocontainers/odgi/0.8.6--py312hc60241a_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### odgi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### odgi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### odgi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### odgi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### odgi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### odgi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### odgi

```bash
$ singularity exec <container> /usr/local/bin/odgi
$ podman run --it --rm --entrypoint /usr/local/bin/odgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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