---
layout: container
name:  "quay.io/biocontainers/kamino"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kamino/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kamino/container.yaml"
updated_at: "2026-04-03 04:38:51.193783"
latest: "0.8.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/kamino"
aliases:
 - "kamino"
versions:
 - "0.1.0--h4349ce8_0"
 - "0.2.1--h4349ce8_0"
 - "0.7.0--h4349ce8_0"
 - "0.6.1--h4349ce8_0"
 - "0.5.1--h4349ce8_0"
 - "0.4.0--h4349ce8_0"
 - "0.3.0--h4349ce8_0"
 - "0.8.0--h4349ce8_0"
description: "singularity registry hpc automated addition for kamino"
config: {"url": "https://biocontainers.pro/tools/kamino", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kamino", "latest": {"0.8.0--h4349ce8_0": "sha256:c429b265ebb289a652616dc6ac85f2d9ff4ffc79dc5565d59f13097d55371c51"}, "tags": {"0.1.0--h4349ce8_0": "sha256:025c7be0e57601396ba7b63358aacf41d86801db099e46a854e6824090fae136", "0.2.1--h4349ce8_0": "sha256:5ab413d58487d018a805b4273320a341ac2f43503fe03055b7f036fe066fe704", "0.7.0--h4349ce8_0": "sha256:69fcaaa473c6597e36b8328b075c5e7c454e1ee77d5650c40d33d6114dd5f273", "0.6.1--h4349ce8_0": "sha256:2c147a957c07c206620c833f2ef70aa5f9ed27d612c21f4e0e8148c44fb6b59c", "0.5.1--h4349ce8_0": "sha256:bfae0c156592c1e719f456c2f43a662f85952d104e59f86cad5cdaed1640b93d", "0.4.0--h4349ce8_0": "sha256:dd6423003c9636ce2e3eb813a7abc27c24d52025f0b7c82f08524fe20a9f5196", "0.3.0--h4349ce8_0": "sha256:ab7a3b694fcca684af22249235b2c30e60364d9844ca78986551412556ede476", "0.8.0--h4349ce8_0": "sha256:c429b265ebb289a652616dc6ac85f2d9ff4ffc79dc5565d59f13097d55371c51"}, "docker": "quay.io/biocontainers/kamino", "aliases": {"kamino": "/usr/local/bin/kamino"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kamino.
singularity registry hpc automated addition for kamino
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kamino
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kamino:0.8.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kamino/0.8.0--h4349ce8_0
$ module help quay.io/biocontainers/kamino/0.8.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kamino-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kamino-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kamino-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kamino-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kamino-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kamino-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kamino

```bash
$ singularity exec <container> /usr/local/bin/kamino
$ podman run --it --rm --entrypoint /usr/local/bin/kamino   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kamino   -v ${PWD} -w ${PWD} <container> -c " $@"
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