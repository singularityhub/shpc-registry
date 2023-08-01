---
layout: container
name:  "quay.io/biocontainers/eden"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eden/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eden/container.yaml"
updated_at: "2023-08-01 02:54:10.051585"
latest: "2.0--pyhd1c1de3_3"
container_url: "https://biocontainers.pro/tools/eden"
aliases:
 - "RNAshapes"
 - "dsdp5"
 - "location_predictor"
 - "model"
 - "motif"
 - "motif_display.py"
 - "obfitall"
 - "obmm"
 - "transformseq"
 - "weblogo"
 - "obabel"
 - "obconformer"
 - "obdistgen"
 - "obenergy"
 - "obfit"
 - "obgen"
 - "obgrep"
 - "obminimize"
versions:
 - "2.0--pyhd1c1de3_3"
description: "shpc-registry automated BioContainers addition for eden"
config: {"url": "https://biocontainers.pro/tools/eden", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eden", "latest": {"2.0--pyhd1c1de3_3": "sha256:7712b82c3a4b8e88e29038028da5609fac8216e1f2fa7743bb329059da30ff63"}, "tags": {"2.0--pyhd1c1de3_3": "sha256:7712b82c3a4b8e88e29038028da5609fac8216e1f2fa7743bb329059da30ff63"}, "docker": "quay.io/biocontainers/eden", "aliases": {"RNAshapes": "/usr/local/bin/RNAshapes", "dsdp5": "/usr/local/bin/dsdp5", "location_predictor": "/usr/local/bin/location_predictor", "model": "/usr/local/bin/model", "motif": "/usr/local/bin/motif", "motif_display.py": "/usr/local/bin/motif_display.py", "obfitall": "/usr/local/bin/obfitall", "obmm": "/usr/local/bin/obmm", "transformseq": "/usr/local/bin/transformseq", "weblogo": "/usr/local/bin/weblogo", "obabel": "/usr/local/bin/obabel", "obconformer": "/usr/local/bin/obconformer", "obdistgen": "/usr/local/bin/obdistgen", "obenergy": "/usr/local/bin/obenergy", "obfit": "/usr/local/bin/obfit", "obgen": "/usr/local/bin/obgen", "obgrep": "/usr/local/bin/obgrep", "obminimize": "/usr/local/bin/obminimize"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eden.
shpc-registry automated BioContainers addition for eden
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eden
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eden:2.0--pyhd1c1de3_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eden/2.0--pyhd1c1de3_3
$ module help quay.io/biocontainers/eden/2.0--pyhd1c1de3_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eden-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eden-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eden-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eden-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eden-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eden-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAshapes

```bash
$ singularity exec <container> /usr/local/bin/RNAshapes
$ podman run --it --rm --entrypoint /usr/local/bin/RNAshapes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAshapes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsdp5

```bash
$ singularity exec <container> /usr/local/bin/dsdp5
$ podman run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### location_predictor

```bash
$ singularity exec <container> /usr/local/bin/location_predictor
$ podman run --it --rm --entrypoint /usr/local/bin/location_predictor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/location_predictor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### model

```bash
$ singularity exec <container> /usr/local/bin/model
$ podman run --it --rm --entrypoint /usr/local/bin/model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/model   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### motif

```bash
$ singularity exec <container> /usr/local/bin/motif
$ podman run --it --rm --entrypoint /usr/local/bin/motif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/motif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### motif_display.py

```bash
$ singularity exec <container> /usr/local/bin/motif_display.py
$ podman run --it --rm --entrypoint /usr/local/bin/motif_display.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/motif_display.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obfitall

```bash
$ singularity exec <container> /usr/local/bin/obfitall
$ podman run --it --rm --entrypoint /usr/local/bin/obfitall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obfitall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obmm

```bash
$ singularity exec <container> /usr/local/bin/obmm
$ podman run --it --rm --entrypoint /usr/local/bin/obmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformseq

```bash
$ singularity exec <container> /usr/local/bin/transformseq
$ podman run --it --rm --entrypoint /usr/local/bin/transformseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weblogo

```bash
$ singularity exec <container> /usr/local/bin/weblogo
$ podman run --it --rm --entrypoint /usr/local/bin/weblogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weblogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obabel

```bash
$ singularity exec <container> /usr/local/bin/obabel
$ podman run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obconformer

```bash
$ singularity exec <container> /usr/local/bin/obconformer
$ podman run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obdistgen

```bash
$ singularity exec <container> /usr/local/bin/obdistgen
$ podman run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obenergy

```bash
$ singularity exec <container> /usr/local/bin/obenergy
$ podman run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obfit

```bash
$ singularity exec <container> /usr/local/bin/obfit
$ podman run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgen

```bash
$ singularity exec <container> /usr/local/bin/obgen
$ podman run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgrep

```bash
$ singularity exec <container> /usr/local/bin/obgrep
$ podman run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obminimize

```bash
$ singularity exec <container> /usr/local/bin/obminimize
$ podman run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
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