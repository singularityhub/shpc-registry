---
layout: container
name:  "quay.io/biocontainers/singlecellnet-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/singlecellnet-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/singlecellnet-cli/container.yaml"
updated_at: "2023-09-13 02:29:01.548041"
latest: "0.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/singlecellnet-cli"
aliases:
 - "bats"
 - "scn-post-install-tests.bats"
 - "scn-post-install-tests.sh"
 - "scn-predict.R"
 - "scn-train-model.R"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "f2py3.9"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
versions:
 - "0.0.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for singlecellnet-cli"
config: {"url": "https://biocontainers.pro/tools/singlecellnet-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for singlecellnet-cli", "latest": {"0.0.1--hdfd78af_0": "sha256:d594924ce6e57609a27febb0b0f43d9049e74a8d959fdc4cfe9340808e88180f"}, "tags": {"0.0.1--hdfd78af_0": "sha256:d594924ce6e57609a27febb0b0f43d9049e74a8d959fdc4cfe9340808e88180f"}, "docker": "quay.io/biocontainers/singlecellnet-cli", "aliases": {"bats": "/usr/local/bin/bats", "scn-post-install-tests.bats": "/usr/local/bin/scn-post-install-tests.bats", "scn-post-install-tests.sh": "/usr/local/bin/scn-post-install-tests.sh", "scn-predict.R": "/usr/local/bin/scn-predict.R", "scn-train-model.R": "/usr/local/bin/scn-train-model.R", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "f2py3.9": "/usr/local/bin/f2py3.9", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/singlecellnet-cli.
shpc-registry automated BioContainers addition for singlecellnet-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/singlecellnet-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/singlecellnet-cli:0.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/singlecellnet-cli/0.0.1--hdfd78af_0
$ module help quay.io/biocontainers/singlecellnet-cli/0.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### singlecellnet-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### singlecellnet-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### singlecellnet-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### singlecellnet-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### singlecellnet-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### singlecellnet-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bats

```bash
$ singularity exec <container> /usr/local/bin/bats
$ podman run --it --rm --entrypoint /usr/local/bin/bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scn-post-install-tests.bats

```bash
$ singularity exec <container> /usr/local/bin/scn-post-install-tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/scn-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scn-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scn-post-install-tests.sh

```bash
$ singularity exec <container> /usr/local/bin/scn-post-install-tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/scn-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scn-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scn-predict.R

```bash
$ singularity exec <container> /usr/local/bin/scn-predict.R
$ podman run --it --rm --entrypoint /usr/local/bin/scn-predict.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scn-predict.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scn-train-model.R

```bash
$ singularity exec <container> /usr/local/bin/scn-train-model.R
$ podman run --it --rm --entrypoint /usr/local/bin/scn-train-model.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scn-train-model.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
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