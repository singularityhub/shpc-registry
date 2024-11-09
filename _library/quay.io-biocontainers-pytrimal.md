---
layout: container
name:  "quay.io/biocontainers/pytrimal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pytrimal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pytrimal/container.yaml"
updated_at: "2024-11-09 03:07:33.387593"
latest: "0.8.0--py310hc31ed2c_1"
container_url: "https://biocontainers.pro/tools/pytrimal"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.5.5--py39h67e14b5_0"
 - "0.5.5--py310h068649b_2"
 - "0.6.0--py38hcbe9525_0"
 - "0.7.0--py39he10ea66_0"
 - "0.7.0--py38hcbe9525_0"
 - "0.6.0--py39he10ea66_0"
 - "0.5.5--py39he10ea66_2"
 - "0.7.0--py311h9f068be_1"
 - "0.8.0--py311h9f068be_0"
 - "0.8.0--py310hc31ed2c_1"
description: "singularity registry hpc automated addition for pytrimal"
config: {"url": "https://biocontainers.pro/tools/pytrimal", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pytrimal", "latest": {"0.8.0--py310hc31ed2c_1": "sha256:2a528c349f1691b41ee05c2f2bff5b3300206f422ba5ccf322d87febc5541ecc"}, "tags": {"0.5.5--py39h67e14b5_0": "sha256:9de448978aad8748e875cc6112578959de1e182b0f4fb0aadcf34aaccba3657b", "0.5.5--py310h068649b_2": "sha256:f6e22f944cdb866e874442f7d22cf31ca475d1bc0ae2a8bcd6c158c21cc6e11e", "0.6.0--py38hcbe9525_0": "sha256:aae0fae121c6ff71a58209b88d8024f979b6b0483bccbe833560e8330b57519e", "0.7.0--py39he10ea66_0": "sha256:3f364b42bd1ce2d217a6612268ded0972d07739207c981b0d7f7ac9e0ced56b8", "0.7.0--py38hcbe9525_0": "sha256:6277e32b7632c2fce060bce26fb2e086e7b65ffe387ded5c7599318d2732cd97", "0.6.0--py39he10ea66_0": "sha256:278794a7012aa710c032cab323b64f86c7166ed2adf9cc5392e1007074028589", "0.5.5--py39he10ea66_2": "sha256:22a162ab22de2d47818fe8b11b7e32102b9b51abff9757caeff6d96d2d2a0726", "0.7.0--py311h9f068be_1": "sha256:deca1f33310ae48facd629239010a36cc323d9368f467ac3a1bd977678582932", "0.8.0--py311h9f068be_0": "sha256:50433f627854077fe1d59c513a2ef90a4989710b4870538b564f4e407e6d705a", "0.8.0--py310hc31ed2c_1": "sha256:2a528c349f1691b41ee05c2f2bff5b3300206f422ba5ccf322d87febc5541ecc"}, "docker": "quay.io/biocontainers/pytrimal", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pytrimal.
singularity registry hpc automated addition for pytrimal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pytrimal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pytrimal:0.8.0--py310hc31ed2c_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pytrimal/0.8.0--py310hc31ed2c_1
$ module help quay.io/biocontainers/pytrimal/0.8.0--py310hc31ed2c_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pytrimal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pytrimal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pytrimal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pytrimal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pytrimal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pytrimal-inspect-deffile:

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