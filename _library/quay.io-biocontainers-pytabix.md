---
layout: container
name:  "quay.io/biocontainers/pytabix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pytabix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pytabix/container.yaml"
updated_at: "2024-07-28 02:50:06.985601"
latest: "0.1--py310hdf79db3_6"
container_url: "https://biocontainers.pro/tools/pytabix"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.1--py39h2add14b_2"
 - "0.1--py39h4e691d4_4"
 - "0.1--py310h6cc9453_4"
 - "0.1--py38h5cf8b27_5"
 - "0.1--py310hdf79db3_6"
description: "shpc-registry automated BioContainers addition for pytabix"
config: {"url": "https://biocontainers.pro/tools/pytabix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pytabix", "latest": {"0.1--py310hdf79db3_6": "sha256:02c2a074fec1e2d924189069ef8bd2f7977109c0229753c68ee0c4c02d787b3c"}, "tags": {"0.1--py39h2add14b_2": "sha256:b46165a98b4361dc4834539b3e98899be7eb5db8df8969ab590c8ca07a86f36c", "0.1--py39h4e691d4_4": "sha256:a3841008dcd3d80cc730dfa6adecc6557673456e2315f2a63287dd8302f0e3d0", "0.1--py310h6cc9453_4": "sha256:af6713e425ef8ee6dc4e24ba72bcc7b0e39b86f6f30302a371c4b747e8dc84a4", "0.1--py38h5cf8b27_5": "sha256:869009ec1c9c788c58abb45063b58b84673aae5e923dff0803ed36c177b9ba88", "0.1--py310hdf79db3_6": "sha256:02c2a074fec1e2d924189069ef8bd2f7977109c0229753c68ee0c4c02d787b3c"}, "docker": "quay.io/biocontainers/pytabix", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pytabix.
shpc-registry automated BioContainers addition for pytabix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pytabix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pytabix:0.1--py310hdf79db3_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pytabix/0.1--py310hdf79db3_6
$ module help quay.io/biocontainers/pytabix/0.1--py310hdf79db3_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pytabix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pytabix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pytabix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pytabix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pytabix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pytabix-inspect-deffile:

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