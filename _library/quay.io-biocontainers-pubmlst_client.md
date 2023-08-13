---
layout: container
name:  "quay.io/biocontainers/pubmlst_client"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pubmlst_client/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pubmlst_client/container.yaml"
updated_at: "2023-08-13 03:12:28.439489"
latest: "0.2.0--py_0"
container_url: "https://biocontainers.pro/tools/pubmlst_client"
aliases:
 - "pubmlst_download"
 - "pubmlst_list"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.2.0--py_0"
description: "shpc-registry automated BioContainers addition for pubmlst_client"
config: {"url": "https://biocontainers.pro/tools/pubmlst_client", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pubmlst_client", "latest": {"0.2.0--py_0": "sha256:8e30c46aad2b82b2e2e4ab37c9f870384b139c888c8f432908b2b55e3a856b11"}, "tags": {"0.2.0--py_0": "sha256:8e30c46aad2b82b2e2e4ab37c9f870384b139c888c8f432908b2b55e3a856b11"}, "docker": "quay.io/biocontainers/pubmlst_client", "aliases": {"pubmlst_download": "/usr/local/bin/pubmlst_download", "pubmlst_list": "/usr/local/bin/pubmlst_list", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pubmlst_client.
shpc-registry automated BioContainers addition for pubmlst_client
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pubmlst_client
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pubmlst_client:0.2.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pubmlst_client/0.2.0--py_0
$ module help quay.io/biocontainers/pubmlst_client/0.2.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pubmlst_client-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pubmlst_client-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pubmlst_client-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pubmlst_client-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pubmlst_client-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pubmlst_client-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pubmlst_download

```bash
$ singularity exec <container> /usr/local/bin/pubmlst_download
$ podman run --it --rm --entrypoint /usr/local/bin/pubmlst_download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pubmlst_download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pubmlst_list

```bash
$ singularity exec <container> /usr/local/bin/pubmlst_list
$ podman run --it --rm --entrypoint /usr/local/bin/pubmlst_list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pubmlst_list   -v ${PWD} -w ${PWD} <container> -c " $@"
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