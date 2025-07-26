---
layout: container
name:  "quay.io/biocontainers/pymzml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pymzml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pymzml/container.yaml"
updated_at: "2025-07-26 03:35:09.933558"
latest: "2.5.11--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pymzml"
aliases:
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "2.5.2--pyhdfd78af_0"
 - "2.5.3--pyhdfd78af_0"
 - "2.5.5--pyhdfd78af_0"
 - "2.5.6--pyhdfd78af_0"
 - "2.5.9--pyhdfd78af_0"
 - "2.5.10--pyhdfd78af_0"
 - "2.5.11--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pymzml"
config: {"url": "https://biocontainers.pro/tools/pymzml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pymzml", "latest": {"2.5.11--pyhdfd78af_0": "sha256:3636fd2a9da4d33f5568e03ddb18feb06551edf7d9a481b7d06b5c2e8576396b"}, "tags": {"2.5.2--pyhdfd78af_0": "sha256:3ebc76112579dd8564784c9ac876626705ea4006653ca317f0e77d71fa96f82a", "2.5.3--pyhdfd78af_0": "sha256:545817b3277aa5f22ab0b2c5e63f8961f24cdefaa5681242190ab5e776fd579f", "2.5.5--pyhdfd78af_0": "sha256:c90fff0ce42efaf4396f721aefb85c7885429a878c4fd7698162fa487548d286", "2.5.6--pyhdfd78af_0": "sha256:3891bd3f970cfa3f38059ab9d5141b0bc1b7a5bf9f13942cdef0c6dbf53d4051", "2.5.9--pyhdfd78af_0": "sha256:8ed1849f4170c56fc89e1839681bdc90a669480aa7a3d9a6c960733022affce8", "2.5.10--pyhdfd78af_0": "sha256:91540ef91daebc3a013ada318f1809935a19e719fc5a0810838bc889d2c0cf19", "2.5.11--pyhdfd78af_0": "sha256:3636fd2a9da4d33f5568e03ddb18feb06551edf7d9a481b7d06b5c2e8576396b"}, "docker": "quay.io/biocontainers/pymzml", "aliases": {"f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pymzml.
shpc-registry automated BioContainers addition for pymzml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pymzml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pymzml:2.5.11--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pymzml/2.5.11--pyhdfd78af_0
$ module help quay.io/biocontainers/pymzml/2.5.11--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pymzml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pymzml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pymzml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pymzml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pymzml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pymzml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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