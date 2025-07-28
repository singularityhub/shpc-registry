---
layout: container
name:  "quay.io/biocontainers/muspinsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/muspinsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/muspinsim/container.yaml"
updated_at: "2025-07-28 09:39:36.471228"
latest: "2.3.0"
container_url: "https://biocontainers.pro/tools/muspinsim"
aliases:
 - "ase"
 - "ase-build"
 - "ase-db"
 - "ase-gui"
 - "ase-info"
 - "ase-run"
 - "magresaverage"
 - "muspinsim"
 - "muspinsim.mpi"
 - "phylogen"
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
 - "1.1.0"
 - "2.0.2"
 - "2.2.0"
 - "2.2.1"
 - "2.3.0"
description: "shpc-registry automated BioContainers addition for muspinsim"
config: {"url": "https://biocontainers.pro/tools/muspinsim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for muspinsim", "latest": {"2.3.0": "sha256:4bbc267ed705a9ec0e16730736a3da1837dd999678a12c29dc0ac6d92af4548c"}, "tags": {"1.1.0": "sha256:a7dcb5d935ac087732b106ce210dc14a8eea5609a5288d497c2538c6643c4dff", "2.0.2": "sha256:72c9c6a0b07086107045f3279a410e76f51a1cf3cb5a8438051ae2f94b885445", "2.2.0": "sha256:644ecbe72f243bf34dee6e7f664d14a4e9c48cff554771a8ff12be8d3231459e", "2.2.1": "sha256:e4d172eb5de26aba90532e1c1ea2497dd4ec63a2247918294de94afbcaaf257b", "2.3.0": "sha256:4bbc267ed705a9ec0e16730736a3da1837dd999678a12c29dc0ac6d92af4548c"}, "docker": "quay.io/biocontainers/muspinsim", "aliases": {"ase": "/usr/local/bin/ase", "ase-build": "/usr/local/bin/ase-build", "ase-db": "/usr/local/bin/ase-db", "ase-gui": "/usr/local/bin/ase-gui", "ase-info": "/usr/local/bin/ase-info", "ase-run": "/usr/local/bin/ase-run", "magresaverage": "/usr/local/bin/magresaverage", "muspinsim": "/usr/local/bin/muspinsim", "muspinsim.mpi": "/usr/local/bin/muspinsim.mpi", "phylogen": "/usr/local/bin/phylogen", "soprano_submitter": "/usr/local/bin/soprano_submitter", "vasp2cell": "/usr/local/bin/vasp2cell", "flask": "/usr/local/bin/flask", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.10": "/usr/local/bin/f2py3.10", "img2webp": "/usr/local/bin/img2webp", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/muspinsim.
shpc-registry automated BioContainers addition for muspinsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/muspinsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/muspinsim:2.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/muspinsim/2.3.0
$ module help quay.io/biocontainers/muspinsim/2.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### muspinsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### muspinsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### muspinsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### muspinsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### muspinsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### muspinsim-inspect-deffile:

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


#### muspinsim

```bash
$ singularity exec <container> /usr/local/bin/muspinsim
$ podman run --it --rm --entrypoint /usr/local/bin/muspinsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muspinsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muspinsim.mpi

```bash
$ singularity exec <container> /usr/local/bin/muspinsim.mpi
$ podman run --it --rm --entrypoint /usr/local/bin/muspinsim.mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muspinsim.mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylogen

```bash
$ singularity exec <container> /usr/local/bin/phylogen
$ podman run --it --rm --entrypoint /usr/local/bin/phylogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylogen   -v ${PWD} -w ${PWD} <container> -c " $@"
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