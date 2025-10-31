---
layout: container
name:  "quay.io/biocontainers/npstructures"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/npstructures/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/npstructures/container.yaml"
updated_at: "2025-10-31 03:35:42.616813"
latest: "0.2.19--pyh05cac1d_1"
container_url: "https://biocontainers.pro/tools/npstructures"
aliases:
 - "f2py3.11"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "0.2.9--pyha8f3691_0"
 - "0.2.10--pyha8f3691_0"
 - "0.2.11--pyha8f3691_0"
 - "0.2.12--pyha8f3691_0"
 - "0.2.14--pyha8f3691_0"
 - "0.2.15--pyha8f3691_0"
 - "0.2.16--pyha8f3691_0"
 - "0.2.17--pyha8f3691_0"
 - "0.2.18--pyha8f3691_0"
 - "0.2.19--pyha8f3691_0"
 - "0.2.19--pyh05cac1d_1"
description: "singularity registry hpc automated addition for npstructures"
config: {"url": "https://biocontainers.pro/tools/npstructures", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for npstructures", "latest": {"0.2.19--pyh05cac1d_1": "sha256:0f7fe4e31bcba1097327bdf31d769e2128065c9170b2b6ded6565bfd221c080f"}, "tags": {"0.2.9--pyha8f3691_0": "sha256:e7f9bf8c7f69af6f8f0af5960cfae067933b4f076a9204b850c3ecfe28425667", "0.2.10--pyha8f3691_0": "sha256:627bc3888fe7749d9eed0b4b9bf3f3a3d025985e28e0b20c871b86c7cddf7fd4", "0.2.11--pyha8f3691_0": "sha256:93dbcfe696a3d6310e0e68ee847359fabfe79bf4994503bd891aef73cd50bafe", "0.2.12--pyha8f3691_0": "sha256:efe86f8a16a6039782b64c528b89e79ac8053b01c6e7719568a1e2e90c23a6f6", "0.2.14--pyha8f3691_0": "sha256:75b86999d2b29db89a7db1294f58c9771eb33c7f7439d7eea3fa38fc31d0cf75", "0.2.15--pyha8f3691_0": "sha256:1e326fb1340a31de09406951e3be12893569333b625db91411ce2769333af495", "0.2.16--pyha8f3691_0": "sha256:4ff0aef4e5a2bc22f3f600fa0238c74dd775db95349b964858a71d87ccd5bdb3", "0.2.17--pyha8f3691_0": "sha256:2e68eb4769615cd200804a6243d6bdcbb9ba09fb8fe3ad0b87aadb8188501075", "0.2.18--pyha8f3691_0": "sha256:4837de76844e53a197961aaacb7709b627b4cb619f2c3bf60c020877bcc13ce8", "0.2.19--pyha8f3691_0": "sha256:dcdd5dbadd4842d89661f86c1e99cc79db1c365fc8b9d47bd12a1411126b93fb", "0.2.19--pyh05cac1d_1": "sha256:0f7fe4e31bcba1097327bdf31d769e2128065c9170b2b6ded6565bfd221c080f"}, "docker": "quay.io/biocontainers/npstructures", "aliases": {"f2py3.11": "/usr/local/bin/f2py3.11", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/npstructures.
singularity registry hpc automated addition for npstructures
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/npstructures
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/npstructures:0.2.19--pyh05cac1d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/npstructures/0.2.19--pyh05cac1d_1
$ module help quay.io/biocontainers/npstructures/0.2.19--pyh05cac1d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### npstructures-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### npstructures-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### npstructures-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### npstructures-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### npstructures-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### npstructures-inspect-deffile:

```bash
$ singularity inspect -d <container>
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