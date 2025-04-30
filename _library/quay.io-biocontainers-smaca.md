---
layout: container
name:  "quay.io/biocontainers/smaca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smaca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smaca/container.yaml"
updated_at: "2025-04-30 03:44:54.651083"
latest: "1.2.3--py311hc1104ee_6"
container_url: "https://biocontainers.pro/tools/smaca"
aliases:
 - "smaca"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.2.3--py39h919a90d_3"
 - "1.2.3--py310h5aa3a86_4"
 - "1.2.3--py38h8c35140_4"
 - "1.2.3--py312h8cd533b_5"
 - "1.2.3--py311hc1104ee_6"
description: "shpc-registry automated BioContainers addition for smaca"
config: {"url": "https://biocontainers.pro/tools/smaca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smaca", "latest": {"1.2.3--py311hc1104ee_6": "sha256:351d0202499315ac12d45f75429b2bba8c630f45a12059b33fbfeb9166570001"}, "tags": {"1.2.3--py39h919a90d_3": "sha256:9f18b52c26a11a73033cb6f7db83bad13b926ca47ed6109b4d0b28a91f35ebcf", "1.2.3--py310h5aa3a86_4": "sha256:5d2c050e435e511c0c26a842e9583f56e6ab2abb9c27bdac284e5ee10bd6f160", "1.2.3--py38h8c35140_4": "sha256:c83b365e70a65cd01a43e6f1895b38f1b8eaed5f140ba9eed8cf6edc7771a15e", "1.2.3--py312h8cd533b_5": "sha256:1974d187cac1d5ba88d9accdc98dadf25af7bbe1d50ecf78b9c7515594632986", "1.2.3--py311hc1104ee_6": "sha256:351d0202499315ac12d45f75429b2bba8c630f45a12059b33fbfeb9166570001"}, "docker": "quay.io/biocontainers/smaca", "aliases": {"smaca": "/usr/local/bin/smaca", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smaca.
shpc-registry automated BioContainers addition for smaca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smaca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smaca:1.2.3--py311hc1104ee_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smaca/1.2.3--py311hc1104ee_6
$ module help quay.io/biocontainers/smaca/1.2.3--py311hc1104ee_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smaca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smaca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smaca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smaca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smaca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smaca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smaca

```bash
$ singularity exec <container> /usr/local/bin/smaca
$ podman run --it --rm --entrypoint /usr/local/bin/smaca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smaca   -v ${PWD} -w ${PWD} <container> -c " $@"
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