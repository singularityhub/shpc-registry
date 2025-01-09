---
layout: container
name:  "quay.io/biocontainers/realphy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/realphy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/realphy/container.yaml"
updated_at: "2025-01-09 13:59:23.031177"
latest: "1.13--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/realphy"
aliases:
 - "Manual_May25_2020.pdf"
 - "REALPHY_v113"
 - "RealPhy_v113.jar"
 - "realphy"
 - "metadata_conda_debug.yaml"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
versions:
 - "1.13--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for realphy"
config: {"url": "https://biocontainers.pro/tools/realphy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for realphy", "latest": {"1.13--hdfd78af_1": "sha256:fcbcfd71a0f49ec4e122fb0b329fae5be85f44735a0596cdc033968d680f0503"}, "tags": {"1.13--hdfd78af_1": "sha256:fcbcfd71a0f49ec4e122fb0b329fae5be85f44735a0596cdc033968d680f0503"}, "docker": "quay.io/biocontainers/realphy", "aliases": {"Manual_May25_2020.pdf": "/usr/local/bin/Manual_May25_2020.pdf", "REALPHY_v113": "/usr/local/bin/REALPHY_v113", "RealPhy_v113.jar": "/usr/local/bin/RealPhy_v113.jar", "realphy": "/usr/local/bin/realphy", "metadata_conda_debug.yaml": "/usr/local/bin/metadata_conda_debug.yaml", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/realphy.
shpc-registry automated BioContainers addition for realphy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/realphy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/realphy:1.13--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/realphy/1.13--hdfd78af_1
$ module help quay.io/biocontainers/realphy/1.13--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### realphy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### realphy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### realphy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### realphy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### realphy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### realphy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Manual_May25_2020.pdf

```bash
$ singularity exec <container> /usr/local/bin/Manual_May25_2020.pdf
$ podman run --it --rm --entrypoint /usr/local/bin/Manual_May25_2020.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Manual_May25_2020.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### REALPHY_v113

```bash
$ singularity exec <container> /usr/local/bin/REALPHY_v113
$ podman run --it --rm --entrypoint /usr/local/bin/REALPHY_v113   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/REALPHY_v113   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RealPhy_v113.jar

```bash
$ singularity exec <container> /usr/local/bin/RealPhy_v113.jar
$ podman run --it --rm --entrypoint /usr/local/bin/RealPhy_v113.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RealPhy_v113.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### realphy

```bash
$ singularity exec <container> /usr/local/bin/realphy
$ podman run --it --rm --entrypoint /usr/local/bin/realphy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/realphy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metadata_conda_debug.yaml

```bash
$ singularity exec <container> /usr/local/bin/metadata_conda_debug.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
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