---
layout: container
name:  "quay.io/biocontainers/virstrain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/virstrain/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/virstrain/container.yaml"
updated_at: "2025-07-31 11:31:49.919753"
latest: "1.17--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/virstrain"
aliases:
 - "virstrain"
 - "virstrain_build"
 - "jupyter-trust"
 - "jupyter"
 - "jupyter-migrate"
 - "jupyter-troubleshoot"
 - "jsonschema"
 - "f2py3.7"
 - "chardetect"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
versions:
 - "1.9--pyhdfd78af_0"
 - "1.12--pyhdfd78af_0"
 - "1.11--pyhdfd78af_0"
 - "1.10--pyhdfd78af_0"
 - "1.13--pyhdfd78af_0"
 - "1.14--pyhdfd78af_0"
 - "1.17--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for virstrain"
config: {"url": "https://biocontainers.pro/tools/virstrain", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for virstrain", "latest": {"1.17--pyhdfd78af_1": "sha256:13df1cea172d3a9fba84bfd358cdfe41e4ebddd7ebf5f32e9c9628f0ee496a06"}, "tags": {"1.9--pyhdfd78af_0": "sha256:aa540a48ebce9f12e99fdcec7241bba20158af862f83802a3396b32e413617bf", "1.12--pyhdfd78af_0": "sha256:c8b466bd77a7b920362fb24630dd1f677ad1eb3c307945f154625fe25ed88f48", "1.11--pyhdfd78af_0": "sha256:7c05337ba3abd140d36e74aa1660cf0de1f23fbfd29a65544c4b935e41b41e92", "1.10--pyhdfd78af_0": "sha256:6a1b072ae815bcd61158129ac7a197600b5c00ff3cd52e535d33e9a0dc3134fd", "1.13--pyhdfd78af_0": "sha256:df76cac3a13e44005f9f2d569073af8b5abce6ee215d9dde2cca8b8c35c51b17", "1.14--pyhdfd78af_0": "sha256:675bdc13102991b0f0783ebe3a0867bac79e6372db64d37079e8973b9e82b11a", "1.17--pyhdfd78af_1": "sha256:13df1cea172d3a9fba84bfd358cdfe41e4ebddd7ebf5f32e9c9628f0ee496a06"}, "docker": "quay.io/biocontainers/virstrain", "aliases": {"virstrain": "/usr/local/bin/virstrain", "virstrain_build": "/usr/local/bin/virstrain_build", "jupyter-trust": "/usr/local/bin/jupyter-trust", "jupyter": "/usr/local/bin/jupyter", "jupyter-migrate": "/usr/local/bin/jupyter-migrate", "jupyter-troubleshoot": "/usr/local/bin/jupyter-troubleshoot", "jsonschema": "/usr/local/bin/jsonschema", "f2py3.7": "/usr/local/bin/f2py3.7", "chardetect": "/usr/local/bin/chardetect", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/virstrain.
shpc-registry automated BioContainers addition for virstrain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/virstrain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/virstrain:1.17--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/virstrain/1.17--pyhdfd78af_1
$ module help quay.io/biocontainers/virstrain/1.17--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### virstrain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### virstrain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### virstrain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### virstrain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### virstrain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### virstrain-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### virstrain

```bash
$ singularity exec <container> /usr/local/bin/virstrain
$ podman run --it --rm --entrypoint /usr/local/bin/virstrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virstrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virstrain_build

```bash
$ singularity exec <container> /usr/local/bin/virstrain_build
$ podman run --it --rm --entrypoint /usr/local/bin/virstrain_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virstrain_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter

```bash
$ singularity exec <container> /usr/local/bin/jupyter
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-migrate

```bash
$ singularity exec <container> /usr/local/bin/jupyter-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-troubleshoot

```bash
$ singularity exec <container> /usr/local/bin/jupyter-troubleshoot
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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