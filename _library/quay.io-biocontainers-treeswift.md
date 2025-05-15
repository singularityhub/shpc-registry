---
layout: container
name:  "quay.io/biocontainers/treeswift"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treeswift/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treeswift/container.yaml"
updated_at: "2025-05-15 03:51:04.532622"
latest: "1.1.45--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/treeswift"
aliases:
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "1.1.6--py_0"
 - "1.1.30--pyh7cba7a3_0"
 - "1.1.33--pyh7cba7a3_0"
 - "1.1.35--pyh7cba7a3_0"
 - "1.1.37--pyh7cba7a3_0"
 - "1.1.39--pyh7cba7a3_0"
 - "1.1.42--pyh7cba7a3_0"
 - "1.1.43--pyh7cba7a3_0"
 - "1.1.44--pyh7e72e81_0"
 - "1.1.45--pyh7e72e81_0"
description: "shpc-registry automated BioContainers addition for treeswift"
config: {"url": "https://biocontainers.pro/tools/treeswift", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for treeswift", "latest": {"1.1.45--pyh7e72e81_0": "sha256:722a5715f1623117356d5f99dcf8960d07124ff4a0e6bade64434b747bbbada7"}, "tags": {"1.1.6--py_0": "sha256:780afa49e29b27a166ba6394919657d53beaf478e73204e3069bbe26caec3204", "1.1.30--pyh7cba7a3_0": "sha256:3478bf11f89f8f5687acc316530158fb7604d70e28c301ea21bc081deb7b2105", "1.1.33--pyh7cba7a3_0": "sha256:2aad19ec3e920425bb2f65649ed5bf2019add1b221e2247912ce7a242b5c8f09", "1.1.35--pyh7cba7a3_0": "sha256:b2adeeee567444c0609e0d2862ee47b18d79e6fe2c1cbb876daf54048a030f40", "1.1.37--pyh7cba7a3_0": "sha256:7a7c5fdea3d13c57fa0d225e44976c783752ae68eaccc6cbfabac3d51b152cee", "1.1.39--pyh7cba7a3_0": "sha256:b8979eedbb54197fdc8dfebb5208e86f440b3606a4a61fe962d983705eb4df21", "1.1.42--pyh7cba7a3_0": "sha256:46b4f7816616b7c8b92ce5fc8ccc4587ea646cd6280e68c26620ded7626bb5d8", "1.1.43--pyh7cba7a3_0": "sha256:a0d4bbb2b7f44ea97ef9f0d1a5588822bf82e948fafbde2525bdd6bf3c33dca0", "1.1.44--pyh7e72e81_0": "sha256:f60dc42e673981e04b0fe524900a0fa10be7c653918e0e94bec01bbd7c1f7b72", "1.1.45--pyh7e72e81_0": "sha256:722a5715f1623117356d5f99dcf8960d07124ff4a0e6bade64434b747bbbada7"}, "docker": "quay.io/biocontainers/treeswift", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treeswift.
shpc-registry automated BioContainers addition for treeswift
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treeswift
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treeswift:1.1.45--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treeswift/1.1.45--pyh7e72e81_0
$ module help quay.io/biocontainers/treeswift/1.1.45--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treeswift-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treeswift-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treeswift-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treeswift-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treeswift-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treeswift-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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