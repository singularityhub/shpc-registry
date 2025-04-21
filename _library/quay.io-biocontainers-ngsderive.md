---
layout: container
name:  "quay.io/biocontainers/ngsderive"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngsderive/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngsderive/container.yaml"
updated_at: "2025-04-21 03:59:21.473165"
latest: "4.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ngsderive"
aliases:
 - "ngsderive"
 - "pkginfo"
 - "poetry"
 - "doesitcache"
 - "jsonschema"
 - "f2py3.7"
 - "chardetect"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
versions:
 - "2.2.0--pyhdfd78af_0"
 - "2.2.0--pyhdfd78af_2"
 - "2.3.1--pyhdfd78af_0"
 - "3.1.0--pyhdfd78af_0"
 - "2.4.0--pyhdfd78af_0"
 - "3.1.1--pyhdfd78af_0"
 - "3.2.1--pyhdfd78af_0"
 - "3.3.2--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ngsderive"
config: {"url": "https://biocontainers.pro/tools/ngsderive", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngsderive", "latest": {"4.0.0--pyhdfd78af_0": "sha256:4ba7367c1d096aa72dbe639edfd51601a4c2a190f73e82f85293662e8f0e9780"}, "tags": {"2.2.0--pyhdfd78af_0": "sha256:4ba72e81999e11fce4dfb90453d33c82c2d07f0880ef8c2df14f54887f3bf8af", "2.2.0--pyhdfd78af_2": "sha256:e7d67221fdb0533864b15b01334bd6f021be06c8415629794472c0e4a14264a6", "2.3.1--pyhdfd78af_0": "sha256:b3c084a1e28e32ec1a0c1d1ffe99a45e66f5fb8799a59405e9c8cfd0297b99b7", "3.1.0--pyhdfd78af_0": "sha256:5fc500ad84bcff16097d3ce318d32f53e061ca7cd50ed636387638ee940ea3ce", "2.4.0--pyhdfd78af_0": "sha256:53e2e89e0ba511972d3175ff33785c0fc5dcdb587f748954254fd45bda8d8a43", "3.1.1--pyhdfd78af_0": "sha256:caeea84904dbcf949e71213c35bbc2e87cb324d2b47656fcf0be310cdec3e1b1", "3.2.1--pyhdfd78af_0": "sha256:5af2dbea809ee7ebf24614109374d5e8dbd9573283b72e5caeb72078eac8f3a8", "3.3.2--pyhdfd78af_0": "sha256:5495337962a44a0ea9743b169f9afab707b423f32c4b7ba264a52a8683c546ef", "4.0.0--pyhdfd78af_0": "sha256:4ba7367c1d096aa72dbe639edfd51601a4c2a190f73e82f85293662e8f0e9780"}, "docker": "quay.io/biocontainers/ngsderive", "aliases": {"ngsderive": "/usr/local/bin/ngsderive", "pkginfo": "/usr/local/bin/pkginfo", "poetry": "/usr/local/bin/poetry", "doesitcache": "/usr/local/bin/doesitcache", "jsonschema": "/usr/local/bin/jsonschema", "f2py3.7": "/usr/local/bin/f2py3.7", "chardetect": "/usr/local/bin/chardetect", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngsderive.
shpc-registry automated BioContainers addition for ngsderive
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngsderive
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngsderive:4.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngsderive/4.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/ngsderive/4.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngsderive-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngsderive-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngsderive-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngsderive-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngsderive-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngsderive-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ngsderive

```bash
$ singularity exec <container> /usr/local/bin/ngsderive
$ podman run --it --rm --entrypoint /usr/local/bin/ngsderive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngsderive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkginfo

```bash
$ singularity exec <container> /usr/local/bin/pkginfo
$ podman run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poetry

```bash
$ singularity exec <container> /usr/local/bin/poetry
$ podman run --it --rm --entrypoint /usr/local/bin/poetry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poetry   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
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