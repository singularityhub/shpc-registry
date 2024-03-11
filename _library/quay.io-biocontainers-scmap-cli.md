---
layout: container
name:  "quay.io/biocontainers/scmap-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scmap-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scmap-cli/container.yaml"
updated_at: "2024-03-11 02:49:30.648888"
latest: "0.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/scmap-cli"
aliases:
 - "scmap-cli-post-install-tests.bats"
 - "scmap-cli-post-install-tests.sh"
 - "scmap-index-cell.R"
 - "scmap-index-cluster.R"
 - "scmap-make-test-data.R"
 - "scmap-preprocess-sce.R"
 - "scmap-scmap-cell.R"
 - "scmap-scmap-cluster.R"
 - "scmap-select-features.R"
 - "scmap_get_std_output.R"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "0.0.9--0"
 - "0.0.11--hdfd78af_1"
 - "0.1.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for scmap-cli"
config: {"url": "https://biocontainers.pro/tools/scmap-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scmap-cli", "latest": {"0.1.0--hdfd78af_0": "sha256:60ebe63a8b3f1b19f0c49f484edba16443c17d2c43478489944fe7afe2d140e1"}, "tags": {"0.0.9--0": "sha256:9713c8fb1a1508db9fb261f4429614d6b609c37612bde66f3729e5cba9b06d27", "0.0.11--hdfd78af_1": "sha256:4380a5149ad33a228467a6ee6b570cfb38a2a8b35e792c88c0e8d0025dee263d", "0.1.0--hdfd78af_0": "sha256:60ebe63a8b3f1b19f0c49f484edba16443c17d2c43478489944fe7afe2d140e1"}, "docker": "quay.io/biocontainers/scmap-cli", "aliases": {"scmap-cli-post-install-tests.bats": "/usr/local/bin/scmap-cli-post-install-tests.bats", "scmap-cli-post-install-tests.sh": "/usr/local/bin/scmap-cli-post-install-tests.sh", "scmap-index-cell.R": "/usr/local/bin/scmap-index-cell.R", "scmap-index-cluster.R": "/usr/local/bin/scmap-index-cluster.R", "scmap-make-test-data.R": "/usr/local/bin/scmap-make-test-data.R", "scmap-preprocess-sce.R": "/usr/local/bin/scmap-preprocess-sce.R", "scmap-scmap-cell.R": "/usr/local/bin/scmap-scmap-cell.R", "scmap-scmap-cluster.R": "/usr/local/bin/scmap-scmap-cluster.R", "scmap-select-features.R": "/usr/local/bin/scmap-select-features.R", "scmap_get_std_output.R": "/usr/local/bin/scmap_get_std_output.R", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scmap-cli.
shpc-registry automated BioContainers addition for scmap-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scmap-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scmap-cli:0.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scmap-cli/0.1.0--hdfd78af_0
$ module help quay.io/biocontainers/scmap-cli/0.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scmap-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scmap-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scmap-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scmap-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scmap-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scmap-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scmap-cli-post-install-tests.bats

```bash
$ singularity exec <container> /usr/local/bin/scmap-cli-post-install-tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/scmap-cli-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap-cli-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmap-cli-post-install-tests.sh

```bash
$ singularity exec <container> /usr/local/bin/scmap-cli-post-install-tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/scmap-cli-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap-cli-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmap-index-cell.R

```bash
$ singularity exec <container> /usr/local/bin/scmap-index-cell.R
$ podman run --it --rm --entrypoint /usr/local/bin/scmap-index-cell.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap-index-cell.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmap-index-cluster.R

```bash
$ singularity exec <container> /usr/local/bin/scmap-index-cluster.R
$ podman run --it --rm --entrypoint /usr/local/bin/scmap-index-cluster.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap-index-cluster.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmap-make-test-data.R

```bash
$ singularity exec <container> /usr/local/bin/scmap-make-test-data.R
$ podman run --it --rm --entrypoint /usr/local/bin/scmap-make-test-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap-make-test-data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmap-preprocess-sce.R

```bash
$ singularity exec <container> /usr/local/bin/scmap-preprocess-sce.R
$ podman run --it --rm --entrypoint /usr/local/bin/scmap-preprocess-sce.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap-preprocess-sce.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmap-scmap-cell.R

```bash
$ singularity exec <container> /usr/local/bin/scmap-scmap-cell.R
$ podman run --it --rm --entrypoint /usr/local/bin/scmap-scmap-cell.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap-scmap-cell.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmap-scmap-cluster.R

```bash
$ singularity exec <container> /usr/local/bin/scmap-scmap-cluster.R
$ podman run --it --rm --entrypoint /usr/local/bin/scmap-scmap-cluster.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap-scmap-cluster.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmap-select-features.R

```bash
$ singularity exec <container> /usr/local/bin/scmap-select-features.R
$ podman run --it --rm --entrypoint /usr/local/bin/scmap-select-features.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap-select-features.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmap_get_std_output.R

```bash
$ singularity exec <container> /usr/local/bin/scmap_get_std_output.R
$ podman run --it --rm --entrypoint /usr/local/bin/scmap_get_std_output.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmap_get_std_output.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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