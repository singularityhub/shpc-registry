---
layout: container
name:  "quay.io/biocontainers/abromics_galaxy_json_extractor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abromics_galaxy_json_extractor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/abromics_galaxy_json_extractor/container.yaml"
updated_at: "2023-07-23 03:27:18.947717"
latest: "0.4--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/abromics_galaxy_json_extractor"
aliases:
 - "abromics_extract"
 - "f2py3.11"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "0.1--pyh7cba7a3_0"
 - "0.1--pyh7cba7a3_1"
 - "0.4--pyh7cba7a3_0"
 - "0.2--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for abromics_galaxy_json_extractor"
config: {"url": "https://biocontainers.pro/tools/abromics_galaxy_json_extractor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for abromics_galaxy_json_extractor", "latest": {"0.4--pyh7cba7a3_0": "sha256:d734adf08305cfd8c254691f306b66686df6d40d4bf98cd2f88cbfe482d128ec"}, "tags": {"0.1--pyh7cba7a3_0": "sha256:82c5f0cb8e22a33725b0682074bb2ac4f0a04a96786fa101b7162702fac0663e", "0.1--pyh7cba7a3_1": "sha256:d747407f794e9bbb9142ee8ff326dc9c285d0edeb891def6915c719fd61c9f97", "0.4--pyh7cba7a3_0": "sha256:d734adf08305cfd8c254691f306b66686df6d40d4bf98cd2f88cbfe482d128ec", "0.2--pyh7cba7a3_0": "sha256:f0c97301c6eaba5445d69ed4816072ebc4bbd4152ce864d5200e1c8bfeee4448"}, "docker": "quay.io/biocontainers/abromics_galaxy_json_extractor", "aliases": {"abromics_extract": "/usr/local/bin/abromics_extract", "f2py3.11": "/usr/local/bin/f2py3.11", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abromics_galaxy_json_extractor.
singularity registry hpc automated addition for abromics_galaxy_json_extractor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abromics_galaxy_json_extractor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abromics_galaxy_json_extractor:0.4--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abromics_galaxy_json_extractor/0.4--pyh7cba7a3_0
$ module help quay.io/biocontainers/abromics_galaxy_json_extractor/0.4--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abromics_galaxy_json_extractor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abromics_galaxy_json_extractor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abromics_galaxy_json_extractor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abromics_galaxy_json_extractor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abromics_galaxy_json_extractor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abromics_galaxy_json_extractor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abromics_extract

```bash
$ singularity exec <container> /usr/local/bin/abromics_extract
$ podman run --it --rm --entrypoint /usr/local/bin/abromics_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abromics_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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