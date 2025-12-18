---
layout: container
name:  "quay.io/biocontainers/snakefmt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakefmt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakefmt/container.yaml"
updated_at: "2025-12-18 03:40:50.189497"
latest: "0.11.2--pyha6daafd_0"
container_url: "https://biocontainers.pro/tools/snakefmt"
aliases:
 - "black"
 - "blackd"
 - "snakefmt"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.6.1--pyhdfd78af_0"
 - "0.7.0--pyhdfd78af_0"
 - "0.8.0--pyhdfd78af_0"
 - "0.8.1--pyhdfd78af_0"
 - "0.8.2--pyhdfd78af_0"
 - "0.8.4--pyhdfd78af_0"
 - "0.8.5--pyhdfd78af_0"
 - "0.9.0--pyhdfd78af_1"
 - "0.10.0--pyhdfd78af_0"
 - "0.10.2--pyhdfd78af_0"
 - "0.11.0--pyhdfd78af_0"
 - "0.11.2--pyha6daafd_0"
description: "shpc-registry automated BioContainers addition for snakefmt"
config: {"url": "https://biocontainers.pro/tools/snakefmt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snakefmt", "latest": {"0.11.2--pyha6daafd_0": "sha256:654974608caebb06bbbf71f32515a3e16c1521af9b327d352c5c4949abfa7e5e"}, "tags": {"0.6.1--pyhdfd78af_0": "sha256:9d7d016c142dab89a2f02835c2ff74f2d523557570c6346536fbf0010d8f7ae8", "0.7.0--pyhdfd78af_0": "sha256:0b85a551ffa5811453c453138cda9c97246aba576249b364582f85bb05c05d32", "0.8.0--pyhdfd78af_0": "sha256:31b0067a2441921cad1438fe4340de3255412d7eb520f6f6701219496310db51", "0.8.1--pyhdfd78af_0": "sha256:de314cbc523e419a7c3a423b489652a3637a93459bb45780232b200dbf5d9855", "0.8.2--pyhdfd78af_0": "sha256:49224f9600551b295318e30e031e58e0158c9ed930bb47745148f7079f32d983", "0.8.4--pyhdfd78af_0": "sha256:073a2e51b4ff194a765095a174dd4e053d46cf5c20c845d20bc35ecfc62e46f8", "0.8.5--pyhdfd78af_0": "sha256:ddf8122907d3e4295d9d9e3e5b3fce013b6fdb83b6c0731f2c872421512b64c3", "0.9.0--pyhdfd78af_1": "sha256:f1e9eca1f2e4151a1a517464f83238f6a207038acc8baf3c903470e41d6e5122", "0.10.0--pyhdfd78af_0": "sha256:daf1b3e5712717d9f577dd32d729c4c531366529375499c41c3a431dd4e7b61b", "0.10.2--pyhdfd78af_0": "sha256:d3aaa2830870c841c2eca757200ff5c3e3fa891a50856df5084ae1578b8875a6", "0.11.0--pyhdfd78af_0": "sha256:7885a28c5673d082abaa4b1fe4fc5adc44e5b95303ca4d6aa2a0b3046af7db05", "0.11.2--pyha6daafd_0": "sha256:654974608caebb06bbbf71f32515a3e16c1521af9b327d352c5c4949abfa7e5e"}, "docker": "quay.io/biocontainers/snakefmt", "aliases": {"black": "/usr/local/bin/black", "blackd": "/usr/local/bin/blackd", "snakefmt": "/usr/local/bin/snakefmt", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakefmt.
shpc-registry automated BioContainers addition for snakefmt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakefmt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakefmt:0.11.2--pyha6daafd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakefmt/0.11.2--pyha6daafd_0
$ module help quay.io/biocontainers/snakefmt/0.11.2--pyha6daafd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakefmt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakefmt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakefmt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakefmt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakefmt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakefmt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### black

```bash
$ singularity exec <container> /usr/local/bin/black
$ podman run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blackd

```bash
$ singularity exec <container> /usr/local/bin/blackd
$ podman run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakefmt

```bash
$ singularity exec <container> /usr/local/bin/snakefmt
$ podman run --it --rm --entrypoint /usr/local/bin/snakefmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakefmt   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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