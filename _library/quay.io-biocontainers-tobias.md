---
layout: container
name:  "quay.io/biocontainers/tobias"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tobias/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tobias/container.yaml"
updated_at: "2025-01-09 03:45:10.192155"
latest: "0.17.0--py312h1f1cfbb_0"
container_url: "https://biocontainers.pro/tools/tobias"
aliases:
 - "TOBIAS"
 - "ccache-swig"
 - "croco-0.6-config"
 - "csslint-0.6"
 - "filter_important_factors.py"
 - "moods-dna.py"
 - "svist4get"
 - "svist4get_copier"
 - "swig"
 - "x86_64-conda_cos6-linux-gnu-pkg-config"
 - "g-ir-doc-tool"
 - "giffilter"
 - "gifsponge"
 - "vba_extract.py"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "intersection_matrix.py"
versions:
 - "0.9.0--py36hc1659b7_0"
 - "0.13.0--py36h4f025d9_0"
 - "0.12.12--py36h4f025d9_0"
 - "0.11.6--py36h29c9776_1"
 - "0.16.1--py38h24c8ff8_0"
 - "0.15.1--py39hec7c8de_0"
 - "0.13.3--py36h40b2fa4_0"
 - "0.12.12--py37h77a2a36_0"
 - "0.11.6--py37h97743b1_1"
 - "0.16.1--py312h1f1cfbb_1"
 - "0.17.0--py312h1f1cfbb_0"
description: "shpc-registry automated BioContainers addition for tobias"
config: {"url": "https://biocontainers.pro/tools/tobias", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tobias", "latest": {"0.17.0--py312h1f1cfbb_0": "sha256:f7108889ba25136ac44186460741c3a9d5eeb99805c54876930053d97d8b163a"}, "tags": {"0.9.0--py36hc1659b7_0": "sha256:ff6d292e80d07210c077d855e8cf45a87f8e0f8f120885b3fad2a4242460f2d5", "0.13.0--py36h4f025d9_0": "sha256:248678d29f151ff297b5b41feaa86d28ab7c3dfe3c08605c19dd9a28003eb570", "0.12.12--py36h4f025d9_0": "sha256:1b1c9ba97db7f468e7d9151d1bcbd1b900d6f1772a62a443f8672a2e12e6a1df", "0.11.6--py36h29c9776_1": "sha256:09780107398b644439cddd1540e6fe3d25e68c6c287355617b3db8f52236e51c", "0.16.1--py38h24c8ff8_0": "sha256:80bd64e937b4340a45d61815ff2ab8a54a3e0f19642543e29e9850673930643d", "0.15.1--py39hec7c8de_0": "sha256:584903685163c108e6df1f0f322eb04d9ca8b99edfe1ede00aece41a81feef1d", "0.13.3--py36h40b2fa4_0": "sha256:e0393232d20a74f526c0ff2e32613dd29f1bffb4458653b88c3af1ed5026785d", "0.12.12--py37h77a2a36_0": "sha256:a2f031d8309e28d9a9d96659ded3b51cdffa4e9b25238e972eb28c1a825e80b0", "0.11.6--py37h97743b1_1": "sha256:5cf6e3564718adb1e9ddf3e0e315d3a586c81479a602fd0fb4d20d854b913b2a", "0.16.1--py312h1f1cfbb_1": "sha256:6f225384747616d0311414c08c665c66a2b9b2fba7b6e4a7655e64a65b27f2db", "0.17.0--py312h1f1cfbb_0": "sha256:f7108889ba25136ac44186460741c3a9d5eeb99805c54876930053d97d8b163a"}, "docker": "quay.io/biocontainers/tobias", "aliases": {"TOBIAS": "/usr/local/bin/TOBIAS", "ccache-swig": "/usr/local/bin/ccache-swig", "croco-0.6-config": "/usr/local/bin/croco-0.6-config", "csslint-0.6": "/usr/local/bin/csslint-0.6", "filter_important_factors.py": "/usr/local/bin/filter_important_factors.py", "moods-dna.py": "/usr/local/bin/moods-dna.py", "svist4get": "/usr/local/bin/svist4get", "svist4get_copier": "/usr/local/bin/svist4get_copier", "swig": "/usr/local/bin/swig", "x86_64-conda_cos6-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config", "g-ir-doc-tool": "/usr/local/bin/g-ir-doc-tool", "giffilter": "/usr/local/bin/giffilter", "gifsponge": "/usr/local/bin/gifsponge", "vba_extract.py": "/usr/local/bin/vba_extract.py", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tobias.
shpc-registry automated BioContainers addition for tobias
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tobias
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tobias:0.17.0--py312h1f1cfbb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tobias/0.17.0--py312h1f1cfbb_0
$ module help quay.io/biocontainers/tobias/0.17.0--py312h1f1cfbb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tobias-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tobias-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tobias-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tobias-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tobias-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tobias-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TOBIAS

```bash
$ singularity exec <container> /usr/local/bin/TOBIAS
$ podman run --it --rm --entrypoint /usr/local/bin/TOBIAS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TOBIAS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccache-swig

```bash
$ singularity exec <container> /usr/local/bin/ccache-swig
$ podman run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### croco-0.6-config

```bash
$ singularity exec <container> /usr/local/bin/croco-0.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/croco-0.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/croco-0.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csslint-0.6

```bash
$ singularity exec <container> /usr/local/bin/csslint-0.6
$ podman run --it --rm --entrypoint /usr/local/bin/csslint-0.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csslint-0.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_important_factors.py

```bash
$ singularity exec <container> /usr/local/bin/filter_important_factors.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_important_factors.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_important_factors.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moods-dna.py

```bash
$ singularity exec <container> /usr/local/bin/moods-dna.py
$ podman run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svist4get

```bash
$ singularity exec <container> /usr/local/bin/svist4get
$ podman run --it --rm --entrypoint /usr/local/bin/svist4get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svist4get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svist4get_copier

```bash
$ singularity exec <container> /usr/local/bin/svist4get_copier
$ podman run --it --rm --entrypoint /usr/local/bin/svist4get_copier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svist4get_copier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swig

```bash
$ singularity exec <container> /usr/local/bin/swig
$ podman run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda_cos6-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-doc-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-doc-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffilter

```bash
$ singularity exec <container> /usr/local/bin/giffilter
$ podman run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifsponge

```bash
$ singularity exec <container> /usr/local/bin/gifsponge
$ podman run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-annotation-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-annotation-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-compiler

```bash
$ singularity exec <container> /usr/local/bin/g-ir-compiler
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-generate

```bash
$ singularity exec <container> /usr/local/bin/g-ir-generate
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-inspect

```bash
$ singularity exec <container> /usr/local/bin/g-ir-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-scanner

```bash
$ singularity exec <container> /usr/local/bin/g-ir-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersection_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/intersection_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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