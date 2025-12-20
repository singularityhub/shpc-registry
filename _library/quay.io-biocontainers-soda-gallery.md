---
layout: container
name:  "quay.io/biocontainers/soda-gallery"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/soda-gallery/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/soda-gallery/container.yaml"
updated_at: "2025-12-20 03:36:50.892500"
latest: "1.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/soda-gallery"
aliases:
 - "dumppdf.py"
 - "pdf2txt.py"
 - "soda"
 - "chardetect"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.0.1--pyh5e36f6f_0"
 - "1.2.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for soda-gallery"
config: {"url": "https://biocontainers.pro/tools/soda-gallery", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for soda-gallery", "latest": {"1.2.0--pyhdfd78af_0": "sha256:18cfbe4b5972771e15514abc85736a9b41960444bebea5e0102908a1e5b4ae63"}, "tags": {"1.0.1--pyh5e36f6f_0": "sha256:112fe8dd6561f8c44348c1af142db19f624fdcd2dcea6d216abd7e6f73518230", "1.2.0--pyhdfd78af_0": "sha256:18cfbe4b5972771e15514abc85736a9b41960444bebea5e0102908a1e5b4ae63"}, "docker": "quay.io/biocontainers/soda-gallery", "aliases": {"dumppdf.py": "/usr/local/bin/dumppdf.py", "pdf2txt.py": "/usr/local/bin/pdf2txt.py", "soda": "/usr/local/bin/soda", "chardetect": "/usr/local/bin/chardetect", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/soda-gallery.
shpc-registry automated BioContainers addition for soda-gallery
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/soda-gallery
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/soda-gallery:1.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/soda-gallery/1.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/soda-gallery/1.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### soda-gallery-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### soda-gallery-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### soda-gallery-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### soda-gallery-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### soda-gallery-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### soda-gallery-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dumppdf.py

```bash
$ singularity exec <container> /usr/local/bin/dumppdf.py
$ podman run --it --rm --entrypoint /usr/local/bin/dumppdf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumppdf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdf2txt.py

```bash
$ singularity exec <container> /usr/local/bin/pdf2txt.py
$ podman run --it --rm --entrypoint /usr/local/bin/pdf2txt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdf2txt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soda

```bash
$ singularity exec <container> /usr/local/bin/soda
$ podman run --it --rm --entrypoint /usr/local/bin/soda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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