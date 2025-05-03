---
layout: container
name:  "quay.io/biocontainers/quicksect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quicksect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/quicksect/container.yaml"
updated_at: "2025-05-03 03:45:48.339019"
latest: "0.2.2--py312h0fa9677_11"
container_url: "https://biocontainers.pro/tools/quicksect"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.2.2--py39hbf8eff0_5"
 - "0.2.2--py310h4b81fae_8"
 - "0.2.2--py38he5da3d1_8"
 - "0.2.2--py312hf67a6ed_9"
 - "0.2.2--py38h0020b31_10"
 - "0.2.2--py312h0fa9677_11"
description: "shpc-registry automated BioContainers addition for quicksect"
config: {"url": "https://biocontainers.pro/tools/quicksect", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for quicksect", "latest": {"0.2.2--py312h0fa9677_11": "sha256:24059f5cfe98eb86804ceae74ac6bdee5dd53ea2e2044fb2fcf401018bc27a68"}, "tags": {"0.2.2--py39hbf8eff0_5": "sha256:6a4ff9123a5e59195c23e198516c7ccd330ebfd7e1e41c8b3dab19d2a7588a38", "0.2.2--py310h4b81fae_8": "sha256:fec00afad177f7400f45c560636a3191603a327873727420a0402ff223edb0f2", "0.2.2--py38he5da3d1_8": "sha256:5f117fc8f24e7050a1ee03c8b73f03bcd3960410b6b789f6757dec7fab76d4f4", "0.2.2--py312hf67a6ed_9": "sha256:278753d1b5b179ab6f35adf7d18a50334f13fec165fea1117c3a3ab4f338252c", "0.2.2--py38h0020b31_10": "sha256:87d4a86d9f93824958d705780d8fa0f0d14454f39285600bce443176043db6f2", "0.2.2--py312h0fa9677_11": "sha256:24059f5cfe98eb86804ceae74ac6bdee5dd53ea2e2044fb2fcf401018bc27a68"}, "docker": "quay.io/biocontainers/quicksect", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quicksect.
shpc-registry automated BioContainers addition for quicksect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quicksect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quicksect:0.2.2--py312h0fa9677_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quicksect/0.2.2--py312h0fa9677_11
$ module help quay.io/biocontainers/quicksect/0.2.2--py312h0fa9677_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quicksect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quicksect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quicksect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quicksect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quicksect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quicksect-inspect-deffile:

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