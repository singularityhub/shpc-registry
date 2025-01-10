---
layout: container
name:  "quay.io/biocontainers/bioconductor-chemmineob"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chemmineob/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chemmineob/container.yaml"
updated_at: "2025-01-10 02:57:57.702865"
latest: "1.40.0--r43hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chemmineob"
aliases:
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "obfitall"
 - "obmm"
 - "obabel"
 - "obconformer"
 - "obdistgen"
 - "obenergy"
 - "obfit"
 - "obgen"
 - "obgrep"
 - "obminimize"
 - "obprobe"
 - "obprop"
 - "obrms"
 - "obrotamer"
 - "obrotate"
 - "obspectrophore"
 - "obsym"
 - "obtautomer"
 - "obthermo"
 - "roundtrip"
 - "python3.1"
versions:
 - "1.36.0--r42hc247a5b_0"
 - "1.36.0--r42hc247a5b_1"
 - "1.38.0--r43hc247a5b_0"
 - "1.40.0--r43hc247a5b_0"
description: "singularity registry hpc automated addition for bioconductor-chemmineob"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chemmineob", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-chemmineob", "latest": {"1.40.0--r43hc247a5b_0": "sha256:b98896eec9589e53fa6258094e2ce6a96825c7213cb9cfc0e60454ad0bd461e6"}, "tags": {"1.36.0--r42hc247a5b_0": "sha256:9d2ffbd36db6e7040b2f04c77164fa9cad33c32d7301e0fbe505cb8ba545c564", "1.36.0--r42hc247a5b_1": "sha256:87afbed8cbe5d7e0e7a825f529577a62cbbd2be3d6b35d2ae22e61233e88abde", "1.38.0--r43hc247a5b_0": "sha256:974f853c3e94ab5f2b717d98fa9d3a0a258e6578b6dd403fcdce9270e4a311f7", "1.40.0--r43hc247a5b_0": "sha256:b98896eec9589e53fa6258094e2ce6a96825c7213cb9cfc0e60454ad0bd461e6"}, "docker": "quay.io/biocontainers/bioconductor-chemmineob", "aliases": {"2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "obfitall": "/usr/local/bin/obfitall", "obmm": "/usr/local/bin/obmm", "obabel": "/usr/local/bin/obabel", "obconformer": "/usr/local/bin/obconformer", "obdistgen": "/usr/local/bin/obdistgen", "obenergy": "/usr/local/bin/obenergy", "obfit": "/usr/local/bin/obfit", "obgen": "/usr/local/bin/obgen", "obgrep": "/usr/local/bin/obgrep", "obminimize": "/usr/local/bin/obminimize", "obprobe": "/usr/local/bin/obprobe", "obprop": "/usr/local/bin/obprop", "obrms": "/usr/local/bin/obrms", "obrotamer": "/usr/local/bin/obrotamer", "obrotate": "/usr/local/bin/obrotate", "obspectrophore": "/usr/local/bin/obspectrophore", "obsym": "/usr/local/bin/obsym", "obtautomer": "/usr/local/bin/obtautomer", "obthermo": "/usr/local/bin/obthermo", "roundtrip": "/usr/local/bin/roundtrip", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chemmineob.
singularity registry hpc automated addition for bioconductor-chemmineob
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chemmineob
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chemmineob:1.40.0--r43hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chemmineob/1.40.0--r43hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-chemmineob/1.40.0--r43hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chemmineob-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chemmineob-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chemmineob-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chemmineob-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chemmineob-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chemmineob-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### obprobe

```bash
$ singularity exec <container> /usr/local/bin/obprobe
$ podman run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprop

```bash
$ singularity exec <container> /usr/local/bin/obprop
$ podman run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obrms

```bash
$ singularity exec <container> /usr/local/bin/obrms
$ podman run --it --rm --entrypoint /usr/local/bin/obrms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obrms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obrotamer

```bash
$ singularity exec <container> /usr/local/bin/obrotamer
$ podman run --it --rm --entrypoint /usr/local/bin/obrotamer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obrotamer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obrotate

```bash
$ singularity exec <container> /usr/local/bin/obrotate
$ podman run --it --rm --entrypoint /usr/local/bin/obrotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obrotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obspectrophore

```bash
$ singularity exec <container> /usr/local/bin/obspectrophore
$ podman run --it --rm --entrypoint /usr/local/bin/obspectrophore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obspectrophore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obsym

```bash
$ singularity exec <container> /usr/local/bin/obsym
$ podman run --it --rm --entrypoint /usr/local/bin/obsym   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obsym   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obtautomer

```bash
$ singularity exec <container> /usr/local/bin/obtautomer
$ podman run --it --rm --entrypoint /usr/local/bin/obtautomer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obtautomer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obthermo

```bash
$ singularity exec <container> /usr/local/bin/obthermo
$ podman run --it --rm --entrypoint /usr/local/bin/obthermo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obthermo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roundtrip

```bash
$ singularity exec <container> /usr/local/bin/roundtrip
$ podman run --it --rm --entrypoint /usr/local/bin/roundtrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roundtrip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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