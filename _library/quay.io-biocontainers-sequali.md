---
layout: container
name:  "quay.io/biocontainers/sequali"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sequali/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sequali/container.yaml"
updated_at: "2024-12-03 04:46:30.294298"
latest: "0.12.0--py311hdad781d_0"
container_url: "https://biocontainers.pro/tools/sequali"
aliases:
 - "pygal_gen.py"
 - "sequali"
 - "sequali-report"
 - "igzip"
 - "pbunzip2"
 - "pbzcat"
 - "pbzip2"
 - "pigz"
 - "unpigz"
 - "tqdm"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.1.0--py310h4b81fae_0"
 - "0.4.1--py39hf95cd2a_0"
 - "0.3.0--py310h4b81fae_0"
 - "0.2.0--py310h4b81fae_0"
 - "0.6.0--py38he5da3d1_0"
 - "0.5.1--py310h4b81fae_0"
 - "0.4.1--py38he5da3d1_0"
 - "0.3.0--py38he5da3d1_0"
 - "0.2.0--py39hf95cd2a_0"
 - "0.7.1--py310h4b81fae_0"
 - "0.10.0--py312hf67a6ed_1"
 - "0.9.1--py310h4b81fae_0"
 - "0.8.0--py310h4b81fae_0"
 - "0.11.1--py38h0020b31_2"
 - "0.12.0--py311hdad781d_0"
description: "singularity registry hpc automated addition for sequali"
config: {"url": "https://biocontainers.pro/tools/sequali", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sequali", "latest": {"0.12.0--py311hdad781d_0": "sha256:419f22c4166d3127ca31e1e4dca02c6e4fb04c32781ba2b800a516cac9b31c37"}, "tags": {"0.1.0--py310h4b81fae_0": "sha256:c8dc189b2acd08be95ed7abc240d2797730cb6d1fb4e54b4d215f67b6443acdf", "0.4.1--py39hf95cd2a_0": "sha256:b158522f050119644e440a481cdd6d12e81e85af62d41a7ba9964d685a6d886c", "0.3.0--py310h4b81fae_0": "sha256:c7049e96977b1b60f99d5f6c45bc8f2ff1bbf7ca016cd1a504723acfd3ea61c1", "0.2.0--py310h4b81fae_0": "sha256:055fa2adee23900dbc530738e478b8f0ae69838c8b413b862480dcf7cd863466", "0.6.0--py38he5da3d1_0": "sha256:306c2bc95e96801b5b8569c683e5b5b72219a431079efa83390754ed3e9730eb", "0.5.1--py310h4b81fae_0": "sha256:d338e0fd0be3d304aafaf35b6b4db964e4e309dfb2190ff02ce11c8916ab52c2", "0.4.1--py38he5da3d1_0": "sha256:a08ba14ff2ed6bc0317b7a01c905a36616bfc156683197409d6e818f32c5ec4c", "0.3.0--py38he5da3d1_0": "sha256:858890dc4b24cf10f21fdeb9e333968cd70749d7ff5b90b7e11866fad6fecc5a", "0.2.0--py39hf95cd2a_0": "sha256:36bc1f1c864d1b47694dcf436df6a5cf03a398e347c6098c1dc0d809b9271a6b", "0.7.1--py310h4b81fae_0": "sha256:abc9128884299885a322fda4b7e0e7074d1821c84dd1568254dc15bc15e8a852", "0.10.0--py312hf67a6ed_1": "sha256:3c612190c5ecaf1692de3f0236620c0a7bf14ce276fa2c66fbce34570984095b", "0.9.1--py310h4b81fae_0": "sha256:fb8a284b3f42a3c0fecf83bb4ec5919faa13f8a1ed77f3b644441dbca55f0433", "0.8.0--py310h4b81fae_0": "sha256:ac9126f93aaf959da8e06ff52d6a0b016ab49aa1ce09a4bb80ad612f46626aaf", "0.11.1--py38h0020b31_2": "sha256:41de184de0f0d9f17fffde1332886b09c7c57301d61648b3f69d805fc307bea1", "0.12.0--py311hdad781d_0": "sha256:419f22c4166d3127ca31e1e4dca02c6e4fb04c32781ba2b800a516cac9b31c37"}, "docker": "quay.io/biocontainers/sequali", "aliases": {"pygal_gen.py": "/usr/local/bin/pygal_gen.py", "sequali": "/usr/local/bin/sequali", "sequali-report": "/usr/local/bin/sequali-report", "igzip": "/usr/local/bin/igzip", "pbunzip2": "/usr/local/bin/pbunzip2", "pbzcat": "/usr/local/bin/pbzcat", "pbzip2": "/usr/local/bin/pbzip2", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "tqdm": "/usr/local/bin/tqdm", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sequali.
singularity registry hpc automated addition for sequali
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sequali
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sequali:0.12.0--py311hdad781d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sequali/0.12.0--py311hdad781d_0
$ module help quay.io/biocontainers/sequali/0.12.0--py311hdad781d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sequali-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sequali-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sequali-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sequali-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sequali-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sequali-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pygal_gen.py

```bash
$ singularity exec <container> /usr/local/bin/pygal_gen.py
$ podman run --it --rm --entrypoint /usr/local/bin/pygal_gen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygal_gen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sequali

```bash
$ singularity exec <container> /usr/local/bin/sequali
$ podman run --it --rm --entrypoint /usr/local/bin/sequali   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequali   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sequali-report

```bash
$ singularity exec <container> /usr/local/bin/sequali-report
$ podman run --it --rm --entrypoint /usr/local/bin/sequali-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequali-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbunzip2

```bash
$ singularity exec <container> /usr/local/bin/pbunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzcat

```bash
$ singularity exec <container> /usr/local/bin/pbzcat
$ podman run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzip2

```bash
$ singularity exec <container> /usr/local/bin/pbzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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