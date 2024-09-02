---
layout: container
name:  "quay.io/biocontainers/pymuonsuite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pymuonsuite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pymuonsuite/container.yaml"
updated_at: "2024-09-02 04:26:59.575346"
latest: "0.3.0"
container_url: "https://biocontainers.pro/tools/pymuonsuite"
aliases:
 - "ase"
 - "ase-build"
 - "ase-db"
 - "ase-gui"
 - "ase-info"
 - "ase-run"
 - "magresaverage"
 - "phylogen"
 - "pm-asephonons"
 - "pm-muairss"
 - "pm-muairss-gen"
 - "pm-nq"
 - "pm-symmetry"
 - "pm-uep-opt"
 - "pm-uep-plot"
 - "soprano_submitter"
 - "vasp2cell"
 - "flask"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "f2py3.10"
 - "img2webp"
 - "cwebp"
 - "dwebp"
versions:
 - "0.2.1"
 - "0.2.3"
 - "0.3.0"
description: "shpc-registry automated BioContainers addition for pymuonsuite"
config: {"url": "https://biocontainers.pro/tools/pymuonsuite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pymuonsuite", "latest": {"0.3.0": "sha256:876818eb7140a5ac373e641928614b08ce2cf3ba056c7a78fa56dbc36f9984ce"}, "tags": {"0.2.1": "sha256:0ebe7c44475a5a8a6e3e261394ff50bf649dfd75e9a51f1031e504f9e6d06693", "0.2.3": "sha256:a035882cde85e758780f522b7374e430e881ff6614111649df3b5da1dbe8f32e", "0.3.0": "sha256:876818eb7140a5ac373e641928614b08ce2cf3ba056c7a78fa56dbc36f9984ce"}, "docker": "quay.io/biocontainers/pymuonsuite", "aliases": {"ase": "/usr/local/bin/ase", "ase-build": "/usr/local/bin/ase-build", "ase-db": "/usr/local/bin/ase-db", "ase-gui": "/usr/local/bin/ase-gui", "ase-info": "/usr/local/bin/ase-info", "ase-run": "/usr/local/bin/ase-run", "magresaverage": "/usr/local/bin/magresaverage", "phylogen": "/usr/local/bin/phylogen", "pm-asephonons": "/usr/local/bin/pm-asephonons", "pm-muairss": "/usr/local/bin/pm-muairss", "pm-muairss-gen": "/usr/local/bin/pm-muairss-gen", "pm-nq": "/usr/local/bin/pm-nq", "pm-symmetry": "/usr/local/bin/pm-symmetry", "pm-uep-opt": "/usr/local/bin/pm-uep-opt", "pm-uep-plot": "/usr/local/bin/pm-uep-plot", "soprano_submitter": "/usr/local/bin/soprano_submitter", "vasp2cell": "/usr/local/bin/vasp2cell", "flask": "/usr/local/bin/flask", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.10": "/usr/local/bin/f2py3.10", "img2webp": "/usr/local/bin/img2webp", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pymuonsuite.
shpc-registry automated BioContainers addition for pymuonsuite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pymuonsuite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pymuonsuite:0.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pymuonsuite/0.3.0
$ module help quay.io/biocontainers/pymuonsuite/0.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pymuonsuite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pymuonsuite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pymuonsuite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pymuonsuite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pymuonsuite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pymuonsuite-inspect-deffile:

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


#### magresaverage

```bash
$ singularity exec <container> /usr/local/bin/magresaverage
$ podman run --it --rm --entrypoint /usr/local/bin/magresaverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magresaverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylogen

```bash
$ singularity exec <container> /usr/local/bin/phylogen
$ podman run --it --rm --entrypoint /usr/local/bin/phylogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-asephonons

```bash
$ singularity exec <container> /usr/local/bin/pm-asephonons
$ podman run --it --rm --entrypoint /usr/local/bin/pm-asephonons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-asephonons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-muairss

```bash
$ singularity exec <container> /usr/local/bin/pm-muairss
$ podman run --it --rm --entrypoint /usr/local/bin/pm-muairss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-muairss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-muairss-gen

```bash
$ singularity exec <container> /usr/local/bin/pm-muairss-gen
$ podman run --it --rm --entrypoint /usr/local/bin/pm-muairss-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-muairss-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-nq

```bash
$ singularity exec <container> /usr/local/bin/pm-nq
$ podman run --it --rm --entrypoint /usr/local/bin/pm-nq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-nq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-symmetry

```bash
$ singularity exec <container> /usr/local/bin/pm-symmetry
$ podman run --it --rm --entrypoint /usr/local/bin/pm-symmetry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-symmetry   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-uep-opt

```bash
$ singularity exec <container> /usr/local/bin/pm-uep-opt
$ podman run --it --rm --entrypoint /usr/local/bin/pm-uep-opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-uep-opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-uep-plot

```bash
$ singularity exec <container> /usr/local/bin/pm-uep-plot
$ podman run --it --rm --entrypoint /usr/local/bin/pm-uep-plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-uep-plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soprano_submitter

```bash
$ singularity exec <container> /usr/local/bin/soprano_submitter
$ podman run --it --rm --entrypoint /usr/local/bin/soprano_submitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soprano_submitter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vasp2cell

```bash
$ singularity exec <container> /usr/local/bin/vasp2cell
$ podman run --it --rm --entrypoint /usr/local/bin/vasp2cell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vasp2cell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2webp

```bash
$ singularity exec <container> /usr/local/bin/img2webp
$ podman run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
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