---
layout: container
name:  "quay.io/biocontainers/biobb_godmd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_godmd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_godmd/container.yaml"
updated_at: "2025-09-26 03:19:58.978170"
latest: "5.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_godmd"
aliases:
 - "discrete"
 - "godmd_prep"
 - "godmd_run"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "3.8.1--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_1"
 - "4.0.2--pyhdfd78af_0"
 - "4.1.0--pyhdfd78af_0"
 - "4.2.0--pyhdfd78af_0"
 - "5.0.0--pyhdfd78af_0"
 - "5.0.0--pyhdfd78af_1"
 - "5.1.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for biobb_godmd"
config: {"url": "https://biocontainers.pro/tools/biobb_godmd", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for biobb_godmd", "latest": {"5.1.1--pyhdfd78af_0": "sha256:fe3f759f96b4e8e788492234ac04366b75efa41c4955e7ef765d0b282d072dbf"}, "tags": {"3.8.1--pyhdfd78af_0": "sha256:79569e71abad74c1bf0dd2413aace5b6a7b6df422606fe164c680042df5b5d5f", "4.0.0--pyhdfd78af_1": "sha256:61efa334cf7b82e8093c8cb23a78d174228b77b81ae3c92ea585abe4b7fe131e", "4.0.2--pyhdfd78af_0": "sha256:0027ef5bcf250fee37905c5db4e31ba13c33d30f826703a0355fed63d800251e", "4.1.0--pyhdfd78af_0": "sha256:39b692a5ca6a9e58c548ec02f724897fe697fb3dd308e77feffe509f5094c317", "4.2.0--pyhdfd78af_0": "sha256:7419932eb0fab810417041a0dd8f8c4ed7f2701d7cbc392c646fdf6bcbd28c6c", "5.0.0--pyhdfd78af_0": "sha256:ae401561581d0876272ba17edb724ded424923e9e986c1ebf64f4458c341305e", "5.0.0--pyhdfd78af_1": "sha256:6339acf6ea280ef8fdc4a7a555c0bb43053268670843ba02e363936788809b8c", "5.1.1--pyhdfd78af_0": "sha256:fe3f759f96b4e8e788492234ac04366b75efa41c4955e7ef765d0b282d072dbf"}, "docker": "quay.io/biocontainers/biobb_godmd", "aliases": {"discrete": "/usr/local/bin/discrete", "godmd_prep": "/usr/local/bin/godmd_prep", "godmd_run": "/usr/local/bin/godmd_run", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_godmd.
singularity registry hpc automated addition for biobb_godmd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_godmd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_godmd:5.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_godmd/5.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_godmd/5.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_godmd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_godmd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_godmd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_godmd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_godmd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_godmd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### discrete

```bash
$ singularity exec <container> /usr/local/bin/discrete
$ podman run --it --rm --entrypoint /usr/local/bin/discrete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/discrete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### godmd_prep

```bash
$ singularity exec <container> /usr/local/bin/godmd_prep
$ podman run --it --rm --entrypoint /usr/local/bin/godmd_prep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/godmd_prep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### godmd_run

```bash
$ singularity exec <container> /usr/local/bin/godmd_run
$ podman run --it --rm --entrypoint /usr/local/bin/godmd_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/godmd_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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