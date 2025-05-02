---
layout: container
name:  "quay.io/biocontainers/mappy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mappy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mappy/container.yaml"
updated_at: "2025-05-02 03:48:00.395660"
latest: "2.28--py312h4711d71_3"
container_url: "https://biocontainers.pro/tools/mappy"
aliases:
 - "minimap2.py"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "ncurses5-config"
versions:
 - "2.9--py36_1"
 - "2.17--py36h955c1b8_2"
 - "2.16--py37h84994c4_0"
 - "2.15--py36ha92aebf_0"
 - "2.14--py35ha92aebf_0"
 - "2.13--py35ha92aebf_0"
 - "2.27--py310h83093d7_0"
 - "2.26--py38h7cf9df2_1"
 - "2.24--py38h7cf9df2_4"
 - "2.23--py36h30a8e3e_0"
 - "2.22--py27h8c2299e_0"
 - "2.28--py39h3d4b85c_0"
 - "2.27--py38h7cf9df2_1"
 - "2.28--py38h6bfa29d_1"
 - "2.28--py310h1af8fb7_2"
 - "2.28--py312h4711d71_3"
description: "shpc-registry automated BioContainers addition for mappy"
config: {"url": "https://biocontainers.pro/tools/mappy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mappy", "latest": {"2.28--py312h4711d71_3": "sha256:a728673f1f96d8d0c9dac9168fcd9576d95e6d5abbf7eee13467b01722bcec2f"}, "tags": {"2.9--py36_1": "sha256:92f01d29efba73925dcdbeccd332850d25caa568012b86af83daf353b659550a", "2.17--py36h955c1b8_2": "sha256:32549721f3553f8372a583c24e02a8033d42b647588ce959e1eddf00ab1498c0", "2.16--py37h84994c4_0": "sha256:37b8dfaf28791956019bb42c1839544ee0cbf1957381d4b8c67fee8432862bc0", "2.15--py36ha92aebf_0": "sha256:de2fa13fd433919c72ad1c3e7fee6e909f6b43b0b6ddaa7cdaf74be47f264674", "2.14--py35ha92aebf_0": "sha256:8f9ca8a108e6f86e868605f983922da60fe77a6b9bf8627b63d70b2012f3309c", "2.13--py35ha92aebf_0": "sha256:8077ad2c056248b22182f77026a7cccdd9cd27457493f5917f93ba278a676c87", "2.27--py310h83093d7_0": "sha256:2eec4ff004a9b332f4687dfab22868c79288a8ceaf46948cec583f0cbb8fb3ce", "2.26--py38h7cf9df2_1": "sha256:20b31a99e0d155b3a8fcc37bedd804810736e049ad5556ef187351fd67707204", "2.24--py38h7cf9df2_4": "sha256:f45ea6adff35fc2ae8bfb936f8d71a768d7cc69102e19819f54db0f52c5399a9", "2.23--py36h30a8e3e_0": "sha256:1f8d40bf9c5256cbf7b9819bc217d1dc6211632264321cc5bf604ca3abe4bbdb", "2.22--py27h8c2299e_0": "sha256:8ad2376218d1f7626915dbe6881f5ed5f3a8228802489cae7a50e490e81d4c88", "2.28--py39h3d4b85c_0": "sha256:f4aff2b9117294b05ce1bbccf31cf2937f2b974ee88ea5a83cbe41080a10c6b2", "2.27--py38h7cf9df2_1": "sha256:1eaafd0f90497343cf9145894a4a1e63dfd85c5f5fee4b9c32da0462b22f11f3", "2.28--py38h6bfa29d_1": "sha256:45ebde5bbf419f7a3e7ab8901d731f69766e6c0b9fd4df8af4289621ed64a4f6", "2.28--py310h1af8fb7_2": "sha256:39f9b955d362a116eaff8585b3345200819483bf103b7b84bd2194e7b1c9691d", "2.28--py312h4711d71_3": "sha256:a728673f1f96d8d0c9dac9168fcd9576d95e6d5abbf7eee13467b01722bcec2f"}, "docker": "quay.io/biocontainers/mappy", "aliases": {"minimap2.py": "/usr/local/bin/minimap2.py", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "ncurses5-config": "/usr/local/bin/ncurses5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mappy.
shpc-registry automated BioContainers addition for mappy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mappy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mappy:2.28--py312h4711d71_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mappy/2.28--py312h4711d71_3
$ module help quay.io/biocontainers/mappy/2.28--py312h4711d71_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mappy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mappy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mappy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mappy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mappy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mappy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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