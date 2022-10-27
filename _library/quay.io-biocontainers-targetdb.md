---
layout: container
name:  "quay.io/biocontainers/targetdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/targetdb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/targetdb/container.yaml"
updated_at: "2022-10-27 00:44:57.291274"
latest: "1.3.1--pyh864c0ab_0"
container_url: "https://biocontainers.pro/tools/targetdb"
aliases:
 - "dpocket"
 - "fpocket"
 - "hyper"
 - "imgcmp"
 - "imginfo"
 - "jasper"
 - "mdpocket"
 - "opencv_annotation"
 - "opencv_interactive-calibration"
 - "opencv_version"
 - "opencv_visualisation"
 - "opencv_waldboost_detector"
 - "setup_vars_opencv4.sh"
 - "targetDB"
 - "target_DB"
 - "tmrdemo"
 - "tpocket"
versions:
 - "1.3.1--pyh864c0ab_0"
description: "shpc-registry automated BioContainers addition for targetdb"
config: {"url": "https://biocontainers.pro/tools/targetdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for targetdb", "latest": {"1.3.1--pyh864c0ab_0": "sha256:4a523b0f824316de7958ed1221b19ed581d71fb9ccef85fadc65e6a10c4ace46"}, "tags": {"1.3.1--pyh864c0ab_0": "sha256:4a523b0f824316de7958ed1221b19ed581d71fb9ccef85fadc65e6a10c4ace46"}, "docker": "quay.io/biocontainers/targetdb", "aliases": {"dpocket": "/usr/local/bin/dpocket", "fpocket": "/usr/local/bin/fpocket", "hyper": "/usr/local/bin/hyper", "imgcmp": "/usr/local/bin/imgcmp", "imginfo": "/usr/local/bin/imginfo", "jasper": "/usr/local/bin/jasper", "mdpocket": "/usr/local/bin/mdpocket", "opencv_annotation": "/usr/local/bin/opencv_annotation", "opencv_interactive-calibration": "/usr/local/bin/opencv_interactive-calibration", "opencv_version": "/usr/local/bin/opencv_version", "opencv_visualisation": "/usr/local/bin/opencv_visualisation", "opencv_waldboost_detector": "/usr/local/bin/opencv_waldboost_detector", "setup_vars_opencv4.sh": "/usr/local/bin/setup_vars_opencv4.sh", "targetDB": "/usr/local/bin/targetDB", "target_DB": "/usr/local/bin/target_DB", "tmrdemo": "/usr/local/bin/tmrdemo", "tpocket": "/usr/local/bin/tpocket"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/targetdb.
shpc-registry automated BioContainers addition for targetdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/targetdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/targetdb:1.3.1--pyh864c0ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/targetdb/1.3.1--pyh864c0ab_0
$ module help quay.io/biocontainers/targetdb/1.3.1--pyh864c0ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### targetdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### targetdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### targetdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### targetdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### targetdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### targetdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dpocket

```bash
$ singularity exec <container> /usr/local/bin/dpocket
$ podman run --it --rm --entrypoint /usr/local/bin/dpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fpocket

```bash
$ singularity exec <container> /usr/local/bin/fpocket
$ podman run --it --rm --entrypoint /usr/local/bin/fpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hyper

```bash
$ singularity exec <container> /usr/local/bin/hyper
$ podman run --it --rm --entrypoint /usr/local/bin/hyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imgcmp

```bash
$ singularity exec <container> /usr/local/bin/imgcmp
$ podman run --it --rm --entrypoint /usr/local/bin/imgcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imgcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imginfo

```bash
$ singularity exec <container> /usr/local/bin/imginfo
$ podman run --it --rm --entrypoint /usr/local/bin/imginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jasper

```bash
$ singularity exec <container> /usr/local/bin/jasper
$ podman run --it --rm --entrypoint /usr/local/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mdpocket

```bash
$ singularity exec <container> /usr/local/bin/mdpocket
$ podman run --it --rm --entrypoint /usr/local/bin/mdpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_annotation

```bash
$ singularity exec <container> /usr/local/bin/opencv_annotation
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_interactive-calibration

```bash
$ singularity exec <container> /usr/local/bin/opencv_interactive-calibration
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_interactive-calibration   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_interactive-calibration   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_version

```bash
$ singularity exec <container> /usr/local/bin/opencv_version
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_visualisation

```bash
$ singularity exec <container> /usr/local/bin/opencv_visualisation
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_visualisation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_visualisation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_waldboost_detector

```bash
$ singularity exec <container> /usr/local/bin/opencv_waldboost_detector
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_waldboost_detector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_waldboost_detector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup_vars_opencv4.sh

```bash
$ singularity exec <container> /usr/local/bin/setup_vars_opencv4.sh
$ podman run --it --rm --entrypoint /usr/local/bin/setup_vars_opencv4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup_vars_opencv4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### targetDB

```bash
$ singularity exec <container> /usr/local/bin/targetDB
$ podman run --it --rm --entrypoint /usr/local/bin/targetDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/targetDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### target_DB

```bash
$ singularity exec <container> /usr/local/bin/target_DB
$ podman run --it --rm --entrypoint /usr/local/bin/target_DB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/target_DB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tmrdemo

```bash
$ singularity exec <container> /usr/local/bin/tmrdemo
$ podman run --it --rm --entrypoint /usr/local/bin/tmrdemo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tmrdemo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tpocket

```bash
$ singularity exec <container> /usr/local/bin/tpocket
$ podman run --it --rm --entrypoint /usr/local/bin/tpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
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