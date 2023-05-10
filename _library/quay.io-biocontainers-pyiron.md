---
layout: container
name:  "quay.io/biocontainers/pyiron"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyiron/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyiron/container.yaml"
updated_at: "2023-05-10 03:18:37.642066"
latest: "0.2.2"
container_url: "https://biocontainers.pro/tools/pyiron"
aliases:
 - "ase"
 - "ase-build"
 - "ase-db"
 - "ase-gui"
 - "ase-info"
 - "ase-run"
 - "phonopy"
 - "phonopy-FHI-aims"
 - "phonopy-bandplot"
 - "phonopy-crystal-born"
 - "phonopy-dispmanager"
 - "phonopy-gruneisen"
 - "phonopy-gruneisenplot"
 - "phonopy-pdosplot"
 - "phonopy-propplot"
 - "phonopy-qha"
 - "phonopy-tdplot"
 - "phonopy-vasp-born"
 - "phonopy-vasp-efe"
 - "flask"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "qhelpconverter"
 - "qwebengine_convert_dict"
 - "canbusutil"
 - "qgltf"
 - "qmlcachegen"
versions:
 - "0.2.2"
description: "shpc-registry automated BioContainers addition for pyiron"
config: {"url": "https://biocontainers.pro/tools/pyiron", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyiron", "latest": {"0.2.2": "sha256:d996c07806a2dc6091480ecc77fd16beab18c56dbb1154145cca199c06879373"}, "tags": {"0.2.2": "sha256:d996c07806a2dc6091480ecc77fd16beab18c56dbb1154145cca199c06879373"}, "docker": "quay.io/biocontainers/pyiron", "aliases": {"ase": "/usr/local/bin/ase", "ase-build": "/usr/local/bin/ase-build", "ase-db": "/usr/local/bin/ase-db", "ase-gui": "/usr/local/bin/ase-gui", "ase-info": "/usr/local/bin/ase-info", "ase-run": "/usr/local/bin/ase-run", "phonopy": "/usr/local/bin/phonopy", "phonopy-FHI-aims": "/usr/local/bin/phonopy-FHI-aims", "phonopy-bandplot": "/usr/local/bin/phonopy-bandplot", "phonopy-crystal-born": "/usr/local/bin/phonopy-crystal-born", "phonopy-dispmanager": "/usr/local/bin/phonopy-dispmanager", "phonopy-gruneisen": "/usr/local/bin/phonopy-gruneisen", "phonopy-gruneisenplot": "/usr/local/bin/phonopy-gruneisenplot", "phonopy-pdosplot": "/usr/local/bin/phonopy-pdosplot", "phonopy-propplot": "/usr/local/bin/phonopy-propplot", "phonopy-qha": "/usr/local/bin/phonopy-qha", "phonopy-tdplot": "/usr/local/bin/phonopy-tdplot", "phonopy-vasp-born": "/usr/local/bin/phonopy-vasp-born", "phonopy-vasp-efe": "/usr/local/bin/phonopy-vasp-efe", "flask": "/usr/local/bin/flask", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "qhelpconverter": "/usr/local/bin/qhelpconverter", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "canbusutil": "/usr/local/bin/canbusutil", "qgltf": "/usr/local/bin/qgltf", "qmlcachegen": "/usr/local/bin/qmlcachegen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyiron.
shpc-registry automated BioContainers addition for pyiron
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyiron
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyiron:0.2.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyiron/0.2.2
$ module help quay.io/biocontainers/pyiron/0.2.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyiron-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyiron-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyiron-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyiron-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyiron-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyiron-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ase

```bash
$ singularity exec <container> /usr/local/bin/ase
$ podman run --it --rm --entrypoint /usr/local/bin/ase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ase-build

```bash
$ singularity exec <container> /usr/local/bin/ase-build
$ podman run --it --rm --entrypoint /usr/local/bin/ase-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ase-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ase-db

```bash
$ singularity exec <container> /usr/local/bin/ase-db
$ podman run --it --rm --entrypoint /usr/local/bin/ase-db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ase-db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ase-gui

```bash
$ singularity exec <container> /usr/local/bin/ase-gui
$ podman run --it --rm --entrypoint /usr/local/bin/ase-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ase-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ase-info

```bash
$ singularity exec <container> /usr/local/bin/ase-info
$ podman run --it --rm --entrypoint /usr/local/bin/ase-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ase-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ase-run

```bash
$ singularity exec <container> /usr/local/bin/ase-run
$ podman run --it --rm --entrypoint /usr/local/bin/ase-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ase-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy

```bash
$ singularity exec <container> /usr/local/bin/phonopy
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-FHI-aims

```bash
$ singularity exec <container> /usr/local/bin/phonopy-FHI-aims
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-FHI-aims   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-FHI-aims   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-bandplot

```bash
$ singularity exec <container> /usr/local/bin/phonopy-bandplot
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-bandplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-bandplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-crystal-born

```bash
$ singularity exec <container> /usr/local/bin/phonopy-crystal-born
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-crystal-born   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-crystal-born   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-dispmanager

```bash
$ singularity exec <container> /usr/local/bin/phonopy-dispmanager
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-dispmanager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-dispmanager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-gruneisen

```bash
$ singularity exec <container> /usr/local/bin/phonopy-gruneisen
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-gruneisen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-gruneisen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-gruneisenplot

```bash
$ singularity exec <container> /usr/local/bin/phonopy-gruneisenplot
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-gruneisenplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-gruneisenplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-pdosplot

```bash
$ singularity exec <container> /usr/local/bin/phonopy-pdosplot
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-pdosplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-pdosplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-propplot

```bash
$ singularity exec <container> /usr/local/bin/phonopy-propplot
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-propplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-propplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-qha

```bash
$ singularity exec <container> /usr/local/bin/phonopy-qha
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-qha   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-qha   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-tdplot

```bash
$ singularity exec <container> /usr/local/bin/phonopy-tdplot
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-tdplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-tdplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-vasp-born

```bash
$ singularity exec <container> /usr/local/bin/phonopy-vasp-born
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-vasp-born   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-vasp-born   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phonopy-vasp-efe

```bash
$ singularity exec <container> /usr/local/bin/phonopy-vasp-efe
$ podman run --it --rm --entrypoint /usr/local/bin/phonopy-vasp-efe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phonopy-vasp-efe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qwebengine_convert_dict

```bash
$ singularity exec <container> /usr/local/bin/qwebengine_convert_dict
$ podman run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qgltf

```bash
$ singularity exec <container> /usr/local/bin/qgltf
$ podman run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlcachegen

```bash
$ singularity exec <container> /usr/local/bin/qmlcachegen
$ podman run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
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