---
layout: container
name:  "quay.io/biocontainers/biobox_add_taxid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobox_add_taxid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobox_add_taxid/container.yaml"
updated_at: "2025-05-22 03:52:39.098249"
latest: "1.2--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/biobox_add_taxid"
aliases:
 - "biobox_add_taxid.py"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.4--pyh7e72e81_0"
 - "0.6--pyh7e72e81_0"
 - "0.5--pyh7e72e81_0"
 - "1.2--pyh7e72e81_0"
 - "1.1--pyh7e72e81_0"
 - "1.0--pyh7e72e81_0"
description: "singularity registry hpc automated addition for biobox_add_taxid"
config: {"url": "https://biocontainers.pro/tools/biobox_add_taxid", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for biobox_add_taxid", "latest": {"1.2--pyh7e72e81_0": "sha256:3f42c49522a5d58861ccd33bb88a2f10ec7ea04d4ca9d78ebc4bc368b26f1f77"}, "tags": {"0.4--pyh7e72e81_0": "sha256:2cec1020918fcd1649b6eb545652234c7ed77b2be4a52a1578712280abf3fe48", "0.6--pyh7e72e81_0": "sha256:9b3957fe95433919bd8fe188114627bf0282184d8535f7108652895aedbc7e6f", "0.5--pyh7e72e81_0": "sha256:a7bba04088e1d2d30783970eb80f7e5511ebe2e6234e8f2c7a4c886c1d8179ce", "1.2--pyh7e72e81_0": "sha256:3f42c49522a5d58861ccd33bb88a2f10ec7ea04d4ca9d78ebc4bc368b26f1f77", "1.1--pyh7e72e81_0": "sha256:0794acce82c3f0571bdcbf86cc70c5b3da019ba1c6be8e04324b936fe6f8069c", "1.0--pyh7e72e81_0": "sha256:0a71fd61596bc5d2867c17bdfa2b7bf6c7c03dd3b3bff2989f92ebcbeb0bbb5c"}, "docker": "quay.io/biocontainers/biobox_add_taxid", "aliases": {"biobox_add_taxid.py": "/usr/local/bin/biobox_add_taxid.py", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobox_add_taxid.
singularity registry hpc automated addition for biobox_add_taxid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobox_add_taxid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobox_add_taxid:1.2--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobox_add_taxid/1.2--pyh7e72e81_0
$ module help quay.io/biocontainers/biobox_add_taxid/1.2--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobox_add_taxid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobox_add_taxid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobox_add_taxid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobox_add_taxid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobox_add_taxid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobox_add_taxid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### biobox_add_taxid.py

```bash
$ singularity exec <container> /usr/local/bin/biobox_add_taxid.py
$ podman run --it --rm --entrypoint /usr/local/bin/biobox_add_taxid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biobox_add_taxid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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