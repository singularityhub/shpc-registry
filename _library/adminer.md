---
layout: container
name:  "adminer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/adminer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/adminer/container.yaml"
updated_at: "2026-01-15 03:45:12.300031"
latest: "5.4.1"
container_url: "https://hub.docker.com/_/adminer"

versions:
 - "4.8.0-fastcgi"
 - "4.8.1"
 - "4.8.1-fastcgi"
 - "latest"
 - "4"
 - "5"
 - "5.0.6"
 - "4.17.1"
 - "5.2.1"
 - "5.1.0"
 - "5.3.0"
 - "5.4.0"
 - "5.4.1"
description: "Database management in a single PHP file."
config: {"docker": "adminer", "url": "https://hub.docker.com/_/adminer", "maintainer": "@vsoch", "description": "Database management in a single PHP file.", "latest": {"5.4.1": "sha256:3bce505927f115e80dedfa3be4c2a7c79226ae8b1994fd5bf7517d83bb8abf60"}, "tags": {"4.8.0-fastcgi": "sha256:5368f087fed03f49e9de8731ee3d9998d7e78391720d500309b5bcde2a401058", "4.8.1": "sha256:34d37131366c5aa84e1693dbed48593ed6f95fb450b576c1a7a59d3a9c9e8802", "4.8.1-fastcgi": "sha256:470601adfd8d1ab5f1006c82ad76022283ce91ea86c56064218514b13b5f7d48", "latest": "sha256:3bce505927f115e80dedfa3be4c2a7c79226ae8b1994fd5bf7517d83bb8abf60", "4": "sha256:c65211d77e5f0097a8794a13f1274e710fd0dc36af899a4328f0f8c937d0dca7", "5": "sha256:3bce505927f115e80dedfa3be4c2a7c79226ae8b1994fd5bf7517d83bb8abf60", "5.0.6": "sha256:82b68b3aad528d09d66ea4cb6930dbc5c8f44317a6bd9d952dcfb99ab00ae601", "4.17.1": "sha256:c65211d77e5f0097a8794a13f1274e710fd0dc36af899a4328f0f8c937d0dca7", "5.2.1": "sha256:44926b66af50cc8accc306a0857567e9d1964cfa0214f8e5ce249d25dbdb6801", "5.1.0": "sha256:0b26fae1673904a6fa4733951be3c3ac906e5921ba140852a8f72bdec894fa15", "5.3.0": "sha256:2b845b0e8e89245afd5bce48c20f3348581021492a64667a2c38a8e7e1096c46", "5.4.0": "sha256:3a1399a54899a9b589885a1b508c37fec816724c7e7f9f883398f943afcebc5c", "5.4.1": "sha256:3bce505927f115e80dedfa3be4c2a7c79226ae8b1994fd5bf7517d83bb8abf60"}}
---

This module is a singularity container wrapper for adminer.
Database management in a single PHP file.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install adminer
```

Or a specific version:

```bash
$ shpc install adminer:5.4.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load adminer/5.4.1
$ module help adminer/5.4.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### adminer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### adminer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### adminer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### adminer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### adminer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### adminer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### adminer

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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