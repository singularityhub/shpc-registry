---
layout: container
name:  "quay.io/biocontainers/sepp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sepp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sepp/container.yaml"
updated_at: "2024-11-22 04:06:05.073806"
latest: "4.5.5--py310h9ee0642_0"
container_url: "https://biocontainers.pro/tools/sepp"

versions:
 - "v4.5.0--py37_0"
 - "4.5.1--py37he4bd417_1"
 - "4.5.1--py37h9ee0642_2"
 - "4.5.1--py37h9ee0642_3"
 - "4.5.1--py38h9ee0642_4"
 - "4.5.4--py310h9ee0642_1"
 - "4.5.5--py310h9ee0642_0"
description: "shpc-registry automated BioContainers addition for sepp"
config: {"url": "https://biocontainers.pro/tools/sepp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sepp", "latest": {"4.5.5--py310h9ee0642_0": "sha256:b1d43360360d9d2eeea1d46a43135840709fa07e09dedd58139436c107c3d62f"}, "tags": {"v4.5.0--py37_0": "sha256:eb84a051d18e3ce745f75022ae81cb5c81b078e6064254879b76ab268870e707", "4.5.1--py37he4bd417_1": "sha256:4c8d644c35724da9b40c63cf5b23a0a01290a0b05460c7d4c01d3b7cef83e055", "4.5.1--py37h9ee0642_2": "sha256:2a3b3440beb035b3306958a47b7d4f7b8315725f18698e86f40cc0d70de8574b", "4.5.1--py37h9ee0642_3": "sha256:45d72609b92a6d458b1d398b148f9e295f11ff65430bd19372d0f6527d6ded09", "4.5.1--py38h9ee0642_4": "sha256:05f6efdee773ddab222ba6a2bce472fe098224fb00ba82c1695363d55b9d60e3", "4.5.4--py310h9ee0642_1": "sha256:cecafad7924bf258b8ffb14e2ae36cbb2222dea041a831231de352bed6b3e262", "4.5.5--py310h9ee0642_0": "sha256:b1d43360360d9d2eeea1d46a43135840709fa07e09dedd58139436c107c3d62f"}, "docker": "quay.io/biocontainers/sepp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/sepp.
shpc-registry automated BioContainers addition for sepp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sepp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sepp:4.5.5--py310h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sepp/4.5.5--py310h9ee0642_0
$ module help quay.io/biocontainers/sepp/4.5.5--py310h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sepp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sepp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sepp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sepp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sepp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sepp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### sepp

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