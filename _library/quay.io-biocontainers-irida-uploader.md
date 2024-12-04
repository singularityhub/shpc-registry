---
layout: container
name:  "quay.io/biocontainers/irida-uploader"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/irida-uploader/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/irida-uploader/container.yaml"
updated_at: "2024-12-04 03:11:22.830748"
latest: "0.9.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/irida-uploader"
aliases:
 - "integration-test"
 - "irida-uploader"
 - "irida-uploader-gui"
 - "normalizer"
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
 - "0.8.3--pyhdfd78af_0"
 - "0.9.0--pyhdfd78af_0"
 - "0.9.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for irida-uploader"
config: {"url": "https://biocontainers.pro/tools/irida-uploader", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for irida-uploader", "latest": {"0.9.2--pyhdfd78af_0": "sha256:dbeabe07e1a63375ec951ed1d3f83de02206968f98a90b6a05c6677351412420"}, "tags": {"0.8.3--pyhdfd78af_0": "sha256:a8975bfde6c9447aa3a570d404bae8b15afe7744dec9b9279b8ad24be66c91a7", "0.9.0--pyhdfd78af_0": "sha256:6583c1124fe93a6d0fcdd50ea81d81d41541ddf611d7f309b4796b73f5b2f5a5", "0.9.2--pyhdfd78af_0": "sha256:dbeabe07e1a63375ec951ed1d3f83de02206968f98a90b6a05c6677351412420"}, "docker": "quay.io/biocontainers/irida-uploader", "aliases": {"integration-test": "/usr/local/bin/integration-test", "irida-uploader": "/usr/local/bin/irida-uploader", "irida-uploader-gui": "/usr/local/bin/irida-uploader-gui", "normalizer": "/usr/local/bin/normalizer", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/irida-uploader.
shpc-registry automated BioContainers addition for irida-uploader
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/irida-uploader
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/irida-uploader:0.9.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/irida-uploader/0.9.2--pyhdfd78af_0
$ module help quay.io/biocontainers/irida-uploader/0.9.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### irida-uploader-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### irida-uploader-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### irida-uploader-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### irida-uploader-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### irida-uploader-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### irida-uploader-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### integration-test

```bash
$ singularity exec <container> /usr/local/bin/integration-test
$ podman run --it --rm --entrypoint /usr/local/bin/integration-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/integration-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irida-uploader

```bash
$ singularity exec <container> /usr/local/bin/irida-uploader
$ podman run --it --rm --entrypoint /usr/local/bin/irida-uploader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irida-uploader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irida-uploader-gui

```bash
$ singularity exec <container> /usr/local/bin/irida-uploader-gui
$ podman run --it --rm --entrypoint /usr/local/bin/irida-uploader-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irida-uploader-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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