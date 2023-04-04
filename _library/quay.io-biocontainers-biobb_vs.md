---
layout: container
name:  "quay.io/biocontainers/biobb_vs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_vs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_vs/container.yaml"
updated_at: "2023-04-04 02:33:21.418816"
latest: "3.9.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_vs"
aliases:
 - "autodock_vina_run"
 - "bindingsite"
 - "box"
 - "box_residues"
 - "dpocket"
 - "extract_model_pdbqt"
 - "fpocket"
 - "fpocket_filter"
 - "fpocket_run"
 - "fpocket_select"
 - "mdpocket"
 - "tpocket"
 - "vina"
 - "vina_split"
 - "zipcmp"
 - "zipmerge"
 - "ziptool"
 - "gif2hdf"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
 - "hdf24to8"
 - "hdf2gif"
versions:
 - "3.8.1--pyhdfd78af_0"
 - "3.9.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_vs"
config: {"url": "https://biocontainers.pro/tools/biobb_vs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_vs", "latest": {"3.9.0--pyhdfd78af_0": "sha256:4b0df305eb747459d0514192cbfe68fc52a76774d593cc27c4e3a8b4d260afeb"}, "tags": {"3.8.1--pyhdfd78af_0": "sha256:a089d7a39d9ef43fcc853dcb5940700a98d95762e83181914c8c72792d81b7bf", "3.9.0--pyhdfd78af_0": "sha256:4b0df305eb747459d0514192cbfe68fc52a76774d593cc27c4e3a8b4d260afeb"}, "docker": "quay.io/biocontainers/biobb_vs", "aliases": {"autodock_vina_run": "/usr/local/bin/autodock_vina_run", "bindingsite": "/usr/local/bin/bindingsite", "box": "/usr/local/bin/box", "box_residues": "/usr/local/bin/box_residues", "dpocket": "/usr/local/bin/dpocket", "extract_model_pdbqt": "/usr/local/bin/extract_model_pdbqt", "fpocket": "/usr/local/bin/fpocket", "fpocket_filter": "/usr/local/bin/fpocket_filter", "fpocket_run": "/usr/local/bin/fpocket_run", "fpocket_select": "/usr/local/bin/fpocket_select", "mdpocket": "/usr/local/bin/mdpocket", "tpocket": "/usr/local/bin/tpocket", "vina": "/usr/local/bin/vina", "vina_split": "/usr/local/bin/vina_split", "zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_vs.
shpc-registry automated BioContainers addition for biobb_vs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_vs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_vs:3.9.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_vs/3.9.0--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_vs/3.9.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_vs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_vs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_vs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_vs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_vs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_vs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autodock_vina_run

```bash
$ singularity exec <container> /usr/local/bin/autodock_vina_run
$ podman run --it --rm --entrypoint /usr/local/bin/autodock_vina_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autodock_vina_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bindingsite

```bash
$ singularity exec <container> /usr/local/bin/bindingsite
$ podman run --it --rm --entrypoint /usr/local/bin/bindingsite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bindingsite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### box

```bash
$ singularity exec <container> /usr/local/bin/box
$ podman run --it --rm --entrypoint /usr/local/bin/box   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/box   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### box_residues

```bash
$ singularity exec <container> /usr/local/bin/box_residues
$ podman run --it --rm --entrypoint /usr/local/bin/box_residues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/box_residues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dpocket

```bash
$ singularity exec <container> /usr/local/bin/dpocket
$ podman run --it --rm --entrypoint /usr/local/bin/dpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_model_pdbqt

```bash
$ singularity exec <container> /usr/local/bin/extract_model_pdbqt
$ podman run --it --rm --entrypoint /usr/local/bin/extract_model_pdbqt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_model_pdbqt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fpocket

```bash
$ singularity exec <container> /usr/local/bin/fpocket
$ podman run --it --rm --entrypoint /usr/local/bin/fpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fpocket_filter

```bash
$ singularity exec <container> /usr/local/bin/fpocket_filter
$ podman run --it --rm --entrypoint /usr/local/bin/fpocket_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fpocket_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fpocket_run

```bash
$ singularity exec <container> /usr/local/bin/fpocket_run
$ podman run --it --rm --entrypoint /usr/local/bin/fpocket_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fpocket_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fpocket_select

```bash
$ singularity exec <container> /usr/local/bin/fpocket_select
$ podman run --it --rm --entrypoint /usr/local/bin/fpocket_select   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fpocket_select   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mdpocket

```bash
$ singularity exec <container> /usr/local/bin/mdpocket
$ podman run --it --rm --entrypoint /usr/local/bin/mdpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tpocket

```bash
$ singularity exec <container> /usr/local/bin/tpocket
$ podman run --it --rm --entrypoint /usr/local/bin/tpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vina

```bash
$ singularity exec <container> /usr/local/bin/vina
$ podman run --it --rm --entrypoint /usr/local/bin/vina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vina   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vina_split

```bash
$ singularity exec <container> /usr/local/bin/vina_split
$ podman run --it --rm --entrypoint /usr/local/bin/vina_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vina_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipcmp

```bash
$ singularity exec <container> /usr/local/bin/zipcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipmerge

```bash
$ singularity exec <container> /usr/local/bin/zipmerge
$ podman run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ziptool

```bash
$ singularity exec <container> /usr/local/bin/ziptool
$ podman run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2hdf

```bash
$ singularity exec <container> /usr/local/bin/gif2hdf
$ podman run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncdump

```bash
$ singularity exec <container> /usr/local/bin/h4_ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncgen

```bash
$ singularity exec <container> /usr/local/bin/h4_ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4cc

```bash
$ singularity exec <container> /usr/local/bin/h4cc
$ podman run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4redeploy

```bash
$ singularity exec <container> /usr/local/bin/h4redeploy
$ podman run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf24to8

```bash
$ singularity exec <container> /usr/local/bin/hdf24to8
$ podman run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2gif

```bash
$ singularity exec <container> /usr/local/bin/hdf2gif
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
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