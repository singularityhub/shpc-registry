---
layout: container
name:  "quay.io/biocontainers/chembl_webresource_client"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chembl_webresource_client/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chembl_webresource_client/container.yaml"
updated_at: "2024-11-02 03:10:23.332787"
latest: "0.10.1"
container_url: "https://biocontainers.pro/tools/chembl_webresource_client"
aliases:
 - "chembl_act"
 - "chembl_ids"
 - "chembl_m2t"
 - "chembl_sim"
 - "chembl_sub"
 - "chembl_t2m"
 - "chardetect"
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
 - "0.9.31"
 - "0.10.1"
description: "shpc-registry automated BioContainers addition for chembl_webresource_client"
config: {"url": "https://biocontainers.pro/tools/chembl_webresource_client", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chembl_webresource_client", "latest": {"0.10.1": "sha256:d60f1846d22ef9cd24b4092ef1e2999ebf1b8c0d811ab285b0558b815e72c77f"}, "tags": {"0.9.31": "sha256:5e99109759b67c5f00803d7dc59a7677a6e6545a831343ecc68d06dda5d2c2f9", "0.10.1": "sha256:d60f1846d22ef9cd24b4092ef1e2999ebf1b8c0d811ab285b0558b815e72c77f"}, "docker": "quay.io/biocontainers/chembl_webresource_client", "aliases": {"chembl_act": "/usr/local/bin/chembl_act", "chembl_ids": "/usr/local/bin/chembl_ids", "chembl_m2t": "/usr/local/bin/chembl_m2t", "chembl_sim": "/usr/local/bin/chembl_sim", "chembl_sub": "/usr/local/bin/chembl_sub", "chembl_t2m": "/usr/local/bin/chembl_t2m", "chardetect": "/usr/local/bin/chardetect", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chembl_webresource_client.
shpc-registry automated BioContainers addition for chembl_webresource_client
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chembl_webresource_client
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chembl_webresource_client:0.10.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chembl_webresource_client/0.10.1
$ module help quay.io/biocontainers/chembl_webresource_client/0.10.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chembl_webresource_client-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chembl_webresource_client-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chembl_webresource_client-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chembl_webresource_client-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chembl_webresource_client-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chembl_webresource_client-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chembl_act

```bash
$ singularity exec <container> /usr/local/bin/chembl_act
$ podman run --it --rm --entrypoint /usr/local/bin/chembl_act   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chembl_act   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chembl_ids

```bash
$ singularity exec <container> /usr/local/bin/chembl_ids
$ podman run --it --rm --entrypoint /usr/local/bin/chembl_ids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chembl_ids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chembl_m2t

```bash
$ singularity exec <container> /usr/local/bin/chembl_m2t
$ podman run --it --rm --entrypoint /usr/local/bin/chembl_m2t   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chembl_m2t   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chembl_sim

```bash
$ singularity exec <container> /usr/local/bin/chembl_sim
$ podman run --it --rm --entrypoint /usr/local/bin/chembl_sim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chembl_sim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chembl_sub

```bash
$ singularity exec <container> /usr/local/bin/chembl_sub
$ podman run --it --rm --entrypoint /usr/local/bin/chembl_sub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chembl_sub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chembl_t2m

```bash
$ singularity exec <container> /usr/local/bin/chembl_t2m
$ podman run --it --rm --entrypoint /usr/local/bin/chembl_t2m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chembl_t2m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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