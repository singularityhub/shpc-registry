---
layout: container
name:  "quay.io/biocontainers/metawepp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metawepp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metawepp/container.yaml"
updated_at: "2026-03-25 04:46:27.197730"
latest: "0.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/metawepp"
aliases:
 - "inv"
 - "invoke"
 - "k2"
 - "menuinst"
 - "run-metawepp"
 - "viral_usher"
 - "viral_usher_build"
 - "wepp"
 - "distro"
 - "jsondiff"
 - "jsonpatch"
 - "mpiexec.gforker"
 - "corepack"
 - "npx"
 - "kraken2"
 - "kraken2-build"
 - "kraken2-inspect"
 - "node"
 - "npm"
 - "jsonpointer"
 - "mamba-package"
 - "wsdump"
 - "archspec"
 - "archive-nlmnlp"
 - "archive-pids"
 - "conda2solv"
 - "download-flatfile"
 - "dumpsolv"
 - "ecollect"
 - "gbf2facds"
 - "gbf2tbl"
 - "gff-sort"
 - "gff2xml"
versions:
 - "0.1.0--hdfd78af_0"
description: "singularity registry hpc automated addition for metawepp"
config: {"url": "https://biocontainers.pro/tools/metawepp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metawepp", "latest": {"0.1.0--hdfd78af_0": "sha256:d41fed3f3403b0c77191af4f00beb93d3f271228fc815b2127843675eacfaa4d"}, "tags": {"0.1.0--hdfd78af_0": "sha256:d41fed3f3403b0c77191af4f00beb93d3f271228fc815b2127843675eacfaa4d"}, "docker": "quay.io/biocontainers/metawepp", "aliases": {"inv": "/usr/local/bin/inv", "invoke": "/usr/local/bin/invoke", "k2": "/usr/local/bin/k2", "menuinst": "/usr/local/bin/menuinst", "run-metawepp": "/usr/local/bin/run-metawepp", "viral_usher": "/usr/local/bin/viral_usher", "viral_usher_build": "/usr/local/bin/viral_usher_build", "wepp": "/usr/local/bin/wepp", "distro": "/usr/local/bin/distro", "jsondiff": "/usr/local/bin/jsondiff", "jsonpatch": "/usr/local/bin/jsonpatch", "mpiexec.gforker": "/usr/local/bin/mpiexec.gforker", "corepack": "/usr/local/bin/corepack", "npx": "/usr/local/bin/npx", "kraken2": "/usr/local/bin/kraken2", "kraken2-build": "/usr/local/bin/kraken2-build", "kraken2-inspect": "/usr/local/bin/kraken2-inspect", "node": "/usr/local/bin/node", "npm": "/usr/local/bin/npm", "jsonpointer": "/usr/local/bin/jsonpointer", "mamba-package": "/usr/local/bin/mamba-package", "wsdump": "/usr/local/bin/wsdump", "archspec": "/usr/local/bin/archspec", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "conda2solv": "/usr/local/bin/conda2solv", "download-flatfile": "/usr/local/bin/download-flatfile", "dumpsolv": "/usr/local/bin/dumpsolv", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metawepp.
singularity registry hpc automated addition for metawepp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metawepp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metawepp:0.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metawepp/0.1.0--hdfd78af_0
$ module help quay.io/biocontainers/metawepp/0.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metawepp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metawepp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metawepp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metawepp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metawepp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metawepp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### inv

```bash
$ singularity exec <container> /usr/local/bin/inv
$ podman run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invoke

```bash
$ singularity exec <container> /usr/local/bin/invoke
$ podman run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k2

```bash
$ singularity exec <container> /usr/local/bin/k2
$ podman run --it --rm --entrypoint /usr/local/bin/k2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### menuinst

```bash
$ singularity exec <container> /usr/local/bin/menuinst
$ podman run --it --rm --entrypoint /usr/local/bin/menuinst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/menuinst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-metawepp

```bash
$ singularity exec <container> /usr/local/bin/run-metawepp
$ podman run --it --rm --entrypoint /usr/local/bin/run-metawepp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-metawepp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viral_usher

```bash
$ singularity exec <container> /usr/local/bin/viral_usher
$ podman run --it --rm --entrypoint /usr/local/bin/viral_usher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viral_usher   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viral_usher_build

```bash
$ singularity exec <container> /usr/local/bin/viral_usher_build
$ podman run --it --rm --entrypoint /usr/local/bin/viral_usher_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viral_usher_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wepp

```bash
$ singularity exec <container> /usr/local/bin/wepp
$ podman run --it --rm --entrypoint /usr/local/bin/wepp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wepp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### distro

```bash
$ singularity exec <container> /usr/local/bin/distro
$ podman run --it --rm --entrypoint /usr/local/bin/distro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/distro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsondiff

```bash
$ singularity exec <container> /usr/local/bin/jsondiff
$ podman run --it --rm --entrypoint /usr/local/bin/jsondiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsondiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpatch

```bash
$ singularity exec <container> /usr/local/bin/jsonpatch
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiexec.gforker

```bash
$ singularity exec <container> /usr/local/bin/mpiexec.gforker
$ podman run --it --rm --entrypoint /usr/local/bin/mpiexec.gforker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiexec.gforker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corepack

```bash
$ singularity exec <container> /usr/local/bin/corepack
$ podman run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npx

```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2

```bash
$ singularity exec <container> /usr/local/bin/kraken2
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-build

```bash
$ singularity exec <container> /usr/local/bin/kraken2-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-inspect

```bash
$ singularity exec <container> /usr/local/bin/kraken2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### node

```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm

```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpointer

```bash
$ singularity exec <container> /usr/local/bin/jsonpointer
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba-package

```bash
$ singularity exec <container> /usr/local/bin/mamba-package
$ podman run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda2solv

```bash
$ singularity exec <container> /usr/local/bin/conda2solv
$ podman run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-flatfile

```bash
$ singularity exec <container> /usr/local/bin/download-flatfile
$ podman run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsolv

```bash
$ singularity exec <container> /usr/local/bin/dumpsolv
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecollect

```bash
$ singularity exec <container> /usr/local/bin/ecollect
$ podman run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2facds

```bash
$ singularity exec <container> /usr/local/bin/gbf2facds
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2tbl

```bash
$ singularity exec <container> /usr/local/bin/gbf2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff-sort

```bash
$ singularity exec <container> /usr/local/bin/gff-sort
$ podman run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2xml

```bash
$ singularity exec <container> /usr/local/bin/gff2xml
$ podman run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
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